"""
main.py: Entry point for the Flask web application.
Author: gh-srinivas

This app provides a simple homepage and a '/predict' endpoint for demo business logic.
Bootstrap is used for basic styling.
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the homepage with Bootstrap styling.
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Demo endpoint to process input and return a prediction.
    """
    data = request.get_json()
    value = data.get('value', 0)
    result = int(value) * 2  # Simple demo logic
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
