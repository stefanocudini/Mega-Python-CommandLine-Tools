#!/usr/bin/env python
#
# Mega Python CommandLine Tools
# Copyright stefano.cudini@gmail.com 2013
# https://opengeo.tech
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

files = m.get_files()
for f in files:
	filename = files[f]['a']['n']

	print(files[f])

	if files[f]['t']==0:
		print filename
		print m.get_link( m.find( filename ) )
	else:
		print 'Dir: '+filename
	print
