# -*- coding: utf-8 -*-
from pygments.lexer import ExtendedRegexLexer, RegexLexer, \
     bygroups, using, include, combined
from pygments.token import *   
import re
from pygments.styles import get_style_by_name
ahkcommandsFile = 'ahkSyntax/CommandNames.txt'
f = open(ahkcommandsFile)
ahkcommands = f.read()
f.close()
ahkfunctionsFile = 'ahkSyntax/functionNames.txt'
f = open(ahkfunctionsFile)
ahkfunctions = f.read()
f.close()
ahkbuiltInVariablesFile = 'ahkSyntax/builtInVariables.txt'
f = open(ahkbuiltInVariablesFile)
ahkbuiltInVariables = f.read()
f.close()

class AhkLexer(ExtendedRegexLexer):    	    
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
            (r'[]{}(),;[]', Punctuation),
            (r'(in|is|and|or|not)\b', Operator.Word),
            (r'\%[a-zA-Z_#@$][a-zA-Z0-9_#@$]*\%', Name.Variable), 
            (r'!=|==|:=|\.=|<<|>>|[-~+/*%=<>&^|?:!.]', Operator),            
            include('commands'),
            include('labels'),
            include('builtInFunctions'),
            include('builtInVariables'),
            (r'"', String, combined('stringescape', 'dqs')),
            include('numbers'),
            (r'[a-zA-Z_#@$][a-zA-Z0-9_#@$]*', Name),  
            (r'\\|\'', Text),
            (r'\`([\,\%\`abfnrtv\-\+;])', String.Escape),
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
            (r'(?i)^(\s*)(global|local|static|'
        r'#AllowSameLineComments|#ClipboardTimeout|#CommentFlag|'
        r'#ErrorStdOut|#EscapeChar|#HotkeyInterval|'
        r'#HotkeyModifierTimeout|#Hotstring|#IfWinActive|'
        r'#IfWinExist|#IfWinNotActive|#IfWinNotExist|'
        r'#IncludeAgain|#Include|#InstallKeybdHook|'
        r'#InstallMouseHook|#KeyHistory|#LTrim|'
        r'#MaxHotkeysPerInterval|#MaxMem|#MaxThreads|'
        r'#MaxThreadsBuffer|#MaxThreadsPerHotkey|#NoEnv|'
        r'#NoTrayIcon|#Persistent|#SingleInstance|'
        r'#UseHook|#WinActivateForce|AutoTrim|'
        r'BlockInput|Break|Click|'
        r'ClipWait|Continue|Control|'
        r'ControlClick|ControlFocus|ControlGetFocus|'
        r'ControlGetPos|ControlGetText|ControlGet|'
        r'ControlMove|ControlSend|ControlSendRaw|'
        r'ControlSetText|CoordMode|Critical|'
        r'DetectHiddenText|DetectHiddenWindows|Drive|'
        r'DriveGet|DriveSpaceFree|Edit|'
        r'Else|EnvAdd|EnvDiv|'
        r'EnvGet|EnvMult|EnvSet|'
        r'EnvSub|EnvUpdate|Exit|'
        r'ExitApp|FileAppend|FileCopy|'
        r'FileCopyDir|FileCreateDir|FileCreateShortcut|'
        r'FileDelete|FileGetAttrib|FileGetShortcut|'
        r'FileGetSize|FileGetTime|FileGetVersion|'
        r'FileInstall|FileMove|FileMoveDir|'
        r'FileRead|FileReadLine|FileRecycle|'
        r'FileRecycleEmpty|FileRemoveDir|FileSelectFile|'
        r'FileSelectFolder|FileSetAttrib|FileSetTime|'
        r'FormatTime|GetKeyState|Gosub|'
        r'Goto|GroupActivate|GroupAdd|'
        r'GroupClose|GroupDeactivate|Gui|'
        r'GuiControl|GuiControlGet|Hotkey|'
        r'IfEqual|IfExist|IfGreaterOrEqual|'
        r'IfGreater|IfInString|IfLess|'
        r'IfLessOrEqual|IfMsgBox|IfNotEqual|'
        r'IfNotExist|IfNotInString|IfWinActive|'
        r'IfWinExist|IfWinNotActive|IfWinNotExist|'
        r'If |ImageSearch|IniDelete|'
        r'IniRead|IniWrite|InputBox|'
        r'Input|KeyHistory|KeyWait|'
        r'ListHotkeys|ListLines|ListVars|'
        r'Loop|Menu|MouseClickDrag|'
        r'MouseClick|MouseGetPos|MouseMove|'
        r'MsgBox|OnExit|OutputDebug|'
        r'Pause|PixelGetColor|PixelSearch|'
        r'PostMessage|Process|Progress|'
        r'Random|RegDelete|RegRead|'
        r'RegWrite|Reload|Repeat|'
        r'Return|RunAs|RunWait|'
        r'Run|SendEvent|SendInput|'
        r'SendMessage|SendMode|SendPlay|'
        r'SendRaw|Send|SetBatchLines|'
        r'SetCapslockState|SetControlDelay|SetDefaultMouseSpeed|'
        r'SetEnv|SetFormat|SetKeyDelay|'
        r'SetMouseDelay|SetNumlockState|SetScrollLockState|'
        r'SetStoreCapslockMode|SetTimer|SetTitleMatchMode|'
        r'SetWinDelay|SetWorkingDir|Shutdown|'
        r'Sleep|Sort|SoundBeep|'
        r'SoundGet|SoundGetWaveVolume|SoundPlay|'
        r'SoundSet|SoundSetWaveVolume|SplashImage|'
        r'SplashTextOff|SplashTextOn|SplitPath|'
        r'StatusBarGetText|StatusBarWait|StringCaseSense|'
        r'StringGetPos|StringLeft|StringLen|'
        r'StringLower|StringMid|StringReplace|'
        r'StringRight|StringSplit|StringTrimLeft|'
        r'StringTrimRight|StringUpper|Suspend|'
        r'SysGet|Thread|ToolTip|'
        r'Transform|TrayTip|URLDownloadToFile|'
        r'While|WinActivate|WinActivateBottom|'
        r'WinClose|WinGetActiveStats|WinGetActiveTitle|'
        r'WinGetClass|WinGetPos|WinGetText|'
        r'WinGetTitle|WinGet|WinHide|'
        r'WinKill|WinMaximize|WinMenuSelectItem|'
        r'WinMinimizeAllUndo|WinMinimizeAll|WinMinimize|'
        r'WinMove|WinRestore|WinSetTitle|'
        r'WinSet|WinShow|WinWaitActive|'
        r'WinWaitClose|WinWaitNotActive|WinWait)\b',
             bygroups(Whitespace,  Name.Builtin)),
            ],
        'builtInFunctions': [
            (r'(?i)(' + ahkfunctions + r')\b\(', Name.Function),            
        ],
        'builtInVariables': [
            (r'(?i)(' + ahkbuiltInVariables + r')\b', Name.Variable), 
            ],
        'labels': [
            # hotkeys and labels 
            # technically, hotkey names are limited to named keys and buttons
            (r'(^\s*)([^:\s\(\"]+?:{1,2})', bygroups(Whitespace, Name.Label)), 
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
        'stringescape': [
            (r'\"\"|\`([\,\%\`abfnrtv])', String.Escape),
        ],
        'strings': [
            (r'[^"\n]+', String),
        ],
        'dqs': [
            (r'"', String, '#pop'),
            include('strings')
        ],        
        'garbage': [
            (r'[^\S\n]', Text),
#            (r'.', Text),      # no cheating
            ],
    }


