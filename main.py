import pyttsx3
from gtts import gTTS

tts = gTTS('this is a sample test to see how the tts works. my name is govind. i am currently using espeak synthesizer')
tts.save('hello.mp3')

# engine = pyttsx3.init()
# engine.say("this is a sample test to see how the tts works. my name is govind. i am currently using espeak synthesizer")
# engine.runAndWait()
 