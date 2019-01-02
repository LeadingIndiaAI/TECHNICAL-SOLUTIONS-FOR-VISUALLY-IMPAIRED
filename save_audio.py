import sys
import os
import yolovoice
#from goto import goto,label
from gtts import gTTS
from playsound import playsound
import random,string
import speech_recognition as sr
r = sr.Recognizer()
def choices():
     str1="Say 1 for live object detection,say 2 for images text to speech conversion,say 0 for exitfrom system"
     str2="you said 1 for live object detection"
     str3="you said 2 for images text to speech conversion"
      
     str4="you said wrong option,please choose correct option"
     str5="Could not understand audio,please say again"
     tts='tts'
      
     name1= "st1"
     name2= "st2"
     name3= "st3"
     name4= "st4"
     name5= "st5"
     print("name1=",name1)
     print("name2=",name2)
     print("name3=",name3)
     print("name4=",name4)
     print("name5=",name5)
     
     
     tts=gTTS(str1)
     file1 = str(name1  + ".mp3")
     tts.save(file1)
     
     tts=gTTS(str2)
     file2 = str(name2  + ".mp3")
     tts.save(file2)
     
     tts=gTTS(str3)
     file3 = str(name3  + ".mp3")
     tts.save(file3)
     
     tts=gTTS(str4)
     file4 = str(name4  + ".mp3")
     tts.save(file4)
     
     tts=gTTS(str5)
     file5 = str(name5  + ".mp3")
     tts.save(file5)
      
     playsound('st1.mp3')
     playsound('st2.mp3')
     playsound('st3.mp3')
     playsound('st4.mp3')
     playsound('st4.mp3')


 
if __name__ == '__main__':
#while True:
    choices()