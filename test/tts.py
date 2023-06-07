import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voice')
engine.setProperty('voice', voices[-2])

engine.say("Eu vou falar esse texto")
engine.runAndWait()