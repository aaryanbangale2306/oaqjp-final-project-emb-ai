"""
Unit tests for the emotion detection module.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion_detector function"""

    def test_emotion_detector_joy(self):
        """Test emotion detection for joyful text"""
        result = emotion_detector("I love this so much!")
        self.assertIsNotNone(result)
        self.assertIn("joy", result)
        self.assertGreater(result["joy"], 0.5)

    def test_emotion_detector_anger(self):
        """Test emotion detection for angry text"""
        result = emotion_detector("I hate it!")
        self.assertIsNotNone(result)
        self.assertIn("anger", result)

    def test_emotion_detector_sad(self):
        """Test emotion detection for sad text"""
        result = emotion_detector("I am very sad.")
        self.assertIsNotNone(result)
        self.assertIn("sadness", result)

    def test_emotion_detector_fear(self):
        """Test emotion detection for fearful text"""
        result = emotion_detector("I am really afraid.")
        self.assertIsNotNone(result)
        self.assertIn("fear", result)

    def test_emotion_detector_disgust(self):
        """Test emotion detection for disgusted text"""
        result = emotion_detector("I am disgusted by this.")
        self.assertIsNotNone(result)
        self.assertIn("disgust", result)

    def test_emotion_detector_empty_string(self):
        """Test that empty string returns None"""
        result = emotion_detector("")
        self.assertIsNone(result)

    def test_emotion_detector_blank_string(self):
        """Test that blank/whitespace string returns None"""
        result = emotion_detector("   ")
        self.assertIsNone(result)

    def test_emotion_detector_null_string(self):
        """Test that None input returns None"""
        result = emotion_detector(None)
        self.assertIsNone(result)

    def test_emotion_detector_dominant_emotion(self):
        """Test that dominant emotion is correctly identified"""
        result = emotion_detector("I am so happy and joyful!")
        self.assertIsNotNone(result)
        self.assertIn("dominant_emotion", result)
        self.assertEqual(result["dominant_emotion"], "joy")


if __name__ == "__main__":
    unittest.main()
