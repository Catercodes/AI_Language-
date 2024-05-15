
from google.cloud import translate_v2
import os

# Get the path to the JSON file from the environment variable
json_file_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Use the JSON file path in your code (e.g., when initializing the Google Cloud Translate client)
client = translate_v2.Client.from_service_account_json("/home/chris/AI_Language/key.json")

def translate_text(text, target_language):
    client = translate_v2.Client()
    result = client.translate(text, target_language=target_language)
    return result['translatedText']
if __name__== '__main__':
 

    text_to_translate = input("Enter the text to translate: ")
    #source_language = detect_language(text_to_translate)
    source_language = "en"  # English
    # Ask user for preferred target language
    target_language = input("Enter the target language (E.g ig for Igbo, ha for hausa, yo for Yoruba: ")

    #Translate to the specified target language
    translated_text = translate_text(text_to_translate, target_language)
    print(f"Translation in {target_language.capitalize()}: {translated_text}")