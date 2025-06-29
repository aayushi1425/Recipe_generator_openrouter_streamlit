import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_recipe(ingredients):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    You are a recipe expert. I have these ingredients: {', '.join(ingredients)}.
    Suggest a detailed Indian recipe with a title, ingredients list, and instructions.
    """

    data = {
    "model": "mistralai/mistral-7b-instruct",  #Correct ID
    "messages": [
        {"role": "user", "content": prompt}
    ]
}


    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )

        response_json = response.json()
        if "choices" not in response_json:
            # Log the error details for debugging
            return f"API Error:\n{response_json}"

        return response_json["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Exception occurred:\n{str(e)}"
