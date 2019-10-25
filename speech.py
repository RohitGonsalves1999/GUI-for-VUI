import tkinter as tk
import requests
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import soundfile as sf
import wavio
import speech_recognition as sr
from tkinter import * 
from tkinter.ttk import *

HEIGHT = 100
WIDTH = 600

def speech_recognizer():
    record_audio(5)
    label['text'] = recognise_speech()

def recognise_speech(filename = 'output.wav'):
    r = sr.Recognizer()
    data = sr.AudioFile('output.wav')
    with data as source:
        audio = r.record(source)
    return (r.recognize_google(audio))


def record_audio(duration,sample_rate = 44100):
    fs = sample_rate  # Sample rate
    seconds = duration  # Duration of recording
    
    print('Baat kar na L****')
    myrecording = sd.rec(int(seconds * fs),fs,1)
    sd.wait()  # Wait until recording is finished
    print('ruk na bsdk')
    #print(myrecording.flatten())
    #print(myrecording)

    '''write('output.wav', fs, myrecording)  # Save as WAV file 
    data, fs = sf.read('output.wav')
    print(data)
    sf.write('output.flac',data,fs)'''

    wavio.write('output.wav',myrecording,fs,sampwidth=2)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='siri.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.3, anchor='n')

#entry = tk.Entry(frame, font=40)
#entry.place(relwidth=0.65, relheight=1)
photo = PhotoImage(file = "play.png")
photoimage = photo.subsample(20, 20) 

button = tk.Button(frame, text="Speak", font=10,image = photoimage, 
                    compound = LEFT, command=lambda: speech_recognizer())
button.place(relx=0.5, relheight=1, relwidth=1,anchor = 'n')

lower_frame = tk.Frame(root, bg='#80c1ff')
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.2, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()