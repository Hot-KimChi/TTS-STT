## 아래는 해당 파일을 읽어서 텍스트 변환.
# import speech_recognition as sr
#
# r = sr.Recognizer()
# harvard = sr.AudioFile('voice.wav')
# with harvard as source:
#     audio = r.record(source)
# print(r.recognize_google(audio, language='ko-KR'))
# # print(r.recognize_google(audio))
#

import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio, language='ko-KR'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))