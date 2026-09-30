"""
This module interfaces with IBM Watson NLP to detect emotions in text.
Supported emotions: anger, disgust, fear, joy, sadness.
"""

try:
    import requests
except ImportError:
    requests = None


def emotion_detector(text_to_analyse):
    """
    Detects emotions in the given text using IBM Watson NLP API.
    
    Args:
        text_to_analyse: String containing the text to analyze for emotions
        
    Returns:
        Dictionary containing emotion scores and dominant emotion,
        or None if text is empty or blank
    """
    # Handle empty or blank input
    if text_to_analyse is None or text_to_analyse.strip() == "":
        return None

    # IBM Watson NLP API URL for emotion detection
    url = (
        "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/"
        "instances/a1234567-89ab-cdef-0123-456789abcdef"
    )

    headers = {"Content-Type": "application/json"}

    input_json = {
        "raw_document": {"text": text_to_analyse},
        "features": {"emotion": {}}
    }

    if requests is None:
        return None

    try:
        response = requests.post(url, json=input_json, headers=headers, timeout=10)
        if response.status_code == 400:
            return None
        response.raise_for_status()
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        return None

    # Parse response from Watson NLP
    response_json = response.json()

    if "emotion" not in response_json:
        return None

    emotions = response_json["emotion"]["document"]["emotion"]

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions.get("anger", 0),
        "disgust": emotions.get("disgust", 0),
        "fear": emotions.get("fear", 0),
        "joy": emotions.get("joy", 0),
        "sadness": emotions.get("sadness", 0),
        "dominant_emotion": dominant_emotion,
    }
