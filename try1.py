import google.generativeai as ai
import speech_recognition as sr
import pyttsx3


def speak(audio):
    engine = pyttsx3.init()  # Initialize the TTS engine
    engine.say(audio)         # Queue the text to be spoken
    engine.runAndWait()      # Wait for the speech to finish

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# API Key
API_KEY = 'AIzaSyBFilThuUNupsqf-YmQ9g_CLebVadWoabk'

#Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()
speak("hello sir , how can i help you today?")
#Start a conversation
while True:

    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            message = recognizer.recognize_google(audio)
            print('You:', message)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            continue
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            break
    if message.lower() == 'exit':
        print('Chatbot: Goodbye!')
        break
    response = chat.send_message(message)
    print('Chatbot:', response.text)
    speak(response.text)
