import os, sys, subprocess, re
from ahkLexer import AutohotkeyLexer 
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
ahklexer = AutohotkeyLexer()
codeh = highlight(code, ahklexer, formatter)
print codeh				
fh = open(ahkfileh, 'w')
linktag = '''<LINK href="styles.css" rel="stylesheet" type="text/css">'''
fh.write(linktag + str(codeh))
fh.close()

if(-1 != codeh.find('class="err"')):
    print "failed"
subprocess.call(['explorer', 'sample1.html'])








