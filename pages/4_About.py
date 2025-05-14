import streamlit as st


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

st.title("About YIPRO App")

st.markdown("""
Welcome to the **YIPRO (Youth Innovation for Post-harvest-loss Reduction & Optimization)** App!  
This platform was developed to explore and visualize the key challenges contributing to post-harvest losses in Nigeria, leveraging real national data and intuitive dashboards.

Whether you're a policymaker, agricultural researcher, or youth innovator, **YIPRO** equips you with critical insights into market access, transportation bottlenecks, and storage infrastructure all which impact smallholder farmers across the country.

### 🔍 Features:
- 📊 **Interactive Visualizations**: Analyze harvest loss, sales, and transportation patterns by state and region.
- 🗺️ **Smart Storage Map**: View and filter prototype storage hubs by geo-zone, location, and refrigeration type.
- 🚜 **Transport Insights**: Understand how farmers move goods from farm to market across different regions.
- 🧠 **Actionable Insights**: Key data-backed takeaways to guide interventions and optimize food supply chains.

YIPRO is built to support **youth-led innovations** that reduce waste, improve post-harvest systems, and boost food security in Nigeria.  
""")

st.title("Meet the Team")

# Create three columns
col1, col2, col3 = st.columns(3)

# Team Member 1
with col1:
    st.write("**Team Lead**")
    st.image("Team\lead profile.png", width=150) 
    st.markdown("**Ogunwole 'HANEZ' Olusegun**")
    st.caption("Python Developer & Data Analyst")

# # Team Member 2
with col2:
    st.write("**Member**")
    st.image("Team\member1 profile.png", width=150)
    st.markdown("**Ogunwole 'SAINT' Olufemi**")
    st.caption("Data Scientist")

# # Team Member 3
with col3:
    st.write("**Member**")
    st.image("Team\member2 profile.jpeg", width=150)
    st.markdown("**Ogunmoroti 'ESTHER' Olapeju**")
    st.caption("Farmer & 3MTT AI/ML Fellow")
