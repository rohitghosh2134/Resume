import pandas as pd

# Read the text file
with open('University_List.txt', 'r') as file:
    content = file.read()

# Split the content into lines and remove leading/trailing spaces
lines = [line.strip() for line in content.split('\n')]

# Extract the headers
headers = lines[0].split('|')
headers = [header.strip() for header in headers if header.strip()]

# Extract the data rows
data = [line.split('|') for line in lines[2:]]
data = [[cell.strip() for cell in row if cell.strip()] for row in data]

# Create a DataFrame using pandas
df = pd.DataFrame(data, columns=headers)

# Save the DataFrame to an Excel file
excel_file = 'Universities.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data has been successfully converted to {excel_file}")
