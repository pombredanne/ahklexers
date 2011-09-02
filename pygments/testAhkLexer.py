import os, sys, subprocess, re
from ahkLexer import AhkLexer, ahkcommands
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.style import Style
from pygments.token import *

ahkfile = 'sample1.ahk'
ahkfileh = 'sample1.html'
f = open(ahkfile)
code = f.read()
f.close()			   				 
formatter = HtmlFormatter() 
codeh = highlight(code, AhkLexer(), formatter)
print codeh				
fh = open(ahkfileh, 'w')
linktag = '''<LINK href="styles.css" rel="stylesheet" type="text/css">'''
fh.write(linktag + str(codeh))
fh.close()

passed = 1
if (-1 == codeh.find('<span class="g">continuation</span>')):
    passed = 0
    print "error with continuation section"
if (-1 == codeh.find('<span class="cm">/*  multiline</span>')):
    passed = 0
    print 'error with multiline comment'
if (-1 == codeh.find('<span class="c-Singleline">; single line comment</span>')):
    passed = 0
    print 'error with single line comment'

if (1 == passed):
    subprocess.call(['explorer', 'sample1.html'])



