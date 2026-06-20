import httpx

response = httpx.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": "Bearer dummy-api-key",
        "Content-Type": "application/json"
    },
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "Analyze the sentiment of the text and classify it as GOOD, BAD, or NEUTRAL."
            },
            {
                "role": "user",
                "content": "d fMZug pX i5Mqz6VJ D s4M2jWL R OL Rx4  ejyoo67"
            }
        ]
    }
)

response.raise_for_status()
print(response.json())