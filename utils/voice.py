import speech_recognition as sr
import pyttsx3
import time
import webbrowser

# Speech recognition
r = sr.Recognizer()

# Text-to-speech
engine = pyttsx3.init("sapi5")

# Get Windows voices
voices = engine.getProperty("voices")

if voices:
    engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)


def speak(text):
    """Make JARVIS speak the given text."""

    print("JARVIS:", text)

    try:
        engine.stop()

        engine.say(str(text))
        engine.runAndWait()

        time.sleep(0.2)

    except Exception as e:
        print("SPEECH ERROR:", e)


def listen():
    """Listen for Jarvis and then listen for the question."""

    try:

        with sr.Microphone() as source:

            print("Listening.......")

            r.adjust_for_ambient_noise(source, duration=0.5)

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        word = r.recognize_google(audio).lower()

        print("I heard:", word)

        if "jarvis" in word:

            print("JARVIS DETECTED!")
            

            speak("yes,how can I help you?")
            
            with sr.Microphone() as source:

                print("Jarvis Active...")

                r.adjust_for_ambient_noise(source, duration=0.3)

                audio = r.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )

            command = r.recognize_google(audio).lower()

            print("You:", command)

            return command

        return ""

    except sr.WaitTimeoutError:

        print("No speech detected.")
        return ""

    except sr.UnknownValueError:

        print("I could not understand you.")
        return ""

    except sr.RequestError:

        print("Speech recognition service unavailable.")
        speak("Speech recognition service unavailable.")
        return ""

    except Exception as e:

        print("ERROR:", e)
        return ""

def processcommand(c):
    if "Sales Distribution chart" in c.lower():
        webbrowser.open("")
