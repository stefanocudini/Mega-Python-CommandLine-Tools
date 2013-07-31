#!/usr/bin/env python
#
# Mega Python CommandLine Tools
# Copyright stefano.cudini@gmail.com 2013
# http://labs.easyblog.it
#
# Source:
#	https://github.com/stefanocudini/Mega-Python-CommandLine-Tools
#
# Require:
#	https://github.com/richardasaurus/mega.py
#
# Config file, ~/.megarc:
#	[default]
#	email = my@email.com
#	pass = mypass
#

import os
import sys
import ConfigParser
from mega import Mega

configfile = os.path.expanduser("~") + os.sep + '.megarc'
if not os.path.exists(configfile):
	sys.exit('File ~/.megarc Not Found!')

config = ConfigParser.RawConfigParser()
config.read(configfile)
email = config.get('default', 'email')
passw = config.get('default', 'pass')

mega = Mega({'verbose': True})
m = mega.login(email, passw)

url = raw_input("Enter mega.co.nz URL: ")
m.download_url(url, os.getcwd() + os.path.sep )


