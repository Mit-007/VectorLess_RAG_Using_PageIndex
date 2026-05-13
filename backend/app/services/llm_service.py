from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(
    api_key=GOOGLE_API_KEY
)

async def call_llm(prompt,model="gemini-3.1-flash-lite-preview",temperature=0):
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={
            "temperature": temperature,
            "tools":[]
        }
    )

    tree_search_result=response.text.strip()

    if tree_search_result.startswith("```"):
        tree_search_result = tree_search_result.replace("```json", "")
        tree_search_result = tree_search_result.replace("```", "")
        tree_search_result = tree_search_result.strip()

    return tree_search_result

