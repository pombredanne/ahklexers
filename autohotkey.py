class AutoHotkeyLexer(RegexLexer):
    """
    For AutoHotkey source code with preprocessor directives.
    """
    name = 'autohotkey'
    aliases = ['ahk']
    filenames = ['*.ahk', '*.ahkl']
    flags = re.IGNORECASE
    #: optional Comment or Whitespace
    _ws = r'(?:\s|;.*?\n|/[*].*?[*]/)+'

    tokens = {
        'whitespace': [
            (r'^\s*#if\s+0', Comment.Preproc, 'if0'),
            (r'^\s*#', Comment.Preproc, 'macro'),
            (r'\n', Text),
            (r'\s+', Text),
             (r';(\n|(.|\n)*?[^\\]\n)', Comment),
            (r'/(\\\n)?[*](.|\n)*?[*](\\\n)?/', Comment),
        ],
        'statements': [
            (r'L?"', String, 'string'),
            (r"L?'(\\.|\\[0-7]{1,3}|\\x[a-fA-F0-9]{1,2}|[^\\\'\n])'", String.Char),
            (r'(\d+\.\d*|\.\d+|\d+)[eE][+-]?\d+[lL]?', Number.Float),
            (r'(\d+\.\d*|\.\d+|\d+[fF])[fF]?', Number.Float),
            (r'0x[0-9a-fA-F]+[Ll]?', Number.Hex),
            (r'\d+[Ll]?', Number.Integer),
            (r'[~!%^&*+=|?:<>/-]', Operator),
            (r'[()\[\],.]', Punctuation),
            (r'\b(case)(.+?)(:)', bygroups(Keyword, using(this), Text)),
            (r'(auto|break|case|const|continue|default|do|else|enum|extern|'
             r'%.*%'
             r'RTrim|JoinLow|BelowNormal|Normal|AboveNormal|'
             r'High|Realtimeahk_id|ahk_pid|ahk_class|ahk_groupBetween|'
             r'Contains|In|Is|Integer|Float|'
             r'IntegerFast|FloatFast|Number|Digit|Xdigit|'
             r'Alpha|Upper|Lower|Alnum|Time|'
             r'DateNot|Or|AndAlwaysOnTop|Topmost|Top|'
             r'Bottom|Transparent|TransColor|Redraw|Region|'
             r'ID|IDLast|ProcessName|MinMax|ControlList|'
             r'Count|List|Capacity|StatusCD|Eject|'
             r'Lock|Unlock|Label|FileSystem|Label|'
             r'SetLabel|Serial|Type|Statusstatic|global|'
             r'local|ByRefSeconds|Minutes|Hours|DaysRead|'
             r'ParseLogoff|Close|Error|SingleTray|Add|'
             r'Rename|Check|UnCheck|ToggleCheck|Enable|'
             r'Disable|ToggleEnable|Default|NoDefault|Standard|'
             r'NoStandard|Color|Delete|DeleteAll|Icon|'
             r'NoIcon|Tip|Click|Show|MainWindow|'
             r'NoMainWindow|UseErrorLevelText|Picture|Pic|GroupBox|'
             r'Button|Checkbox|Radio|DropDownList|DDL|'
             r'ComboBox|ListBox|ListView|DateTime|MonthCal|'
             r'Slider|StatusBar|Tab|Tab2|TreeView|'
             r'UpDownIconSmall|Tile|Report|SortDesc|NoSort|'
             r'NoSortHdr|Grid|Hdr|AutoSize|Rangexm|'
             r'ym|ys|xs|xp|ypFont|'
             r'Resize|Owner|Submit|NoHide|Minimize|'
             r'Maximize|Restore|NoActivate|NA|Cancel|'
             r'Destroy|CenterMargin|MaxSize|MinSize|OwnDialogs|'
             r'GuiEscape|GuiClose|GuiSize|GuiContextMenu|GuiDropFilesTabStop|'
             r'Section|AltSubmit|Wrap|HScroll|VScroll|'
             r'Border|Top|Bottom|Buttons|Expand|'
             r'First|ImageList|Lines|WantCtrlA|WantF2|'
             r'Vis|VisFirst|Number|Uppercase|Lowercase|'
             r'Limit|Password|Multi|WantReturn|Group|'
             r'Background|bold|italic|strike|underline|'
             r'norm|BackgroundTrans|Theme|Caption|Delimiter|'
             r'MinimizeBox|MaximizeBox|SysMenu|ToolWindow|Flash|'
             r'Style|ExStyle|Check3|Checked|CheckedGray|'
             r'ReadOnly|Password|Hidden|Left|Right|'
             r'Center|NoTab|Section|Move|Focus|'
             r'Hide|Choose|ChooseString|Text|Pos|'
             r'Enabled|Disabled|Visible|LastFound|LastFoundExistAltTab|'
             r'ShiftAltTab|AltTabMenu|AltTabAndMenu|AltTabMenuDismissNoTimers|Interrupt|'
             r'Priority|WaitClose|Wait|Exist|Close{Blind}|'
             r'Mod|Pow|Exp|Sqrt|Log|'
             r'Ln|Round|Ceil|Floor|Abs|'
             r'Sin|Cos|Tan|ASin|ACos|'
             r'ATan|BitNot|BitAnd|BitOr|BitXOr|'
             r'BitShiftLeft|BitShiftRightYes|No|Ok|Cancel|'
             r'Abort|Retry|Ignore|TryAgainOn|Off|'
             r'for|goto|if|register|restricted|return|sizeof|static|struct|'
             r'switch|typedef|union|volatile|virtual|while)\b', Keyword),
            (r'(global|static|local)\b',
             Keyword.Type),
            (r'(_{0,2}inline|naked|restrict|thread|typename)\b', Keyword.Reserved),
            (r'__(asm|int8|based|except|int16|stdcall|cdecl|fastcall|int32|'
             r'true|false|NULL|try|leave)\b', Keyword.Reserved),
            (r'(true|false|NULL)\b'
             r'BlockInput|Break|Click|ClipWait|Continue|'
             r'Control|ControlClick|ControlFocus|ControlGet|ControlGetFocus|'
             r'ControlGetPos|ControlGetText|ControlMove|ControlSend|ControlSendRaw|'
             r'ControlSetText|CoordMode|Critical|DetectHiddenText|DetectHiddenWindows|'
             r'Drive|DriveGet|DriveSpaceFree|Edit|Else|'
             r'EnvAdd|EnvDiv|EnvGet|EnvMult|EnvSet|'
             r'EnvSub|EnvUpdate|Exit|ExitApp|FileAppend|'
             r'FileCopy|FileCopyDir|FileCreateDir|FileCreateShortcut|FileDelete|'
             r'FileGetAttrib|FileGetShortcut|FileGetSize|FileGetTime|FileGetVersion|'
             r'FileInstall|FileMove|FileMoveDir|FileRead|FileReadLine|'
             r'FileRecycle|FileRecycleEmpty|FileRemoveDir|FileSelectFile|FileSelectFolder|'
             r'FileSetAttrib|FileSetTime|FormatTime|GetKeyState|Gosub|'
             r'Goto|GroupActivate|GroupAdd|GroupClose|GroupDeactivate|'
             r'Gui|GuiControl|GuiControlGet|Hotkey|If Else|'
             r'IfExist|IfGreater|IfGreaterOrEqual|IfInString|IfLess|'
             r'IfLessOrEqual|IfMsgBox|IfNotEqual|IfNotExist|IfNotInString|'
             r'IfWinActive|IfWinExist|IfWinNotActive|IfWinNotExist|ImageSearch|'
             r'IniDelete|IniRead|IniWrite|Input|InputBox|'
             r'KeyHistory|KeyWait|ListHotkeys|ListLines|ListVars|'
             r'Loop|Loop, FilePattern|Loop, Parse|Loop, Read|Loop, Reg|'
             r'Menu|MouseClick|MouseClickDrag|MouseGetPos|MouseMove|'
             r'MsgBox|OnExit|OutputDebug|Pause|PixelGetColor|OnMessage|'
             r'PixelSearch|PostMessage|Process|Progress|Random|'
             r'RegExMatch|RegExReplace|IsFunc|DllCall|'
             r'RegDelete|RegRead|RegWrite|Reload|Repeat|'
             r'Return|Run|RunAs|RunWait|Send|'
             r'SendEvent|SendInput|SendMessage|SendMode|SendPlay|'
             r'SendRaw|SetBatchLines|SetCapslockState|SetControlDelay|SetDefaultMouseSpeed|'
             r'SetEnv|SetFormat|SetKeyDelay|SetMouseDelay|SetNumlockState|'
             r'SetScrollLockState|SetStoreCapslockMode|SetTimer|SetTitleMatchMode|SetWinDelay|'
             r'SetWorkingDir|Shutdown|Sleep|Sort|SoundBeep|'
             r'SoundGet|SoundGetWaveVolume|SoundPlay|SoundSet|SoundSetWaveVolume|'
             r'SplashImage|SplashTextOff|SplashTextOn|SplitPath|StatusBarGetText|'
             r'StatusBarWait|StringCaseSense|StringGetPos|StringLeft|StringLen|'
             r'StringLower|StringMid|StringReplace|StringRight|StringSplit|'
             r'StringTrimLeft|StringTrimRight|StringUpper|Suspend|SysGet|'
             r'Thread|ToolTip|Transform|TrayTip|URLDownloadToFile|'
             r'While|WinActivate|WinActivateBottom|WinClose|WinGet|'
             r'WinGetActiveStats|WinGetActiveTitle|WinGetClass|WinGetPos|WinGetText|'
             r'WinGetTitle|WinHide|WinKill|WinMaximize|WinMenuSelectItem|'
             r'WinMinimize|WinMinimizeAll|WinMinimizeAllUndo|WinMove|WinRestore|'
             r'WinSet|WinSetTitle|WinShow|WinWait|WinWaitActive|'
             r'WinWaitClose|WinWaitNotActive', Name.Builtin),
            ('[a-zA-Z_][a-zA-Z0-9_]*:(?!:)', Name.Label),
            (r'[a-zA-Z_][a-zA-Z0-9_]*::(?!:)', Name.Label),
            (r'::[a-zA-Z_][a-zA-Z0-9_]*::(?!:)', Name.Label),
            ('[a-zA-Z_][a-zA-Z0-9_]*', Name),
        ],
        'root': [
            include('whitespace'),
            # functions
            (r'((?:[a-zA-Z0-9_*\s])+?(?:\s|[*]))'    # return arguments
             r'([a-zA-Z_][a-zA-Z0-9_]*)'             # method name
             r'(\s*\([^;]*?\))'                      # signature
             r'(' + _ws + r')({)',
             bygroups(using(this), Name.Function, using(this), using(this),
                      Punctuation),
             'function'),
            # function declarations
            (r'((?:[a-zA-Z0-9_*\s])+?(?:\s|[*]))'    # return arguments
             r'([a-zA-Z_][a-zA-Z0-9_]*)'             # method name
             r'(\s*\([^;]*?\))'                      # signature
             r'(' + _ws + r')(;)',
             bygroups(using(this), Name.Function, using(this), using(this),
                      Punctuation)),
            ('', Text, 'statement'),
        ],
        'statement' : [
            include('whitespace'),
            include('statements'),
            ('[{}]', Punctuation),
            (';', Punctuation, '#pop'),
        ],
        'function': [
            include('whitespace'),
            include('statements'),
            ('{', Punctuation, '#push'),
            ('}', Punctuation, '#pop'),
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            (r'[^`"\n]+', String), # all other characters
            (r'\\', String), # stray backslash
        ],
        'macro': [
            (r'[^/\n]+', Comment.Preproc),
            (r'/[*](.|\n)*?[*]/', Comment),
            (r'//.*?\n', Comment, '#pop'),
            (r'/', Comment.Preproc),
            (r'(?<=\\)\n', Comment.Preproc),
            (r'\n', Comment.Preproc, '#pop'),
        ],
        'if0': [
            (r'^\s*#if.*?(?<!\\)\n', Comment, '#push'),
            (r'^\s*#el(?:se|if).*\n', Comment.Preproc, '#pop'),
            (r'^\s*#endif.*?(?<!\\)\n', Comment, '#pop'),
            (r'.*?\n', Comment),
        ]
    }

    stdlib_types = ['global', 'local', 'static']

    def __init__(self, **options):
        self.stdlibhighlighting = get_bool_opt(options,
                'stdlibhighlighting', True)
        self.c99highlighting = get_bool_opt(options,
                'c99highlighting', True)
        RegexLexer.__init__(self, **options)

    def get_tokens_unprocessed(self, text):
        for index, token, value in \
            RegexLexer.get_tokens_unprocessed(self, text):
            if token is Name:
                if self.stdlibhighlighting and value in self.stdlib_types:
                    token = Keyword.Type
            yield index, token, value
