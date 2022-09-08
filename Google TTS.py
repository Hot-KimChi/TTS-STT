from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='ko')
    tts.save('voice.wav')

speak("안녕하십니까 황선우 어린이 축하합니다.")
