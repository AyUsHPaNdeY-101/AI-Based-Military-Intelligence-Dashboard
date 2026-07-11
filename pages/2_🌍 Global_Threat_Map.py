import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("🌍 Global Threat Map")

df = load_data()

st.sidebar.header("Filters")

year = st.sidebar.selectbox(
    "Year",
    ["All"] + sorted(df["iyear"].unique().tolist())
)

attack_types = sorted(df["attacktype1_txt"].dropna().unique().tolist())
selected_attacks = st.sidebar.multiselect(
    "Attack Type",
    attack_types,
    default=[]
)

if year != "All":
    df = df[df["iyear"] == year]

if selected_attacks:
    df = df[df["attacktype1_txt"].isin(selected_attacks)]

df = df.dropna(subset=["latitude", "longitude"])

with st.spinner("Generating Global Threat Map..."):
    fig = px.scatter_geo(
        df,
        lat="latitude",
        lon="longitude",
        color="attacktype1_txt",
        hover_name="country_txt",
        hover_data=["city", "gname", "nkill"],
        projection="natural earth"
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.info("👈 Change filters from the sidebar.")