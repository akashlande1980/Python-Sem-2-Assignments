import json
import csv

def json_to_csv(json_data, csv_file_name):
    # Open the CSV file in write mode
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=json_data[0].keys())
        
        # Write the header (fieldnames)
        writer.writeheader()
        
        # Write the data rows
        writer.writerows(json_data)
    
    print(f"Data successfully written to {csv_file_name}")

if __name__ == "__main__":
    # Example JSON array (usually you'd load this from a JSON file)
    json_data = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Anna", "age": 22, "city": "London"},
        {"name": "Mike", "age": 32, "city": "San Francisco"}
    ]
    
    # Convert JSON array to CSV
    json_to_csv(json_data, "output.csv")