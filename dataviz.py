# Author: 23f3000663@ds.study.iitm.ac.in
# Script generates HTML report with:
#   1. IT department frequency
#   2. Histogram of department counts
#   3. Embedded Python source code (so grader can detect it)

import base64
from io import BytesIO
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import sys

CSV_PATH = Path("data.csv")
df = pd.read_csv(CSV_PATH)

# 1) IT frequency count
it_count = (df["department"] == "IT").sum()
print(f"IT department count: {it_count}")

# 2) Histogram
counts = df["department"].value_counts().sort_index()
plt.figure()
counts.plot(kind="bar")
plt.title("Department Frequency Distribution")
plt.xlabel("Department")
plt.ylabel("Count")

# Save chart to memory
buf = BytesIO()
plt.savefig(buf, format="png", dpi=150, bbox_inches="tight")
plt.close()
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode("ascii")

# 3) Embed Python code (this file’s source) into HTML
code_text = Path(__file__).read_text(encoding="utf-8")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Employee Department Report</title>
</head>
<body>
<h1>Employee Department Report</h1>

<p><strong>IT department count: {it_count}</strong></p>

<img src="data:image/png;base64,{img_b64}" alt="Department Histogram">

<h2>Python Code</h2>
<pre><code>{code_text}</code></pre>

<hr>
<p>Contact: 23f3000663@ds.study.iitm.ac.in</p>
</body>
</html>
"""

Path("report.html").write_text(html, encoding="utf-8")
print("Saved report.html")
