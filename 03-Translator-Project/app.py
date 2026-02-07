from flask import Flask, render_template

import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# get env variable using og.getenv
openai_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET"])
def index():
    # render_template() function from flask library is
    # - to render the template (path as specified in the template_folder parameter of the Flask app) and return it as a response to the client.
    return render_template("index.html")

# python app.py (Start the Flask application)
if __name__ == "__main__":
    app.run(debug=True)