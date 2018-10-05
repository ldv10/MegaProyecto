#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:19:50 2018

@author: leonel
"""

import speech_recognition as sr

r = sr.Recognizer()

google = sr.AudioFile('prueba.wav')

with google as source:
    audio = r.record(google)
    
    
text = r.recognize_google(audio,language = "es-GT")

print(text)
    
