# -*- coding: utf-8 -*-
import re
from pygments.lexer import Lexer, ExtendedRegexLexer, RegexLexer, include, bygroups, using, \
     this, do_insertions
 
from pygments.token import *       
class AutohotkeyLexer(ExtendedRegexLexer):
    """  
    For `autohotkey <http://www.autohotkey.com/>`_ source code.
       
    *New in Pygments 1.4.*
    """
    name = 'autohotkey'
    aliases = ['ahk']
    filenames = ['*.ahk', '*.ahkl']
    mimetypes = ['text/x-autohotkey']
    from pygments.lexer import ExtendedRegexLexer, RegexLexer, \
    bygroups, using, include, combined
    def commands_callback(lexer, match, ctx):
        pwhitespace = match.group(1)
        yield match.start(), Whitespace, pwhitespace
        ctx.pos = match.end() - 2
    tokens = { 	               	
        'root': [	        
            include('comments'),
            (r'^(\s*)(\()', bygroups(Whitespace, Generic), 'incontinuation'),
            include('labels'),  
            include('commands'),
            (r'(\s*)([a-zA-Z_#@$][a-zA-Z0-9_#@$]*)(\s*)(\W=)',
             bygroups(Whitespace, Name, Punctuation, Whitespace)), 
            (r'\s*\w[^=:(,%\s]*', Name, 'incommand'),       
            include('variables'),
            include('expressions'),                        
            include('builtInFunctions'),                   
            include('builtInVariables'),                   
            (r'"', String, combined('stringescape', 'dqs')),
            include('numbers'),                            
            (r'[a-zA-Z_#@$][a-zA-Z0-9_#@$]*', Name),       
            (r'\\|\'', Text),                              
            (r'\`([\,\%\`abfnrtv\-\+;])', String.Escape),  
            include('garbage'),                            
        ],  
        'variables': [(r'\%[a-zA-Z_#@$][a-zA-Z0-9_#@$]*\%', Name.Variable),
                      ], 
        'expressions': [                                   
            (r'\s+', Whitespace),                          
            (r'[]{}(),;[]', Punctuation),                  
            (r'(in|is|and|or|not)\b', Operator.Word),      
            (r'!=|==|:=|\.=|<<|>>|[-~+/*%=<>&^|?:!.]', Operator),            
            ],                                             
        'incommand': [                                     
            (r'(\s*)(,)', bygroups(Whitespace, Punctuation)),
            (r'\s*%\s', Punctuation, '#pop'),
            (r'[^\n]', String, 'rawstring'),
            include('comments'),
            ],                  
        'comments': [           
            (r'^(\s*)(/\*)', bygroups(Whitespace, Comment.Multiline),
                             'incomment'),
            (r'\s+;.*?$', Comment.Singleline),
            (r'^;.*?$', Comment.Singleline),
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
             bygroups(Whitespace,  Name.Builtin), 'incommand' ),
            ],                                                 
        'builtInFunctions': [                                  
            (r'(?i)(Abs|ACos|Asc|'
        r'ASin|ATan|Ceil|'
        r'Chr|Cos|DllCall|'
        r'Exp|FileExist|Floor|'
        r'GetKeyState|IL_Add|IL_Create|'
        r'IL_Destroy|InStr|IsFunc|'
        r'IsLabel|Ln|Log|'
        r'LV_Add|LV_Delete|LV_DeleteCol|'
        r'LV_GetCount|LV_GetNext|LV_GetText|'
        r'LV_Insert|LV_InsertCol|LV_Modify|'
        r'LV_ModifyCol|LV_SetImageList|Mod|'
        r'NumGet|NumPut|OnMessage|'
        r'RegExMatch|RegExReplace|RegisterCallback|'
        r'Round|SB_SetIcon|SB_SetParts|'
        r'SB_SetText|Sin|Sqrt|'
        r'StrLen|SubStr|Tan|'
        r'TV_Add|TV_Delete|TV_GetChild|'
        r'TV_GetCount|TV_GetNext|TV_Get|'
        r'TV_GetParent|TV_GetPrev|TV_GetSelection|'
        r'TV_GetText|TV_Modify|VarSetCapacity|'
        r'WinActive|WinExist|Object|'
        r'ComObjActive|ComObjArray|ComObjEnwrap|'
        r'ComObjUnwrap|ComObjParameter|ComObjType|'
        r'ComObjConnect|ComObjCreate|ComObjGet|'
        r'ComObjError|ComObjValue|Insert|'
        r'MinIndex|MaxIndex|Remove|'
        r'SetCapacity|GetCapacity|GetAddress|'
        r'_NewEnum|FileOpen|Read|'
        r'Write|ReadLine|WriteLine|'
        r'ReadNumType|WriteNumType|RawRead|'
        r'RawWrite|Seek|Tell|'
        r'Close|Next|IsObject|'
        r'StrPut|StrGet|Trim|'
        r'LTrim|RTrim)\b', Name.Function),            
        ],
        'builtInVariables': [
            (r'(?i)(A_AhkPath|A_AhkVersion|A_AppData|'
        r'A_AppDataCommon|A_AutoTrim|A_BatchLines|'
        r'A_CaretX|A_CaretY|A_ComputerName|'
        r'A_ControlDelay|A_Cursor|A_DD|'
        r'A_DDD|A_DDDD|A_DefaultMouseSpeed|'
        r'A_Desktop|A_DesktopCommon|A_DetectHiddenText|'
        r'A_DetectHiddenWindows|A_EndChar|A_EventInfo|'
        r'A_ExitReason|A_FormatFloat|A_FormatInteger|'
        r'A_Gui|A_GuiEvent|A_GuiControl|'
        r'A_GuiControlEvent|A_GuiHeight|A_GuiWidth|'
        r'A_GuiX|A_GuiY|A_Hour|'
        r'A_IconFile|A_IconHidden|A_IconNumber|'
        r'A_IconTip|A_Index|A_IPAddress1|'
        r'A_IPAddress2|A_IPAddress3|A_IPAddress4|'
        r'A_ISAdmin|A_IsCompiled|A_IsCritical|'
        r'A_IsPaused|A_IsSuspended|A_KeyDelay|'
        r'A_Language|A_LastError|A_LineFile|'
        r'A_LineNumber|A_LoopField|A_LoopFileAttrib|'
        r'A_LoopFileDir|A_LoopFileExt|A_LoopFileFullPath|'
        r'A_LoopFileLongPath|A_LoopFileName|A_LoopFileShortName|'
        r'A_LoopFileShortPath|A_LoopFileSize|A_LoopFileSizeKB|'
        r'A_LoopFileSizeMB|A_LoopFileTimeAccessed|A_LoopFileTimeCreated|'
        r'A_LoopFileTimeModified|A_LoopReadLine|A_LoopRegKey|'
        r'A_LoopRegName|A_LoopRegSubkey|A_LoopRegTimeModified|'
        r'A_LoopRegType|A_MDAY|A_Min|'
        r'A_MM|A_MMM|A_MMMM|'
        r'A_Mon|A_MouseDelay|A_MSec|'
        r'A_MyDocuments|A_Now|A_NowUTC|'
        r'A_NumBatchLines|A_OSType|A_OSVersion|'
        r'A_PriorHotkey|A_ProgramFiles|A_Programs|'
        r'A_ProgramsCommon|A_ScreenHeight|A_ScreenWidth|'
        r'A_ScriptDir|A_ScriptFullPath|A_ScriptName|'
        r'A_Sec|A_Space|A_StartMenu|'
        r'A_StartMenuCommon|A_Startup|A_StartupCommon|'
        r'A_StringCaseSense|A_Tab|A_Temp|'
        r'A_ThisFunc|A_ThisHotkey|A_ThisLabel|'
        r'A_ThisMenu|A_ThisMenuItem|A_ThisMenuItemPos|'
        r'A_TickCount|A_TimeIdle|A_TimeIdlePhysical|'
        r'A_TimeSincePriorHotkey|A_TimeSinceThisHotkey|A_TitleMatchMode|'
        r'A_TitleMatchModeSpeed|A_UserName|A_WDay|'
        r'A_WinDelay|A_WinDir|A_WorkingDir|'
        r'A_YDay|A_YEAR|A_YWeek|'
        r'A_YYYY|Clipboard|ClipboardAll|'
        r'ComSpec|ErrorLevel|ProgramFiles|'
        r'True|False|A_IsUnicode|'
        r'A_FileEncoding|A_OSVersion|A_PtrSize)\b', Name.Variable), 
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
        'rawstring': [
            (r'\`[\,\%\`abfnrtv]', String.Escape),
            (r'(\n\s*)([^,])', commands_callback, '#pop:2'),
            (r',\s*%\s', Punctuation, '#pop'),
            include('comments'),            
            (r'\s+', Whitespace),  
            include('variables'), 
            (r'[^,\n]+', String),
            (r',', Punctuation),
            ],
        'garbage': [
            (r'[^\S\n]', Text),
#            (r'.', Text),      # no cheating
            ],
    }
