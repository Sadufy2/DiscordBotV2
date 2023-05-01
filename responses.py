import urllib.request
import socket
import subprocess
def get_response(message: str) -> str:
    msg = message.lower()

    if msg == '?online':
        return "Response Good"
    if msg == '?ip':
        return urllib.request.urlopen('https://ident.me').read().decode('utf8') + ":25565"
    if msg == '?server':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', 25565))
        if result == 0:
            return f"```diff\n+ Server is ONLINE\n at [{urllib.request.urlopen('https://ident.me').read().decode('utf8')}:25565]```"
        else:
            return "```diff\n- Server is OFFLINE\n```"
        sock.close()
    if msg == '?start':
        #subprocess.call(['java', '-jar', r'C:\Users\safis\PycharmProjects\DiscordBot\minecraft_server.jar', 'nogui'])
        #return "Server is starting..."
        return "feature is work in progress"
    if msg == 'szeretlek hodo':
        return "Én is szeretlek <3"