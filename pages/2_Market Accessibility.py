import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown(
    """
    <style>
        /* Reduce sidebar width */
        [data-testid="stSidebar"] {
            width: 240px !important;
            min-width: 240px !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
) 



st.markdown("""
        <div class="animate-fade-in">
            <h1>Market Accessibility</h1>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                Market access plays a crucial role in reducing post-harvest losses.
                When farmers face poor road networks, long distances to markets, or lack of reliable buyers, 
                perishable produce often spoils before it can be sold. Improving access to markets enables faster sales, 
                reduces spoilage, and increases farmers’ income.
        </div>
            """, unsafe_allow_html=True)

df = pd.read_stata("4_c2c_Market_Access_ano.dta")

st.header("Market Access Across Zones")

# Add a multiselect filter for zones
zones = df['zone_id'].unique()
selected_zones = st.multiselect("Select Zones to View", zones, default=zones)

filtered_df = df[df['zone_id'].isin(selected_zones)]

# Create tabs
tab1, tab2 = st.tabs(["📊 Bar Chart", "🌀 Sunburst Chart"])

with tab1:
    st.subheader("Farmer's Accessibility to Market by Zone")
    fig_bar = px.histogram(
        filtered_df,
        x="zone_id",
        color="c2cq1a",
        barmode="group",
        #title="Nearest Market by Zone",
         labels={"zone_id": "Zone", "c2cq1a": "Location of Market"},
        category_orders={"c2cq1a": ["In the community", "In the LGA", "In another LGA", "In another state"]}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.subheader("Market Access Breakdown: Zone → State → Sector → Market Location")
    fig_sunburst = px.sunburst(
        filtered_df,
        path=["zone_id", "state_id", "sector", "c2cq1a"],
        title="Sunburst View of Market Access",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_sunburst, use_container_width=True)


    # Mapping transport codes to readable labels
transport_map = {
    1: "Foot",
    2: "Bicycle",
    3: "Tricycle/Motorcycle",
    4: "Car/Van",
    5: "Boat/Canoe",
    6: "Animal-drawn Cart",
    999: "Others"
}

# Load the data for the next visualization
df2 = pd.read_stata("1_Identification_ano.dta")

# Count transport method occurrences
transport_counts = df2['c2cq2'].value_counts().reset_index()
transport_counts.columns = ['Transport Method', 'Count']

st.subheader("How Farmers Transport Produce to Selling Points")

# Tabs for interactivity
tab3, tab4 = st.tabs(["📊 Bar Chart", "🥧 Donut Chart"])

with tab3:
    fig_bar = px.bar(
        transport_counts,
        x='Transport Method',
        y='Count',
        color='Transport Method',
        title='Transport Methods Used by Farmers',
        labels={'Count': 'Number of Farmers'}
    )
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

with tab4:
    fig_pie = px.pie(
        transport_counts,
        names='Transport Method',
        values='Count',
        title='Distribution of Transport Methods',
        hole=0.4  # Donut chart
    )
    st.plotly_chart(fig_pie, use_container_width=True)


st.markdown("---")

st.subheader("🔍 Insights")

st.markdown("""
1. **Market Location Access:**  
   In **five out of six geo-zones** (North Central, North East, North West, South West, and South South), more farmers access markets located **in their Local Government Area (LGA)** rather than within their own community. This may indicate a **lack of nearby or functional community markets**, suggesting a need for **infrastructure investment or market development closer to farms**, particularly in rural zones.

2. **Transport Challenges:**  
   A majority of farmers (**53.29%**) rely on **tricycles or motorcycles** to transport produce, followed by **car/vans (21.5%)** and **on foot (19.8%)**. This heavy reliance on two-wheelers and walking implies **inadequate transport infrastructure** or lack of affordable alternatives, which may **contribute to post-harvest losses**, especially in remote areas.

💡 **Suggested Intervention Focus:**  
Investments in **local market infrastructure** and **rural road networks**, as well as **affordable and reliable transportation options**, could significantly reduce post-harvest losses and improve market access for farmers.
""")
