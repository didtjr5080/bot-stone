import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("안녕하세요. ")