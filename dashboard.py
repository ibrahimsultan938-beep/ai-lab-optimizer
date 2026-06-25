import pandas as pd
import streamlit as st

# ==============================
# PAGE CONFIG + TITLE
# ==============================
st.set_page_config(
    page_title="AI GPU Resource Optimizer",
    layout="wide"
)

st.title("🤖 AI GPU Resource Optimizer")
st.subheader("Smart GPU Monitoring & Resource Allocation System")

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("lab_usage.csv")

# ==============================
# STATUS CALCULATION
# ==============================
status = []

for usage in df["GPU_Usage"]:
    if usage > 80:
        status.append("Overloaded")
    elif usage < 30:
        status.append("Underutilized")
    else:
        status.append("Normal")

df["Status"] = status

# ==============================
# BASIC METRICS
# ==============================
total_pcs = len(df)
overloaded_count = len(df[df["Status"] == "Overloaded"])
underutilized_count = len(df[df["Status"] == "Underutilized"])
avg_usage = df["GPU_Usage"].mean()

# ==============================
# KPI DASHBOARD
# ==============================
st.subheader("📌 System Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Systems", total_pcs)
col2.metric("Overloaded GPUs", overloaded_count)
col3.metric("Underutilized GPUs", underutilized_count)
col4.metric("Avg GPU Usage", f"{avg_usage:.2f}%")

st.divider()

# ==============================
# FULL TABLE
# ==============================
st.subheader("📊 Full GPU Resource Overview")
st.dataframe(df, use_container_width=True)

# ==============================
# GPU USAGE CHART
# ==============================
st.subheader("📈 GPU Usage per System")
st.bar_chart(df.set_index("PC")["GPU_Usage"])

# ==============================
# STATUS DISTRIBUTION
# ==============================
st.subheader("📊 Status Distribution")

status_counts = df["Status"].value_counts()
st.bar_chart(status_counts)

st.divider()

# ==============================
# ALERT SYSTEM
# ==============================
st.subheader("🚨 Live Alert System")

if overloaded_count > 0:
    st.error(
        f"⚠️ ALERT: {overloaded_count} GPU-enabled systems are overloaded!"
    )
    st.warning(
        "Immediate workload redistribution is recommended."
    )
else:
    st.success(
        "✅ System Stable: No critical overload detected."
    )

st.divider()

# ==============================
# SMART RECOMMENDATION ENGINE
# ==============================
st.subheader("🧠 AI Smart Recommendation Engine")

best_pcs = (
    df[df["Status"] == "Underutilized"]
    .sort_values(by="GPU_Usage")
    .head(3)
)

if not best_pcs.empty:
    st.write(
        "👉 Recommended systems for assigning new AI workloads:"
    )
    st.dataframe(best_pcs, use_container_width=True)
else:
    st.info(
        "No underutilized systems are currently available."
    )

st.divider()

# ==============================
# EFFICIENCY SCORE
# ==============================
st.subheader("📊 System Efficiency Score")

imbalance = abs(
    overloaded_count - underutilized_count
)

if imbalance > 3:
    st.error(
        "❌ Low Efficiency: Significant resource imbalance detected."
    )
elif imbalance > 1:
    st.warning(
        "⚠️ Moderate Efficiency: Some imbalance exists."
    )
else:
    st.success(
        "✅ High Efficiency: Resources are well balanced."
    )

st.divider()

# ==============================
# FILTER SYSTEM
# ==============================
st.subheader("🔍 Filter Systems by Status")

selected_status = st.selectbox(
    "Select Status",
    ["All", "Overloaded", "Underutilized", "Normal"]
)

if selected_status != "All":
    filtered_df = df[df["Status"] == selected_status]
else:
    filtered_df = df

st.dataframe(filtered_df, use_container_width=True)

st.divider()

# ==============================
# SEARCH SYSTEM
# ==============================
st.subheader("🔎 Search System")

pc_name = st.text_input(
    "Enter System Name (Example: PC1)"
)

if pc_name:
    result = df[
        df["PC"].str.lower() == pc_name.lower()
    ]

    if not result.empty:
        st.dataframe(result, use_container_width=True)
    else:
        st.error("System not found.")

st.divider()

# ==============================
# AI PREDICTION ENGINE
# ==============================
st.subheader("🧠 AI Prediction Engine")

if avg_usage > 75:
    st.error(
        "Prediction: High GPU demand expected for upcoming AI training workloads."
    )
elif avg_usage > 50:
    st.warning(
        "Prediction: Moderate GPU demand expected."
    )
else:
        st.success(
        "Prediction: Current GPU resources appear sufficient for upcoming workloads."
    )

st.divider()

# ==============================
# FINAL SUMMARY
# ==============================
st.subheader("📋 Executive Summary")

st.info(
    f"""
    Total Systems: {total_pcs}

    Overloaded Systems: {overloaded_count}

    Underutilized Systems: {underutilized_count}

    Average GPU Utilization: {avg_usage:.2f}%

    This prototype demonstrates intelligent GPU resource monitoring,
    workload balancing, and optimization recommendations for
    university AI laboratories.
    """
)
