import os, sys, subprocess, re
from ahkLexer import AhkLexer 
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.style import Style
from pygments.token import *
from pygments.lexers import AutohotkeyLexer
ahkfile = 'sample1.ahk'
ahkfileh = 'sample1.html'
f = open(ahkfile)
code = f.read()
f.close()			   				 
formatter = HtmlFormatter() 
codeh = highlight(code, AhkLexer(), formatter)
codeo = highlight(code, AutohotkeyLexer(), formatter)
print codeh				
fh = open(ahkfileh, 'w')
linktag = '''<LINK href="styles.css" rel="stylesheet" type="text/css">'''
fh.write(linktag + "old lexer: \n" + codeo + "\n\nNew Lexer: \n" + codeh)
fh.close()

if(-1 != codeh.find('class="err"')):
    print "failed"
subprocess.call(['explorer', 'sample1.html'])








