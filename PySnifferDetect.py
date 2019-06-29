#!/usr/bin/python
#sniffer detector
#rondinelli Castilho ;)

import sys, ast
from scapy.all import promiscping
from termcolor import colored
import time
import os

os.system("clear")
print colored(''' 
  ___      ___      _  __  __         ___      _          _   
 | _ \_  _/ __|_ _ (_)/ _|/ _|___ _ _|   \ ___| |_ ___ __| |_ 
 |  _/ || \__ \ ' \| |  _|  _/ -_) '_| |) / -_)  _/ -_) _|  _|
 |_|  \_, |___/_||_|_|_| |_| \___|_| |___/\___|\__\___\__|\__|
      |__/                                                    
''', '''white''')

if len(sys.argv) < 2:
        print ("")
        print colored(" ___________________________________", 'magenta')
        print colored(" net - 192.168.0.1/24 ou 192.168.0.*", 'white')
        print sys.argv[0] + colored(" <net>", 'magenta')
	print colored(" ___________________________________",'magenta')
	sys.exit()

print colored('[+]', 'red'), colored('Possiveis sniffers:', 'white'), colored('[+]', 'red')
print ("")
horas =  (time.strftime("%H:%M:%S"))
data = (time.strftime("%d/%m/%Y"))
print ("")
print colored('#############', 'white')
print colored('#', 'white'), colored(horas, 'magenta'), colored("|", 'white')
print colored('#', 'white'), colored(data, 'magenta'), colored("| ", 'white')
print colored('#############', 'white')

(promiscping(sys.argv[1]))
