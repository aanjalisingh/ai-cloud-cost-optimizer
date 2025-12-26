from analysis.profile_extractor import extract_profile
from billing.billing_generator import generate_billing
from analysis.cost_analyzer import analyze_costs

def show_menu():
    while True:
        print("\nAI Powered Cloud Cost Optimizer")
        print("1. Enter Project Description")
        print("2. Generate Billing & Analyze Costs")
        print("3. View Optimization Report")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            text = input("Enter project description:\n")
            open("data/project_description.txt", "w").write(text)
            extract_profile()

        elif choice == "2":
            generate_billing()
            analyze_costs()

        elif choice == "3":
            print(open("data/cost_optimization_report.json").read())

        elif choice == "4":
            break
