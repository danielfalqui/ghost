#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core
from nlu.classifier import classify

engine = pyttsx3.init()

#sintese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#reconhecimento de fala

model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

#loop do reconhecimento de fala
while True:
    data = stream.read(2048)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            # Reconhecer entidade do texto.
            entity = classify(text)

            if entity == 'time|getTime':
                speak(core.SystemInfo.get_time())

            print('Text: {}  Entity: {}'.format(text, entity))

