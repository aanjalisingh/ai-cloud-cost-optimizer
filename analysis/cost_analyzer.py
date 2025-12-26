import json
from pathlib import Path

BILLING_FILE = Path("data/generated_billing.json")
PROFILE_FILE = Path("data/project_profile.json")
OUTPUT_FILE = Path("data/cost_optimization_report.json")


def analyze_costs():
    try:

        # Load billing

        if not BILLING_FILE.exists():
            raise FileNotFoundError("generated_billing.json not found")

        with open(BILLING_FILE, "r", encoding="utf-8") as f:
            billing = json.load(f)


        # Load project profile

        if not PROFILE_FILE.exists():
            raise FileNotFoundError("project_profile.json not found")

        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            profile_data = json.load(f)

        # FIX: profile is a LIST
        if isinstance(profile_data, dict):
            project = profile_data

        elif isinstance(profile_data, list) and len(profile_data) > 0:
            project = profile_data[0]

        else:
            raise ValueError("Invalid project_profile.json format")

        budget = project.get("budget_inr_per_month", 50000)


        # Cost aggregation

        total_cost = sum(item["cost_inr"] for item in billing)
        variance = budget - total_cost


        # Recommendations

        recommendations = []

        for item in billing:
            if item["service"] == "Compute":
                recommendations.append({
                    "title": "Switch to Reserved Instances",
                    "current_cost": item["cost_inr"],
                    "potential_savings": 4000,
                    "cloud_providers": ["AWS", "Azure", "GCP"]
                })

            if item["service"] == "Monitoring":
                recommendations.append({
                    "title": "Use Open-Source Monitoring",
                    "current_cost": item["cost_inr"],
                    "potential_savings": item["cost_inr"],
                    "cloud_providers": ["Open Source"]
                })


        # Final report (STRICT FORMAT)

        report = {
            "total_cost_inr": total_cost,
            "budget_inr": budget,
            "variance_inr": variance,
            "over_budget": total_cost > budget,
            "recommendations": recommendations
        }


        # Write JSON to file

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print(" cost_optimization_report.json generated successfully")

    except json.JSONDecodeError:
        print(" JSON parsing failed")

    except Exception as e:
        print(f" Error: {e}")
