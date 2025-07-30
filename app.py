import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve

# Set page config
st.set_page_config(page_title="Smart Login Risk Score Generator", layout="wide")

st.title("🔐 Smart Login Risk Score Generator Dashboard")

# Load your DataFrame (replace with your own CSV if needed)
@st.cache_data
def load_data():
    return pd.read_csv("dataset/scored_login_predictions.csv")


df = load_data()

# --- Risk Category Mapping ---
def categorize_risk(score):
    if score > 90:
        return "Critical"
    elif score > 70:
        return "High"
    elif score > 50:
        return "Medium"
    else:
        return "Low"

df["risk_category"] = df["risk_score"].apply(categorize_risk)

# --- Sidebar Filter ---
selected_category = st.sidebar.selectbox("Filter by Risk Category", ["All", "Critical", "High", "Medium", "Low"])
if selected_category != "All":
    df_filtered = df[df["risk_category"] == selected_category]
else:
    df_filtered = df

st.markdown(f"### 🔍 Showing {len(df_filtered)} login attempts in category: {selected_category}")

# --- Display Top Suspicious Logins ---
st.markdown("### 🔝 Top 10 Suspicious Logins")
top_10 = df_filtered.sort_values(by="risk_score", ascending=False).head(10)
st.dataframe(top_10.style.highlight_max(axis=0), use_container_width=True)

# --- Risk Score Histogram ---
st.markdown("### 📊 Risk Score Distribution")
fig1, ax1 = plt.subplots()
df["risk_score"].hist(bins=20, color='orange', edgecolor='black', ax=ax1)
ax1.set_title("Distribution of Risk Scores")
ax1.set_xlabel("Risk Score")
ax1.set_ylabel("Frequency")
st.pyplot(fig1)

# --- Precision-Recall Curve ---
st.markdown("### 📈 Precision & Recall vs Threshold")

# Generate curve using test labels and scores
precision, recall, thresholds = precision_recall_curve(df["actual_label"], df["risk_score"] / 100)

fig2, ax2 = plt.subplots()
ax2.plot(thresholds, precision[:-1], label='Precision', color='blue')
ax2.plot(thresholds, recall[:-1], label='Recall', color='green')
ax2.set_xlabel('Threshold')
ax2.set_ylabel('Score')
ax2.set_title('Precision and Recall vs Threshold')
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

st.markdown("---")
st.markdown("*This system was optimized for high recall to detect suspicious logins, while minimizing false negatives. Thresholds and scores are adjustable for real-world deployment.*")

import streamlit as st

# Divider line
st.markdown("---")

# Footer content
st.markdown(
    "<div style='text-align: center; font-size: 16px;'>"
    " <em>This tool flags suspicious login attempts and helps security teams mitigate potential breaches.</em><br>"
    "</div>",
    unsafe_allow_html=True
)
