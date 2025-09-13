Set objShell = CreateObject("Wscript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.OpenTextFile("C:\Users\admin\Downloads\log.txt", 8, True)  ' Open or create log file

' Log that the script is starting
objFile.WriteLine("VBScript started at: " & Now)

' Run the Python script silently (no console window)
objShell.Run """C:\Users\admin\AppData\Local\Programs\Python\Python313\pythonw.exe"" ""C:\Users\admin\Downloads\S&P500\sp500.py""", 0, False

' Log that the Python script was triggered
objFile.WriteLine("Python script triggered at: " & Now)

' Close the log file
objFile.Close
