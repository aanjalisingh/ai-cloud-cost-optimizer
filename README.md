AI Powered Cloud Cost Optimizer
📌 Project Overview

The AI Powered Cloud Cost Optimizer is a command-line based application that uses a Large Language Model (LLM) to analyze cloud project requirements, generate synthetic billing data, and provide actionable cost optimization recommendations.

This project demonstrates how AI can assist in cloud cost management, budget analysis, and multi-cloud optimization, following best practices in modular Python design.

🎯 Key Objectives

Extract structured project profiles from natural language descriptions

Generate realistic synthetic cloud billing data

Analyze costs against budget constraints

Provide optimization recommendations including:

Cost savings

Risks

Open-source alternatives

Multi-cloud strategies

Orchestrate the entire workflow using a CLI interface

🏗️ Project Architecture
ai_cloud_optimiser/
│
├── analysis/
│   ├── profile_extractor.py
│   ├── cost_analyzer.py
│
├── billing/
│   ├── billing_generator.py
│
├── cli/
│   ├── menu.py
│
├── llm/
│   ├── llm_client.py
│
├── data/
│   ├── generated_billing.json
│
├── project_description.txt
├── project_profile.json
├── cost_optimization_report.json
├── main.py
├── requirements.txt
└── README.md

🧠 Technologies Used

Python 3.10+

TinyLLaMA (via Ollama – local LLM inference)

Requests (API communication)

JSON (data interchange format)

Virtual Environment (venv)

🔁 Workflow (As Per Assignment Tasks)
1. Profile Extraction

User enters a project description via CLI

Description saved to project_description.txt

LLM converts description into structured JSON:

Output → project_profile.json

Invalid LLM responses are handled safely

2. Billing Generation

Input → project_profile.json

LLM generates 12–20 billing records

Costs distributed across:

Compute

Database

Storage

Networking

Monitoring

Output → data/generated_billing.json

3. Cost Analysis & Recommendations

Inputs:

project_profile.json

generated_billing.json

Calculates:

Total cost

Budget variance

Over-budget flag

Generates:

5–8 optimization recommendations

Savings estimates

Open-source alternatives

Multi-cloud options

Output → cost_optimization_report.json

4. CLI Orchestration
AI Powered Cloud Cost Optimizer
1. Enter Project Description
2. Generate Billing & Analyze Costs
3. View Optimization Report
4. Export Report
5. Exit

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <repository-url>
cd ai_cloud_optimiser

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install & Run Ollama

Download from:
👉 https://ollama.com

Pull TinyLLaMA:

ollama pull tinyllama


Start Ollama service:

ollama serve

▶️ How to Run the Project
Run the CLI
python main.py

Run Individual Steps (Testing)
Profile Extraction
python -c "from analysis.profile_extractor import extract_profile; extract_profile()"

Billing Generation
python -c "from billing.billing_generator import generate_billing; generate_billing()"

Cost Analysis
python -c "from analysis.cost_analyzer import analyze_costs; analyze_costs()"

📄 Sample Input (Project Description)
A cloud-based data analytics platform using Python backend,
PostgreSQL database, and Elasticsearch for search.
Requires monitoring, alerting, and scalability.
Monthly budget is 80,000 INR.

📄 Sample Output Files
project_profile.json
{
  "name": "Data Analytics Platform",
  "budget_inr_per_month": 80000,
  "tech_stack": ["Python", "PostgreSQL", "Elasticsearch"],
  "non_functional_requirements": ["Monitoring", "Alerting"]
}

cost_optimization_report.json
{
  "total_cost_inr": 39000,
  "budget_inr": 80000,
  "variance_inr": 41000,
  "over_budget": false,
  "recommendations": [
    {
      "title": "Switch to Reserved Instances",
      "potential_savings": 4000,
      "cloud_providers": ["AWS", "Azure", "GCP"]
    }
  ]
}

🔐 AI Usage & Academic Integrity

AI tools were used for assistance only

All generated outputs are validated and processed

Code logic and integration were implemented manually

No full solutions were copy-pasted

🚀 Future Enhancements

Web dashboard (Streamlit / React)

Real cloud billing integration (AWS/GCP/Azure APIs)

Visualization of cost breakdown

Support for multiple projects

👩‍💻 Author

Anjali Singh
AI Powered Cloud Cost Optimizer
2025