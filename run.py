import requests,random,json,os, time,string
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from multiprocessing import Pool
from time import sleep
from faker import Faker
fake = Faker() 
  
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)

def sign_up(k):
    sess = requests.Session()
    password = "password123OK$$"
    additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    username = fake.first_name()+str(random_angka)
    username = username.lower()
    email = fake.first_name()+fake.last_name()+str(random_angka)+"@getnada.com"
    email = email.lower()
    
    r = sess.get('https://seal-symph.com/member/register').text

    token = r.split('<meta name="csrf-token" content="')[1].split('">')[0]
    headerz = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "Referer": "https://seal-symph.com/member/register",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    r = sess.get('https://2captcha.com/in.php?key=795244db2816e5e5d29a788c818bba10&method=userrecaptcha&googlekey=6LcDMjYeAAAAAEwohRY899O6W49VKD9jUX4011eZ&pageurl=https://www.gratislampu.lighting.philips.com/')

    get_id = r.text.split("|")
    get_id = get_id[1]
    while True:
        time.sleep(5)
        r = sess.get(f'https://2captcha.com/res.php?key=795244db2816e5e5d29a788c818bba10&action=get&id={get_id}')
        
        if r.text == "CAPCHA_NOT_READY":
            print(f"[*] {username}: {r.text}")
        else:
            global token_captcha
            print(f'[*] {username}: Solved Captcha')
            get_capt =  str(r.text)
            ress = get_capt.split("|")
            token_captcha = ress[1]
            break
    datas = {
        '_token': token,
        'username': username,
        'password': password,
        'cf_password': password,
        'email': email,
        'pin': '22882392',
        'birthday': '2002-02-19',
        'gender': '0',
        'g-recaptcha-response': token_captcha
    }
    check_resp = sess.post('https://seal-symph.com/member/register',json=datas,headers=headerz,allow_redirects=True)
    print(f'[*] {username}: Success Registrated!')
    with open('success.txt','a') as f:
        f.write('{0}|{1}\n'.format(username,password))
   
if __name__ == '__main__':
 
    global password
    print("[*] Auto Creator Account")
    jumlah = input("[*] Multiprocessing: ")
    loop_input = int(input("[*] How Much Account: "))
    loop = []
    for i in range(1, loop_input+1):
        loop.append(i)
    
    start = time.time()
    with Pool(int(jumlah)) as p:  
        p.map(sign_up, loop)
      
            
    end = time.time()
    print("[*] Time elapsed: ", end - start)
