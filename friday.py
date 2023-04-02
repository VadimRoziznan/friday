import speech_recognition
import pyttsx3

tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voices', 'ru')

while True:

    print('Говори')

    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5




    def greeting():
        """Greeting function"""
        return 'Привет)'


    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    if query == 'привет':
        print(greeting())

        tts.say(greeting())
        tts.runAndWait()
    elif query == 'как тебя зовут':
        print('Меня зовут пятница')

        tts.say('Меня зовут пятница')
        tts.runAndWait()
    elif query == 'пятница':
        print('Слушаю')

        tts.say('Слушаю')
        tts.runAndWait()
    else:
        print('Я вас не понимаю')

        tts.say('Я вас не понимаю')
        tts.runAndWait()
