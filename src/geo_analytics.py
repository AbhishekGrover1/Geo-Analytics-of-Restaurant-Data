# ============================================================
# Task 3: Geo Analytics of Restaurant Data
# Intern: Abhishek | Enrollment: CTI/A1/C358755
# Organization: Cognifyz Technologies
# Course: BCA | Domain: Machine Learning
# ============================================================

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import os

SCREENSHOTS = os.path.join(os.path.dirname(__file__), '..', 'Screenshots')
os.makedirs(SCREENSHOTS, exist_ok=True)

# ── 1. Load Dataset ────────────────────────────────────────
df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'Dataset', 'Dataset.csv'))
df['Cuisines'] = df['Cuisines'].fillna('Unknown')
df['Primary Cuisine'] = df['Cuisines'].apply(lambda x: x.split(',')[0].strip())

print(f"Dataset loaded: {df.shape[0]} restaurants | {df['City'].nunique()} cities")
print(f"Latitude  range: {df['Latitude'].min():.4f} to {df['Latitude'].max():.4f}")
print(f"Longitude range: {df['Longitude'].min():.4f} to {df['Longitude'].max():.4f}")

# Filter out invalid/zero coordinates (some rows have 0,0)
geo_df = df[(df['Latitude'].abs() > 0.01) & (df['Longitude'].abs() > 0.01)].copy()
print(f"Restaurants with valid coordinates: {geo_df.shape[0]}")

# ── 2. Visualise Geographic Distribution ──────────────────
sns.set_theme(style='dark')

# 2a. Scatter map — all restaurants
fig, ax = plt.subplots(figsize=(14, 8), facecolor='#1a1a2e')
ax.set_facecolor('#16213e')
sc = ax.scatter(
    geo_df['Longitude'], geo_df['Latitude'],
    c=geo_df['Aggregate rating'], cmap='YlOrRd',
    s=8, alpha=0.6, linewidths=0
)
cbar = fig.colorbar(sc, ax=ax, shrink=0.7)
cbar.set_label('Aggregate Rating', color='white')
cbar.ax.yaxis.set_tick_params(color='white')
plt.setp(cbar.ax.yaxis.get_ticklabels(), color='white')
ax.set_title('Global Restaurant Distribution (Colour = Rating)', fontsize=15,
             fontweight='bold', color='white', pad=10)
ax.set_xlabel('Longitude', color='white')
ax.set_ylabel('Latitude', color='white')
ax.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_edgecolor('#444')
fig.tight_layout()
fig.savefig(os.path.join(SCREENSHOTS, '01_global_distribution_map.png'), dpi=150)
plt.close(fig)
print("\nSaved: 01_global_distribution_map.png")

# 2b. 2D Density heatmap using hexbin
sns.set_theme(style='whitegrid')
fig, ax = plt.subplots(figsize=(14, 7), facecolor='#0d0d0d')
ax.set_facecolor('#0d0d0d')
hb = ax.hexbin(geo_df['Longitude'], geo_df['Latitude'],
               gridsize=60, cmap='inferno', mincnt=1)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('Restaurant Density', color='white')
cb.ax.yaxis.set_tick_params(color='white')
plt.setp(cb.ax.yaxis.get_ticklabels(), color='white')
ax.set_title('Restaurant Density Heatmap', fontsize=15, fontweight='bold',
             color='white', pad=10)
ax.set_xlabel('Longitude', color='white')
ax.set_ylabel('Latitude', color='white')
ax.tick_params(colors='white')
fig.tight_layout()
fig.savefig(os.path.join(SCREENSHOTS, '02_density_heatmap.png'), dpi=150)
plt.close(fig)
print("Saved: 02_density_heatmap.png")

# ── 3. City-Level Analysis ─────────────────────────────────
sns.set_theme(style='whitegrid')

city_stats = df.groupby('City').agg(
    count=('Restaurant ID', 'count'),
    avg_rating=('Aggregate rating', 'mean'),
    avg_cost=('Average Cost for two', 'mean'),
    avg_price_range=('Price range', 'mean'),
).reset_index()

city_stats = city_stats.sort_values('count', ascending=False)
top20_cities = city_stats.head(20)

print("\nTop 10 Cities by Restaurant Count:")
print(top20_cities[['City', 'count', 'avg_rating', 'avg_cost']].head(10).to_string(index=False))

# 3a. Top 20 cities by restaurant count
fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(top20_cities['City'], top20_cities['count'],
              color=plt.cm.tab20.colors, edgecolor='white')
ax.set_title('Top 20 Cities by Number of Restaurants', fontsize=14, fontweight='bold')
ax.set_xlabel('City')
ax.set_ylabel('Number of Restaurants')
ax.tick_params(axis='x', rotation=45)
fig.tight_layout()
fig.savefig(os.path.join(SCREENSHOTS, '03_top20_cities_count.png'), dpi=150)
plt.close(fig)
print("Saved: 03_top20_cities_count.png")

# 3b. Average rating per city (top 20 by count)
fig, ax = plt.subplots(figsize=(12, 6))
top20_by_rating = city_stats[city_stats['count'] >= 30].sort_values('avg_rating', ascending=False).head(20)
ax.bar(top20_by_rating['City'], top20_by_rating['avg_rating'],
       color='mediumseagreen', edgecolor='white')
ax.axhline(df['Aggregate rating'].mean(), color='red', ls='--', lw=1.5, label='Dataset Mean')
ax.set_title('Top 20 Cities by Average Rating (min 30 restaurants)', fontsize=13, fontweight='bold')
ax.set_xlabel('City')
ax.set_ylabel('Average Rating')
ax.tick_params(axis='x', rotation=45)
ax.set_ylim(0, 5)
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(SCREENSHOTS, '04_city_avg_rating.png'), dpi=150)
plt.close(fig)
print("Saved: 04_city_avg_rating.png")

# 3c. Price range trends by top 10 cities
top10_cities = city_stats.head(10)['City'].tolist()
price_city = df[df['City'].isin(top10_cities)].groupby(['City', 'Price range']).size().unstack(fill_value=0)
fig, ax = plt.subplots(figsize=(12, 6))
price_city.plot(kind='bar', ax=ax, colormap='tab10', edgecolor='white', width=0.75)
ax.set_title('Price Range Distribution in Top 10 Cities', fontsize=13, fontweight='bold')
ax.set_xlabel('City')
ax.set_ylabel('Number of Restaurants')
ax.tick_params(axis='x', rotation=30)
ax.legend(title='Price Range', labels=['1-Cheap', '2-Moderate', '3-Expensive', '4-Premium'])
fig.tight_layout()
fig.savefig(os.path.join(SCREENSHOTS, '05_price_range_by_city.png'), dpi=150)
plt.close(fig)
print("Saved: 05_price_range_by_city.png")

# ── 4. Cuisine Popularity by Region ───────────────────────
top_cuisines_overall = df['Primary Cuisine'].value_counts().head(10).index.tolist()
cuisine_city = (df[df['City'].isin(top10_cities) & df['Primary Cuisine'].isin(top_cuisines_overall)]
                .groupby(['City', 'Primary Cuisine'])
                .size().unstack(fill_value=0))

fig, ax = plt.subplots(figsize=(13, 7))
cuisine_city.plot(kind='bar', ax=ax, colormap='Paired', edgecolor='white', width=0.75)
ax.set_title('Top Cuisine Popularity Across Top 10 Cities', fontsize=13, fontweight='bold')
ax.set_xlabel('City')
ax.set_ylabel('Count')
ax.tick_params(axis='x', rotation=30)
ax.legend(title='Cuisine', bbox_to_anchor=(1, 1))
fig.tight_layout()
fig.savefig(os.path.join(SCREENSHOTS, '06_cuisine_popularity_by_city.png'), dpi=150)
plt.close(fig)
print("Saved: 06_cuisine_popularity_by_city.png")

# ── 5. Pie Chart – Overall Cuisine Share ──────────────────
top10_cuisines = df['Primary Cuisine'].value_counts().head(10)
other_count    = df['Primary Cuisine'].value_counts().iloc[10:].sum()
pie_data  = pd.concat([top10_cuisines, pd.Series({'Other': other_count})])
fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    pie_data.values, labels=pie_data.index,
    autopct='%1.1f%%', startangle=140,
    colors=plt.cm.Set3.colors[:len(pie_data)],
    pctdistance=0.82
)
for at in autotexts:
    at.set_fontsize(8)
ax.set_title('Overall Cuisine Share (Primary Cuisine)', fontsize=14, fontweight='bold')
fig.tight_layout()
fig.savefig(os.path.join(SCREENSHOTS, '07_cuisine_pie_chart.png'), dpi=150)
plt.close(fig)
print("Saved: 07_cuisine_pie_chart.png")

# ── 6. Rating Trend: Online Delivery by City ───────────────
delivery_city = (df[df['City'].isin(top10_cities)]
                 .groupby(['City', 'Has Online delivery'])['Aggregate rating']
                 .mean().unstack())
fig, ax = plt.subplots(figsize=(11, 6))
delivery_city.plot(kind='bar', ax=ax, color=['#e07b54', '#5b8db8'], edgecolor='white', width=0.6)
ax.set_title('Avg Rating by Online Delivery Status — Top 10 Cities', fontsize=12, fontweight='bold')
ax.set_xlabel('City')
ax.set_ylabel('Average Rating')
ax.tick_params(axis='x', rotation=30)
ax.set_ylim(0, 5)
ax.legend(title='Has Online Delivery')
fig.tight_layout()
fig.savefig(os.path.join(SCREENSHOTS, '08_delivery_rating_by_city.png'), dpi=150)
plt.close(fig)
print("Saved: 08_delivery_rating_by_city.png")

# ── 7. Business Insights Summary ──────────────────────────
print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

most_restaurants_city = city_stats.iloc[0]['City']
highest_rated_city    = city_stats[city_stats['count'] >= 30].sort_values('avg_rating', ascending=False).iloc[0]
most_popular_cuisine  = df['Primary Cuisine'].value_counts().index[0]
expensive_city        = city_stats[city_stats['count'] >= 30].sort_values('avg_cost', ascending=False).iloc[0]

print(f"\n1. City with most restaurants : {most_restaurants_city} ({city_stats.iloc[0]['count']} restaurants)")
print(f"2. Highest-rated city (≥30)   : {highest_rated_city['City']} (avg {highest_rated_city['avg_rating']:.2f})")
print(f"3. Most popular primary cuisine: {most_popular_cuisine}")
print(f"4. Most expensive avg city    : {expensive_city['City']} (avg cost ₹{expensive_city['avg_cost']:.0f})")
print(f"5. Restaurants with valid GPS : {geo_df.shape[0]} / {df.shape[0]}")
print(f"6. Cities with online delivery available vary widely — higher-rated")
print(f"   restaurants tend to offer online delivery in metro areas.")

print("\n✅ Task 4 Complete — All geo visualizations saved.")
