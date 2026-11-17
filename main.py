import requests
import pyttsx3
from datetime import datetime

# Initialize Jarvis voice
engine = pyttsx3.init()

engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)


# Jarvis speaks
def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()


# Connect to Ollama AI
def ask_jarvis(question):

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2:1b",
        "prompt": question,
        "stream": False,
        "keep_alive": "10m",
        "options": {
            "num_predict": 60,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(url, json=data, timeout=180)
        response.raise_for_status()

        answer = response.json()["response"]
        return answer

    except requests.exceptions.RequestException:
        return "Sorry, I cannot connect to Ollama. Please check if Ollama is running."


# Main Jarvis program
def start_jarvis():

    speak("Hello! I am Jarvis. How can I help you?")

    while True:

        user_input = input("YOU: ")

        command = user_input.lower()

        if command in ["exit", "quit", "bye"]:
            speak("Goodbye! Have a nice day.")
            break

        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            speak("The current time is " + current_time)

        elif "date" in command:
            current_date = datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + current_date)

        else:
            answer = ask_jarvis(user_input)
            speak(answer)


# Run Jarvis
if __name__ == "__main__":
    start_jarvis()