import requests

host_endpoint = 'https://tkbn3aja47.execute-api.us-east-2.amazonaws.com/default/hostIsUp-stack-hostIsUp-fMhG6iLfqfpO'
host_id = 'home-server'

response = requests.put(f'{host_endpoint}?host={host_id}')
print(f'returned {response.status_code}')