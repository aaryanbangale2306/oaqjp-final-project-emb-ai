# Emotion Detection Application

A Flask-based web application that uses IBM Watson NLP to detect emotions in text.

## Features

- Detects five emotions: anger, disgust, fear, joy, and sadness
- Identifies the dominant emotion from input text
- RESTful API for emotion detection
- Interactive web interface
- Proper error handling for invalid/blank input (400 status code)

## Project Structure

```
emotion-detector/
├── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py      # Core emotion detection module
│   └── test_emotion_detection.py # Unit tests
├── templates/
│   └── index.html               # Web interface
├── server.py                     # Flask application
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aaryanbangale2306/emotion-detector.git
cd emotion-detector
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python server.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Enter text in the text area and click "Analyze Emotions" to detect emotions.

## API Usage

### POST /emotion_detection

Send a POST request with JSON body:
```json
{
    "textToAnalyze": "Your text here"
}
```

Response on success (200):
```json
{
    "anger": 0.0,
    "disgust": 0.0,
    "fear": 0.0,
    "joy": 0.85,
    "sadness": 0.0,
    "dominant_emotion": "joy"
}
```

Response on error (400):
```json
{
    "error": "Invalid text! Please enter some text."
}
```

## Running Tests

Run the unit tests:
```bash
python -m pytest EmotionDetection/test_emotion_detection.py -v
```

Or with unittest:
```bash
python -m unittest discover
```

## Code Quality

Run Pylint to check code quality:
```bash
pylint EmotionDetection/*.py server.py
```

## Emotions Detected

- **Anger**: Detects expressions of anger or hostility
- **Disgust**: Detects expressions of disgust or distaste
- **Fear**: Detects expressions of fear or anxiety
- **Joy**: Detects expressions of happiness or contentment
- **Sadness**: Detects expressions of sadness or sorrow

## Error Handling

- Returns **400 status code** for empty or blank input
- Returns **400 status code** for None input
- Proper error messages displayed to the user

## Author

Aaryan Bangale

## License

IBM Skills Network Final Project
