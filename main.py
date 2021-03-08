import  googletrans
import  speech_recognition as sr
import gtts
import playsound


recognizer = sr.Recognizer()
input_language = 'es-MX'
output_lang = 'es'


try:
    with sr.Microphone() as  source:
        print('Speak now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice)
        print(text)
except:
    pass


translator = googletrans.Translator()
translated = translator.translate(text , dest=output_lang)
converted_audio = gtts.gTTS(translated.text , lang = output_lang )
converted_audio.save('translator.mp3')
playsound.playsound('translator.mp3')

print(translated.text)