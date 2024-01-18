tests # 

import json

with open('path_to_exported_json_file.json', 'r') as file:
    data = json.load(file)

# Analyze the Data: Once you have the data loaded, you can analyze it as needed. For example, if you want to extract specific information like the label or comments from each entry:
for entry in data:
    print(f'ID: {entry["id"]}, Text: {entry["text"]}, Label: {entry["label"]}, Comments: {entry["comments"]}')


# KPI Extraction: If your exported data contains information about KPIs like annotation time, you can extract it similarly by accessing the relevant keys in your JSON object.
# Keep in mind that the structure and content of your JSON file might vary, so you'll need to adjust the keys you're accessing in the script according to the actual format of your JSON data.

# Ajout d'utilisateurs (Add Users):
client.create_user(username='new_user', password='password', email='email@example.com')
# 
project = client.create_project(name='New Project', description='Project Description', project_type='DocumentClassification')
# Importation des données (Import Data):


client.upload_document(project_id=project['id'], file_path='path/to/your/file.jsonl')
Exportation des données (Export Data):

exported_data = client.export_data(project_id=project['id'], export_format='JSON')

# Vérification des KPIs (Check KPIs): To check KPIs like annotation time, you might need to extract this information from the exported data. The availability of such KPIs depends on the data exported by
# from doccano_client import DoccanoClient

# # Initialize and login
# client = DoccanoClient('http://doccano.example.com')
# client.login('username', 'password')

# # Get user profile
# user_profile = client.get_profile()

# # Create a new project
# new_project = client.create_project(
#     name='New Project',
#     description='Description of the new project',
#     project_type='DocumentClassification'
# )

# # Add a member to the project
# client.add_member_to_project(
#     project_id=new_project['id'],
#     username='member_username',
#     role='annotator'
# )

# The use of .jsonl (JSON Lines) format in the client.upload_document function instead of standard .json is primarily due to its efficiency in handling large datasets. JSON Lines is a convenient format for storing structured data that may be processed one record at a time. It works well with typical Unix style text processing tools and shell pipelines.
# 
# In .jsonl, each line is a valid JSON object, separated by newline characters. This is particularly useful for large datasets as it allows for the streaming of individual JSON objects, making it more memory efficient. In contrast, a standard .json file would require parsing the entire file at once, which can be resource-intensive for large datasets.

# Therefore, when dealing with potentially large datasets in tools like Doccano, .jsonl is often preferred for its performance benefits.

