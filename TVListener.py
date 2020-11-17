import subprocess
import os
import sys
import time
import urllib2
import subprocess
import signal
import os
from datetime import datetime as dt
from signal import signal, SIGINT
from sys import exit
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
counterscript = 0
if os.name =="nt": 
	os.system("cls")
else: 
	os.system("clear")
print 'Reading config...'
fn2 = 'tvconfig'
try:
	file = open(fn2, 'r')
except IOError:
	print 'Unable to find config, creating from default TV1...'
	file = open(fn2, 'w')
	file.write("tv1")
	file.close()
tvc = open("tvconfig",'r')
lines = tvc.read().split('\n')
tvcc = lines[0]
try:
	main_test = lines[1]
except:
	main_test = "https://example.com/DefaultPage"
try:
	dev_mode = lines[2]
except:
	dev_mode = "false"
try:
	process_name = lines[3]
except:
	process_name = "chromium-browser"
fn = 'keyver'
def mainu():
	print 'Attempting to auto update...'
	updateurl = 'http://example.com/external/abstv/update.txt'
	keyverserv = 'http://example.com/external/abstv/key.txt'
	keyvers = urllib2.urlopen(keyverserv).read()
	updatemain = urllib2.urlopen(updateurl).read()
	try:
		try:
			file = open(fn, 'r')
		except IOError:
			file = open(fn, 'w')
			file.write("1000")
			file.close()
		if updatemain == 'true':
			print 'Please wait/Verifiying Version...'
			cv = open("keyver", "r")
			cvv = cv.read()
			if cvv == keyvers:
				print 'No update found.'
				time.sleep(1)
			else:
				file = open(fn, 'w')
				file.write(keyvers)
				file.close()
				time.sleep(1)
				os.system('wget --output-document=TVListener.py http://example.com/external/abstv/pis/script.txt')
				time.sleep(1)
				os.system('clear')
				os.system('DISPLAY=:0 python TVListener.py')
		else:
			print 'No update found.'
			time.sleep(1)
	except:
		print '503 Oof! Server down and or no update found.'
time.sleep(.5)
try:
	mainu()
except:
	print '503 Oof! Server down and or no update found.'
time.sleep(2)
if os.name =="nt": 
	os.system("cls")
else: 
	os.system("clear")
def handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully. Bye!')
    exit(0)
animate = .07
signal(SIGINT, handler)
print '\033[91m      ___                         ___     '
time.sleep(animate)
print ' \033[91m    /  /\   \33[37m      _____     \033[91m    /  /\    '
time.sleep(animate)
print ' \033[91m   /  /::\   \33[37m    /  /::\    \033[91m   /  /:/_   '
time.sleep(animate)
print ' \033[91m  /  /:/\:\  \33[37m   /  /:/\:\   \033[91m  /  /:/ /\  '
time.sleep(animate)
print '\033[91m  /  /:/~/::\ \33[37m  /  /:/~/::\  \033[91m /  /:/ /::\ '
time.sleep(animate)
print ' \033[91m/__/:/ /:/\:\ \33[37m/__/:/ /:/\:| \033[91m/__/:/ /:/\:\ '
time.sleep(animate)
print ' \033[91m\  \:\/:/__\/ \33[37m\  \:\/:/~/:/ \033[91m\  \:\/:/~/:/'
time.sleep(animate)
print ' \033[91m \  \::/     \33[37m  \  \::/ /:/   \033[91m\  \::/ /:/ '
time.sleep(animate)
print ' \033[91m  \  \:\      \33[37m  \  \:\/:/    \033[91m \__\/ /:/  '
time.sleep(animate)
print ' \033[91m   \  \:\     \33[37m   \  \::/    \033[91m    /__/:/   '
time.sleep(animate)
print ' \033[91m    \__\/      \33[37m   \__\/     \033[91m    \__\/    '
time.sleep(animate)
print '\33[37m'
print 'TV Controller V1.6'
time.sleep(animate)
print 'Created by X1pe0' 
print '\33[90m'

def logo():
	print '\033[91m      ___                         ___     '
	print ' \033[91m    /  /\   \33[37m      _____     \033[91m    /  /\    '
	print ' \033[91m   /  /::\   \33[37m    /  /::\    \033[91m   /  /:/_   '
	print ' \033[91m  /  /:/\:\  \33[37m   /  /:/\:\   \033[91m  /  /:/ /\  '
	print '\033[91m  /  /:/~/::\ \33[37m  /  /:/~/::\  \033[91m /  /:/ /::\ '
	print ' \033[91m/__/:/ /:/\:\ \33[37m/__/:/ /:/\:| \033[91m/__/:/ /:/\:\ '
	print ' \033[91m\  \:\/:/__\/ \33[37m\  \:\/:/~/:/ \033[91m\  \:\/:/~/:/'
	print ' \033[91m \  \::/     \33[37m  \  \::/ /:/   \033[91m\  \::/ /:/ '
	print ' \033[91m  \  \:\      \33[37m  \  \:\/:/    \033[91m \__\/ /:/  '
	print ' \033[91m   \  \:\     \33[37m   \  \::/    \033[91m    /__/:/   '
	print ' \033[91m    \__\/      \33[37m   \__\/     \033[91m    \__\/    '
	print 'TV Controller V1.6'
	print 'Created by X1pe0' 
	print '\33[37m'
	print ("Switches Made: %s"%(counterscript))
	print '------Current Config--------'
	print ("TV ID:       %s"%(tvcc))
	print ("Default URL: %s"%(main_test))
	print ("Dev Mode:    %s"%(dev_mode))
	print ("Browser:     %s"%(process_name))
	print ("----------------------------")
	print '\33[90m'
def load_animation(): 
    load_str = "Please Wait... Loading Server Settings..."
    ls_len = len(load_str) 
    animation = "|/-\\"
    anicount = 0
    counttime = 0        
    i = 0                     
    while (counttime != 100): 
        time.sleep(0.075)  
        load_str_list = list(load_str)  
        x = ord(load_str_list[i]) 
        y = 0                             
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
        load_str = res 
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
    if os.name =="nt": 
        os.system("cls")
    else: 
        os.system("clear")
#----------------------------------------------------------------------------------------------------------------------#
				                   ###Main Settings###
mass_update = "http://example.com/TF.txt"        		                            #Mass Update to Hard coded website URL
log_file_name = "test.log"                                       		            #Log File
switch = "http://google.com"                                     		            #Hard coded Main Webpage to Switch too. 
tv_val = ("http://example.com/tvs/%s.txt"%(tvcc))      		                      #TV Number for remote updating/Single Control.
tv_val_url = ("http://example.com/tvs/%surl.txt"%(tvcc)) 		                    #Remote Update URL
thread_time = 1                                                  		            #Thread Time in seconds. aka Ping Rate.
text_mode_url_tf = ("http://example.com/%stext.txt"%(tvcc))
text_mode_url = ("http://example.com/%stexttf.txt"%(tvcc))  
default_main_remote = ("http://example.com/tvs/%sdefaultremote.txt"%(tvcc))
#----------------------------------------------------------------------------------------------------------------------#
								   ###Value Settings###
a = 'F'
b = ''
e = ''
t2_true = 'F'
t2 = 'F'
c = ''
tmtf = ''
tmtf_v = ''
z = '1'
y = '0'
flip = 1
flop = 0
flip2 = 0
defaultremote = ''

#----------------------------------------------------------------------------------------------------------------------#
load_animation()
print '\33[90m'
while True:
	counterscript = counterscript + 1
	time.sleep(thread_time)
	try:
		main = urllib2.urlopen(default_main_remote).read()
		flip2 = 0
	except:
		main = main_test
		if flip2 == 0:
			flip2 = 1
			if os.name =="nt": 
				os.system("cls") 
			else: 
				os.system("clear") 
				logo()
				print 'Unable to find Remote Default page. Using hard coded URL...'
				time.sleep(1)
	try:

		a = urllib2.urlopen(mass_update).read()
		c = urllib2.urlopen(tv_val).read()
		e = urllib2.urlopen(tv_val_url).read()
		if flip == 0:
			flip = 1
			if os.name =="nt": 
				os.system("cls") 
			else: 
				os.system("clear")
			logo()
			print 'PONG! Server is alive...What Shall I do? Waiting...'
	except:
		if os.name =="nt": 
			os.system("cls") 
		else: 
			os.system("clear")
		logo()
		print 'Oof! Server Down?'
		flip = 0

	if c == 'T':
		os.system("clear")
		logo()
		print 'Entering Single Use Mode...'
		while True:
			counterscript = counterscript + 1
			time.sleep(1)
			try:
				tmtf = urllib2.urlopen(text_mode_url_tf).read()
				e = urllib2.urlopen(tv_val_url).read()
				c = urllib2.urlopen(tv_val).read()
				if flip == 0:
					flip = 1
					if os.name =="nt": 
						os.system("cls") 
					else: 
						os.system("clear") 
						logo()
						print 'PONG! Server is alive...What Shall I do? Waiting...'
			except:
				if os.name =="nt": 
					os.system("cls") 
				else: 
					os.system("clear") 
					logo()
					print 'Oof! Server Down?'
					flip = 0

			if tmtf == 'T':
				#os.system("killall chromium-browser")
				os.system("clear")
				logo()
				print 'Entering Text Mode...'
				while True:
					counterscript = counterscript + 1
					time.sleep(1)
					try:
						ost = urllib2.urlopen(text_mode_url).read()
						tmtf = urllib2.urlopen(text_mode_url_tf).read()
						if flip == 0:
							flip = 1
							if os.name =="nt": 
								os.system("cls") 
							else: 
								os.system("clear") 
								logo()
								print 'PONG! Server is alive...What Shall I do? Waiting...'
					except:
						if os.name =="nt": 
							os.system("cls") 
						else: 
							os.system("clear") 
						logo()
						print 'Oof! Server Down?'
						flip = 0

					if tmtf == tmtf_v:
						time.sleep(0)

					elif tmtf == 'F':
						if dev_mode == 'true':
							print 'App currently in Dev mode.'
						else:
							os.system("killall %s"%(process_name))
						tmtf_v = 'R@nDoM!' 
						os.system("clear")
						logo()
						print 'Calling Browser...'
						#os.system("chromium-browser %s --start-fullscreen -kiosk &> /dev/null &" %(e))
						break					
					else:
						#os.system("killall chromium-browser")
						time.sleep(1)
						os.system("clear")
						logo()
						print 'Calling Browser...'
						if dev_mode == 'true':
							print 'App currently in Dev mode.'
						else:
							os.system("%s %s --start-fullscreen -kiosk &> /dev/null & "%(process_name,ost))
						tmtf_v = tmtf
						time.sleep(0)
			if c == 'F':
				if dev_mode == 'true':
					print 'App currently in Dev mode.'
				else:
					os.system("killall %s"%(process_name))
				os.system("clear")
				logo()
				print 'Calling Browser...'
				#os.system("chromium-browser %s  --start-fullscreen -kiosk &> /dev/null & "%(main))
				break
			else:
				if e == t2_true:
					time.sleep(0)
					#print 'Nope'
				else:
					t2_true = e
					#os.system("killall chromium-browser")
					os.system("clear")
					logo()
					print 'Calling Browser...'
					if dev_mode == 'true':
						print 'App currently in Dev mode.'
					else:
						os.system("%s %s --start-fullscreen -kiosk &> /dev/null & "%(process_name,e))
	elif a == b:

		time.sleep(0)
	elif a == 'T':
		try:
			#os.system("killall chromium-browser")
			time.sleep(1)
			os.system("clear")
			logo()
			print 'Calling Browser...'
			if dev_mode == 'true':
				print 'App currently in Dev mode.'
			else: 
				os.system("%s %s --no-sandbox --start-fullscreen -kiosk &> /dev/null & "%(process_name,switch))
			#os.system("chromium-browser %s"%(switch))
		except Exception, e:
			print 'Debug: T was called. Unable to open Browser.'
	 	b = a
	elif a == 'S':
		exit()
	elif a == 'F':
		proc = subprocess.Popen(["pgrep", process_name], stdout=subprocess.PIPE) 
		for pid in proc.stdout:													 
			os.kill(int(pid), signal.SIGTERM)                                    
			try: 																 
				os.kill(int(pid), 0)
				raise Exception("""wasn't able to kill the process 
                         HINT:use signal.SIGKILL or signal.SIGABORT""")
			except OSError as ex:
				continue
			b = a
			os.system("cp {0} '{0}-dup-{1}'".format(log_file_name, dt.now()))
			with open(log_file_name, "w") as f:
				pass
		b = a
		#os.system("killall chromium-browser")
		time.sleep(1)
		try:
			#subprocess.call("epiphany-browser %s"%(main))
			os.system("clear")
			logo()
			print 'Calling Browser...'
#			os.system("chromium-browser %s"%(main))
			#os.system("chromium-browser %s --start-fullscreen -kiosk &> /dev/null & "%(main))
			if dev_mode == 'true':
				print 'App currently in Dev mode.'
			else:
				os.system("killall %s"%(process_name))
		except Exception, e:
			print 'Debug: F was called. Unable to open browser.'
