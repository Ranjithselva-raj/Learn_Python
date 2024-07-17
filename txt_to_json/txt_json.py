import json

def update_json_from_txt(txt_file_path, json_file_path):
    # Read existing data from JSON file
    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []

    # Load existing PatientIDs to a set for fast lookup
    existing_ids = {data['PatientID'] for data in existing_data}

    # Read and append new data from TXT file
    with open(txt_file_path, 'r') as txt_file:
        headers = txt_file.readline().strip().split(', ')
        new_data = []

        for line in txt_file:
            record = dict(zip(headers, line.strip().split(', ')))
            if record['PatientID'] not in existing_ids:
                new_data.append(record)

    # Save updated data to JSON file if there are new records
    if new_data:
        existing_data.extend(new_data)
        with open(json_file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)
        print(f"Added {len(new_data)} new records to JSON file.")
    else:
        print("No new records found to add.")

# Example file paths
txt_file_path = r'C:\\Users\\ranje\\OneDrive\\Desktop\\Data_stream.txt'
json_file_path = r'C:\\Users\\ranje\\OneDrive\\Desktop\\Data_stream.json'

# Call the function to update the JSON file
update_json_from_txt(txt_file_path, json_file_path)

