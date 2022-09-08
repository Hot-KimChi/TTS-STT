from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang='ko')
    tts.save('voice.mp3')

speak("안녕하십니까 황선우 어린이 축하합니다. 지금 게임하고 있습니다.")
