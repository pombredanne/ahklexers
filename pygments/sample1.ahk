 ; single line comment
; single line comment
#NoTrayIcon  ; single line comment
k::
::sdf::
label:
  Msgbox % "hello" . A_UserName
Msgbox % "hello escaped "" quotes."
foo := regexmatch(bar, "reg")
Return
/*  multiline
comment
*/
(
continuation
section
)
