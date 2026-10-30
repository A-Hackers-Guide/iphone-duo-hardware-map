# `VTSyncKeywordAnalyzerQuasar`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"_EARSyncSpeechRecognizer" _syncRecognizer;
B _requireReset;
B _preventDuplicatedReset;
@"NSDictionary" _phToPhIdMap;
Q _numPhrases;
```

## Class methods

```
+[VTSyncKeywordAnalyzerQuasar _phToPhIdMapFromTriggerTokensArray:];
+[VTSyncKeywordAnalyzerQuasar dumpEARSpeechRecognitionResults:];
```

## Instance methods

```
-[VTSyncKeywordAnalyzerQuasar reset];
-[VTSyncKeywordAnalyzerQuasar _getAnalyzedResults:];
-[VTSyncKeywordAnalyzerQuasar flushAudio];
-[VTSyncKeywordAnalyzerQuasar getResultsFromFlushedAudio];
-[VTSyncKeywordAnalyzerQuasar initWithConfigPath:triggerTokensArray:preventDuplicatedReset:memoryLock:];
-[VTSyncKeywordAnalyzerQuasar getAnalyzedResultsFromFloatAudioBuffer:numSamples:];
-[VTSyncKeywordAnalyzerQuasar getAnalyzedResultsFromInt16AudioBuffer:numSamples:];
```
