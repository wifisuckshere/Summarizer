import requests

prompt = "Summarize the Singleton pattern."

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3", "prompt": prompt, "stream": False},
)

print(response.text)