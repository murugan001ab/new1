import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the recognizer
recognizer = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error connecting to Google's servers.")
            return ""


def respond(text):
    if not text:
        return

    response = "I'm sorry, I don't know how to respond to that."

    if "hello" in text:
        response = "Hello, how can I assist you?"
    elif "what is your name" in text:
        response = "I am your virtual assistant."

    print("Assistant:", response)

    # Convert response to speech
    tts = gTTS(text=response, lang='en')
    tts.save("response.mp3")
    os.system("response.mp3")


if __name__ == "__main__":
    while True:
        user_input = listen()
        respond(user_input.lower())
