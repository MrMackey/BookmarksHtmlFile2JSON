#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import re
import json

def GetATagFromHtmlFile(filename):
	bookmarks_dict = {}
	fileobject = open(filename, 'r')
	try:
		filetext = fileobject.read()
		atag = re.findall(r'<A .*?<\/A>', filetext)
		for one_atag in atag:
			if re.search(r'HREF="(http.*?)"', one_atag) and re.search(r'>(.*?)<', one_atag):
				bookmarks_dict[re.search(r'>(.*?)<', one_atag).group(1)] = re.search(r'HREF="(http.*?)"', one_atag).group(1)
			else:
				print one_atag
	except Exception, e:
		print e
	finally:
		fileobject.close()
	return bookmarks_dict

if __name__ == '__main__':
	if len(sys.argv)!=3:
		print 'ERROR: Syntax is error!'
		print 'BookmarksHtmlFile2JSON.py SourceFile DestinationFile'
	else:
		if os.path.exists(sys.argv[1]):
			# enter main function
			encodedjson = json.dumps(GetATagFromHtmlFile(sys.argv[1]), ensure_ascii=False, indent=4)
			fileobject = open(sys.argv[2], 'wb')
			fileobject.write(encodedjson)
			fileobject.close()
		else:
			print 'ERROR: SourceFile is not exist!'