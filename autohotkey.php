<?php
/*************************************************************************************
 * autohotkey.php
 * --------
 * Author: naveen garg (naveen.garg@gmail.com)
 * Copyright: (c) 2009 and to GESHi ;)
 * Release Version: 0.2
 * Date Started: 2009/06/11
 *
 * Autohotkey language file for GeSHi.
 *
 * CHANGES
 * -------
 * Release 0.1 (2009/06/11)
 * - First Release
 *
 * Current bugs & todo:
 * ----------
 * Reference: http://www.autohotkey.com/docs/
 *************************************************************************************
 *
 *    This file is part of GeSHi.
 *
 *   GeSHi is free software; you can redistribute it and/or modify
 *   it under the terms of the GNU General Public License as published by
 *   the Free Software Foundation; either version 2 of the License,
or
 *   (at your option) any later version.
 *
 *   GeSHi is distributed in the hope that it will be useful,
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *   GNU General Public License for more details.
 *
 *   You should have received a copy of the GNU General Public License
 *   along with GeSHi; if not,
write to the Free Software
 *   Foundation,
Inc.,
59 Temple Place,
Suite 330,
Boston,
MA  02111-1307  USA
 *
 ************************************************************************************/

$language_data = array (
    'LANG_NAME' => 'Autohotkey',
    'COMMENT_SINGLE' => array(';'),
    'COMMENT_MULTI' => array('/*' => '*/'),
    'CASE_KEYWORDS' => GESHI_CAPS_NO_CHANGE,
    'QUOTEMARKS' => array('"'),
    'ESCAPE_CHAR' => '',
    'KEYWORDS' => array(
    1 => array(
    'while','if','and','or','else','return'
    ),
    2 => array('A_(\w+)'  // built in variables
    ),
    3 => array(
    'AutoTrim',
    'BlockInput','Break','Click',
    'ClipWait','Continue','Control',
    'ControlClick','ControlFocus','ControlGet',
    'ControlGetFocus','ControlGetPos','ControlGetText',
    'ControlMove','ControlSend','ControlSendRaw',
    'ControlSetText','CoordMode','Critical',
    'DetectHiddenText','DetectHiddenWindows','DllCall','Drive',
    'DriveGet','DriveSpaceFree',
    'Else','EnvAdd','EnvDiv',
    'EnvGet','EnvMult','EnvSet',
    'EnvSub','EnvUpdate','Exit',
    'ExitApp','FileAppend','FileCopy',
    'FileCopyDir','FileCreateDir','FileCreateShortcut',
    'FileDelete','FileGetAttrib','FileGetShortcut',
    'FileGetSize','FileGetTime','FileGetVersion',
    'FileInstall','FileMove','FileMoveDir',
    'FileRead','FileReadLine','FileRecycle',
    'FileRecycleEmpty','FileRemoveDir','FileSelectFile',
    'FileSelectFolder','FileSetAttrib','FileSetTime',
    'FormatTime','Gosub',
    'Goto','GroupActivate','GroupAdd',
    'GroupClose','GroupDeactivate','Gui',
    'GuiControl','GuiControlGet','Hotkey',
    'IfExist','IfGreater','IfGreaterOrEqual',
    'IfInString','IfLess','IfLessOrEqual',
    'IfMsgBox','IfNotEqual','IfNotExist',
    'IfNotInString','IfWinActive','IfWinExist',
    'IfWinNotActive','IfWinNotExist','ImageSearch',
    'IniDelete','IniRead','IniWrite',
    'Input','InputBox','KeyHistory',
    'KeyWait','ListHotkeys','ListLines',
    'ListVars','Loop',
    'Menu','MouseClick','MouseClickDrag',
    'MouseGetPos','MouseMove','MsgBox',
    'OnMessage','OnExit','OutputDebug',
    'PixelGetColor','PixelSearch','PostMessage',
    'Process','Progress','Random',
    'RegExMatch','RegExReplace','RegisterCallback',
    'RegDelete','RegRead','RegWrite',
    'Reload','Repeat','Return',
    'Run','RunAs','RunWait',
    'Send','SendEvent','SendInput',
    'SendMessage','SendMode','SendPlay',
    'SendRaw','SetBatchLines','SetCapslockState',
    'SetControlDelay','SetDefaultMouseSpeed','SetEnv',
    'SetFormat','SetKeyDelay','SetMouseDelay',
    'SetNumlockState','SetScrollLockState','SetStoreCapslockMode',
    'SetTimer','SetTitleMatchMode','SetWinDelay',
    'SetWorkingDir','Shutdown','Sleep',
    'Sort','SoundBeep','SoundGet',
    'SoundGetWaveVolume','SoundPlay','SoundSet',
    'SoundSetWaveVolume','SplashImage','SplashTextOff',
    'SplashTextOn','SplitPath','StatusBarGetText',
    'StatusBarWait','StringCaseSense','StringGetPos',
    'StringLeft','StringLen','StringLower',
    'StringMid','StringReplace','StringRight',
    'StringSplit','StringTrimLeft','StringTrimRight',
    'StringUpper','Suspend','SysGet',
    'Thread','ToolTip','Transform',
    'TrayTip','URLDownloadToFile','While',
    'VarSetCapacity',
    'WinActivate','WinActivateBottom','WinClose',
    'WinGet','WinGetActiveStats','WinGetActiveTitle',
    'WinGetClass','WinGetPos','WinGetText',
    'WinGetTitle','WinHide','WinKill',
    'WinMaximize','WinMenuSelectItem','WinMinimize',
    'WinMinimizeAll','WinMinimizeAllUndo','WinMove',
    'WinRestore','WinSet','WinSetTitle',
    'WinShow','WinWait','WinWaitActive',
    'WinWaitClose','WinWaitNotActive'
    ),
    4 => array(
    'Abs','ACos','Asc','ASin',
    'ATan','Ceil','Chr','Cos',
    'Exp','FileExist','Floor',
    'GetKeyState','IL_Add','IL_Create','IL_Destroy',
    'InStr','IsFunc','IsLabel','Ln',
    'Log','LV_Add','LV_Delete','LV_DeleteCol',
    'LV_GetCount','LV_GetNext','LV_GetText','LV_Insert',
    'LV_InsertCol','LV_Modify','LV_ModifyCol','LV_SetImageList',
    'Mod','NumGet','NumPut',
    'Round',
    'SB_SetIcon','SB_SetParts','SB_SetText','Sin',
    'Sqrt','StrLen','SubStr','Tan',
    'TV_Add','TV_Delete','TV_GetChild','TV_GetCount',
    'TV_GetNext','TV_Get','TV_GetParent','TV_GetPrev',
    'TV_GetSelection','TV_GetText','TV_Modify',
    'WinActive','WinExist'
    ),
    5 => array(   // #Directives
    'AllowSameLineComments','ClipboardTimeout','CommentFlag',
    'ErrorStdOut','EscapeChar','HotkeyInterval',
    'HotkeyModifierTimeout','Hotstring','IfWinActive',
    'IfWinExist','IfWinNotActive','IfWinNotExist',
    'Include','IncludeAgain','InstallKeybdHook',
    'InstallMouseHook','KeyHistory','LTrim',
    'MaxHotkeysPerInterval','MaxMem','MaxThreads',
    'MaxThreadsBuffer','MaxThreadsPerHotkey','NoEnv',
    'NoTrayIcon','Persistent','SingleInstance',
    'UseHook','WinActivateForce'
    ),
    6 => array(
    'Shift','LShift','RShift',
    'Alt','LAlt','RAlt',
    'LControl','RControl',
    'Ctrl','LCtrl','RCtrl',
    'LWin','RWin','AppsKey',
    'AltDown','AltUp','ShiftDown',
    'ShiftUp','CtrlDown','CtrlUp',
    'LWinDown','LWinUp','RWinDown',
    'RWinUp','LButton','RButton',
    'MButton','WheelUp','WheelDown',
    'WheelLeft','WheelRight','XButton1',
    'XButton2','Joy1','Joy2',
    'Joy3','Joy4','Joy5',
    'Joy6','Joy7','Joy8',
    'Joy9','Joy10','Joy11',
    'Joy12','Joy13','Joy14',
    'Joy15','Joy16','Joy17',
    'Joy18','Joy19','Joy20',
    'Joy21','Joy22','Joy23',
    'Joy24','Joy25','Joy26',
    'Joy27','Joy28','Joy29',
    'Joy30','Joy31','Joy32',
    'JoyX','JoyY','JoyZ',
    'JoyR','JoyU','JoyV',
    'JoyPOV','JoyName','JoyButtons',
    'JoyAxes','JoyInfo','Space',
    'Tab','Enter',
    'Escape','Esc','BackSpace',
    'BS','Delete','Del',
    'Insert','Ins','PGUP',
    'PGDN','Home','End',
    'Up','Down','Left',
    'Right','PrintScreen','CtrlBreak',
    'Pause','ScrollLock','CapsLock',
    'NumLock','Numpad0','Numpad1',
    'Numpad2','Numpad3','Numpad4',
    'Numpad5','Numpad6','Numpad7',
    'Numpad8','Numpad9','NumpadMult',
    'NumpadAdd','NumpadSub','NumpadDiv',
    'NumpadDot','NumpadDel','NumpadIns',
    'NumpadClear','NumpadUp','NumpadDown',
    'NumpadLeft','NumpadRight','NumpadHome',
    'NumpadEnd','NumpadPgup','NumpadPgdn',
    'NumpadEnter','F1','F2',
    'F3','F4','F5',
    'F6','F7','F8',
    'F9','F10','F11',
    'F12','F13','F14',
    'F15','F16','F17',
    'F18','F19','F20',
    'F21','F22','F23',
    'F24','Browser_Back','Browser_Forward',
    'Browser_Refresh','Browser_Stop','Browser_Search',
    'Browser_Favorites','Browser_Home','Volume_Mute',
    'Volume_Down','Volume_Up','Media_Next',
    'Media_Prev','Media_Stop','Media_Play_Pause',
    'Launch_Mail','Launch_Media','Launch_App1',
    'Launch_App2'  
    ),
    7 => array('Add',  // Gui commands  
    'Show', 'Submit', 'Cancel', 'Destroy',
    'Font', 'Color', 'Margin', 'Flash', 'Default', 
    'GuiEscape','GuiClose','GuiSize','GuiContextMenu','GuiDropFilesTabStop',
    ),
    8 => array('Button',  // Gui Controls
    'Checkbox','Radio','DropDownList','DDL',
    'ComboBox','ListBox','ListView',
    'Text', 'Edit', 'UpDown', 'Picture',
    'TreeView','DateTime', 'MonthCal',
    'Slider'
    ),

    ),
    'SYMBOLS' => array(
    '(',')','[',']',
    '+','-','*','/','&','^',
    '=','+=','-=','*=','/=','&=',
    '==','<','<=','>','>=',':=',
    ',','.'
    ),
    'CASE_SENSITIVE' => array(
    GESHI_COMMENTS => false,
    1 => false,
    2 => false,
    3 => false,
    4 => false,
    5 => false,
    6 => false,
    7 => false,
    8 => false
    ),
    'STYLES' => array(
    'KEYWORDS' => array(
    1 => 'color: #AAAAFF; font-weight: bold;',       // reserved #blue
    2 => 'color: #88FF88;',                         // BIV yellow
    3 => 'color: #FF00FF; font-style: italic;',       // commands purple
    4 => 'color: #888844; font-weight: bold;',       // functions #0080FF
    5 => 'color: #000000; font-style: italic;',    // directives #black
    6 => 'color: #FF0000; font-style: italic;',      // hotkeys #red
    7 => 'color: #000000; font-style: italic;',    // gui commands #black
    8 => 'color: #000000; font-style: italic;'      // gui controls
    ),
    'COMMENTS' => array(
    0 => 'font-style: italic; color: #009933;',
    'MULTI' => 'font-style: italic; color: #669900;'
    ),
    'ESCAPE_CHAR' => array(
    0 => ''
    ),
    'BRACKETS' => array(
    0 => 'color: #00FF00; font-weight: bold;'
    ),
    'STRINGS' => array(
    0 => 'font-weight: bold; color: #008080;'
    ),
    'NUMBERS' => array(
    0 => 'color: #0000dd;'
    ),
    'METHODS' => array(
    1 => 'color: #0000FF; font-style: italic; font-weight: italic;'
    ),
    'SYMBOLS' => array(
    0 => 'color: #000000; font-weight: italic;'
    ),
    'REGEXPS' => array(
    0 => 'font-weight: italic; color: #A00A0;',
    1 => 'color: #CC0000; font-style: italic;',
    2 => 'color: #DD0000; font-style: italic;'
    ),
    'SCRIPT' => array(
    )
    ),
    'OOLANG' => false,
    'OBJECT_SPLITTERS' => array(
    1 => '_'
    ),
    'REGEXPS' => array(
    //Variables
    0 => '%[a-zA-Z_][a-zA-Z0-9_]*%',
    //hotstrings
    1 => '::[\w\d]+::',
    //labels
    2 => '\w[\w\d]+:\s'  // labels
    ),    
    'URLS' => array(
    1 => '',
    2 => 'http://www.autohotkey.com/docs/Variables.htm#{FNAME}',
    3 => 'http://www.autohotkey.com/docs/commands/{FNAME}.htm',
    4 => 'http://www.autohotkey.com/docs/Functions.htm#BuiltIn',
    5 => 'http://www.autohotkey.com/docs/commands/_{FNAME}.htm',
    6 => '',
    7 => 'http://www.autohotkey.com/docs/commands/Gui.htm#{FNAME}',
    8 => 'http://www.autohotkey.com/docs/commands/GuiControls.htm#{FNAME}'
    ),
    'STRICT_MODE_APPLIES' => GESHI_MAYBE,
    'SCRIPT_DELIMITERS' => array(
    ),
    'HIGHLIGHT_STRICT_BLOCK' => array(
    0 => true,
    1 => true,
    2 => true,
    3 => true
    ),
    'PARSER_CONTROL' => array(
    'KEYWORDS' => array(
    5 => array(
    'DISALLOWED_BEFORE' => '(?<!\w)\#'
    )
    )
    )
);

?>