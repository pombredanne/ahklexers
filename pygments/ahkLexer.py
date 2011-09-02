from pygments.lexer import RegexLexer
from pygments.token import *   
from pygments.styles import get_style_by_name		       
class AhkLexer(RegexLexer):    	    
    name = 'AHK'	       	    
    aliases = ['ahk']	       	
    filenames = ['*.ahk', '*.ahk2']   
    tokens = { 		       	
        'root': [	       
            (r'^\s*/\*', Comment.Multiline, 'comment'),
	    (r'^\s*\(', Generic, 'continuation'),
            (r'\s;.*?$', Comment.Singleline),
            (r'/', Text),      
            (r'[^/(]+', Text), 
        ],		       
        'comment': [	       
            (r'^\s*\*/', Comment.Multiline, '#pop'),
            (r'[^*/]', Comment.Multiline),
            (r'[*/]', Comment.Multiline)
        ],		       
	'continuation': [      
	    (r'^\s*\)', Generic, '#pop'), 
	    (r'[^)]', Generic),
	    (r'[)]', Generic),
	    ]
    }


