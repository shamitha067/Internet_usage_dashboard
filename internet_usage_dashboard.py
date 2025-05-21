import os
import pandas as pd
import streamlit as st

DATA_DIR = 'data'
DATA_USAGE_PATH = os.path.join(DATA_DIR, 'internet_usage.csv')

# Step 1: Ensure the CSV file exists BEFORE loading
def ensure_csv_exists():
    if not os.path.exists(DATA_USAGE_PATH):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        csv_content = """Country,Year,Internet_Users_Pct
India,2010,7.5
India,2015,27.0
India,2020,50.0
USA,2010,71.7
USA,2015,74.6
USA,2020,87.0
China,2010,34.3
China,2015,50.3
China,2020,70.4
Brazil,2010,40.6
Brazil,2015,57.6
Brazil,2020,74.2
"""
        with open(DATA_USAGE_PATH, 'w') as f:
            f.write(csv_content)
        print("✔️ CSV created.")

# Step 2: Load the CSV data (this can be cached safely)
@st.cache_data
def load_usage_data():
    return pd.read_csv(DATA_USAGE_PATH)

# Streamlit UI
st.set_page_config(page_title="Internet Usage Dashboard", layout="wide")
st.title("🌐 Internet Usage Dashboard")

# Step 3: Ensure file is there before loading
ensure_csv_exists()
df_usage = load_usage_data()

# Step 4: Show data and chart
st.subheader("📊 Internet Usage Data")
st.dataframe(df_usage)

st.subheader("📈 Internet Usage Over Time")
selected_country = st.selectbox("Select Country", df_usage['Country'].unique())
filtered_df = df_usage[df_usage['Country'] == selected_country]
st.line_chart(filtered_df.set_index("Year")["Internet_Users_Pct"])
