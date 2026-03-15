"""
Server module for Emotion Detection Application.
This file deploys the emotion detector using Flask.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    This function handles emotion detection requests.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again."

    return str(response)


@app.route("/")
def index():
    """
    Render the home page of the application.
    """
    return "Emotion Detection Application"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
