import pandas as pd
import numpy as np

# List of Nigerian states
states = [
    'Lagos', 'Kano', 'Kaduna', 'Rivers', 'Oyo', 'Katsina', 'Delta', 'Borno', 
    'Bauchi', 'Benue', 'Anambra', 'Adamawa', 'Akwa Ibom', 'Bayelsa', 
    'Cross River', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kebbi', 
    'Kogi', 'Kwara', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Plateau', 
    'Sokoto', 'Taraba', 'Yobe', 'Zamfara', 'FCT'
]

# Function to generate random data
def generate_data(num_records):
    data = {
        'state': np.random.choice(states, num_records),
        'year': np.random.randint(2000, 2024, num_records),
        'hiv_cases': np.random.randint(100, 10000, num_records),
        'tb_cases': np.random.randint(50, 5000, num_records),
        'population': np.random.randint(1000000, 50000000, num_records),
        'gdp_per_capita': np.random.uniform(500, 50000, num_records).round(2),
        'access_to_healthcare': np.random.uniform(40, 100, num_records).round(2)
    }
    return pd.DataFrame(data)

# Generate 50 records
df = generate_data(50)

# Split the data into two separate files for TB and HIV
tb_data = df[['state', 'year', 'tb_cases']]
hiv_data = df[['state', 'year', 'hiv_cases']]

# Save to CSV
tb_data.to_csv('tb_data.csv', index=False)
hiv_data.to_csv('hiv_data.csv', index=False)

# Display the generated data
print("TB Data:")
print(tb_data.head())
print("\nHIV Data:")
print(hiv_data.head())
