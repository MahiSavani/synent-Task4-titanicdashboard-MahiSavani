
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🚢 Titanic Dashboard")

# Upload CSV
file = st.file_uploader("Upload Titanic CSV", type=["csv"])

if file is not None:

    df = pd.read_csv(file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Sidebar Filters
    st.sidebar.header("Filters")

    gender = st.sidebar.multiselect(
        "Gender",
        df["Sex"].unique(),
        default=df["Sex"].unique()
    )

    # Filter
    filtered_df = df[df["Sex"].isin(gender)]

    # KPI
    st.subheader("Summary")

    total = filtered_df.shape[0]
    survived = filtered_df["Survived"].sum()

    col1, col2 = st.columns(2)

    col1.metric("Total Passengers", total)
    col2.metric("Survived", int(survived))

    # Chart
    st.subheader("Survival Count")

    fig, ax = plt.subplots()

    sns.countplot(
        data=filtered_df,
        x="Survived",
        ax=ax
    )

    st.pyplot(fig)

    # Gender Chart
    st.subheader("Gender Wise Survival")

    fig, ax = plt.subplots()

    sns.countplot(
        data=filtered_df,
        x="Sex",
        hue="Survived",
        ax=ax
    )

    st.pyplot(fig)

else:
    st.warning("Please upload Titanic CSV file")
