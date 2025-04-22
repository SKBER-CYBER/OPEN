# OWNER BY SCRIPT : MR OGGY
# GITHUB LINK : SKBER-CYBER
# MACK BY : MUHAMMAD JAKARIYA HASAN

import os, uuid, base64, requests, zlib, time, subprocess
from datetime import datetime

ID_FILE = '/data/data/com.termux/files/usr/bin/.oggy-lock'

def clear(): os.system('clear')

def banner():
    clear()
    print("\033[1;92m")
    print("╔════════════════════════════════════╗")
    print("║      \033[1;97mWELCOME TO \033[1;92mOGGY TOOL PREMIUM  \033[1;92m║")
    print("║       \033[1;91mCREATED BY MR. OGGY XD       \033[1;92m║")
    print("║        \033[1;93mFB CLONING TOOL SYSTEM      \033[1;92m║")
    print("╚════════════════════════════════════╝")
    print("\033[0m")

try:
    key_local = open(ID_FILE, 'r').read()
except:
    key_local = uuid.uuid4().hex[:5].upper()
    open(ID_FILE, 'w').write(key_local)

uid = os.getuid()
raw_key = f"OGGY-LOCK-{uid}XX{key_local}2025=="
encoded_key = base64.b64encode(raw_key.encode()).decode()
compressed_url = b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0f\xf6vr\r\xd2u\x8e\x04\x92\xfa\xde\xc1!\xfa\xb9\x89\x99y \x86^IE\t\x00\xcbC\x15\xda'
approval_link = zlib.decompress(compressed_url).decode()

def line(): print("\033[1;92m═══════════════════════════════════════\033[0m")

def approve_check():
    banner()
    print("\033[1;92mChecking your key...\033[0m")
    time.sleep(1)
    try:
        data = requests.get(approval_link).text.strip().splitlines()
        found = False
        for line_data in data:
            if raw_key in line_data:
                found = True
                parts = line_data.split('|')
                join_date = expire_date = 'Unknown'
                for part in parts:
                    if part.startswith('JOIN:'): join_date = part.replace('JOIN:', '')
                    if part.startswith('EXPIRE:'): expire_date = part.replace('EXPIRE:', '')

                today = datetime.today().date()
                expire_obj = datetime.strptime(expire_date, '%Y-%m-%d').date()
                if today > expire_obj:
                    print("\033[1;91m[×] Your Subscription Has Expired!\033[0m")
                    print(f"\033[1;97mJOINED : \033[1;96m{join_date}")
                    print(f"\033[1;97mEXPIRE : \033[1;91m{expire_date}")
                    line()
                    exit()
                print(f"\n\033[1;92m[✓] KEY APPROVED: \033[0m{raw_key}")
                print(f"\033[1;97mJOINED : \033[1;96m{join_date}")
                print(f"\033[1;97mEXPIRE : \033[1;92m{expire_date}")
                time.sleep(2)
                main(join_date, expire_date)
                break
        if not found:
            print("\033[1;91m[×] Your Key is Not Approved\033[0m")
            line()
            print(f"\033[1;97mYour Key : \033[1;92m{raw_key}")
            print("\033[1;97mStatus   : \033[1;91mTRIAL / BLOCKED")
            line()
            name = input("\033[1;97mEnter your name for Premium : ")
            msg = f"Hi OGGY Admin,\n\nI want to activate my key.\n\nName: {name}\nKey: {raw_key}"
            url = f"https://api.whatsapp.com/send?phone=+8801000000000&text={msg}"
            subprocess.run(["am", "start", url])
            exit()
    except requests.exceptions.ConnectionError:
        print("\n\033[1;91mNo Internet Connection...\033[0m")
        exit()

def main(join_date, expire_date):
    banner()
    line()
    print(f"\033[1;92m[✓] KEY APPROVED: \033[0m{raw_key}")
    print(f"\033[1;97mJOINED : \033[1;96m{join_date}")
    print(f"\033[1;97mEXPIRE : \033[1;92m{expire_date}")
    print("\033[1;97mWelcome to \033[1;92mOGGY PREMIUM TOOL")
    print("\033[1;97mYou are now Premium User. Enjoy!")
    line()

approve_check()
