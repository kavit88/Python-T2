import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Advanced Bootstrap Streamlit App",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# LOAD BOOTSTRAP + ICONS + CSS
# --------------------------------------------------
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
""", unsafe_allow_html=True)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER (PURE HTML)
# --------------------------------------------------
st.markdown("""
<div class="container-fluid bg-primary text-white p-4 rounded">
    <h1 class="text-center">
        <i class="bi bi-bar-chart-line-fill"></i>
        Charts & Visualization Dashboard
    </h1>
    <p class="text-center mb-0">
        Streamlit + HTML + Bootstrap UI Demo
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA
# --------------------------------------------------
x = np.arange(1, 11)
y = np.random.randint(50, 100, 10)

# --------------------------------------------------
# BOOTSTRAP GRID START
# --------------------------------------------------
st.markdown('<div class="container custom-container">', unsafe_allow_html=True)
st.markdown('<div class="row g-4">', unsafe_allow_html=True)

# ---------- CARD 1 : LINE CHART ----------
st.markdown('<div class="col-md-6">', unsafe_allow_html=True)
st.markdown("""
<div class="chart-card">
    <h4>
        <span class="badge bg-success">
            <i class="bi bi-graph-up"></i> Line Chart
        </span>
    </h4>
</div>
""", unsafe_allow_html=True)

plt.figure()
plt.plot(x, y, marker="o")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.title("Marks Line Chart")
st.pyplot(plt)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- CARD 2 : HISTOGRAM ----------
st.markdown('<div class="col-md-6">', unsafe_allow_html=True)
st.markdown("""
<div class="chart-card">
    <h4>
        <span class="badge bg-warning text-dark">
            <i class="bi bi-bar-chart"></i> Histogram
        </span>
    </h4>
</div>
""", unsafe_allow_html=True)

plt.figure()
plt.hist(y, bins=5)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
st.pyplot(plt)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# STREAMLIT BUILT-IN CHARTS (CARD STYLE)
# --------------------------------------------------
st.markdown("""
<div class="container mt-4">
    <div class="chart-card">
        <h4>
            <span class="badge bg-info text-dark">
                <i class="bi bi-lightning-charge-fill"></i>
                Streamlit Built-in Charts
            </span>
        </h4>
    </div>
</div>
""", unsafe_allow_html=True)

df = pd.DataFrame({"Marks": y})
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
