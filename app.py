# app.py

import streamlit as st
from planner import (
    calculate_current_attendance,
    calculate_bunkable_classes,
    project_attendance_if_all_attended
)

st.set_page_config(page_title="Smart Attendance Bunk Planner")#, layout="centered")

st.title("🎓 Smart Attendance Bunk Planner")
st.markdown("Plan your class bunks smartly without dropping below required attendance!")

# --- Input Section ---
st.header("📝 Enter Your Details")

attended = st.number_input("✔️ Classes Attended", min_value=0, value=76)
conducted = st.number_input("📚 Total Classes Conducted", min_value=1, value=100)
upcoming = st.number_input("📅 Upcoming Classes", min_value=0, value=10)
min_required = st.slider("📉 Minimum Attendance Requirement (%)", min_value=50, max_value=100, value=75)

if st.button("📊 Show Analysis"):
    # --- Calculations ---
    current_percent = calculate_current_attendance(attended, conducted)
    max_bunkable = calculate_bunkable_classes(attended, conducted, upcoming, min_required)
    future_percent = project_attendance_if_all_attended(attended, conducted, upcoming)

    # --- Display ---
    st.subheader("📈 Results")
    st.success(f"✅ Current Attendance: **{current_percent}%**")
    st.info(f"📌 You can safely bunk **{max_bunkable}** more class(es) and still maintain **{min_required}%** attendance.")
    st.warning(f"📈 If you attend all upcoming classes, final attendance will be: **{future_percent}%**")

    if max_bunkable == 0:
        st.error("⚠️ Warning: You cannot bunk any more classes without dropping below the limit!")

# Footer
st.markdown("---")
st.markdown("👨‍💻 Built by Yash Kakadiya for Hackathons")


