import pandas as pd
from streamlit_autorefresh import st_autorefresh

from utils.voice import listen, speak
from analysis.answer import( answer_question, 
                            chart_command
                            )


# Load dataset
df = pd.read_csv("data/retail sales dataset.csv")
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

# Remove accidental spaces from column names
df.columns = df.columns.str.strip()


print("===================================")
print("     JARVIS DATA ASSISTANT")
print("===================================")



speak("Hey, I am JARVIS. Your data analytics assistant.")



while True:

    try:

        # Listen for Jarvis + question
        command = listen()

        if not command:
            continue

        print()
        print("YOU:", command)

        # Stop commands
        if (
            "stop" in command
            or "exit" in command
            or "goodbye" in command
        ):
            speak("Goodbye. Have a great day.")
            break

        chart = chart_command(command)

        if chart:

            if chart == "distribution":

                with open("chart_command.txt", "w") as file:
                    file.write("distribution")

                speak("Opening sales distribution chart.")

            elif chart == "region":

                with open("chart_command.txt", "w") as file:
                    file.write("region")

                speak("Opening sales by region chart.")

            elif chart == "month":

                with open("chart_command.txt", "w") as file:
                    file.write("month")

                speak("Opening sales by month chart.")

            elif chart == "all":

                with open("chart_command.txt", "w") as file:
                    file.write("all")

                speak("Opening all sales charts.")

            continue

        # Send question to answer engine
        answer = answer_question(df, command)

        print("JARVIS:", answer)

        # Speak answer
        speak(answer)

    except KeyboardInterrupt:

        print("\nJARVIS stopped.")
        break

    except Exception as e:

        print("ERROR:", e)
        speak("Sorry, something went wrong.")