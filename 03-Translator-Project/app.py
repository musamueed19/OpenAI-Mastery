from flask import Flask, render_template, request
from openai_service import OpenAIService

import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# get env variable using og.getenv
openai_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def index():
    # render_template() function from flask library is
    # - to render the template (path as specified in the template_folder parameter of the Flask app) and return it as a response to the client.
    
    openai_client = OpenAIService(openai_key)
    
    translated_text = ""
    if request.method == "POST":
        # Get the text to be translated and the target language from the form
        original_text = request.form["original_text"]
        target_language = request.form["target_language"]
        
        translated_text = openai_client.translate_text(original_text=original_text, target_language=target_language)
        
        
    return render_template("index.html", translated_text=translated_text)

# python app.py (Start the Flask application)
if __name__ == "__main__":
    app.run(debug=True)