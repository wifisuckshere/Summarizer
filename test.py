import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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"
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1:fireworks-ai",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)