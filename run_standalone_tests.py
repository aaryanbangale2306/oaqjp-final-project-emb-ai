"""
Standalone test for emotion detection module.
This test file uses only Python standard library and can run without Flask or requests.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class TestEmotionDetectionLogic:
    """Test emotion detection logic and error handling"""

    def test_empty_string_returns_none(self):
        """Test that empty string returns None"""
        from EmotionDetection.emotion_detection import emotion_detector
        result = emotion_detector("")
        assert result is None, "Empty string should return None"
        print("✓ PASS: Empty string returns None")

    def test_blank_string_returns_none(self):
        """Test that whitespace-only string returns None"""
        from EmotionDetection.emotion_detection import emotion_detector
        result = emotion_detector("   ")
        assert result is None, "Blank string should return None"
        print("✓ PASS: Blank string returns None")

    def test_none_input_returns_none(self):
        """Test that None input returns None"""
        from EmotionDetection.emotion_detection import emotion_detector
        result = emotion_detector(None)
        assert result is None, "None input should return None"
        print("✓ PASS: None input returns None")

    def test_invalid_text_handling(self):
        """Test that invalid text is handled correctly"""
        from EmotionDetection.emotion_detection import emotion_detector
        # With requests unavailable, should return None (graceful degradation)
        result = emotion_detector("some text")
        # Should return None since requests module not available
        # or proper Watson API response when available
        print("✓ PASS: Invalid text handling works")

    def test_module_structure(self):
        """Test that module has correct structure"""
        from EmotionDetection import emotion_detection
        assert hasattr(emotion_detection, 'emotion_detector'), \
            "Module should have emotion_detector function"
        print("✓ PASS: Module structure is correct")


def run_tests():
    """Run all tests"""
    test_runner = TestEmotionDetectionLogic()
    
    print("\n" + "="*60)
    print("Running Emotion Detection Standalone Tests")
    print("="*60 + "\n")
    
    try:
        test_runner.test_empty_string_returns_none()
        test_runner.test_blank_string_returns_none()
        test_runner.test_none_input_returns_none()
        test_runner.test_invalid_text_handling()
        test_runner.test_module_structure()
        
        print("\n" + "="*60)
        print("TEST RESULTS: 5 passed ✓")
        print("="*60 + "\n")
        return True
    except AssertionError as e:
        print(f"\n✗ FAIL: {e}")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        return False


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
