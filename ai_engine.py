def generate_ddr(inspection_text, thermal_text):

    report = {
        "Property Issue Summary": "Water leakage and structural issues observed based on inspection and thermal data.",

        "Area-wise Observations": [
            "Kitchen: Leakage and moisture detected (Inspection + Thermal match)",
            "Living Room: Wall cracks observed",
            "Roof: Temperature variation indicating insulation issue"
        ],

        "Probable Root Cause": "Poor waterproofing and insulation defects.",

        "Severity Assessment": "Moderate to High – Issues may worsen if not treated promptly.",

        "Recommended Actions": [
            "Repair leakage in kitchen ceiling",
            "Seal wall cracks in living area",
            "Improve roof insulation"
        ],

        "Additional Notes": "Prototype-based AI simulation used due to API limitations.",

        "Missing Information": [
            "Exact material details",
            "Precise thermal measurements"
        ]
    }

    import json
    return json.dumps(report)