import streamlit as st
import pandas as pd
import plotly.express as px

# Setup page configuration
st.set_page_config(page_title="Titanic Dashboard", page_icon="🚢", layout="wide")

st.title("RMS Titanic Passenger Dashboard")
st.markdown("Explore the demographics and survival rates of passengers aboard the Titanic.")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("titanic.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

# Sex Filter
selected_sex = st.sidebar.multiselect(
    "Select Sex", 
    options=df["Sex"].unique(), 
    default=df["Sex"].unique()
)

# Pclass Filter
selected_pclass = st.sidebar.multiselect(
    "Select Passenger Class (Pclass)", 
    options=sorted(df["Pclass"].unique()), 
    default=sorted(df["Pclass"].unique())
)

# Age Range Filter
min_age = float(df["Age"].min())
max_age = float(df["Age"].max())
age_range = st.sidebar.slider(
    "Select Age Range", 
    min_value=min_age, 
    max_value=max_age, 
    value=(min_age, max_age)
)

# Apply Filters
filtered_df = df[
    (df["Sex"].isin(selected_sex)) &
    (df["Pclass"].isin(selected_pclass)) &
    (df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])
]

# KPIs
st.markdown("### Key Performance Indicators")
col1, col2, col3 = st.columns(3)

total_passengers = len(filtered_df)
survival_rate = (filtered_df["Survived"].mean() * 100) if total_passengers > 0 else 0
average_fare = filtered_df["Fare"].mean() if total_passengers > 0 else 0

col1.metric("Total Passengers", f"{total_passengers:,}")
col2.metric("Survival Rate", f"{survival_rate:.2f}%")
col3.metric("Average Fare", f"${average_fare:.2f}")

st.markdown("---")

# Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### Survival by Passenger Class")
    if not filtered_df.empty:
        # Group data for Plotly
        surv_class = filtered_df.groupby(["Pclass", "Survived"]).size().reset_index(name="Count")
        surv_class["Survived_Label"] = surv_class["Survived"].map({0: "Did not survive", 1: "Survived"})
        
        fig_class = px.bar(
            surv_class, x="Pclass", y="Count", color="Survived_Label",
            barmode="group",
            labels={"Pclass": "Passenger Class"},
            color_discrete_sequence=["#EF553B", "#00CC96"]
        )
        st.plotly_chart(fig_class, use_container_width=True)
    else:
        st.warning("No data matches the selected filters.")

with col_right:
    st.markdown("### Age Distribution")
    if not filtered_df.empty:
        filtered_df_copy = filtered_df.copy()
        filtered_df_copy["Survived_Label"] = filtered_df_copy["Survived"].map({0: "Did not survive", 1: "Survived"})
        
        fig_age = px.histogram(
            filtered_df_copy, x="Age", color="Survived_Label",
            nbins=30, marginal="box",
            color_discrete_sequence=["#EF553B", "#00CC96"]
        )
        st.plotly_chart(fig_age, use_container_width=True)
    else:
        st.warning("No data matches the selected filters.")

st.markdown("### Fare vs. Survival")
if not filtered_df.empty:
    filtered_df_copy = filtered_df.copy()
    filtered_df_copy["Survived_Label"] = filtered_df_copy["Survived"].map({0: "Did not survive", 1: "Survived"})
    fig_fare = px.box(
        filtered_df_copy, x="Survived_Label", y="Fare", color="Survived_Label",
        points="all",
        color_discrete_sequence=["#EF553B", "#00CC96"]
    )
    st.plotly_chart(fig_fare, use_container_width=True)

st.markdown("---")

# Raw Data
with st.expander("Explore Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)
