import requests

token = input("Token >> ")
channelid = input("ChannelID >> ")

def messagegetter():
    url = f"https://discord.com/api/v9/channels/{channelid}/messages?limit=100"
    headers = {
        'accept-encoding': 'gzip', 
        'accept-language': 'de-DE', 
        'authorization': token, 
        'connection': 'Keep-Alive', 
        'host': 'discord.com', 
        'user-agent': 'Discord-Android/236117;RNA', 
        'x-debug-options': 'bugReporterEnabled', 
        'x-discord-locale': 'de', 
        'x-discord-timezone': 'Europe/Berlin', 
        'x-super-properties': 'eyJvcyI6IkFuZHJvaWQiLCJicm93c2VyIjoiRGlzY29yZCBBbmRyb2lkIiwiZGV2aWNlIjoiU00tRzkzNUYiLCJzeXN0ZW1fbG9jYWxlIjoiZGUtREUiLCJjbGllbnRfdmVyc2lvbiI6IjIzNi4xNyAtIHJuIiwicmVsZWFzZV9jaGFubmVsIjoiYmV0YVJlbGVhc2UiLCJkZXZpY2VfdmVuZG9yX2lkIjoiMzY0MTM2NWQtMzk0Ni00NjJiLWJkMGYtYjdkYWE5Njk1ZTM3IiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiIiwiYnJvd3Nlcl92ZXJzaW9uIjoiIiwib3NfdmVyc2lvbiI6IjI1IiwiY2xpZW50X2J1aWxkX251bWJlciI6MjM2MTE3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjJ9'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        messages = response.json()
        message_ids = [message['id'] for message in messages]
        
        for mes in message_ids:
            delete_url = f"https://discord.com/api/v9/channels/{channelid}/messages/{mes}"
            dele = requests.delete(delete_url, headers=headers)
            
            if dele.status_code == 204:
                print(f"Message {mes} deleted")
            elif dele.status_code == 403:
                print(f"Not your message or invalid token")
            else:
                print(f"Failed delete message {mes} >> Status code -> {dele.status_code} -> {dele.text}")
    else:
        print(f"Failed to get messages >> {response.status_code} -> {response.text}")

messagegetter()
