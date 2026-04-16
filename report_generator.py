import json
import os

def generate_report(ddr_json):

    os.makedirs("output_folder", exist_ok=True)

    try:
        data = json.loads(ddr_json)
    except:
        print("⚠️ JSON parsing failed. Saving raw output.")
        with open("output/report.txt", "w") as f:
            f.write(ddr_json)
        return

    report = f"""
================ DDR REPORT ================

1. Property Issue Summary:
{data.get("Property Issue Summary", "")}

--------------------------------------------

2. Area-wise Observations:
"""
    for obs in data.get("Area-wise Observations", []):
        report += f"- {obs}\n"

    report += f"""
--------------------------------------------

3. Probable Root Cause:
{data.get("Probable Root Cause", "")}

--------------------------------------------

4. Severity Assessment:
{data.get("Severity Assessment", "")}

--------------------------------------------

5. Recommended Actions:
"""
    for action in data.get("Recommended Actions", []):
        report += f"- {action}\n"

    report += f"""
--------------------------------------------

6. Additional Notes:
{data.get("Additional Notes", "")}

--------------------------------------------

7. Missing Information:
"""
    for miss in data.get("Missing Information", []):
        report += f"- {miss}\n"

    report += "\n============================================\n"

    with open("output/report.txt", "w") as f:
        f.write(report)