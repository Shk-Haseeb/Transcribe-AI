import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_summary(text):
    prompt = (
        "You are an assistant that summarizes meeting transcripts. "
        "Summarize the following text in a concise paragraph:\n\n"
        f"{text}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content.strip()

def simplify_text(text):
    prompt = (
        "You are an assistant that simplifies complex meeting transcripts into easy-to-understand notes. "
        "Rewrite the following text in simple, clear language:\n\n"
        f"{text}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
    )

    return response.choices[0].message.content.strip()
