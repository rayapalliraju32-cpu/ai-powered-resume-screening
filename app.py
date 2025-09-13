from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Dummy resume parser function
def parse_resume(text):
    skills = re.findall(r"Python|Java|C\+\+|SQL|Machine Learning|AI", text, re.IGNORECASE)
    return {
        "skills": list(set([s.lower() for s in skills])),
        "experience": "2 years (dummy)",
        "education": "B.Tech (dummy)"
    }

@app.route("/")
def home():
    return "AI Powered Resume Screening System is Running ✅"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    resume_text = data.get("resume", "")
    job_desc = data.get("job_desc", "")

    resume_data = parse_resume(resume_text)

    # Dummy score calculation
    score = 0
    for skill in resume_data["skills"]:
        if skill.lower() in job_desc.lower():
            score += 10

    return jsonify({
        "parsed_resume": resume_data,
        "job_desc": job_desc,
        "match_score": score
    })

if __name__ == "__main__":
    app.run(debug=True)
