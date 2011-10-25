 ; single line comment
; single line comment
#NoTrayIcon  ; single line comment
k::
::sdf::
label:
Msgbox, hello world, % 1, 2
Msgbox % "A_ScriptDir\lib\" . A_UserName
Msgbox % "hello escaped "" quotes and other escapes `n`r."
tooltip %mytip%
foo := regexmatch(bar, "reg")
Return
/*  multiline
comment
*/
Msgbox, hello world, % 1, 2
(
continuation
section
)
