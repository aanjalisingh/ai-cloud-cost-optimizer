import requests

def call_llm(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=300)
        response.raise_for_status()
        return response.json()["response"].strip()

    except Exception as e:
        print("LLM Error:", e)
        return None
