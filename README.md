# Task-3 — Geo Analytics of Restaurant Data

<p>
  <img src="https://img.shields.io/badge/Type-Geospatial%20Analytics-4A90D9?style=flat-square" />
  <img src="https://img.shields.io/badge/Visualizations-8-FF6B35?style=flat-square" />
  <img src="https://img.shields.io/badge/GPS%20Points-9%2C052-2ECC71?style=flat-square" />
  <img src="https://img.shields.io/badge/Cities-141-lightgrey?style=flat-square" />
</p>

---

## Overview

A comprehensive geospatial analysis of the Cognifyz restaurant dataset using latitude, longitude, city, and locality information. The project maps the global distribution of restaurants, identifies density hotspots, and uncovers city-level patterns in ratings, pricing, cuisine popularity, and online delivery adoption.

---

## Problem Statement

Understanding where restaurants cluster, which cities outperform in quality, which cuisines dominate by region, and how pricing varies geographically are critical inputs for expansion strategy, market entry decisions, and competitive analysis on restaurant platforms.

---

## Objective

Produce a suite of geospatial and city-level visualizations that reveal distribution patterns, concentration hotspots, cuisine trends, pricing variations, and the relationship between online delivery availability and average restaurant rating.

---

## Technologies Used

| Category | Tool |
|----------|------|
| Language | Python 3.9+ |
| Data manipulation | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Notebook | Jupyter |

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
| Total restaurants | 9,551 |
| Cities covered | 141 |
| Valid GPS coordinates | 9,052 (499 rows had lat=0, lon=0 — excluded) |
| Latitude range | –41.33° to +55.98° (Southern New Zealand to Scotland) |
| Longitude range | –157.95° to +174.83° (Hawaii to New Zealand) |

---

## Project Workflow

```
Raw Dataset (9,551 rows)
        │
        ▼
1. Load dataset — inspect geographic columns (lat, lon, city, locality)
        │
        ▼
2. Filter invalid GPS coordinates (lat=0, lon=0 → Gulf of Guinea placeholder)
   Valid GPS records: 9,052
        │
        ▼
3. Geographic distribution analysis
   - Global scatter map (colour-coded by rating)
   - 2D hexbin density heatmap
        │
        ▼
4. City-level analysis
   - Top 20 cities by restaurant count
   - Top 20 cities by average rating (min 30 restaurants)
   - Price range distribution across top 10 cities
        │
        ▼
5. Cuisine analysis
   - Cuisine popularity across top 10 cities (stacked bar)
   - Overall cuisine share (pie chart)
        │
        ▼
6. Service & rating trends
   - Average rating with/without online delivery per city
        │
        ▼
7. Business insights synthesis
```

---

## Machine Learning Techniques Used

This task focuses on **Exploratory Data Analysis (EDA)** and **Geospatial Visualization** rather than predictive modelling. Techniques applied:

- Coordinate filtering and validation
- Aggregation and groupby operations for city-level statistics
- Hexbin density estimation for hotspot identification
- Normalized stacked bar charts for multi-category geographic comparison
- Correlation analysis between service features (online delivery) and rating

---

## Results

### Geographic Distribution

| Region | Restaurant Count | Notes |
|--------|-----------------|-------|
| India (South Asia) | ~8,700+ | Dominant cluster, Delhi-NCR hub |
| Southeast Asia | ~400 | Philippines, Indonesia |
| International | ~400 | UAE, South Africa, New Zealand, UK |

### City-Level Statistics (Top 5 by Count)

| City | Restaurant Count | Avg Rating |
|------|-----------------|------------|
| New Delhi | 5,473 | 2.44 |
| Gurgaon | 1,118 | 2.65 |
| Noida | 1,080 | 2.04 |
| Faridabad | 251 | 1.87 |
| Ghaziabad | 25 | 2.85 |

**Key Insight:** Smaller cities significantly outperform high-volume metros in average rating. Lucknow averages 4.20 and Guwahati 4.19 — far above Delhi's 2.44.

### Pricing

Gurgaon is the most expensive city (avg ₹714 per two), consistent with its premium business-district positioning. Price Range 1 (cheapest) dominates across all cities, reflecting the dataset's India-heavy composition.

### Cuisine Landscape

| Rank | Cuisine | Approximate Count |
|------|---------|-------------------|
| 1 | North Indian | 1,400+ |
| 2 | Chinese | 600+ |
| 3 | Fast Food | 500+ |
| 4 | Mughlai | 400+ |
| 5 | South Indian | 300+ |

### Online Delivery Effect

Cities with high delivery penetration (New Delhi, Gurgaon) show that delivery-enabled restaurants maintain slightly higher average ratings, suggesting that established, tech-forward restaurants are more likely to adopt delivery platforms.

---

## Visualizations

| File | Description |
|------|-------------|
| `01_global_distribution_map.png` | Global scatter map, colour-coded by rating |
| `02_density_heatmap.png` | 2D hexbin density heatmap showing concentration hotspots |
| `03_top20_cities_count.png` | Horizontal bar chart — top 20 cities by restaurant volume |
| `04_city_avg_rating.png` | Top 20 cities by average rating (min 30 restaurants) |
| `05_price_range_by_city.png` | Stacked bar — price tier distribution across top 10 cities |
| `06_cuisine_popularity_by_city.png` | Stacked bar — cuisine mix across top 10 cities |
| `07_cuisine_pie_chart.png` | Pie chart — overall cuisine share across full dataset |
| `08_delivery_rating_by_city.png` | Side-by-side avg rating: online delivery vs no delivery |

---

## Business Insights

| Insight | Detail |
|---------|--------|
| Market opportunity | Smaller cities (Lucknow, Guwahati, Ahmedabad) have high ratings and few restaurants — underserved demand |
| Price positioning | Gurgaon customers spend the most per visit — ideal market for premium-tier chains |
| Cuisine gap | International cuisines are underrepresented in smaller Indian cities despite metro popularity |
| Rating vs volume | Delhi's high restaurant volume correlates with lower avg ratings — saturated, competitive market |
| Delivery adoption | High delivery penetration correlates with rating consistency — argument for delivery incentivisation in Tier-2 cities |

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

**Run the Python script:**

```bash
python src/geo_analytics.py
```

All 8 visualizations are generated and saved to the `outputs/` folder.

**Run the notebook:**

```bash
jupyter notebook notebook.ipynb
```

---

## Future Improvements

- Integrate Folium or Plotly `scatter_mapbox` for interactive, clickable maps
- Add neighbourhood-level analysis using locality column
- Incorporate external data: population density, foot traffic, competitor proximity
- Build a choropleth map showing rating performance by country
- Apply clustering (DBSCAN) to identify natural restaurant hotspot boundaries

---

## Author

**Abhishek** | Ref: CTI/A1/C358755
BCA — Amity University Online, Noida , UP
Machine Learning Internship @ Cognifyz Technologies
