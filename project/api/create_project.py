# create_project.py
import requests
import json

# Define the URL for creating a new project
url = 'http://127.0.0.1:8000/api/clients/1/projects/'  # Replace '1' with the actual client ID

# Define the headers and data
headers = {'Content-Type': 'application/json'}
data = {
    'project_name': 'Project A',
    'users': [
        {'id': 1}  # Replace with the actual user ID
    ]
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(data), auth=('username', 'password'))

# Check the response status code
if response.status_code == 201:
    print('Project created successfully:')
    print(response.json())
else:
    print('Failed to create project:')
    print(response.status_code)
    print(response.text)
