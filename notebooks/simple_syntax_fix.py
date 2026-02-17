# Simple fix for the syntax error
# Replace the problematic line with this:

# PROBLEMATIC LINE (causes error):
# with open(dashboard_dir / "dashboard_summary.json", 'w") as f:

# FIXED VERSION (use single quotes consistently):
with open(dashboard_dir / "dashboard_summary.json", "w") as f:

# OR use raw string to avoid conflicts:
with open(dashboard_dir / "dashboard_summary.json", "w") as f:

# OR escape quotes properly:
with open(dashboard_dir / "dashboard_summary.json", "w") as f:

# The issue is likely from mixing single and double quotes in the same line
# Use consistent quote types throughout the line
