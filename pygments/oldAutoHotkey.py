# -*- coding: utf-8 -*-
"""
    pygments.lexers.autohotkey
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for autohotkey.

    :copyright: Copyright 2006-2009 by Naveen Garg.
    :license: BSD, see LICENSE for details.
"""
import re
try:
    set
except NameError:
    from sets import Set as set
from pygments.scanner import Scanner

from pygments.lexer import Lexer, RegexLexer, bygroups, include
from pygments.token import *

__all__ = ['autohotkeyLexer']

class autohotkeyLexer(ExtendedRegexLexer):
    """
    For autohotkey source code
    """
    name = 'autohotkey'
    aliases = ['ahk']
    filenames = ['*.ahk', '*.ahkl']
    flags = re.IGNORECASE | re.DOTALL | re.MULTILINE

    tokens = {
        'root': [
            include('whitespace'),
            (r'^\(', String, 'continuation'),
            include('comments'),
            (r'(^\s*)(\w+)(\s*)(=)', 
             bygroups(Whitespace, Name, Whitespace, Operator),
             'command'),
            (r'([\w#@$?\[\]]+)(\s*)(\()', 
             bygroups(Name.Function, Whitespace, Punctuation),
             'parameters'),
            include('directives'),
            include('labels'),
            include('commands'),
            include('expressions'),
            include('numbers'),
            include('literals'),
            include('keynames'),
            include('keywords'),
        ],
        'command': [
            include('comments'),
            include('whitespace'),
            (r'^\(', String, 'continuation'),
            (r'[^\n]*?(?=;*|$)', String, '#pop'),
            include('numbers'),
            include('literals'),
        ],

        'expressions': [
            include('comments'),
            include('whitespace'),
            include('numbers'),
            include('literals'),
            (r'([]\w#@$?[]+)(\s*)(\()', 
             bygroups(Name.Function, Whitespace, Punctuation),
             'parameters'),
            (r'A_\w+', Name.Builtin),
            (r'%[]\w#@$?[]+?%', Name.Variable),
            # blocks: if, else, function definitions
            (r'{', Punctuation, 'block'),
            # parameters in function calls
            ],
        'literals': [
            (r'"', String, 'string'),
            (r'A_\w+', Name.Builtin),
            (r'%[]\w#@$?[]+?%', Name.Variable),
            (r'[-~!%^&*+|?:<>/=]=?', Operator, 'expressions'),
            (r'==', Operator, 'expressions'),
            ('[{()},.%#`;]', Punctuation),
            (r'\\', Punctuation),
            include('keywords'),
            (r'\w+', Text),
            ],
        'string': [
            (r'"', String, '#pop'),
            (r'""|`.', String.Escape),
            (r'[^\`"\n]+', String), # all other characters
        ],
        'block': [
            include('root'),
            ('{', Punctuation, '#push'),
            ('}', Punctuation, '#pop'),
        ],
        'parameters': [
            (r'\)', Punctuation, '#pop'),
            (r'\(', Punctuation, '#push'),
            include('numbers'),
            include('literals'),
            include('whitespace'),
#            (r'=', Operator, 'expressions'),
        ],
        'keywords': [
            (r'(static|global|local)\b', Keyword.Type),
            (r'(if|else|and|or)\b', Keyword.Reserved),
            ],
        'directives': [
            (r'#\w+?\s', Keyword),
            ],
        'labels': [
            # hotkeys and labels 
            # technically, hotkey names are limited to named keys and buttons
            (r'(^\s*)([^:\s]+?:{1,2})', bygroups(Whitespace, Name.Label)), 
             # hotstrings
            (r'(^\s*)(::[]\w#@$?[]+?::)', bygroups(Whitespace, Name.Label)),  
            ],
        'comments': [
            (r'^;+.*?$', Comment.Single),  # beginning of line comments
            (r'(?<=\s);+.*?$', Comment.Single),    # end of line comments
            (r'^/\*.*?\n\*/', Comment.Multiline),  
            (r'(?<!\n)/\*.*?\n\*/', Error),  # must be at start of line
            ],
        'whitespace': [
            (r'[ \t]', Whitespace),
            ],
        'numbers': [
            (r'(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?', Number.Float),
            (r'\d+[eE][+-]?[0-9]+', Number.Float),
            (r'0\d+', Number.Oct),
            (r'0[xX][a-fA-F0-9]+', Number.Hex),
            (r'\d+L', Number.Integer.Long),
            (r'\d+', Number.Integer)
        ],
        'continuation': [
            (r'\n\)', Punctuation, '#pop'),
            (r'\s[^\n\)]+', String),
        ],
        'keynames': [
            (r'\[[^\]]+\]', Keyword, 'keynames')
        ],
        'commands': [
            (r'(autotrim|blockinput|break|click|'
             r'clipwait|continue|control|'
             r'controlclick|controlfocus|controlget|'
             r'controlgetfocus|controlgetpos|controlgettext|'
             r'controlmove|controlsend|controlsendraw|'
             r'controlsettext|coordmode|critical|'
             r'detecthiddentext|detecthiddenwindows|'
             r'dllcall|drive|'
             r'driveget|drivespacefree|'
             r'else|envadd|envdiv|'
             r'envget|envmult|envset|'
             r'envsub|envupdate|exit|'
             r'exitapp|fileappend|filecopy|'
             r'filecopydir|filecreatedir|filecreateshortcut|'
             r'filedelete|filegetattrib|filegetshortcut|'
             r'filegetsize|filegettime|filegetversion|'
             r'fileinstall|filemove|filemovedir|'
             r'fileread|filereadline|filerecycle|'
             r'filerecycleempty|fileremovedir|fileselectfile|'
             r'fileselectfolder|filesetattrib|filesettime|'
             r'formattime|gosub|'
             r'goto|groupactivate|groupadd|'
             r'groupclose|groupdeactivate|gui|'
             r'guicontrol|guicontrolget|hotkey|'
             r'ifexist|ifgreater|ifgreaterorequal|'
             r'ifinstring|ifless|iflessorequal|'
             r'ifmsgbox|ifnotequal|ifnotexist|'
             r'ifnotinstring|ifwinactive|ifwinexist|'
             r'ifwinnotactive|ifwinnotexist|imagesearch|'
             r'inidelete|iniread|iniwrite|'
             r'input|inputbox|keyhistory|'
             r'keywait|listhotkeys|listlines|'
             r'listvars|loop|'
             r'menu|mouseclick|mouseclickdrag|'
             r'mousegetpos|mousemove|msgbox|'
             r'onmessage|onexit|outputdebug|'
             r'pixelgetcolor|pixelsearch|postmessage|'
             r'process|progress|random|'
             r'regexmatch|regexreplace|registercallback|'
             r'regdelete|regread|regwrite|'
             r'reload|repeat|return|'
             r'run|runas|runwait|'
             r'send|sendevent|sendinput|'
             r'sendmessage|sendmode|sendplay|'
             r'sendraw|setbatchlines|setcapslockstate|'
             r'setcontroldelay|setdefaultmousespeed|setenv|'
             r'setformat|setkeydelay|setmousedelay|'
             r'setnumlockstate|setscrolllockstate|'
             r'setstorecapslockmode|'
             r'settimer|settitlematchmode|setwindelay|'
             r'setworkingdir|shutdown|sleep|'
             r'sort|soundbeep|soundget|'
             r'soundgetwavevolume|soundplay|soundset|'
             r'soundsetwavevolume|splashimage|splashtextoff|'
             r'splashtexton|splitpath|statusbargettext|'
             r'statusbarwait|stringcasesense|stringgetpos|'
             r'stringleft|stringlen|stringlower|'
             r'stringmid|stringreplace|stringright|'
             r'stringsplit|stringtrimleft|stringtrimright|'
             r'stringupper|suspend|sysget|'
             r'thread|tooltip|transform|'
             r'traytip|urldownloadtofile|while|'
             r'varsetcapacity|'
             r'winactivate|winactivatebottom|winclose|'
             r'winget|wingetactivestats|wingetactivetitle|'
             r'wingetclass|wingetpos|wingettext|'
             r'wingettitle|winhide|winkill|'
             r'winmaximize|winmenuselectitem|winminimize|'
             r'winminimizeall|winminimizeallundo|winmove|'
             r'winrestore|winset|winsettitle|'
             r'winshow|winwait|winwaitactive|'
             r'winwaitclose|winwaitnotactive'
             r'true|false|NULL)\b', Keyword, 'command'),
            ],

        }





