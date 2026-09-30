"""
Flask server for the Emotion Detection application.
Provides REST API and web interface for emotion analysis.
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def index():
    """Render the main HTML interface"""
    return render_template("index.html")


@app.route("/emotion_detection", methods=["POST"])
def detect_emotion():
    """
    API endpoint for emotion detection.
    
    Returns:
        JSON response with emotion scores and dominant emotion,
        or 400 error for invalid/blank input
    """
    # Get text from request
    request_json = request.get_json()
    
    if not request_json or "textToAnalyze" not in request_json:
        return jsonify({"error": "No text provided"}), 400
    
    text = request_json.get("textToAnalyze", "").strip()
    
    # Check if text is empty or blank
    if not text:
        return jsonify({"error": "Invalid text! Please enter some text."}), 400
    
    # Call emotion detection function
    result = emotion_detector(text)
    
    # If result is None (empty/blank input), return 400 error
    if result is None:
        return jsonify({"error": "Invalid text! Please enter some text."}), 400
    
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
