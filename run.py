from email import header
import random,json,os, time,string
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from multiprocessing import Pool
from time import sleep
from faker import Faker
fake = Faker() 
  
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)
from requests_html import HTMLSession

def check_mail(email,sess,username):
    header_check = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "sec-ch-ua": "\"\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "",
        "x-requested-with": "XMLHttpRequest",
        "Referer": "https://tempmail.plus/en/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    email = email.replace("@",'%40')
    get_mail = sess.get(f'https://tempmail.plus/api/mails?email={email}&limit=20&epin=',headers=header_check)
    get_mail = get_mail.json()
    id_mail = get_mail['last_id']
    # print(id_mail)
    
    headers={
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9,ru;q=0.8,id;q=0.7",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-requested-with": "XMLHttpRequest",
        "cookie": f"email={email}",
        "Referer": "https://tempmail.plus/en/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }#admin@mail-notifyle.com|ridzigaming54321
    get_mail = sess.get(f'https://tempmail.plus/api/mails/{id_mail}?email={email}&epin=',headers=headers,stream=True)
    get_mail =  get_mail.text.encode().decode('unicode_escape')
    get_url = str(get_mail).split('https://seal-symph.com/member/verify/')[1].split('target="_blank"')[0].strip().replace('"','').replace(' class=es-button','')
    check_verify = sess.get(f"https://seal-symph.com/member/verify/{get_url}")
    get_mail = check_verify.html.xpath('//div[@class="caption m-b-md"]/text()')[0]
    get_mail = str(get_mail).strip()
    print(f'[*] {username}: {get_mail}')
    
def sign_up(k):
    
    sess = HTMLSession()
    password = "passworO123"
 
    headers = {
            "accept": "text/plain, */*; q=0.01",
            "accept-language": "id-ID,id;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "Referer": "https://www.abandonmail.com/id",
            "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    additonal = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    username = fake.first_name()+str(random_angka)
    username = username.lower()
    email = fake.first_name()+fake.last_name()+f"{random_angka}@"+"mailto.plus"
    email = email.lower()
    response = sess.get('https://seal-symph.com/member/register') 

    
    get_token = response.html.xpath('/html/head/meta[4]')
    get_token = str(get_token)
    get_token = get_token.split("token")[1].split("' content='")[1].split("'>]")[0]
     
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
    r = sess.get(f'https://2captcha.com/in.php?key=795244db2816e5e5d29a788c818bba10&method=userrecaptcha&googlekey=6LfAV2QgAAAAAI4vbdQ0fNC204S7RAHTdC-D_d9i&pageurl=https://seal-symph.com/member/register/')

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
        '_token': get_token,
        'username': username,
        'password': password,
        'cf_password': password,
        'email': email,
        'pin': '22882392',
        'birthday': '2002-02-19',
        'gender': '0',
        'g-recaptcha-response': token_captcha
    }
    check_resp = sess.post('https://seal-symph.com/member/register',data=datas,headers=headerz,allow_redirects=True)
    print(f'[*] {username}: Success Registrated!')
    with open('success.txt','a') as f:
        f.write('{0}|{1}\n'.format(username,password))
    n = 1
    while True:
        sleep(5)
        if n == 5:
            print(f"[*] {username}: Verification Failed!")
            break
        try:
            check_mail(email,sess,username)
            break
        except Exception as e:
            if "list index out of range" == str(e):
                print(f"[*] {username}: Your Email doesn't have a new message, Reload!")
            else:
                print(f'[*] {username}: Error{e}')
            n = n+1
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
