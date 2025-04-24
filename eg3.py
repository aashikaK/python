#install an external module and use it to perform an operation of ur interest
#we are installing pyttsx3 so do pip intall pyttsx3
#go to website pyttsx3 then copy code from usage section 

import pyttsx3
engine = pyttsx3.init()
engine.say("Aashika is the sweetest and richest person you will ever meet in your life")
engine.runAndWait()

# It speaaks whatever we tell it to do here...