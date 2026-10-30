# `CSVTUITwoPassKeywordDetector`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CSVTUIKeywordDetector`
- 9 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"CSKeywordAnalyzerNDAPI" _keywordAnalyzer;
@"CSPhraseDetector" _phraseDetector;
f _keywordThreshold;
@"CSAudioCircularBuffer" _audioBuffer;
Q _extraSamplesAtStart;
Q _analyzerTrailingSamples;
B _isFirstPassTriggered;
@"CSKeywordAnalyzerNDAPIResult" _firstPassResult;
B _supportsMph;
```

## Instance methods

```
-[CSVTUITwoPassKeywordDetector reset];
-[CSVTUITwoPassKeywordDetector initWithAsset:];
-[CSVTUITwoPassKeywordDetector _sampleLengthFrom:To:];
-[CSVTUITwoPassKeywordDetector analyzeWithBuffer:];
-[CSVTUITwoPassKeywordDetector initWithAsset:supportMph:];
-[CSVTUITwoPassKeywordDetector internalReset];
-[CSVTUITwoPassKeywordDetector isRunningTwoPass];
-[CSVTUITwoPassKeywordDetector triggeredUtteranceWithVoiceTriggerEventInfo:];
```
