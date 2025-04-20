import ee
import os
import geemap
import datetime
import plotly.graph_objects as go
from ipyleaflet import WidgetControl
from ipywidgets import HTML

ee.Authenticate()

project = 'ee-vl99956018'
ee.Initialize(project=project)


def get_ndvi(image):
    ndvi = image.normalizedDifference(['B8', 'B4']).rename('NDVI')
    return image.addBands(ndvi)

def get_nbr(image):
    nbr = image.normalizedDifference(['B12', 'B8']).rename('NBR')
    return image.addBands(nbr)

def get_ndwi(image):
    ndwi = image.normalizedDifference(['B8', 'B3']).rename('NDWI')
    return image.addBands(ndwi)

def get_evi(image):
    evi = image.expression(
        '2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))',
        {
            'NIR': image.select('B8'),
            'RED': image.select('B4'),
            'BLUE': image.select('B2')
        }).rename('EVI')
    return image.addBands(evi)

def ndvi_nbr_plot(start_date, end_date):
    collection = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                    .filterDate(start_date, end_date)
                    .filterBounds(roi)
                    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 40))
                    .map(get_ndvi)
                    .map(get_nbr)
                    .map(get_ndwi)
                    .map(get_evi)
                    .select(['NDVI', 'NBR', 'NDWI', 'EVI']))

    def reduce_img(img):
        stats = img.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=roi,
            scale=10,
            maxPixels=1e9
        )
        return ee.Feature(None, {
            'date': img.date().format('YYYY-MM-dd'),
            'NDVI': stats.get('NDVI'),
            'NBR': stats.get('NBR'),
            'NDWI': stats.get('NDWI'),
            'EVI': stats.get('EVI')
        })

    features = collection.map(reduce_img)

    stats_list = features.aggregate_array('date').getInfo()
    ndvi_values = features.aggregate_array('NDVI').getInfo()
    nbr_values = features.aggregate_array('NBR').getInfo()
    ndwi_values = features.aggregate_array('NDWI').getInfo()
    evi_values = features.aggregate_array('EVI').getInfo()

    dates = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in stats_list]

    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=ndvi_values,
        mode='lines+markers',
        name='NDVI',
        line=dict(color='green', width=2),
        marker=dict(size=8, color='green'),
        yaxis='y1'
    ))
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=nbr_values,
        mode='lines+markers',
        name='NBR',
        line=dict(color='red', width=2),
        marker=dict(size=8, color='red'),
        yaxis='y1'
    ))

    fig.add_trace(go.Scatter(
        x=dates,
        y=ndwi_values,
        mode='lines+markers',
        name='NDWI',
        line=dict(color='blue', width=2),
        marker=dict(size=8, color='blue'),
        yaxis='y1'
    ))

    fig.add_trace(go.Scatter(
        x=dates,
        y=evi_values,
        mode='lines+markers',
        name='EVI',
        line=dict(color='orange', width=2),
        marker=dict(size=8, color='orange'),
        yaxis='y1'
    ))

    fig.add_vline(
        x=datetime.datetime(2025, 1, 7).timestamp() * 1000,
        line_width=2,
        line_dash="dash",
        line_color="blue",
        annotation_text="First Fire detected",
        annotation_position="top right"
    )

    fig.update_layout(
        title='NDVI, NBR, NDWI and EVI TimeSeries',
        xaxis_title='Date',
        yaxis_title='Index Value',
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True, title='Index Value'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        template='plotly_white',
        hovermode='x unified'
    )

    os.makedirs("results", exist_ok=True)
    fig.write_html("results/ndvi_nbr_plot.html")
    print("Graphic saved at 'results/ndvi_nbr_plot.html'")


if __name__ == "__main__":
    curve_start_date = '2024-11-01'
    curve_end_date = '2025-04-01'

    latitude = 34.092615
    longitude = -118.532875

    roi = ee.Geometry.Point(longitude, latitude).buffer(1000)

    ndvi_nbr_plot(curve_start_date, curve_end_date)
