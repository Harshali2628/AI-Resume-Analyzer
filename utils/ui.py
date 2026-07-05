import streamlit as st


def show_resume_status(score):

    if score >= 80:
        st.success("⭐⭐⭐⭐⭐ Excellent Resume")

    elif score >= 60:
        st.warning("⭐⭐⭐ Good Resume")

    else:
        st.error("⚠ Needs Improvement")