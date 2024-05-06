#!/usr/bin/python3

import logging
import os
import requests

logger = logging.getLogger(__name__)

targets = ["https://ipinfo.io/ip", "https://api.ipify.org"]

def get_public_ip() -> str:
    for target in targets:
        response = requests.get(target)
        if response.status_code == 200:
            ip_address = response.text.strip()
            if ip_address:
                return ip_address
            else:
                continue
        else:
            continue
    logger.error("Failed to get IP address.")
    return None

def send_discord_notification(message: str):
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    content = message
    data = {"content": content}
    headers = {
        "Content-Type": "application/json"
    }
    requests.post(
        WEBHOOK_URL,
        headers=headers,
        json=data
    )

def main():
    ip_address = get_public_ip()
    if ip_address:
        message = f"The current IP address is {ip_address}."
    else:
        message = "Did not find valid IP address."
    send_discord_notification(message)

if __name__ == "__main__": 
    main()
