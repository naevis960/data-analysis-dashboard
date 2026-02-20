import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="Data Analysis Dashboard", layout="wide")
st.title("📊 Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("📋 Data Preview")
    st.dataframe(df.head(50))

    st.subheader("📈 Statistics")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()

    if numeric_cols:
        st.subheader("📊 Visualization")
        chart_type = st.selectbox("Chart Type", ["Line", "Bar", "Scatter", "Histogram"])
        x_col = st.selectbox("X Axis", df.columns)
        y_col = st.selectbox("Y Axis", numeric_cols)

        if chart_type == "Line":
            fig = px.line(df, x=x_col, y=y_col)
        elif chart_type == "Bar":
            fig = px.bar(df, x=x_col, y=y_col)
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_col, y=y_col)
        else:
            fig = px.histogram(df, x=y_col)

        st.plotly_chart(fig, use_container_width=True)

    csv = df.to_csv(index=False)
    st.download_button("💾 Download CSV", csv, "processed_data.csv", "text/csv")
else:
    st.info("Upload a file to get started!")
