import streamlit as st
import pandas as pd
from scoring_engine import compute_dqs
from llm_agent import generate_insight
from dimension_detector import detect_dimensions

st.set_page_config(page_title="Visa DQS Agent", layout="wide")

st.title("GenAI Data Quality Agent for Payments")

uploaded_file = st.file_uploader("Upload Payments CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    dimensions = detect_dimensions(df)
    st.subheader("Agent-Detected Dimensions")
    st.write(dimensions)

    scores, composite = compute_dqs(df)

    st.subheader(" Data Quality Scores")
    for k, v in scores.items():
        st.progress(v / 100)
        st.write(f"{k}: {v}%")

    st.metric("Composite DQS", f"{composite}%")

    st.subheader(" AI Explanation")
    with st.spinner("Analyzing data quality..."):
        insight = generate_insight(scores, composite)
        st.write(insight)
