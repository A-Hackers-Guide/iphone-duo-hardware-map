# `_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_TtP18SpeakerRecognition29CSVTUIKeywordDetectorProtocol_`
- 13 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
CoreSpeechUtils.SecureKeywordAnalyzerNDAPI ? keywordAnalyzer;
CoreSpeechUtils.SecurePhraseDetector ? phraseDetector;
_$sSf keywordThreshold;
_$sSo21CSAudioCircularBufferC audioBuffer;
_$sSu extraSamplesAtStart;
_$sSu analyzerTrailingSamples;
Swift.Bool supportsMph;
Swift.Bool isFirstPassTriggered;
CoreSpeechUtils.SecureKeywordAnalyzerNDAPIResult ? firstPassResult;
_$sSu totalSamples;
_$sSu startSampleCount;
_$sSo22CSPlainAudioFileWriterCSg audioFileWriter;
_$sSo22CSPlainAudioFileWriterCSg audioFileWriterSecondPass;
```

## Instance methods

```
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper init];
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper reset];
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper initWithAsset:];
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper initWithSecureAsset:supportMph:];
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper analyzeWithBuffer:];
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper initWithAsset:supportMph:];
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper initWithSecureAsset:];
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper isRunningTwoPass];
-[_TtC18SpeakerRecognition34CSVTUITwoPassKeywordDetectorHelper triggeredUtteranceWithVoiceTriggerEventInfo:];
```
