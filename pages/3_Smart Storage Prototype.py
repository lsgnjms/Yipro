import streamlit as st
import pydeck as pdk
import pandas as pd
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static


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



st.title("🗺️ Smart Storage Locator")

# Dummy storage locations per geo-zone with lat/lon coordinates
storage_data = pd.DataFrame([
    {"Geo-zone": "North Central", "State": "Kwara", "Facility": "Ilorin Cold Hub", "Latitude": 8.4966, "Longitude": 4.5421, "Capacity": "Large", "Type": "Cold Storage"},
    {"Geo-zone": "North Central", "State": "Nasarawa", "Facility": "Lafia Storage Center", "Latitude": 8.4966, "Longitude": 8.5156, "Capacity": "Medium", "Type": "Dry Storage"},
    {"Geo-zone": "North East", "State": "Borno", "Facility": "Maiduguri Smart Storage", "Latitude": 11.8333, "Longitude": 13.1500, "Capacity": "Large", "Type": "Cold Storage"},
    {"Geo-zone": "North West", "State": "Kano", "Facility": "Kano Agro Storage", "Latitude": 12.0000, "Longitude": 8.5167,  "Capacity": "Small", "Type": "Dry Storage"},
    {"Geo-zone": "South South", "State": "Rivers", "Facility": "Port Harcourt Hub", "Latitude": 4.8156, "Longitude": 7.0498, "Capacity": "Medium", "Type": "Cold Storage"},
    {"Geo-zone": "South West", "State": "Oyo", "Facility": "Ibadan Cold Chain", "Latitude": 7.3775, "Longitude": 3.9470, "Capacity": "Large", "Type": "Cold Storage"},
    {"Geo-zone": "South East", "State": "Enugu", "Facility": "Enugu Storage Facility", "Latitude": 6.5244, "Longitude": 7.5139, "Capacity": "Small", "Type": "Dry Storage"}
])

df = pd.DataFrame(storage_data)

zone = st.selectbox("Select your geo-zone:", storage_data["Geo-zone"].unique())

#  Filter by selected zone
zone_df = storage_data[storage_data["Geo-zone"] == zone]

# Sidebar filters
selected_type = st.sidebar.multiselect("Select Storage Type", storage_data["Type"].unique(), default=storage_data["Type"].unique())
selected_capacity = st.sidebar.multiselect("Select Storage Capacity", storage_data["Capacity"].unique(), default=storage_data["Capacity"].unique())


# Apply type and capacity filters within the selected zone
filtered_storage = zone_df[
    zone_df["Type"].isin(selected_type) & zone_df["Capacity"].isin(selected_capacity)
]

st.subheader("Available Storage Facilities in Your Zone")
st.dataframe(filtered_storage[["State", "Facility", "Type", "Capacity"]])

# Create Folium map
m = folium.Map(location=[9.0820, 8.6753], zoom_start=6)

# Add filtered markers
for _, row in filtered_storage.iterrows():
    popup_content = (
        f"<b>{row['Facility']}</b><br>"
        f"State: {row['State']}<br>"
        f"Capacity: {row['Capacity']}<br>"
        f"Type: {row['Type']}"
    )
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=popup_content,
        icon=folium.Icon(color="blue" if row["Type"] == "Cold Storage" else "green", icon="tint" if row["Type"] == "Cold Storage" else "archive",
        prefix='fa')
    ).add_to(m)

# Display map
st.subheader("Facility Locations")
#folium_static(m)
st_folium(m, width=700, height=500)
