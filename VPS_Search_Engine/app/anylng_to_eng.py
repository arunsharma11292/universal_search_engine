import speech_recognition as sr
from googletrans import Translator
# def live_kannada_to_english():
#     # Initialize tools
#     recognizer = sr.Recognizer()
#     translator = Translator()

#     with sr.Microphone() as source:
#         print("\nAdjusting for background noise... Please wait.")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
        
#         print("Now speak in KANNADA...")
        
#         try:
#             audio = recognizer.listen(source, timeout=5)
            
#             print("Processing your voice...")
#             kannada_text = recognizer.recognize_google(audio, language='kn-IN')
#             print(f"You said (Kannada): {kannada_text}")

#             translation = translator.translate(kannada_text, src='kn', dest='en')
            
#             return translation.text

#         except sr.UnknownValueError:
#             print("Sorry, I could not understand the audio.")
#         except sr.RequestError:
#             print("Could not request results; check your internet connection.")
#         except Exception as e:
#             print(f"An error occurred: {e}")

# import speech_recognition as sr
# from googletrans import Translator

def live_speech_to_english():
    recognizer = sr.Recognizer()
    translator = Translator()

    with sr.Microphone() as source:
        print("\nAdjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Now speak in ANY language...")# it will support  languages (like Hindi,Engish ,kannada)
        
        try:
            audio = recognizer.listen(source, timeout=10) # You can increse the time out
            
            print("Processing your voice...")
            spoken_text = recognizer.recognize_google(audio)
            print(f"You said: {spoken_text}")
            translation = translator.translate(spoken_text, src='auto', dest='en') #Auto translate from any language to english langauge
            print(f"Detected Language: {translation.src}")
            print(f"English Output: {translation.text}")

            return translation.text

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
        except Exception as e:
            print(f"An error occurred: {e}")