import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.title("🏠 Home")

df = load_data()

st.sidebar.header("Filters")
regions = ["All Regions"] + sorted(df["region_txt"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

if selected_region != "All Regions":
    filtered_df = df[df["region_txt"] == selected_region]
else:
    filtered_df = df

st.subheader("Dashboard Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Incidents", len(filtered_df))
c2.metric("Fatalities", int(filtered_df["nkill"].sum()))
c3.metric("Injured", int(filtered_df["nwound"].sum()))
c4.metric("Countries", filtered_df["country_txt"].nunique())

st.divider()

st.subheader("Attacks Over Years")

with st.spinner("Generating chart..."):
    yearly = (
        filtered_df.groupby("iyear")
          .size()
          .reset_index(name="Attacks")
    )
    
    fig = px.line(
        yearly,
        x="iyear",
        y="Attacks",
        markers=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.success("👉 Click **Global Threat Map** from the left sidebar to explore incidents geographically.")