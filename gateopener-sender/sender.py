import requests
import json
import time
import os


OPENINGS_LOG_API_URL = os.getenv('OPENINGS_LOG_API_URL')
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', '/data/openings.txt')
GATEOPENER_API_KEY = os.getenv('GATEOPENER_API_KEY', '')



while True:

    toSendJson = []
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 4 and parts[3].strip():
                openingTime = f'{parts[0]}:{parts[1]}:{parts[2]}'
                numberplate = parts[3].strip()
                toSendJson.append({'numberplate': numberplate, 'time': openingTime})


    print("[*] Sending openings...")
    response = requests.post(OPENINGS_LOG_API_URL, json=toSendJson, headers={'X-API-Key': GATEOPENER_API_KEY})
    print(response)

    print("[*] Sleeping for 15 minutes...\n")
    time.sleep(15*60)
