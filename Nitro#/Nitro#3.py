import random
import string
from colorama import init, Fore, Back, Style
import colorama
import time
import json
from urllib import request
from urllib.error import HTTPError
init(convert=True)

text = 'Nitro#3'

with open('config.json') as config_file:
    data = json.load(config_file)
    config_file.close()

WEBHOOK_URL = data['nitro3']

print(Fore.CYAN + text)
amount = 0
fix = 1
while fix >= amount:

    fichier = open("src/var", "r")
    var_stop = fichier.read()
    fichier.close()
    nombre = 1
    int_var_stop = int(var_stop)
    #---------------
    # script stop
    #---------------
    if int_var_stop == nombre:
        payload = {
        'username': "XDWOLF #3",
        'content': '''
███████████████████████████
Nitro#3 Done! !
███████████████████████████
        ''',
        'avatar_url': "https://yt3.ggpht.com/a/AATXAJwCp2lbp6K-3MsdrV7Tjl1gxCh49ZDP7hqidg=s100-c-k-c0xffffffff-no-rj-mo",
       }
        headers = {
        'Content-Type': 'application/json',
          'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
        }
        req = request.Request(url=WEBHOOK_URL,
                      data=json.dumps(payload).encode('utf-8'),
                       headers=headers,
                       method='POST')
        try:
            response = request.urlopen(req)
        except HTTPError as e:
            print('ERROR')
            print(e.reason)
            print(e.hdrs)
            print(e.file.read())
        exit()
    #---------------
    # script loop
    #---------------
    else: 
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        discord_url = "discordapp.com/gifts/"
        discord_code = discord_url + code
        print(Fore.CYAN + '#3 ' + Fore.GREEN + discord_code)

        payload = {
            'username': "XDWOLF #3",
        	'content': discord_code,
        	'avatar_url': "https://yt3.ggpht.com/a/AATXAJwCp2lbp6K-3MsdrV7Tjl1gxCh49ZDP7hqidg=s100-c-k-c0xffffffff-no-rj-mo",
        }
        headers = {
        'Content-Type': 'application/json',
          'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
        }
        req = request.Request(url=WEBHOOK_URL,
    	              data=json.dumps(payload).encode('utf-8'),
    	               headers=headers,
    	               method='POST')
        try:
            response = request.urlopen(req)
        except HTTPError as e:
            print('ERROR')
            print(e.reason)
            print(e.hdrs)
            print(e.file.read())
        time.sleep(10)
        fix += 1
