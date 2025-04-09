#A python script to parse a timestamp log file and extract timestamps and error messages and store output in json file. 
#Author: Gowri Sankar

import re
import json

#A pip command to install the required libraries assuming the necessary libraries are stored in requirements.txt
#pip install -r requirements.txt
errors_data = []
print("Enter timestamp log file path")
timestamplog_file_path = input()
print("Enter output json file path")
output_file_path = input()

with open(timestamplog_file_path, 'r') as log:
    log_content = log.read()
    #Regular expression search to match error 
    error_pat = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - ERROR - (.*?)(?=\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}|\Z)'
    #matching the errors pattern
    matches = re.findall(error_pat, log_content, re.DOTALL)
    for match in matches:
      timestamp = match[0]
      error_message = match[1].strip()
      # Appending the extracted data to the list
      errors_data.append({'timestamp': timestamp, 'error_message': error_message})

with open(output_file_path, 'w') as json_file:
    # Dumping the extracted data to json file
    json.dump(errors_data, json_file) 
    print("Successfully extracted error data and saved to {output_file_path}")