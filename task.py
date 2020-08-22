import pyttsx3
import os
import pyfiglet

result = pyfiglet.figlet_format("<>==Sweta==<>")
print(result)

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.8)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
engine.say("welcome learners, I'm Swetaa, tell me how can i help you")
engine.setProperty('voice', voices[0].id)
engine.say("can u run with my requirement: ")
engine.setProperty('voice', voices[1].id) 
engine.runAndWait()

while True:
       print()
       
      
       print("can u run with my requirement: ", end = '')
       a = input()
       #print(a)

       if(("run" in a) or ("launch" in a) or ("open" in a) or ("execute" in a)) and (("chrome" in a) or ("browser" in a) or ("google chrome" in a) or ("google" in a) or ("chrome browser" in a)):
        pyttsx3.speak("please wait your google chrome is opening")
        os.system("chrome")

          

       elif(("run" in a) or ("open" in a) or ("show" in a) or ("today") or ("show me" in a) or ("launch" in a)) and ("date" in a):
        pyttsx3.speak("today is")
        os.system("date")

       elif(("run" in a) or ("open" in a) or ("show" in a) or ("show me" in a) or ("launch" in a)) and (("time" in a) or ("clock" in a)):
        pyttsx3.speak("time is")
        os.system("time")
            
        
       elif(("run" in a) or ("play" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("media" in a) or ("media player" in a) or ("musics" in a) or ("wmplayer" in a) or ("music player" in a)):
        pyttsx3.speak("please wait your windows media player is opening")
        os.system("wmplayer")
       

       elif(("run" in a) or ("play" in a) or ("launch" in a) or ("execute" in a) or ("open" in a)) and (("vlc player" in a) or ("vlc" in a)):
        pyttsx3.speak("please wait your vlc player is opening")
        os.system("vlc")


       elif(("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("notepad" in a) or ("text editor" in a)):
        pyttsx3.speak("please wait your notepad is opening")
        os.system("notepad")

       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("virtual box" in a) or ("vb" in a) or ("vbox" in a) or ("oracle box" in a) or ("oracle" in a)):
        pyttsx3.speak("please wait your oracle virtual box is opening")
        os.system("virtualbox")

       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("vs code" in a) or ("code" in a) or ("visual studio code" in a) or ("vs" in a)):
        pyttsx3.speak("please wait your visual studio code is opening")
        os.system("code")

       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("ie" in a) or ("i explore" in a) or ("explorer" in a) or ("internet explorer" in a)):
        pyttsx3.speak("please wait your internet explorer is opening")
        os.system("iexplore")

    
       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("wp" in a) or ("whatsapp" in a) or ("wapp" in a)):
        pyttsx3.speak("please wait your whatsapp is opening")
        os.system("whatsapp")
       

       elif(("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("camera" in a) or ("pc camera" in a)):
        pyttsx3.speak("please wait your camera is opening")
        os.system("Start microsoft.windows.camera:")


       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("settings" in a) or ("setting" in a)):
        pyttsx3.speak("please wait your settings is opening")
        os.system("Start ms-settings:")


       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("bluetooth" in a) or ("blue" in a)):
        pyttsx3.speak("please wait your bluetooth is opening")
        os.system("Start ms-settings:bluetooth")


       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and ("display" in a):
        pyttsx3.speak("please wait your display is opening")
        os.system("Start ms-settings:display")


       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("ij" in a) or ("idea" in a) or ("intellij id" in a) or ("intellij idea" in a)):
        pyttsx3.speak("please wait your intellij idea is opening")
        os.system("idea64")

 
       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("photoshop" in a) or ("photo editor" in a) or ("pic editor" in a) or ("adobe" in a) or ("ps" in a)):
        pyttsx3.speak("please wait your photoshop is opening")
        os.system("photoshop") 


       elif(("thank you" in a) or ("thanku" in a) or ("thank u" in a) or ("thanks" in a)):
        print("always welcome sir")
        pyttsx3.speak("always welcome sir")


       elif(("run" in a) or ("open" in a) or ("execute" in a) or ("launch" in a)) and (("firefox" in a) or ("ff" in a) or ("firef" in a) or ("ffox"in a) or ("fox" in a)):
        pyttsx3.speak("please wait your firefox is opening")
        os.system("firefox")
       

       elif(("exit" in a) or ("stop" in a) or ("quit" in a) or ("close" in a)):
        break  

       else: 
        pyttsx3.speak("sorry not available")

       


