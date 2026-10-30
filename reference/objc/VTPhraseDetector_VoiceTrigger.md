# `VTPhraseDetector`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _isSecondChance;
@"VTKeywordAnalyzerNDAPI" _syncKeywordAnalyzerNDAPI;
@"VTSyncKeywordAnalyzerQuasar" _syncKeywordAnalyzerQuasar;
@"NSMutableArray" _phraseDetectorInfos;
Q _nearMissDelayTimeout;
Q _nearMissCandidateDetectedSamples;
@"NSMutableArray" _phraseResult;
```

## Properties

```
@property (T@"VTKeywordAnalyzerNDAPI",&,N,V_syncKeywordAnalyzerNDAPI) syncKeywordAnalyzerNDAPI;
@property (T@"VTSyncKeywordAnalyzerQuasar",&,N,V_syncKeywordAnalyzerQuasar) syncKeywordAnalyzerQuasar;
@property (T@"NSMutableArray",&,N,V_phraseDetectorInfos) phraseDetectorInfos;
@property (TQ,N,V_nearMissDelayTimeout) nearMissDelayTimeout;
@property (TQ,N,V_nearMissCandidateDetectedSamples) nearMissCandidateDetectedSamples;
@property (TB,N,V_isSecondChance) isSecondChance;
@property (T@"NSMutableArray",&,N,V_phraseResult) phraseResult;
```

## Instance methods

```
-[VTPhraseDetector setConfig:];
-[VTPhraseDetector init];
-[VTPhraseDetector dealloc];
-[VTPhraseDetector reset];
-[VTPhraseDetector nearMissCandidateDetectedSamples];
-[VTPhraseDetector setNearMissCandidateDetectedSamples:];
-[VTPhraseDetector isSecondChance];
-[VTPhraseDetector setIsSecondChance:];
-[VTPhraseDetector _getResultWithPhId:phraseDetectorInfo:ndapiResult:quasarResult:forceMaximized:];
-[VTPhraseDetector _isSecondChanceCandidateWithScore:effectiveThreshold:secondChanceThreshold:];
-[VTPhraseDetector _phraseDetectorResultFromNDAPIResults:quasarResult:forceMaximized:];
-[VTPhraseDetector _resultCopyWithKeywordDetectorDecision:bestPhId:phraseResult:];
-[VTPhraseDetector getAnalyzedResultFromFlushedAudio];
-[VTPhraseDetector nearMissDelayTimeout];
-[VTPhraseDetector phraseDetectorInfoFromPhId:];
-[VTPhraseDetector phraseDetectorInfos];
-[VTPhraseDetector phraseResult];
-[VTPhraseDetector setNearMissDelayTimeout:];
-[VTPhraseDetector setPhraseDetectorInfos:];
-[VTPhraseDetector setPhraseResult:];
-[VTPhraseDetector setRunAsSecondChance:];
-[VTPhraseDetector setSyncKeywordAnalyzerNDAPI:];
-[VTPhraseDetector setSyncKeywordAnalyzerQuasar:];
-[VTPhraseDetector syncKeywordAnalyzerNDAPI];
-[VTPhraseDetector syncKeywordAnalyzerQuasar];
-[VTPhraseDetector getAnalyzedResultFromFloatAudioBuffer:numSamples:];
-[VTPhraseDetector getAnalyzedResultFromInt16AudioBuffer:numSamples:];
```
