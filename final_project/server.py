from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_ToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    final_result = translator.englishToFrench(textToTranslate)
    return final_result

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    final_result = translator.frenchToEnglish(textToTranslate)
    # Write your code here
    return final_result

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
