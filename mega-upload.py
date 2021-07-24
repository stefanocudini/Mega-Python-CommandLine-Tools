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

curDir = os.getcwd() + os.path.sep
dstDirId = None

if len(sys.argv)>1 and sys.argv[1]:
	srcs = sys.argv[1:]
else:
	srcs = None

print srcs

if srcs:
	if len(srcs) > 1 and not os.path.isfile( srcs[-1] ):#if last param isn't a local file then it is dest remote folder
		dstName = srcs.pop()
		dstId = m.find( dstName )
		if dstId:
			dstDirId = dstId[0]
			print 'Destination Folder: '+ dstName

	for src in srcs:
		srcFile = curDir + src
		if os.path.isfile( srcFile ):
			print srcFile
			print dstDirId
			uppedFile = m.upload(srcFile, dstDirId)
			print 'Upped File Link: ' + m.get_upload_link( uppedFile )

