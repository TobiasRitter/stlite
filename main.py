import streamlit as st
import numpy as np
import plotly.express as px

st.markdown("# Normal Distribution Sample Generator")

size = st.slider("Sample size", 100, 1000)

arr = np.random.normal(1, 1, size=size)
fig = px.histogram(arr)

st.plotly_chart(fig)
