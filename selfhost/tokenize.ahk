#NoEnv
pos = 1
parse(filename := A_ScriptName)
return

parse(filename)
{
  global
  FileRead, file, %filename%
  Loop, parse, file, `n
  {
    length := strlen(A_LoopField)
    pos += length
    if (context = "multiline")
    {
      StringLeft, first2, A_LoopField, 2
 ; msgbox, %first2% %context%
      if (first2 = "*/")
      {
	context = "normal"
}
  continue
}


  StringLeft, first, A_LoopField, 1
  char := Asc(first)
  if char%char%(A_LoopField)
  {
    lastline := A_LoopField
    continue
    }
  RegExMatch(A_LoopField, "\S", char1)
/*
multiline comment multiline comment
   ; msgbox %char1%
*/
   ; msgbox %char1%
    char := Asc(char1)
    char%char%(A_LoopField)
    lastline := A_LoopField
  }
}


char59(line)  ;; ';'
{
  msgbox, comment `n %line%
  return 1
}


char35(line)  ;; '#'
{
  msgbox, directive `n %line%
  return 1
}

char47(line) ;; /
{
  global
  if (substr(line, 1, 2) = "/*")
  {
    context := "multiline"
    result := regexmatch(file, "/\*(.|[\r\n])*?\*/", comment) ; http://ostermiller.org/findcomment.html
    msgbox, multiline comment `n %comment% %comment1%
  }
  return 1
}
