import streamlit as st
import pandas as pd
import plotly.express as px
import pyreadstat
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go


st.set_page_config(layout="wide")
st.title("Post Harvest Crop Disposition Survey")


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

df, meta = pyreadstat.read_sav("secta3_harvestW1.sav")
df.to_csv('secta.csv', index=False)


#======================#
#   Summary            #
#======================#


# Define the target columns
target_cols = ['sa3q23b', 'sa3q6b', 'sa3q11b']

# Filter rows where all target columns are exactly 1(representing Kilogram Unit according to Metadata)
filtered_df = df[df[target_cols].eq(1).all(axis=1)]

#Set metric elements 
st.header("Summary Statistics")

mean_harvest = filtered_df['sa3q6a'].mean() 
min_harvest = filtered_df['sa3q6a'].min()         
max_harvest = filtered_df['sa3q6a'].max() 

mean_sale = filtered_df['sa3q11a'].mean() 
min_sale =filtered_df['sa3q11a'].min()        
max_sale =filtered_df['sa3q11a'].max()

mean_loss = filtered_df['sa3q23a'].mean() 
min_loss = filtered_df['sa3q23a'].min()        
max_loss =filtered_df['sa3q23a'].max()

# Green: #228B22
# Yello: #F4B400

st.markdown("""
            <div style="padding: 2px; border-radius: 10px; background-color: #e8f5e9; height: 100%;">
                <h4 style="color:#228B22 ;">Crop Quantity Harvested</h4>
            </div>
            """, unsafe_allow_html=True)
 

col1, col2, col3 = st.columns(3)
col1.metric("Average Harvest (KG):", f"{mean_harvest:.2f}")
col2.metric("Maximum Harvest (KG):", f"{max_harvest:.2f}")
col3.metric("Minimum Harvest (KG):", f"{min_harvest:.2f}")


st.markdown("""
            <div style="padding: 2px; border-radius: 10px; background-color: #e8f5e9; height: 100%;">
                <h4 style="color:#F4B400 ;">Crop Quantity Sold</h4>
            </div>
            """, unsafe_allow_html=True)
 

col1, col2, col3 = st.columns(3)
col1.metric("Average Quantity Sold (KG):", f"{mean_sale:.2f}")
col2.metric("Maximum Quantity Sold (KG):", f"{max_sale:.2f}")
col3.metric("Minimum Quantity Sold (KG):", f"{min_sale:.2f}")

st.markdown("""
            <div style="padding: 2px; border-radius: 10px; background-color: #e8f5e9; height: 100%;">
                <h4 style="color:#FF0000 ;">Crop Quantity Lost (Post-Harvest-Loss)</h4>
            </div>
            """, unsafe_allow_html=True)
 

col1, col2, col3 = st.columns(3)
col1.metric("Average Quantity Lost (KG):", f"{mean_loss:.2f}")
col2.metric("Maximum Quantity Lost (KG):", f"{max_loss:.2f}")
col3.metric("Minimum Quantity Lost (KG):", f"{min_loss:.2f}")

st.markdown("---")

#======================#
#   Visualization A    #
#======================#


# Rename columns for plotting
plot_data = filtered_df[['sa3q6a', 'sa3q11a', 'sa3q23a']].rename(columns={
    'sa3q6a': 'Harvest',
    'sa3q11a': 'Sell',
    'sa3q23a': 'Lost'
})

# Violin Plot
# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
sns.violinplot(data=plot_data, palette='pastel', ax=ax)
ax.set_title('Violin Plot of Harvest, Sales, and Loss (in kg)', fontsize=14)
ax.set_ylabel('Kilograms')
ax.set_xlabel('Harvest Categories')
plt.tight_layout()

# Show plot in Streamlit
st.pyplot(fig)


rename_map = {
    'sa3q6a': 'Harvest',
    'sa3q11a': 'Sell',
    'sa3q23a': 'Lost'
}

melted_df = filtered_df[['sa3q6a', 'sa3q11a', 'sa3q23a']].melt(var_name='variable', value_name='Kilograms')

# Replace column codes with readable labels
melted_df['variable'] = melted_df['variable'].map(rename_map)

#Create the violin plot
fig = px.violin(melted_df, x='variable', y='Kilograms',
                box=True, points="all",
                labels={'variable': 'Category', 'Kilograms': 'Kilograms'},
                title="Interactive Violin Plot: Harvest, Sell, and Loss")
st.plotly_chart(fig, use_container_width=True)


# fig = px.violin(filtered_df, y=['sa3q6a', 'sa3q11a', 'sa3q23a'],
#                 box=True, points="all",
#                 labels={'variable': 'Category', 'value': 'Kilograms'},
#                 title="Interactive Violin Plot: Harvest, Sales, and Loss")
# st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.markdown("""
        <div class="animate-fade-in">
            <h2>The Role of Processing in Preventing Post-Harvest Losses.</h2>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                Processing plays a vital role in minimizing post-harvest losses by extending the shelf life, market value, 
                and usability of agricultural products. In Nigeria, where high humidity, poor storage, and limited cold-chain 
                infrastructure often lead to rapid spoilage, timely processing transforms perishable produce into more stable forms.
        </div>
            """, unsafe_allow_html=True)
st.subheader("Common Crop Processing Methods in Nigeria")

methods = [
    ("🌞 Drying", "Removes moisture to extend shelf life."),
    ("🌾 Milling", "Crushes grains into flour or powder."),
    ("🌀 Grinding", "Pulverizes crops into finer textures."),
    ("🔥 Roasting", "Uses dry heat to enhance flavor and preserve."),
    ("🍳 Frying", "Cooks and preserves using oil."),
    ("🥥 Oil Extraction", "Derives oil from seeds or nuts."),
    ("🍊 Juice Extraction", "Converts fresh produce into liquid form.")
]

cols = st.columns(3)  # 3 cards per row

for i, (title, desc) in enumerate(methods):
    with cols[i % 3]:
        st.markdown(f"### {title}")
        st.markdown(desc)


