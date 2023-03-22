#!/usr/bin/env python

from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)
template = "index.html"

api_key = os.environ["OPENAI_API_KEY"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the user input and model selection
        user_input = request.form["user_input"]
        model = request.form["model"]

        # Call OpenAI API and handle the response
        response_data = call_openai_api(user_input, model)

        # Render the response data
        return render_template(template, response_data=response_data)
    else:
        return render_template(template)


def call_openai_api(user_input, model):
    # Set up the necessary headers and data for the OpenAI API
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "messages": [{
            "role": "user",
            "content": user_input,
        }],
        "max_tokens": 25,  # Adjust the number of tokens as needed
        "temperature": 0
    }

    # Make the API request
    response = requests.post("https://api.openai.com/v1/chat/completions",
                             headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]
    else:
        return f"Error: Unable to process your request. Received error {response.status_code}"


if __name__ == "__main__":
    app.run(debug=True)
