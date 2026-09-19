import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def summarize_text(text, length="medium", style="simple"):
    system_prompt = f"You are a summarization assistant. Summarize the given text in a {length} length, using a {style} style."
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.3,
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    sample = "Artificial intelligence is transforming industries by automating tasks, improving decision-making, and enabling new products."
    print(summarize_text(sample, length="short", style="simple"))
