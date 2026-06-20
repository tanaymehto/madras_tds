import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer dummy_api_key",
    "Content-Type": "application/json",
}

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "Analyze the sentiment of the given text and classify it as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": "d fMZug pX i5Mqz6VJ D s4M2jWL R OL Rx4  ejyoo67"
        }
    ]
}

response = httpx.post(url, json=payload, headers=headers)
response.raise_for_status()
result = response.json()
print(result)