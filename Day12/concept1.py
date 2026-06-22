from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#── Exercise 1 — Few-shot sentiment classifier ──────────────────
def classify_sentiment(text):
    prompt = f"""
Classify sentiment as positive or negative. Return ONLY one word.

Examples:
Text: "I love this product" → positive
Text: "Terrible experience" → negative
Text: "Not worth the money" → negative

Now classify:
Text: "{text}" →"""
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt)
    return response.text.strip().lower()

#── Exercise 2 — Chain of thought ──────────────────────────────
def solve_with_reasoning(problem):
    prompt = f"""
Solve this step by step, then give a final answer on the last line.

Problem: {problem}

Let's think step by step:"""
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt)
    return response.text

# ── Exercise 3 — Structured JSON output ────────────────────────
def analyze_resume_bullet(bullet):
    prompt = f"""
You are a technical recruiter for AI roles.
Analyze this resume bullet and return ONLY valid JSON, nothing else.

Bullet: "{bullet}"

Return this exact JSON structure:
{{
  "score": <number 1-10>,
  "issues": ["issue1", "issue2"],
  "rewritten": "improved version here",
  "keywords_to_add": ["keyword1", "keyword2"]
}}"""
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt)
    raw = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(raw)

#── Exercise 4 — Role prompting ─────────────────────────────────
def code_review(code):
    prompt = f"""
You are a senior GenAI engineer with 10 years experience.
Review this Python code brutally and honestly.
Point out issues, bad practices, and suggest improvements.
Keep it under 5 bullet points.

Code:
{code}"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", contents=prompt)
    return response.text

#── Exercise 5 — Upgraded Interview Coach prompt ────────────────
def interview_coach(question):
    prompt = f"""
You are an expert GenAI interview coach who has helped 500+ candidates
land roles at top AI companies.

When answering interview questions:
1. Give a 1-line definition first
2. Explain with a real-world analogy
3. Give a specific technical example
4. End with one tip to impress the interviewer

Keep total response under 150 words.

Question: {question}"""
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite", contents=prompt)
    return response.text

#─ Run all exercises ───────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 50)
    print("EXERCISE 1 — Few-shot sentiment")
    print("=" * 50)
    print(classify_sentiment("This course is incredible"))
    print(classify_sentiment("Waste of time"))
    print(classify_sentiment("Not bad but could be better"))

    print("\n" + "=" * 50)
    print("EXERCISE 2 — Chain of thought")
    print("=" * 50)
    print(solve_with_reasoning(
        "I have 3 GenAI projects. Each takes 1 week to build and "
        "1 day to deploy. How many days total to complete all 3?"
    ))

    print("\n" + "=" * 50)
    print("EXERCISE 3 — Structured JSON output")
    print("=" * 50)
    result = analyze_resume_bullet("Built a chatbot using Python")
    print(json.dumps(result, indent=2))

    print("\n" + "=" * 50)
    print("EXERCISE 4 — Role prompting")
    print("=" * 50)
    print(code_review("""
def get_response(prompt):
    response = client.models.generate_content(
        model="gemini-1.5-flash", contents=prompt)
    return response
"""))

    print("\n" + "=" * 50)
    print("EXERCISE 5 — Upgraded interview coach")
    print("=" * 50)
    print(interview_coach("What is RAG and how does it work?"))