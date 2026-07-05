# Task-3 · Geo Analytics of Restaurant Data

<p>
  <img src="https://img.shields.io/badge/Type-Geospatial%20Analytics-4A90D9?style=flat-square" />
  <img src="https://img.shields.io/badge/Visualizations-8-FF6B35?style=flat-square" />
  <img src="https://img.shields.io/badge/Valid%20GPS%20Points-9%2C052-2ECC71?style=flat-square" />
  <img src="https://img.shields.io/badge/Cities%20Analysed-141-lightgrey?style=flat-square" />
</p>

---

## Overview

A comprehensive geospatial analysis of the Cognifyz restaurant dataset using coordinate, city, and locality data. The project maps the global distribution of restaurants, identifies geographic density hotspots, and uncovers city-level patterns across ratings, pricing tiers, cuisine popularity, and online delivery adoption — surfacing actionable market insights from spatial data.

---

## Problem Statement

Understanding where restaurants concentrate, which cities outperform on quality, which cuisines dominate by region, and how pricing varies geographically are essential inputs for platform expansion strategy, market entry decisions, and competitive positioning analysis on restaurant aggregators.

---

## Objective

Produce a structured suite of eight geospatial and city-level visualizations that expose distribution patterns, concentration hotspots, cuisine composition trends, price tier variation, and the relationship between online delivery availability and average restaurant rating — synthesized into business-ready insights.

---

## Technologies Used

| Category | Tool |
|----------|------|
| Language | Python 3.9+ |
| Data Manipulation | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Environment | Jupyter Notebook |

---

## Python Libraries

```python
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
jupyter>=1.0.0
```

---

## Dataset Information

| Property | Value |
|----------|-------|
| File | `dataset/Dataset.csv` |
| Total Restaurants | 9,551 |
| Cities | 141 |
| Valid GPS Records | 9,052 · (499 rows with lat = 0, lon = 0 excluded as invalid placeholders) |
| Latitude Range | –41.33° to +55.98° · Southern New Zealand → Scotland |
| Longitude Range | –157.95° to +174.83° · Hawaii → New Zealand |

---

## Project Workflow

```
Raw Dataset  ·  9,551 rows
        │
        ▼
 01  Load dataset
     Inspect geographic columns  :  latitude · longitude · city · locality
        │
        ▼
 02  Coordinate validation
     Filter rows where  lat = 0  and  lon = 0
     (Gulf of Guinea placeholder values  →  not real locations)
     Valid GPS records  :  9,052
        │
        ▼
 03  Geographic distribution analysis
     ├─ Global scatter map — colour-coded by aggregate rating
     └─ 2D hexbin density heatmap — concentration hotspots
        │
        ▼
 04  City-level analysis
     ├─ Top 20 cities by restaurant count
     ├─ Top 20 cities by average rating  (minimum 30 restaurants per city)
     └─ Price range distribution across top 10 cities
        │
        ▼
 05  Cuisine landscape analysis
     ├─ Cuisine popularity across top 10 cities  (stacked bar)
     └─ Overall cuisine share  (pie chart · full dataset)
        │
        ▼
 06  Service and rating correlation
     Average rating — delivery-enabled vs non-delivery restaurants per city
        │
        ▼
 07  Business insights synthesis
```

---

## Analytical Techniques Applied

This task focuses on **Exploratory Data Analysis (EDA)** and **Geospatial Visualization** rather than predictive modelling. Techniques employed:

- GPS coordinate validation and filtering
- City-level aggregation via `groupby` operations
- Hexbin density estimation for hotspot identification
- Normalised stacked bar charts for multi-category geographic comparison
- Correlation analysis between service features (online delivery) and average rating

---

## Results

### Geographic Distribution

| Region | Restaurant Count | Notes |
|--------|-----------------|-------|
| India — South Asia | ~8,700+ | Dominant cluster · Delhi-NCR at the centre |
| Southeast Asia | ~400 | Philippines · Indonesia |
| International | ~400 | UAE · South Africa · New Zealand · United Kingdom |

### City-Level Statistics · Top 5 by Volume

| City | Restaurant Count | Avg Rating |
|------|-----------------|------------|
| New Delhi | 5,473 | 2.44 |
| Gurgaon | 1,118 | 2.65 |
| Noida | 1,080 | 2.04 |
| Faridabad | 251 | 1.87 |
| Ghaziabad | 25 | 2.85 |

**Key Insight:** Smaller cities substantially outperform high-volume metros on average rating. Lucknow records an average of 4.20 and Guwahati 4.19 — far above New Delhi's 2.44. This inversion signals an underserved, high-quality tier-2 market.

### Price Distribution

Gurgaon is the most expensive city in the dataset, averaging ₹714 per two — consistent with its premium business-district positioning. Price Range 1 (budget) dominates across all cities, reflecting the dataset's predominantly India-based composition.

### Cuisine Landscape

| Rank | Cuisine | Approx. Count |
|------|---------|---------------|
| 1 | North Indian | 1,400+ |
| 2 | Chinese | 600+ |
| 3 | Fast Food | 500+ |
| 4 | Mughlai | 400+ |
| 5 | South Indian | 300+ |

### Online Delivery Effect

Cities with high delivery penetration — New Delhi and Gurgaon — show that delivery-enabled restaurants maintain slightly higher average ratings than non-delivery counterparts. This suggests that established, operationally mature restaurants are disproportionately adopting delivery infrastructure, not that delivery itself drives ratings.

---

## Visualizations

| File | Description |
|------|-------------|
| `01_global_distribution_map.png` | Global scatter map — each point is a restaurant, colour-coded by rating |
| `02_density_heatmap.png` | 2D hexbin density heatmap — reveals concentration hotspots |
| `03_top20_cities_count.png` | Horizontal bar chart — top 20 cities ranked by restaurant count |
| `04_city_avg_rating.png` | Top 20 cities ranked by average rating (minimum 30 restaurants threshold) |
| `05_price_range_by_city.png` | Stacked bar — price tier composition across top 10 cities |
| `06_cuisine_popularity_by_city.png` | Stacked bar — cuisine type mix across top 10 cities |
| `07_cuisine_pie_chart.png` | Pie chart — overall cuisine share across the full dataset |
| `08_delivery_rating_by_city.png` | Side-by-side comparison — avg rating for delivery vs non-delivery restaurants per city |

---

## Business Insights

| Insight | Detail |
|---------|--------|
| **Underserved Markets** | Lucknow, Guwahati, and Ahmedabad combine high ratings with low restaurant density — strong indicators of unmet demand |
| **Premium Positioning** | Gurgaon commands the highest average spend per visit — the optimal market for premium-tier chain expansion |
| **Cuisine Gaps** | International cuisines are significantly underrepresented in smaller Indian cities despite strong metro-level popularity |
| **Volume vs Quality** | Delhi's high restaurant count correlates with below-average ratings — characteristic of a saturated, highly competitive market |
| **Delivery Correlation** | High delivery adoption correlates with rating consistency — a case for incentivising delivery infrastructure in tier-2 cities |

---

## Folder Structure

```
Task-3/
├── README.md
├── notebook.ipynb
├── src/
│   └── geo_analytics.py
├── dataset/
│   └── Dataset.csv
├── outputs/
└── images/
    ├── 01_global_distribution_map.png
    ├── 02_density_heatmap.png
    ├── 03_top20_cities_count.png
    ├── 04_city_avg_rating.png
    ├── 05_price_range_by_city.png
    ├── 06_cuisine_popularity_by_city.png
    ├── 07_cuisine_pie_chart.png
    └── 08_delivery_rating_by_city.png
```

---

## Installation

```bash
cd Task-3
pip install -r ../requirements.txt
```

---

## Usage

**Execute the script:**

```bash
python src/geo_analytics.py
```

All 8 visualizations are generated and written to the `outputs/` directory.

**Launch the notebook:**

```bash
jupyter notebook notebook.ipynb
```

---

## Future Improvements

- Integrate Folium or Plotly `scatter_mapbox` for interactive, clickable maps
- Extend analysis to neighbourhood level using the locality column
- Incorporate external datasets — population density, foot traffic, competitor proximity
- Build a choropleth map showing rating performance aggregated by country
- Apply DBSCAN clustering to identify natural restaurant hotspot boundaries from raw GPS coordinates

---

## Author

**Abhishek** · Ref: CTI/A1/C358755
BCA · Amity University Online, Noida
Machine Learning Internship · Cognifyz Technologies
