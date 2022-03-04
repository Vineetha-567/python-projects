# text convert to audio

from gtts import gTTS
from playsound import playsound
audio= 'speech.mp3'
language= 'en'
sp=gTTS(text='plese vinny learning python and focus on your studies. then you get in a good job ', lang=language,slow=False)
sp.save(audio)
playsound(audio)
print('==audio is playing ====')