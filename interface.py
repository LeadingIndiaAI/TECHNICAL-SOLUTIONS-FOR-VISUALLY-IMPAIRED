# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:01:00 2018

@author: arcse
"""
import sys
import yolowebcam
import imagetospeech
from playsound import playsound
import speech_recognition as sr
r = sr.Recognizer()
def choices():
  while True:
     #st1="Say 1 for live object detection,say 2 for images text to speech conversion,say 0 for exitfrom system"
     #st2="you said 1 for live object detection"
     #st3="you said 2 for images text to speech conversion"
      
     #st4="you said wrong option,please choose correct option"
     #st5="Could not understand audio,please say again"
    
     playsound('st1.mp3')
     print("say something")
     with sr.Microphone() as source:   
      r.adjust_for_ambient_noise(source, duration=1)  
      r.dynamic_energy_threshold = True              
       
      audio = r.listen(source)                      
      option=r.recognize_google(audio)
     try:
         print(option)
     except LookupError:                             
         playsound('st5.mp3')
     
     if option=="1": 
         playsound('st2.mp3')
         yolowebcam.test()
        
     elif option=="2":
         playsound('st3.mp3')
         imagetospeech.test()
          
         
     elif option=="0":
         print("Program stopped")
         sys.exit()
         
     else:
         playsound('st4.mp3')
         continue
 
if __name__ == '__main__':
    choices()