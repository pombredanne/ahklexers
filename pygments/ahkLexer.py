from pygments.lexer import RegexLexer, bygroups, using, include
from pygments.token import *   
from pygments.styles import get_style_by_name
ahkcommandsFile = 'ahkSyntax/CommandNames.txt'
f = open(ahkcommandsFile)
ahkcommands = f.read()
f.close()

class AhkLexer(RegexLexer):    	    
    name = 'AHK'	       	    
    aliases = ['ahk']	       	
    filenames = ['*.ahk', '*.ahk2']   
    tokens = { 		       	
        'root': [	       
            (r'^(\s*)(/\*)', bygroups(Whitespace, Comment.Multiline),
                             'incomment'),
	    (r'^(\s*)(\()', bygroups(Whitespace, Generic), 'incontinuation'),
            (r'\s+;.*?$', Comment.Singleline),
            (r'^;.*?$', Comment.Singleline),
            include('commands'),
            include('garbage'),
        ],		       
        'incomment': [	       
            (r'^\s*\*/', Comment.Multiline, '#pop'),
            (r'[^*/]', Comment.Multiline),
            (r'[*/]', Comment.Multiline)
        ],		       
	'incontinuation': [      
	    (r'^\s*\)', Generic, '#pop'), 
	    (r'[^)]', Generic),
	    (r'[)]', Generic),
	    ],
        'commands': [
            (r'^(\s*)(' + ahkcommands + r')\b', bygroups(Whitespace,  Keyword))
            ],
        'garbage': [
            (r'[^\S\n]', Text),
            (r'/', Text),      
            (r'[^/(]', Text), 
            ],
    }


