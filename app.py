import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_helper import analyze_resume

from utils.report_generator import create_pdf

from utils.charts import show_gauge, show_pie
from utils.ui import show_resume_status



st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

st.sidebar.title("📄 AI Resume Analyzer")

st.sidebar.markdown("---")

st.sidebar.info(
"""
### Features

✅ ATS Score

✅ Skill Gap Analysis

✅ Resume Suggestions

✅ Interview Questions
"""
)

st.sidebar.markdown("---")


st.sidebar.success("🤖 Powered by Gemini AI")

st.sidebar.info(
"""
📌 Version : 1.0

👩‍💻 Developer:
Harshali Panchal
"""
)

st.title("📄 AI Resume Analyzer")

st.caption(
"Analyze your resume against any Job Description using Gemini AI."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    uploaded_file = st.file_uploader(
        "📂 Upload Resume",
        type=["pdf"]
    )

with col2:

    job_description = st.text_area(
        "📝 Paste Job Description",
        height=250
    )

if uploaded_file is not None and job_description:

    resume_text = extract_text_from_pdf(uploaded_file)

    analyze = st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    )

    if analyze:

        with st.spinner("🤖 Gemini is analyzing your resume..."):

            result = analyze_resume(
                resume_text,
                job_description
            )

        st.success("✅ Analysis Completed Successfully!")

        with st.container():

            st.markdown("## 📋 Analysis Report")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "🎯 ATS Score",
                    f"{result['ats_score']}%"
                )

            with col2:
                st.metric(
                    "💼 Matching Skills",
                    len(result["matching_skills"])
                )

            with col3:
                st.metric(
                    "⚠ Missing Skills",
                    len(result["missing_skills"])
                )

            st.progress(result["ats_score"] / 100)


            

            chart1, chart2 = st.columns(2)

            with chart1:
                show_gauge(result["ats_score"])

            with chart2:
                show_pie(
                    len(result["matching_skills"]),
                    len(result["missing_skills"])
                )
            


            show_resume_status(result["ats_score"])

            with st.expander("✅ Matching Skills", expanded=True):

                for skill in result["matching_skills"]:
                    st.success(skill)

            with st.expander("❌ Missing Skills", expanded=True):

                for skill in result["missing_skills"]:
                    st.error(skill)

            with st.expander("💪 Strengths"):

                for item in result["strengths"]:
                    st.success(item)

            with st.expander("⚠ Weaknesses"):

                for item in result["weaknesses"]:
                    st.warning(item)

            with st.expander("💡 Suggestions"):

                for item in result["suggestions"]:
                    st.info(item)
    
            with st.expander("🎤 Interview Questions"):

                for question in result["interview_questions"]:
                    st.write("✅", question)

            pdf_file = create_pdf(result)

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="📥 Download PDF Report",
                    data=file,
                    file_name="Resume_Analysis_Report.pdf",
                    mime="application/pdf"
                )


            st.divider()

            st.markdown(
                """
                <center>
                    <b>AI Resume Analyzer</b><br>
                    Developed by <b>Harshali Panchal</b><br>
                    Powered by Gemini AI | Streamlit | Python
                </center>
                """,
                unsafe_allow_html=True
            )