import speech_recognition as speech

recognizer = speech.Recognizer()

def get_voice_command(prompt="Say a command..."):
    with speech.Microphone() as source:
        print(prompt)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print("Did you say:", text)
            return text.lower()
        except Exception as err:
            print("Error:", str(err))
            return ""
