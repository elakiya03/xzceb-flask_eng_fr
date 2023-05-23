from machinetranslation import translator
# from translator import englishtofrench,frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchText = translator.englishtofrench(textToTranslate)  # Assuming translate_text function takes source and target languages as parameters
    return frenchText

@app.route("/frenchToEnglish")
def frenchoEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.frenchToEnglish(textToTranslate)
    return englishText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090)
