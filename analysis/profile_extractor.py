import json
from llm.llm_client import call_llm

def extract_profile():
    with open("data/project_description.txt", "r") as f:
        description = f.read()

    prompt = f"""
Convert the following project description into VALID JSON.

Required fields:
- name
- budget_inr_per_month
- description
- tech_stack
- non_functional_requirements

Return ONLY JSON. No explanation.

Text:
{description}
"""

    response = call_llm(prompt)

    if not response:
        print("LLM failed")
        return

    try:
        profile = json.loads(response)
    except:
        print("Invalid JSON from LLM")
        print(response)
        return

    with open("data/project_profile.json", "w") as f:
        json.dump(profile, f, indent=2)

    print("project_profile.json created")
