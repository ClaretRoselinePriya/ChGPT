# make_report.py
# Requirements: pandas, matplotlib (pip install pandas matplotlib)
# This script:
#  1) Loads employee data from data.csv
#  2) Prints the frequency count for the "IT" department
#  3) Creates a histogram-like bar chart (count per department)
#  4) Saves an HTML file embedding the chart
# Includes required email: 23f3000663@ds.study.iitm.ac.in

import base64
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "data.csv"
HTML_PATH = "report.html"

# 1) Load data
df = pd.read_csv(CSV_PATH)

# 2) Frequency count for "IT"
it_count = (df["department"] == "IT").sum()
print(f'IT department count: {it_count}')

# 3) Histogram of department distribution (bar counts)
counts = df["department"].value_counts().sort_index()

# One chart per the assignment (no subplots)
plt.figure()                     # do not set colors or styles
counts.plot(kind="bar")          # bar chart of counts
plt.title("Department Frequency")
plt.xlabel("Department")
plt.ylabel("Count")

# Save figure to a PNG in memory
buf = BytesIO()
plt.savefig(buf, format="png", bbox_inches=None, pad_inches=0, dpi=144)
plt.close()
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode("ascii")

# 4) Write HTML with the embedded PNG + printed count + email
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Employee Department Frequency</title>
</head>
<body>
<h1>Employee Department Frequency</h1>
<p><strong>IT department count:</strong> {it_count}</p>
<img alt="Department frequency" src="data:image/png;base64,{img_b64}">
<hr>
<p>Contact: 23f3000663@ds.study.iitm.ac.in</p>
</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Saved {HTML_PATH}")
