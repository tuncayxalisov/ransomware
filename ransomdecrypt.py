import os
from cryptography.fernet import Fernet

my_files = []

for file in os.listdir():
        if file == "ransomware.py" or file == "ransomdecrypt.py" or file == "generatedkey.key" or not os.path.isfile(file):
                continue
        else:
                my_files.append(file)

with open("generatedkey.key","rb") as generatedkey:
        private_key = generatedkey.read()

for file in my_files:
        with open(file,"rb") as the_file:
                content = the_file.read()
        content_decrypted = Fernet(private_key).decrypt(content)
        with open(file,"wb") as the_file:
                the_file.write(content_decrypted)
