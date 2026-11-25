import csv
from collections import defaultdict

# Simulate scraped data from a website
# Each tuple represents a potential contact record
scraped_data = [
    ('John Doe', 'john.doe@example.com', '123 Main St'),
    ('Jane Smith', 'jane.smith@example.com', '456 Oak Ave'),
    ('John Doe', 'john.doe@example.com', '123 Main St'), # Duplicate
    ('Peter Jones', 'peter.jones@example.com', '789 Pine Ln'),
    ('Jane Smith', 'jane.smith@example.com', '456 Oak Ave'), # Duplicate
    ('Alice Brown', 'alice.brown@example.com', '101 Maple Dr'),
    ('John Doe', 'john.doe@example.com', '123 Main St, Apt 1'), # Slightly different address, but same email/name
]

# Define a unique identifier for deduplication
# In a real CRM, this might be email, phone number, or a combination
def get_unique_key(record):
    # Using email as the primary unique identifier
    return record[1].lower() # Case-insensitive email comparison

# Dictionary to store unique records, keyed by their unique identifier
# defaultdict is used to simplify adding new entries
unique_records = defaultdict(dict)

print("Processing scraped data for deduplication...")

for record in scraped_data:
    key = get_unique_key(record)
    name, email, address = record

    if key not in unique_records:
        # If the key is not yet in our dictionary, add the record
        # We store the entire record as the value
        unique_records[key] = record
        print(f"  Added unique record: {name} ({email})")
    else:
        # If the key already exists, it's a duplicate. We can optionally
        # implement logic here to merge or update existing records if needed.
        # For this example, we simply skip adding it again.
        print(f"  Skipping duplicate record: {name} ({email})")

# Convert the values of the dictionary back to a list of unique records
final_unique_list = list(unique_records.values())

print(f"\nTotal scraped records: {len(scraped_data)}")
print(f"Unique records after deduplication: {len(final_unique_list)}")

# Simulate CRM import by writing to a CSV file
output_filename = 'crm_import_data.csv'

with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write header
    csv_writer.writerow(['Name', 'Email', 'Address'])
    # Write unique records
    csv_writer.writerows(final_unique_list)

print(f"\nUnique records have been written to '{output_filename}' for CRM import.")
