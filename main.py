import pyttsx3  # Import the pyttsx3 library

def speak(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init('sapi5')  # Explicitly specify sapi5 for Windows

    # Set properties (optional)
    engine.setProperty('rate', 130)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Set voice (female or male)
    # voices = engine.getProperty('voices')  # Get available voices
    # engine.setProperty('voice', voices[1].id)  # Female voice (voices[0] is typically male)

    # Speak the text
    engine.say(text)

    # Wait until the speaking is finished
    engine.runAndWait()



while True:
     # Take user input
     text = input("Enter text for Robo Speaker (type 'exit' to quit): ")

     # If the user types 'exit', break the loop
     if text.lower() == 'exit':
        print("Exiting Robo Speaker.")
        break

     # Call the speak function to convert text to speech
     speak(text)
