import os, sys, subprocess, re, codecs
from pygments.lexers import AutohotkeyLexer
from ahkLexer import AhkLexer 
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.style import Style
from pygments.token import *
import os, os.path, glob
samplesDir = 'samples/stdlib/'
for f in glob.glob( os.path.join(samplesDir, '*.ahk') ):
#    print "current file is: " + f
    fh = open(f, 'r')
    code = fh.read()
    fh.close()			   				 
    formatter = HtmlFormatter() 
    codeh = highlight(code, AhkLexer(), formatter)
    codeo = highlight(code, AutohotkeyLexer(), formatter)
    if(-1 != codeh.find('class="err"')):
        print "new lexer failed on file {0}".format(f,)
    if(-1 != codeo.find('class="err"')):
        print "old lexer failed on file {0}".format(f,)
    g = f.replace("ahk", "html")
    gh = codecs.open(g, 'w', 'utf-8')
    linktag = '''<LINK href="styles.css" rel="stylesheet" type="text/css">'''
    gh.write(linktag + "old lexer: \n" + codeo + "\n\nNew Lexer: \n" + codeh)
    gh.close()

