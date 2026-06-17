import pandas as pd
import streamlit as st

# ==============================
# 🟢 PAGE CONFIG + TITLE
# ==============================
st.set_page_config(page_title="AI Lab Optimizer", layout="wide")

st.title("🤖 AI Lab Resource Optimizer")
st.subheader("Smart Monitoring & Resource Allocation System")

# ==============================
# 📂 LOAD DATA
# ==============================
df = pd.read_csv("lab_usage.csv")

# ==============================
# 🧠 STATUS CALCULATION
# ==============================
status = []

for usage in df["CPU_Usage"]:
    if usage > 80:
        status.append("Overloaded")
    elif usage < 30:
        status.append("Underutilized")
    else:
        status.append("Normal")

df["Status"] = status

# ==============================
# 📊 BASIC METRICS
# ==============================
total_pcs = len(df)
overloaded_count = len(df[df["Status"] == "Overloaded"])
underutilized_count = len(df[df["Status"] == "Underutilized"])
avg_usage = df["CPU_Usage"].mean()

# ==============================
# 📌 KPI DASHBOARD
# ==============================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total PCs", total_pcs)
col2.metric("Overloaded", overloaded_count)
col3.metric("Underutilized", underutilized_count)
col4.metric("Avg CPU %", f"{avg_usage:.2f}%")

st.divider()

# ==============================
# 📊 DATA TABLE
# ==============================
st.subheader("📊 Full System Overview")
st.dataframe(df, use_container_width=True)

# ==============================
# 📈 CPU USAGE CHART (Streamlit built-in)
# ==============================
st.subheader("📈 CPU Usage per PC")
st.bar_chart(df.set_index("PC")["CPU_Usage"])

# ==============================
# 📊 STATUS DISTRIBUTION
# ==============================
st.subheader("📊 System Status Distribution")
status_counts = df["Status"].value_counts()
st.bar_chart(status_counts)

st.divider()

# ==============================
# 🚨 ALERT SYSTEM
# ==============================
st.subheader("🚨 Live Alert System")

if overloaded_count > 0:
    st.error(f"⚠️ ALERT: {overloaded_count} PCs are overloaded!")
    st.warning("Immediate workload redistribution recommended.")
else:
    st.success("✅ System Stable: No critical overload detected.")

st.divider()

# ==============================
# 🧠 AI SMART RECOMMENDATION
# ==============================
st.subheader("🧠 AI Smart Recommendation Engine")

best_pcs = df[df["Status"] == "Underutilized"].sort_values(by="CPU_Usage").head(3)

if not best_pcs.empty:
    st.write("👉 Best PCs for new workload assignment:")
    st.dataframe(best_pcs, use_container_width=True)
else:
    st.info("No suitable idle PCs available.")

st.divider()

# ==============================
# 📊 EFFICIENCY SCORE
# ==============================
st.subheader("📊 System Efficiency Score")

imbalance = overloaded_count - underutilized_count

if imbalance > 5:
    st.error("❌ Low Efficiency: High imbalance detected")
elif imbalance > 0:
    st.warning("⚠️ Moderate imbalance in system")
else:
    st.success("✅ High Efficiency: Balanced system")

st.divider()

# ==============================
# 🔍 FILTER SYSTEM
# ==============================
st.subheader("🔍 Filter PCs by Status")

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
# 🔎 SEARCH FEATURE
# ==============================
st.subheader("🔍 Search PC")

pc_name = st.text_input("Enter PC Name (e.g., PC1)")

if pc_name:
    result = df[df["PC"].str.lower() == pc_name.lower()]

    if not result.empty:
        st.dataframe(result, use_container_width=True)
    else:
        st.error("PC not found")

st.divider()

# ==============================
# 🧠 AI PREDICTION ENGINE
# ==============================
st.subheader("🧠 AI Prediction Engine")

if avg_usage > 75:
    st.error("Prediction: High load expected in upcoming sessions.")
elif avg_usage > 50:
    st.warning("Prediction: Moderate load expected.")
else:
    st.success("Prediction: System is stable for upcoming usage.")