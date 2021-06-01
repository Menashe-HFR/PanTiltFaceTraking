import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 135)
engine.say("hi, my name is elon mask")
engine.runAndWait()