# `VTKeywordAnalyzerNDAPI`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"VTNovDetector" _novDetector;
Q _startAnalyzeSampleCount;
B _isStartSampleCountMarked;
Q _lastSampleFed;
Q _sampleFedWrapAroundOffset;
I _activePhId;
```

## Properties

```
@property (TI,N,V_activePhId) activePhId;
```

## Instance methods

```
-[VTKeywordAnalyzerNDAPI reset];
-[VTKeywordAnalyzerNDAPI analyzeWavFloatData:numSamples:];
-[VTKeywordAnalyzerNDAPI _keywordAnalyzerNDAPIResultFromNovDetectorResult:phId:];
-[VTKeywordAnalyzerNDAPI _resetStartAnalyzeTime];
-[VTKeywordAnalyzerNDAPI _setStartAnalyzeTime:];
-[VTKeywordAnalyzerNDAPI activePhId];
-[VTKeywordAnalyzerNDAPI analyzeWavData:numSamples:];
-[VTKeywordAnalyzerNDAPI getAnalyzedResults];
-[VTKeywordAnalyzerNDAPI getBestAnalyzedResults];
-[VTKeywordAnalyzerNDAPI getLoggingThreshold];
-[VTKeywordAnalyzerNDAPI getRejectLoggingThreshold];
-[VTKeywordAnalyzerNDAPI getSuperVectorWithEndPoint:];
-[VTKeywordAnalyzerNDAPI getThreshold];
-[VTKeywordAnalyzerNDAPI initWithConfigPath:resourcePath:];
-[VTKeywordAnalyzerNDAPI resetBest];
-[VTKeywordAnalyzerNDAPI setActivePhId:];
-[VTKeywordAnalyzerNDAPI _processAudioFloatBuffer:numSamples:];
-[VTKeywordAnalyzerNDAPI _processAudioInt16Buffer:numSamples:];
-[VTKeywordAnalyzerNDAPI getAnalyzedResultsFromFloatAudioBuffer:numSamples:];
-[VTKeywordAnalyzerNDAPI getAnalyzedResultsFromInt16AudioBuffer:numSamples:];
-[VTKeywordAnalyzerNDAPI getBestAnalyzedResultsFromFloatAudioBuffer:numSamples:];
-[VTKeywordAnalyzerNDAPI getBestAnalyzedResultsFromInt16AudioBuffer:numSamples:];
```
