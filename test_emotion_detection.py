"""
Unit tests for the EmotionDetection package.
Verifies emotion predictions for standard test statements.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test suite for the emotion_detector function."""

    def test_emotion_detector_joy(self):
        """Test joy statement: 'I am glad this happened'."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        """Test anger statement: 'I am really mad about this'."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        """Test disgust statement: 'I feel disgusted just hearing about this'."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_sadness(self):
        """Test sadness statement: 'I am so sad about this'."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_fear(self):
        """Test fear statement: 'I am really afraid that this will happen'."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input(self):
        """Test that blank input returns None for all emotions."""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])


if __name__ == '__main__':
    unittest.main()
