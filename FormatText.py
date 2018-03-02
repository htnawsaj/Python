##########################################################################
##Modified the script from http://www.macdrifter.com/2012/07/pythonista-app-from-toy-to-tool.html
##Thanks to this http://www.macstories.net/stories/editorial-for-ipad-review/ for pointing it.
##########################################################################


import sys
import re
import urllib
import android

def titleCase(s):
    newText = re.sub(r"[A-Za-z]+('[A-Za-z]+)?",lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(),s)
    return newText

droid = android.Android()

inputString= droid.dialogGetInput("Select Conversion:","[1] Title Case\n[2] lowercase\n[3] UPPERCASE\n[4] Capital case\n[5] Strip Leading\n[6] Strip Trailing\n[7] Strip All\n[8] URL Quote\n[x] Exit")

formatType = inputString.result
if formatType == "x":
    droid.dialogCreateAlert("Result","Closing as per your choice")
    droid.dialogShow()
else:
    rawInput = droid.dialogGetInput("Input","Enter the string to convert")
    userInput = rawInput.result

if formatType == "1":
    outString =  titleCase(userInput)
elif formatType == "2":
    outString = userInput.lower()
elif formatType == "3":
    outString = userInput.upper()
elif formatType == "4":
    outString = userInput.capitalize()
elif formatType == "5":
    outString = userInput.lstrip()
elif formatType == "7":
    outString = userInput.strip()
elif formatType == "8":
    outString = urllib.quote(userInput)

droid.setClipboard(outString)
droid.dialogCreateAlert("Result",outString + "\n This string is also copied to the clipboard")
droid.dialogShow()