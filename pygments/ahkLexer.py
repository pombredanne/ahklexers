from pygments.lexer import RegexLexer, bygroups, using, include
from pygments.token import *   
import re
from pygments.styles import get_style_by_name
ahkcommandsFile = 'ahkSyntax/CommandNames.txt'
f = open(ahkcommandsFile)
ahkcommands = f.read()
f.close()

class AhkLexer(RegexLexer):    	    
    name = 'AHK'	       	    
    aliases = ['ahk']	       	
    filenames = ['*.ahk', '*.ahk2']
#    flags = re.IGNORECASE  use (?i) in commands only 
    tokens = { 		       	
        'root': [	       
            (r'^(\s*)(/\*)', bygroups(Whitespace, Comment.Multiline),
                             'incomment'),
	    (r'^(\s*)(\()', bygroups(Whitespace, Generic), 'incontinuation'),
            (r'\s+;.*?$', Comment.Singleline),
            (r'^;.*?$', Comment.Singleline),
            include('commands'),
            include('labels'),
            include('numbers'),
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
            (r'(?i)^(\s*)(' + ahkcommands + r')\b', bygroups(Whitespace,  Keyword))
            ],
        'labels': [
            # hotkeys and labels 
            # technically, hotkey names are limited to named keys and buttons
            (r'(^\s*)([^:\s]+?:{1,2})', bygroups(Whitespace, Name.Label)), 
            (r'(^\s*)(::[^:\s]+?::)', bygroups(Whitespace, Name.Label)),  
            ],
        
        'numbers': [
            (r'(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?', Number.Float),
            (r'\d+[eE][+-]?[0-9]+', Number.Float),
            (r'0\d+', Number.Oct),
            (r'0[xX][a-fA-F0-9]+', Number.Hex),
            (r'\d+L', Number.Integer.Long),
            (r'\d+', Number.Integer)
        ],        
        'garbage': [
            (r'[^\S\n]', Text),
            (r'/', Text),      
            (r'[^/(]', Text), 
            ],
    }


