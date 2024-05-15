from flask import Flask, render_template, request
from translate import translate_text
import requests

app = Flask(__name__,static_folder='static')

# Replace 'YOUR_TRANSLATION_API_KEY' with your actual API key
API_KEY = 'YOUR_TRANSLATION_API_KEY'
API_URL = 'https://translation.googleapis.com/language/translate/v2'

#def translate_text(text):
#    params = {
#        'key': API_KEY,
#        'source': 'en',
#        'target': 'yo',  # Yoruba language code
#        'q': text
#    }
#   response = requests.post(API_URL, json=params)
#    data = response.json()
#    translated_text = data['data']['translations'][0]['translatedText']
#    return translated_text

@app.route('/translator')
def index():
    return render_template('index.html')

@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/translate', methods=['POST'])
def translate():
    # TODO get the text to be translated:
    text = request.form['text_to_translate']
    # text = request.form['text']
    # TODO get the lang to translate it in
    lang = request.form['target_language']
    # lang = request.form['lang'] // example 'ib'
    # TODO pass them into the translate function
    translated_text  = translate_text(text, lang)
    # translated_text = translate_text(text, lang)
    # TODO render the page again with the translated text
    #print()
    return render_template('index.html', text= text, translated_text = translated_text)
    # return render_template(index.html, text=text, translated_text=translated_text)
    # If you will be using the result page then it should be able to show both texts (text itself and the translated version)
    # return render_template('result.html', translated_text=translated_text)
    text_to_translate = request.form['text']
    translated_text = translate_text(text_to_translate)
    return render_template('result.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)