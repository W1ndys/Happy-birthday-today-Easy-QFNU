import yaml
from datetime import datetime

# Load the YAML data
with open('birthdays.yml', 'r') as file:
    data = yaml.safe_load(file)

# Get current date
current_date = datetime.now().strftime("%m-%d")

# Find names with birthdays matching the current date
matching_names = [entry['name'] for entry in data if entry['birthday'][5:] == current_date]

# Write the matching names to index.html
with open('index.html', 'w') as file:
    file.write(', '.join(matching_names))
