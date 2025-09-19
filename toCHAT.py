import requests

def toChat(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,  # use prompt directly
            "stream": False
        }
    )

    data = response.json()
    return data.get("response", "")