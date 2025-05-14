import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium
from io import StringIO
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Page config (no forced theme)
st.set_page_config(
    page_title="YIPRO", 
    page_icon=":evergreen_tree:", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title (no forced color)
st.title(":evergreen_tree: YIPRO")
#st.markdown("(Youth Innovation for Post-harvet Loss Reduction and Optimization)")


# ==============================================
# HOMEPAGE
# ==============================================
# Title and Subtitle Section (Centered with animation class)
st.markdown(
        """
        <div style="text-align: center;" class="animate-fade-in">
            <h1 style="font-size: 2.8em; margin-bottom: 0; color: #228B22;">Reducing Post-Harvest Losses with Smart Innovation</h1>
            
        </div>
        """,
        unsafe_allow_html=True,
)

with st.container():
        # Hero Section with two columns
        col1, col2 = st.columns([2, 1])
        
        with col1:
                    st.markdown("""
            <div class="animate-fade-in">
                <h2>📊 Visualize Risk. Target Solutions.</h2>
                <p style="font-size: 1.1rem; line-height: 1.6;">
                    In Nigeria, up to 50% of perishable crops are lost after harvest. YIPRO combines data analytics, risk mapping, 
                    and smart technology to help youth-led agri-businesses minimize these losses and maximize profits.


            </div>
            """, unsafe_allow_html=True)

        with col2:
         
            st.markdown("""
            <div style="background-color: #e8f5e9; border-radius: 10px; padding: 15px; text-align: center; margin-bottom: 10px;">
                <h4 style="color: #228B22; margin-top: 0;">YIPRO – Youth Innovation for Post-Harvest-Loss Reduction & Optimization</h4>
                <p style="margin-bottom: 10px;">Empowering young agripreneurs with data-driven tools to reduce crop loss, optimize storage, and build resilient agri-businesses.</p>
            </div>
            """, unsafe_allow_html=True)


# Key Benefits Section
st.markdown("""
    <div class="animate-fade-in">
        <h2 style="text-align: center; margin-bottom: 20px;">Key Features</h2>
    </div>
    """, unsafe_allow_html=True)


# Modern card layout for benefits
col1, col2 = st.columns(2)
with col1:
        with st.container():
            st.markdown("""
            <div style="padding: 20px; border-radius: 10px; background-color: #e8f5e9; height: 100%;">
                <h3 style="color: #228B22;">📍 High-Risk Area Visualization</h3>
                <p>Use interactive charts & maps to identify regions, crops, and seasons most vulnerable to post-harvest loss.</p>
            </div>
            """, unsafe_allow_html=True)
    
with col2:
        with st.container():
            st.markdown("""
            <div style="padding: 20px; border-radius: 10px; background-color: #e8f5e9; height: 100%;">
                <h3 style="color: #F4B400;">⚙️ Smart Storage Insights</h3>
                <p>Design intelligent storage interventions tailored to regional loss patterns.</p>
            </div>
            """, unsafe_allow_html=True)

col3, col4 = st.columns(2)
    
with col3:
        with st.container():
            st.markdown("""
            <div style="padding: 20px; border-radius: 10px; background-color: #e8f5e9; height: 100%; margin-top: 15px;">
                <h3 style="color: #F4B400;">🚨 Targeted Interventions</h3>
                <p> Know exactly where to invest in cold chains, storage hubs, or transportation upgrades for maximum impact.</p>
            </div>
            """, unsafe_allow_html=True)
    
with col4:
        with st.container():
            st.markdown("""
            <div style="padding: 20px; border-radius: 10px; background-color: #e8f5e9; height: 100%; margin-top: 15px;">
                <h3 style="color: #2E7D32;">🚜 Loss-Prevention Tips</h3>
                <p>Practical, easy-to-follow advice to help farmers reduce waste during storage, handling, and transport.</p>
            </div>
            """, unsafe_allow_html=True)
    
st.markdown("---")
            


#### OPTIONAL FEATURES: PROJECT HIGHLIGHTS ####

# ==============================================
# HOMEPAGE
# ==============================================


