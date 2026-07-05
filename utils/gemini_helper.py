import os
import json
from unittest import result
from urllib import response
from dotenv import load_dotenv
import google.generativeai as genai


# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze the resume against the job description.

Return ONLY valid JSON.

Do not add explanation.
Do not use markdown.
Do not use ```.

Return in this exact format:

{{
"ats_score": 0,
"matching_skills": [],
"missing_skills": [],
"strengths": [],
"weaknesses": [],
"suggestions": [],
"interview_questions": []
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""
    response = model.generate_content(prompt)

    result = response.text.strip()

    data = json.loads(result)

    return data