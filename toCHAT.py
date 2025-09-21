import requests
from flask import Response
import json


def toChat(prompt):
    def generate():
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": True},
            stream=True,
        )
        for line in r.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    print("CHUNK >>>", data["response"])
                    yield data["response"]
            except:
                pass
    return Response(generate(), mimetype="text/plain")