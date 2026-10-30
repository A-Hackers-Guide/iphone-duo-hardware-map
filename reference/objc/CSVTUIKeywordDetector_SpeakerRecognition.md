# `CSVTUIKeywordDetector`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"SSRTriggerPhraseDetectorNDAPI" _keywordAnalyzer;
f _lastKeywordScore;
f _keywordThreshold;
@"CSAudioCircularBuffer" _audioBuffer;
Q _extraSamplesAtStart;
```

## Instance methods

```
-[CSVTUIKeywordDetector reset];
-[CSVTUIKeywordDetector initWithAsset:];
-[CSVTUIKeywordDetector _sampleLengthFrom:To:];
-[CSVTUIKeywordDetector analyzeWithBuffer:];
-[CSVTUIKeywordDetector isRunningTwoPass];
-[CSVTUIKeywordDetector triggeredUtteranceWithVoiceTriggerEventInfo:];
```
