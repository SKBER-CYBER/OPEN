# GITHUB LINK : SKBER-CYBER
# DECODE BY : MUHAMMAD JAKARIYA HASAN
import os
import sys
import re
import time
import json
import requests
from bs4 import BeautifulSoup
from faker import Faker
import random

# Function to generate fake name using Faker
def fake_name():
    fake = Faker()
    first = fake.first_name()
    last = fake.last_name()
    return first, last

# Function to extract data from HTML using BeautifulSoup
def extractor(data):
    try:
        soup = BeautifulSoup(data, 'html.parser')
        result = {}
        inputs = soup.find_all('input')
        
        for input_tag in inputs:
            name = input_tag.get('name')
            value = input_tag.get('value')
            if name:
                result[name] = value
        return result
    except Exception as e:
        return {'error': str(e)}

# Function to generate a random user agent from a list of agents
def ugenX():
    agents = [
        'Dalvik/2.1.0 (Linux; U; Android 14; SM-A146P Build/UP1A.231005.007) [FBAN/FBLite;FBAV/425.0.0.10.100;FBPN/com.facebook.lite;FBLC/en_US;FBBV/587295421;]',
        'Dalvik/2.1.0 (Linux; U; Android 13; 2201117TG Build/TQ3A.230805.001) [FBAN/FBLite;FBAV/420.1.0.45.120;FBPN/com.facebook.lite;FBLC/fr_FR;FBBV/493491272;]',
        'Dalvik/2.1.0 (Linux; U; Android 12; M2006C3LG Build/SP1A.210812.016) [FBAN/FBLite;FBAV/415.0.0.30.90;FBPN/com.facebook.lite;FBLC/es_ES;FBBV/587295421;]',
        'Dalvik/2.1.0 (Linux; U; Android 14; CPH2387 Build/UP1A.231005.007) [FBAN/FBLite;FBAV/430.0.0.15.110;FBPN/com.facebook.lite;FBLC/en_US;FBBV/884744917;]',
        # Add more agents as needed
    ]
    return random.choice(agents)

# Function to get a temporary email using requests
def GetEmail():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new')
    response_data = response.json()
    return response_data.get('email')

# Main function
if __name__ == "__main__":
    email = GetEmail()
    print(f"Temporary Email: {email}")
    
    fake_first_name, fake_last_name = fake_name()
    print(f"Fake Name: {fake_first_name} {fake_last_name}")
    
    random_user_agent = ugenX()
    print(f"Random User-Agent: {random_user_agent}")
    
    html_data = "<html><body><input name='username' value='test_user'/></body></html>"
    extracted_data = extractor(html_data)
    print(f"Extracted Data: {extracted_data}")
 import requests
import re
import os

def GetCode(email):
    """
    Fetches the verification code from the temporary email service.
    
    Args:
        email (str): The temporary email address to check for messages.
    
    Returns:
        str: The verification code extracted from the email message.
    """
    url = f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages'
    response = requests.get(url).text
    code_match = re.search(r'FB-(\d+)', response)
    
    if code_match:
        code = code_match.group(1)
        return code
    return None

def banner():
    """
    Displays the banner information for the tool.
    """
    os.system('clear')
    print('''
    F ██████  ██ ███    ██ ██████  
    B     ██  ██ ████   ██ ██   ██
    F    ██   ██ ██ ██  ██ ██   ██ 
    AUTO-FB CREATE
    B   ██    ██ ██  ██ ██ ██   ██
    0  ██████ ██ ██   ████ ██████ 
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    [•] 
    DEVELOPER   : KHARAL MODS
    GITHUB      : KHARAL-404
    VERSION     : 1.9.2
    TOOL        : AUTO-CREATE
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ''')

def linex():
    """
    Prints a line separator.
    """
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Example usage
if __name__ == "__main__":
    banner()
    email = "example@example.com"  # Replace with the actual email
    code = GetCode(email)
    if code:
        print(f"Verification code: {code}")
    else:
        print("No code found.")
    linex()
import requests
import random
import re
import time

def main():
    print(" Start Auto Create >")
    
    for _ in range(100):
        session = requests.Session()
        response = session.get('https://x.facebook.com/reg', params={
            '1': '',
            'rdr_0t3qOXoIHbMS6isLw': 'deprecated',
            '_rdc': '',
            '_rdr': '',
            'wtsid': '',
            'refsrc': ''
        })
        
        mts = session.get('https://x.facebook.com').text
        m_ts = re.search(r'name="m_ts" value="(.*?)"', mts).group(1)
        
        formula = extractor(response.text)
        email2 = GetEmail()
        firstname, lastname = fake_name()
        
        print(f' NAME  - {firstname} {lastname}')
        print(f' EMAIL - {email2}')
        
        payload = {
            'ccp': '2',
            'reg_instance': str(formula['reg_instance']),
            'submission_request': 'true',
            'helper': '',
            'reg_impression_id': str(formula['reg_impression_id']),
            'ns': '1',
            'zero_header_af_client': '',
            'app_id': '103',
            'logger_id': str(formula['logger_id']),
            'field_names[0]': 'firstname',
            'firstname': firstname,
            'lastname': lastname,
            'field_names[1]': 'birthday_wrapper',
            'birthday_day': str(random.randint(1, 28)),
            'birthday_month': str(random.randint(1, 12)),
            'birthday_year': str(random.randint(1992, 2009)),
            'age_step_input': '',
            'did_use_age': 'false',
            'field_names[2]': 'reg_email__',
            'reg_email__': email2,
            'field_names[3]': 'sex',
            'sex': '2',
            'preferred_pronoun': '',
            'custom_gender': '',
            'field_names[4]': 'reg_passwd__',
            'reg_passwd__': f'#PWD_BROWSER:0:{time.time()}:{random.randint(1000, 9999)}',
            'name_suggest_elig': 'false',
            'was_shown_name_suggestions': 'false',
            'did_use_suggested_name': 'false',
            'use_custom_gender': 'true',
            'guid': '',
            'pre_form_step': '',
            'encpass': f'#PWD_BROWSER:0:{time.time()}:{random.randint(1000, 9999)}',
            'submit': 'Sign Up',
            'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0',
            'jazoest': str(formula['jazoest']),
            'lsd': str(formula['lsd']),
            # Additional parameters can be added here
        }
        
        headers = {
            'Host': 'm.facebook.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'dnt': '1',
            'X-Requested-With': 'mark.via.gp',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        
        registration_url = 'https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1'
        session.post(registration_url, data=payload, headers=headers)

import requests
import re

def confirm_id(ses, email, uid, otp, con_sub):
    url = 'https://m.facebook.com/confirmation_cliff/'
    params = {
        'contact': email,
        'type': 'submit',
        'is_soft_cliff': 'false',
        'medium': 'email',
        'code': otp
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': f'https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty'
    }
    
    try:
        response = ses.post(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        
        # Check for confirmation in the response
        if re.search(r'SUCCESS - ', response.text):
            print(f"SUCCESS - {uid} | {email}")
            with open('/sdcard/FRESH-OK-ID.txt', 'a') as f:
                f.write(f"{uid}\n")
        else:
            print(f"CHECKPOINT ID - {uid} | {email}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Initialize Faker
fake = Faker()

def ugenX():
    user_agents = [
        'Dalvik/2.1.0 (Linux; U; Android 14; SM-A146P Build/UP1A.231005.007) [FBAN/FBLite;FBAV/425.0.0.10.100;FBPN/com.facebook.lite;FBLC/en_US;FBBV/587295421;]',
        # Add more user agents as needed
    ]
    return random.choice(user_agents)

def fake_name():
    return fake.name()

def extractor(data):
    # Extract information from data
    return data

def GetEmail():
    # Generate a fake email
    return fake.email()

def GetCode():
    # Generate a random code
    return random.randint(1000, 9999)

def banner():
    print("┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃─꯭─̽⃝SUBSCRIBE MY YOUTUBE CHANNEL")
    print("┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━┛")

def confirm_id(uid, ses, otp):
    url = 'https://m.facebook.com/confirmation_cliff/'
    params = {
        'contact': 'email',
        'type': 'false',
        'is_soft_cliff': 'medium',
        'code': otp
    }
    
    # Prepare payload
    payload = {
        'fb_dtsg': '',
        'jazoest': '',
        'lsd': '',
        '__dyn': '',
        '__csr': '',
        '__req': '',
        '__fmt': '',
        '__a': '',
        '__user': uid
    }
    
    headers = {
        'User-Agent': ugenX(),
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'origin': 'https://m.facebook.com',
        'referer': 'https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }
    
    try:
        response = ses.post(url, params=params, data=payload, headers=headers)
        if 'checkpoint' in response.url:
            print(f"{uid} FUCKED ID DISABLED")
            return None
        else:
            cookie = response.cookies.get_dict()
            print(f"SUCCESS - {uid} |Kharal@404| {cookie}")
            with open('/sdcard/FRESH-OK-ID.txt', 'a') as f:
                f.write(f"{uid}|Kharal@404|{cookie}\n")
            return cookie
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    # Example usage
    uid = GetEmail()
    ses = requests.Session()
    otp = GetCode()
    confirm_id(uid, ses, otp)

if __name__ == '__main__':
    main()