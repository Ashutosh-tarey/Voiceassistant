import speech_recognition as sr
import screen_brightness_control as sbc
import time
import datetime
from time import ctime
from gtts import gTTS
import random
import playsound
import os
import webbrowser
import wikipedia
import cv2
from better_profanity import profanity

import tkinter
from tkinter import *
from PIL import Image,ImageTk




r=sr.Recognizer()  #creating instance of Recognizer Class.

def record(x=False):    #optional parameter
   
                                      #for taking input 
   with sr.Microphone() as source:
                            #open the microphone and start recording
      if x:   #if x is true,   
         stacy_speak(x)   #then speak out the required message stored in the corresponding variables for the audio input.
      r.adjust_for_ambient_noise(source)
      audio=r.listen(source)  #extract audio data from the file.
      try:
          voice_data=r.recognize_google(audio)  #recogize speech using google speech API
      except sr.UnknownValueError: 
          stacy_speak('Sorry, i did not get that')
      except sr.RequestError:
          stacy_speak('Sorry,the request could not be processed')
      return voice_data

def stacy_speak(x):                         #for converting text to audio and play the audio
   tts=gTTS(text=x,lang='en',tld='com')
   r=random.randint(1,10000)    #to randomly generate file numbers.
   audio_file='audio-'+str(r)+'.mp3'
   tts.save(audio_file)  
   playsound.playsound(audio_file)
   print(x)
   os.remove(audio_file)    #Deletes the audio file path.



def feedback(voice_data):     #for giving response on the basis of the input
  
   if 'what is your name' in voice_data:
      stacy_speak('My name is Stacy')
   if 'what is the time' in voice_data:
      stacy_speak(ctime())
   if 'find the location' in voice_data:
      loc=record('What is the location ?')
      url='https://google.nl/maps/place/'+ loc +'/&amp;'
      webbrowser.get().open(url)
      stacy_speak('Here is the location of :'+loc)
   if 'search' in voice_data:
       sea=record('What do you want to Search ?')
       url = "https://google.com/search?q=" + sea
       webbrowser.get().open(url)
       stacy_speak('Here are the Search Results For:'+sea)
   if 'open my mail' in voice_data:
      url="https://mail.google.com/mail/u/0/#inbox"
      webbrowser.get().open(url)
      stacy_speak('Your gmail has been opened')
   if 'convert the unit' in voice_data:
      val = int(input('Enter the value: '))
      x=str(input('Which unit do you want it converted from:  '))
      y=str(input('Which unit do you want it converted to: '))
      if x== "centimetres" and y== "metres":
         ans = str((val) / 100)
         stacy_speak("The Answer is :"+ans+"metres")
      elif x == "metres" and y == "centimetres":
         ans = str(val * 10)
         stacy_speak("The Answer is :"+ans+"centimetres")
      else:
         stacy_speak('The unit was not recognizable')
   if 'define' in voice_data:
      wor=record('Tell me the Word')
      stacy_speak(wikipedia.summary(wor,sentences=3))
   if 'brightness' in voice_data:
      x=str(input("Tell me the Adjustment Setting:"))
      if(x=='low'):
            sbc.set_brightness(50)
            stacy_speak('The Brightness Has Been Decreased.')
      if(x=='medium'):
            sbc.set_brightness(50)
      if(x=='high'):
            sbc.set_brightness(75)
            stacy_speak('The Brightness Has Been Increased.')      
   if 'check my vocabulary' in voice_data:
      profanity.load_censor_words()        
      res=record('Speak up a Sentence')
      output=profanity.censor(res)
      stacy_speak(''+output)
   if 'open camera' in voice_data:
      #creating an object to capture the video
      vid= cv2.VideoCapture(0)
      while(True): #to run the window infinitely.
         ret,frame = vid.read()  
         cv2.imshow('frame', frame)  #captures the video frame by frame.
         if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
         # After the loop release the cap object,releases the memory 
      vid.release() 
      # Destroy all the windows opened
      cv2.destroyAllWindows() 
   if 'thank you' in voice_data:
      stacy_speak('You are Welcome.')
      exit()         
   if 'exit' in voice_data:
      exit()   

time.sleep(1)      #suspends the execution of the current thread.

def execute():
   stacy_speak('How can i Help You?')
   while 1:                                 #For Taking the Input Infinitely.
      voice_data=record()
      feedback(voice_data)
   
x=Tk()
x.title('Voice Assistant')
x.geometry('600x600')
x.resizable(0,0)

img=Image.open("microphone1.png")
y=img.resize((300,300))
z=ImageTk.PhotoImage(y)
label1=Label(x,image=z,background="#ffffff")
label2=Button(x,text="Stacy's Charm",font=("Comic Sans MS",22,"bold","italic"),relief=FLAT)
label3=Label(x,text="Helping You Out,Makes Me Happy!",font=("Comic Sans MS",16,"bold","italic"),relief=GROOVE,width=60,bg="grey")
btn1=Button(x,text="Speak Up!",font=("Comic Sans MS",16,"bold"),command=execute,relief=RAISED,pady=10)
btn2=Button(x,text="Exit",font=("Comic Sans MS",20,"bold"),command=exit)
label1.pack()
label2.pack()
btn1.pack()
btn2.pack()
label3.pack(pady=25)
x.mainloop()
      
  
  
   
   
   
   
   
   
   



