import os, sys, subprocess, re
from ahkLexer import AhkLexer 
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.style import Style
from pygments.token import *
 
ahkfile = 'ahkexpr.ahk'
          
f = open(ahkfile)
code = f.read()
f.close()       		   				 
formatter = HtmlFormatter() 
alexer = AhkLexer()
codeh = highlight(code, alexer, formatter)
print codeh
 
           
class mytoken:
    def __init__(self, type, value, lineno, lexpos):
        self.type = type
        self.value = value                                            
        self.lineno = lineno                                          
        self.lexpos = lexpos                                          
                                                                      
class ltoken:                                                           
    def __init__(self, t):                                              
        self.t = t                                                      
    def token(self):                                                    
        try:                                                            
            x = self.t.next()                                           
            while (re.search("whitespace", str(x[1])[6:], re.IGNORECASE)):
                   x = self.t.next()                                    
            y = mytoken(str(x[1])[6:], x[2], 1, x[0])
            print "type: {0}, value: {1}, line: {2}, pos: {3}".format(y.type, y.value, y.lineno, y.lexpos)
            return y
        except:
            return None
    
# Parsing rules
from ahkparser import parser    
                     
tokens = alexer.get_tokens_unprocessed(code)        
x = ltoken(tokens)   
x.token()            
parser.parse(lexer=x)
    
 
 
 

