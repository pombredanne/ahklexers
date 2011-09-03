import os, sys, subprocess, re, codecs
from ahkLexer import AhkLexer, ahkcommands
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.style import Style
from pygments.token import *
import os, os.path, glob
samplesDir = 'samples/demo/'
for f in glob.glob( os.path.join(samplesDir, '*.ahk') ):
    print "current file is: " + f
    fh = open(f, 'r')
    code = fh.read()
    fh.close()			   				 
    formatter = HtmlFormatter() 
    codeh = highlight(code, AhkLexer(), formatter)
    if(-1 != codeh.find('''class="err"''')):
        print "failed on file {0}".format(f,)
    g = f.replace("ahk", "html")
    g = g.replace(r"\\", "/")
    gh = open(g, 'w')
#    gh = codecs.open(g, 'w', 'utf-8')
    linktag = '''<LINK href="styles.css" rel="stylesheet" type="text/css">'''
    gh.write(linktag + codeh)
    gh.close()

