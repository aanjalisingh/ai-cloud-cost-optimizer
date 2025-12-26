import json
import os
from llm.llm_client import call_llm

OUTPUT_FILE = "data/generated_billing.json"

def generate_billing():
    prompt = """
Generate ONLY a valid JSON array.
NO explanation.
NO markdown.

Format:
[
  {"service": "Compute", "cost_inr": 15000, "desc": "Backend server"},
  {"service": "Database", "cost_inr": 10000, "desc": "PostgreSQL DB"},
  {"service": "Storage", "cost_inr": 5000, "desc": "Image storage"},
  {"service": "Monitoring", "cost_inr": 2000, "desc": "Uptime checks"},
  {"service": "Networking", "cost_inr": 7000, "desc": "Traffic costs"}
]
"""

    raw_response = call_llm(prompt)

    try:
        #  CONVERT STRING → JSON
        billing_json = json.loads(raw_response)
    except Exception as e:
        print(" Invalid billing JSON")
        print(raw_response)
        return None

    os.makedirs("data", exist_ok=True)

    # SAVE AS PROPER FORMATTED JSON
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(billing_json, f, indent=2)

    print(f"Synthetic billing saved to {OUTPUT_FILE}")
    return billing_json
