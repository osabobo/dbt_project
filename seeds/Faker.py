from faker import Faker
import pandas as pd

# Initialize Faker
fake = Faker()

# Generate a list of fake data
data = {
    'customer_id': [fake.unique.random_int(min=1000, max=9999) for _ in range(100)],
    'customer_name': [fake.name() for _ in range(100)],
    'purchase_date': [fake.date_this_year() for _ in range(100)],
    'purchase_amount': [fake.random_int(min=10, max=1000) for _ in range(100)],
}

# Convert to a Pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV (or use directly in dbt)
df.to_csv('seed_data.csv', index=False)
