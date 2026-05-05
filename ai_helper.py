import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_logs():
    with open("logs/error.log", "r") as f:
        logs = f.read()

    prompt = f"""
    You are a senior DevOps engineer.
    Analyze this Jenkins failure log.

    Provide:
    1. Root cause
    2. Fix
    3. Preventive action

    Logs:
    {logs}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    analyze_logs()
