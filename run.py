#Author Mohammad sultani

import os, platform
os.system('git pull')
try:os.system('mkdir OK')
except:pass
try:os.system('mkdir CP')
except:pass
try:os.system('mkdir IG')
except:pass

try:

   import requests

except:

   os.system('pip2 install requests')

import requests
import platform 
bit = platform.architecture()[0]

if bit == '64bit':
	from mpro import menu
	menu()
elif bit == '32bit':
	from mpro32 import menu32
	menu32()



   



