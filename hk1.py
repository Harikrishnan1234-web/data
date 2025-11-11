1
import socket

target = "127.0.0.1"   # Localhost
start_port = 20
end_port = 30

print(f"Scanning ports {start_port}-{end_port} on {target}")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")
    s.close()

print("Verification: Compare with 'nmap 127.0.0.1 -p 20-30'")

2

from datetime import datetime

with open("input_log.txt", "a") as file:
    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            print("Logging stopped.")
            break
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {command}\n")
        print("Command logged successfully.")

3

import requests

url = "http://example.com/login.php?id="
payloads = ["1", "1' OR '1'='1", "1'--", "1' OR 'a'='a"]

for p in payloads:
    target = url + p
    response = requests.get(target)
    print(f"Testing payload: {p}")
    if "error" in response.text.lower() or "sql" in response.text.lower():
        print(" Possible SQL Injection Vulnerability!")
    else:
        print(" Secure against payload.")

4

import pyotp
import time

# Shared secret
secret = pyotp.random_base32()
totp = pyotp.TOTP(secret)

print("Generated OTP (user side):", totp.now())
print("Please wait 30 seconds to test OTP expiry...")

# Simulating user input
user_otp = input("Enter OTP: ")

if totp.verify(user_otp):
    print("Login Successful (OTP Verified)")
else:
    print("Invalid OTP or Expired")

5


from cryptography.fernet import Fernet
message = "hello geeks"
key = Fernet.generate_key()
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)
