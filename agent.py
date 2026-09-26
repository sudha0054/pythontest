import os

from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Set the GEMINI_API_KEY environment variable before running this script.")

client = genai.Client(
    api_key=api_key
)

def agent(user_prompt):
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user_prompt
    )

    return response.text


while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    answer = agent(prompt)

    print("Agent:", answer)