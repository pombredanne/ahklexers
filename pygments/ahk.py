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
#            (r'/\*', Comment.Multiline, '#push'),
            (r'[*/]', Comment.Multiline)
        ],		       
	'continuation': [      
	    (r'^\s*\)', Generic, '#pop'), 
	    (r'[^)]', Generic),
	    (r'[)]', Generic),
	    ]
    }


from pygments import highlight
from pygments.formatters import HtmlFormatter

code = '''
 ; single line comment
; single line comment
3 + 3 ; single line comment
/*  multiline
comment
*/
(
continuation
section
)
'''

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic

class ahkStyle(Style):
    default_style = ""		       	 
    styles = {				 
        Comment:                'italic #888',
        Keyword:                'bold #005',
        Name:                   '#f00',	 
        Name.Function:          '#0f0',	 
        Name.Class:             'bold #0f0',
        String:                 'bg:#eee #111',
	Generic:                '#00f',	 
    }					 
					 
formatter = HtmlFormatter(style=ahkStyle, linenos=True) 
print highlight(code, AhkLexer(), formatter)
