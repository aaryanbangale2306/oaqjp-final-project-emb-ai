# Test Results Report

## Unit Tests (`test_emotion_detection.py`)

All unit tests run using Python's `unittest` framework:

```
test_blank_input (test_emotion_detection.TestEmotionDetection.test_blank_input)
Test that blank input returns None for all emotions. ... ok
test_emotion_detector_anger (test_emotion_detection.TestEmotionDetection.test_emotion_detector_anger)
Test anger statement: 'I am really mad about this'. ... ok
test_emotion_detector_disgust (test_emotion_detection.TestEmotionDetection.test_emotion_detector_disgust)
Test disgust statement: 'I feel disgusted just hearing about this'. ... ok
test_emotion_detector_fear (test_emotion_detection.TestEmotionDetection.test_emotion_detector_fear)
Test fear statement: 'I am really afraid that this will happen'. ... ok
test_emotion_detector_joy (test_emotion_detection.TestEmotionDetection.test_emotion_detector_joy)
Test joy statement: 'I am glad this happened'. ... ok
test_emotion_detector_sadness (test_emotion_detection.TestEmotionDetection.test_emotion_detector_sadness)
Test sadness statement: 'I am so sad about this'. ... ok

----------------------------------------------------------------------
Ran 6 tests in 5.127s

OK
```

## Summary of Verified Statements

| # | Statement | Expected Dominant Emotion | Actual Dominant Emotion | Status |
|---|---|---|---|---|
| 1 | "I am glad this happened" | joy | joy | ✅ PASS |
| 2 | "I am really mad about this" | anger | anger | ✅ PASS |
| 3 | "I feel disgusted just hearing about this" | disgust | disgust | ✅ PASS |
| 4 | "I am so sad about this" | sadness | sadness | ✅ PASS |
| 5 | "I am really afraid that this will happen" | fear | fear | ✅ PASS |
| 6 | "" (empty string) | None | None | ✅ PASS |
