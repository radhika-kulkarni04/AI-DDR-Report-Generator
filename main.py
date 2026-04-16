import os
from extractor import extract_text
from ai_engine import generate_ddr
from report_generator import generate_report

# Input files
inspection_file = "sample_input/inspection.pdf"
thermal_file = "sample_input/thermal.pdf"

# Step 1: Extract text
inspection_text = extract_text(inspection_file)
thermal_text = extract_text(thermal_file)

# Step 2: Generate DDR JSON using AI
ddr_json = generate_ddr(inspection_text, thermal_text)

# Step 3: Generate final report
generate_report(ddr_json)

print("✅ DDR Report Generated Successfully! Check output/report.txt")