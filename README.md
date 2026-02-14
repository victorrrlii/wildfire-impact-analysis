# 🔥 Wildfire Impact Analysis: Data-Driven Assessment of the 2025 Palisades Fire

## Project Overview

An end-to-end data analytics project leveraging **geospatial data** and **satellite imagery** to quantify wildfire damage and track environmental recovery. This analysis of the 2025 Palisades Fire (Los Angeles, CA) demonstrates proficiency in **data acquisition, cleaning, transformation, statistical analysis, and interactive visualization** using Python and cloud computing platforms.

**Business Value**: This type of analysis supports disaster response planning, insurance risk assessment, environmental impact reporting, and resource allocation for recovery efforts.

## 📊 Key Data Analytics Skills Demonstrated

### Data Acquisition & Processing
- ✅ **API Integration**: Automated data extraction from Google Earth Engine's satellite database
- ✅ **Data Cleaning**: Implemented cloud coverage filtering and quality control measures
- ✅ **ETL Pipeline**: Get satellite data source (Sentinel-2)

### Statistical Analysis & Feature Engineering
- ✅ **Index Calculation**: Computed vegetation health metrics (NDVI, NBR) from multispectral bands
- ✅ **Change Detection**: Applied differencing techniques to quantify before/after impacts
- ✅ **Classification**: Categorized fire severity into 5 distinct classes based on statistical thresholds
- ✅ **Time Series Analysis**: Tracked vegetation indices over 6-month period with smoothing algorithms
- ✅ **Outlier Detection**: Filtered anomalous data points using cloud coverage thresholds

### Data Visualization & Reporting
- ✅ **Interactive Dashboards**: Built dynamic maps with split-screen comparisons
- ✅ **Time Series Plots**: Created publication-ready charts with Plotly (HTML/PDF export)
- ✅ **Geospatial Visualization**: Developed color-coded severity maps for stakeholder communication

## 🎯 Business Applications

This project methodology can be applied to:
- **Insurance Analytics**: Quantify property damage and risk assessment for claims processing
- **Environmental Consulting**: Generate impact reports for regulatory compliance
- **Urban Planning**: Inform land use decisions and disaster preparedness strategies
- **Emergency Management**: Prioritize resource allocation during disaster response
- **Climate Research**: Track long-term environmental changes and recovery patterns

## 📈 Analysis Results & Key Metrics

### Quantitative Findings
The analysis provides data-driven insights including:
- **Total Affected Area**: Calculated burned area in square kilometers by severity class
- **Vegetation Health Decline**: Measured percentage change in NDVI pre/post-fire
- **Recovery Timeline**: Time-series tracking showing vegetation regeneration rates
- **Severity Distribution**: Statistical breakdown of burn intensity across the region

### Data Processing Workflow
```
Raw Satellite Data (10-30m resolution)
    ↓
Cloud Filtering (<10% coverage) + Quality Control
    ↓
Getting Data (Sentinel-2)
    ↓
Feature Engineering (NDVI, NBR calculations)
    ↓
Change Detection Analysis (dNBR)
    ↓
Classification & Statistical Summary
    ↓
Interactive Visualizations + Export
```

## 🛠️ Technical Stack

**Languages & Tools:**
- **Python**: Primary analysis language
- **Jupyter Notebook**: Interactive development and documentation
- **Google Earth Engine**: Cloud-based geospatial data platform

**Key Libraries:**
| Library | Purpose |
|---------|---------|
| `earthengine-api` | Satellite data acquisition & processing |
| `geemap` | Interactive geospatial visualization |
| `pandas` | Data manipulation (via numpy arrays) |
| `plotly` | Interactive charts and dashboards |
| `matplotlib` | Static visualizations |

## Prerequisites

- Python 3.8 or higher
- Google Earth Engine account ([sign up here](https://earthengine.google.com/signup/))
- Google Earth Engine project
- Basic understanding of Python and data analysis

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/wildfire-analysis-gee.git
cd wildfire-analysis-gee
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Authenticate with Google Earth Engine:
```bash
earthengine authenticate
```

## 🚀 Quick Start

1. Clone this repository:
```bash
git clone https://github.com/yourusername/wildfire-impact-analysis.git
cd wildfire-impact-analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Authenticate with Google Earth Engine:
```bash
earthengine authenticate
```

4. Launch the analysis:
```bash
jupyter notebook main.ipynb
```

## 📁 Project Structure

```
wildfire-impact-analysis/
├── main.ipynb              # Primary analysis notebook
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── results/                # Output directory (auto-generated)
    ├── ndvi_nbr_plot.html  # Interactive time-series chart
    └── ndvi_nbr_plot.pdf   # Publication-ready visualization
```

## 🔍 Analysis Workflow

### 1. Data Collection
- Define study area and time periods (pre-fire, post-fire, current)
- Query satellite imagery from multiple sources
- Apply quality filters (cloud coverage <10%)

### 2. Data Preprocessing
- Merge multi-source imagery into composite images
- Extract spectral bands (Red, NIR, SWIR)
- Handle outliers

### 3. Feature Engineering
Calculate key vegetation indices:
- **NDVI** = `(NIR - Red) / (NIR + Red)` → Vegetation density and health
- **NBR** = `(NIR - SWIR2) / (NIR + SWIR2)` → Burn sensitivity index
- **dNBR** = `NBR_prefire - NBR_postfire` → Fire severity measure

### 4. Statistical Analysis
- Classify fire severity into 5 categories
- Calculate area statistics per severity class
- Generate time-series trends with Savitzky-Golay smoothing
- Identify recovery patterns and anomalies

### 5. Visualization & Reporting
- Create interactive before/after map comparisons
- Generate color-coded severity classification maps
- Plot time-series of vegetation indices
- Export results in HTML and PDF

## 📊 Analytical Methodology

### Study Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Study Area** | Palisades Fire, Los Angeles | High-impact urban wildfire event |
| **Coordinates** | 34.092615°N, 118.532875°W | Fire origin point |
| **Analysis Radius** | 15 km buffer | Captures primary impact zone |
| **Pre-fire Period** | Jan 1-5, 2025 | Baseline vegetation conditions |
| **Post-fire Period** | Jan 6-16, 2025 | Immediate fire impact |
| **Time Series** | Oct 2024 - Apr 2025 | 6-month trend analysis |

### Fire Severity Classification
Statistical thresholds based on dNBR (Differenced Normalized Burn Ratio):

| Class | dNBR Range | Interpretation | Color Code |
|-------|------------|----------------|------------|
| **Unburned** | < 0.1 | No detectable impact | 🟢 Green |
| **Low Severity** | 0.1 - 0.27 | Minor vegetation damage | 🟡 Yellow |
| **Moderate-Low** | 0.27 - 0.44 | Partial canopy loss | 🟠 Orange |
| **Moderate-High** | 0.44 - 0.66 | Significant vegetation loss | 🔴 Red |
| **High Severity** | ≥ 0.66 | Complete vegetation destruction | 🔴 Dark Red |

### Data Quality Controls
- Cloud coverage threshold: **<10%** for all imagery
- Multi-image mosaicking for complete spatial coverage
- Temporal smoothing using **Savitzky-Golay filter** (window=5, polynomial=2)
- Outlier detection and removal in time-series analysis

## 📦 Deliverables

### Visual Outputs
1. **Interactive Split-Screen Maps**: Side-by-side comparison of fire impact over time
2. **Fire Severity Classification Map**: Color-coded spatial distribution of burn intensity
3. **Time-Series Dashboard**: 6-month trend analysis of vegetation indices (HTML)
4. **Publication-Ready Charts**: High-resolution PDF exports for reports

### Statistical Summaries
- Total affected area by severity classification
- Percentage distribution of burn severity
- Vegetation health metrics (NDVI/NBR) before and after fire
- Recovery rate calculations from time-series data

### Use Cases for Deliverables
- **Insurance Claims**: Quantify damage extent with statistical evidence
- **Government Reporting**: Meet regulatory requirements for environmental impact
- **Stakeholder Communication**: Present findings through clear visualizations
- **Research Publications**: Export-ready charts and methodology documentation

## 💡 Key Insights & Learnings

This project demonstrates:
- **Scalable Analysis**: Methodology applicable to any wildfire or environmental disaster
- **Reproducible Research**: Fully documented workflow from raw data to insights
- **Cloud Computing**: Leveraged Google Earth Engine for processing terabytes of satellite data
- **Automated Workflows**: Built reusable functions for data extraction and visualization
- **Data Storytelling**: Translated complex geospatial data into actionable insights

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/victorrrlii/wildfire-impact-analysis/issues).

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Earth Engine** for providing cloud-based geospatial analysis platform
- **NASA & ESA** for Sentinel-2 satellite missions
- **geemap** library developers for interactive mapping tools

## 📧 Contact

**Victor Li** - Data Analyst

- LinkedIn: https://www.linkedin.com/in/victor-li-6b682a314/
- Email: victorrrli0720@gmail.com

---

### 🎓 About This Project

This project was developed to demonstrate **data analytics capabilities** for **real-world environmental and disaster management applications**. It showcases proficiency in:
- Python programming for data analysis
- API integration and ETL processes
- Statistical analysis and feature engineering
- Data visualization and storytelling
- Geospatial data processing
- Cloud computing platforms

**Perfect for portfolios targeting**: Data Analyst, Business Analyst, GIS Analyst, Environmental Analyst, or Analytics Consultant roles.

---

⭐ **If you find this project helpful, please consider giving it a star!**
