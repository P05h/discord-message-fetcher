import requests
import json

def retrieve_messages(id, discord-token):
  headers = {
    'authorization': discord-token
  }
  r = requests.get('https://discord.com/api/v8/channels/{id}/messages', headers=headers)
  jsonn = json.loads(r.text)
  for value in jsonn:
    print(value.content, '\n')

retrieve_messages('put-id-here', 'put-token-here');
