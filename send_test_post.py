import requests

resp = requests.post('http://127.0.0.1:5000/chat', json={'message': 'hello from test'})
print('Status:', resp.status_code)
print('Body:', resp.text)
