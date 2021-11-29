from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    word = language_translator.translate(
    text=textToTranslate, model_id='en-fr').get_result()
    french_text= word['translations'][0]['translation']
    return french_text
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    word = language_translator.translate(
    text=textToTranslate, model_id='fr-en').get_result()
    english_text= word['translations'][0]['translation']
    return english_text
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    if __name__ == '__main__':
    app.run()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
