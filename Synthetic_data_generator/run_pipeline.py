import subprocess
import os

INPUT_CSV = "employees.csv"

# Check if the input CSV exists
if not os.path.exists(INPUT_CSV):
    print(f"❌ Error: '{INPUT_CSV}' not found. Please place it in the current directory.")
    exit(1)

print(f"\n📁 Starting pipeline with '{INPUT_CSV}'...")

try:
    print("🔁 Running initial_50000_data.py...")
    subprocess.run(["python", "initial_50000_data.py"], check=True)

    print("🔁 Running enriched_employee_data.py...")
    subprocess.run(["python", "enrich_employee_data.py"], check=True)

    print("🔁 Running csv_to_json.py...")
    subprocess.run(["python", "csv_to_json.py"], check=True)

    print("🔁 Running main.py...")
    subprocess.run(["python", "main.py"], check=True)

    print("\n✅ Pipeline executed successfully. All outputs generated.")

except subprocess.CalledProcessError as e:
    print(f"\n❌ An error occurred while running: {e.cmd}")
    print(f"Exit status: {e.returncode}")
    exit(1)
