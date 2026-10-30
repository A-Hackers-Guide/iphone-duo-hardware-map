# `VTKeywordAnalyzerQuasar`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_EARSpeechRecognitionResultStream`
- 10 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _previousUtteranceTokens;
@"NSArray" _triggerTokenList;
@"_EARSpeechRecognizer" _recognizer;
@"_EARSpeechRecognitionAudioBuffer" _recognizerBuffer;
B _useKeywordSpotting;
@"NSDictionary" _ctcKwdToPhIdMap;
d _triggerConfidence;
Q _activeChannel;
@"<VTKeywordAnalyzerQuasarScoreDelegate>" _delegate;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_ctcKwdToPhIdMap) ctcKwdToPhIdMap;
@property (Td,R,N,V_triggerConfidence) triggerConfidence;
@property (TQ,N,V_activeChannel) activeChannel;
@property (T@"<VTKeywordAnalyzerQuasarScoreDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTKeywordAnalyzerQuasar dealloc];
-[VTKeywordAnalyzerQuasar reset];
-[VTKeywordAnalyzerQuasar setDelegate:];
-[VTKeywordAnalyzerQuasar delegate];
-[VTKeywordAnalyzerQuasar activeChannel];
-[VTKeywordAnalyzerQuasar setActiveChannel:];
-[VTKeywordAnalyzerQuasar endAudio];
-[VTKeywordAnalyzerQuasar _getConfidence:];
-[VTKeywordAnalyzerQuasar ctcKwdToPhIdMap];
-[VTKeywordAnalyzerQuasar _phIdToCtcScoreMap];
-[VTKeywordAnalyzerQuasar _recognizeWavData:length:];
-[VTKeywordAnalyzerQuasar initWithConfigPath:triggerTokens:useKeywordSpotting:];
-[VTKeywordAnalyzerQuasar runRecognition];
-[VTKeywordAnalyzerQuasar setCtcKwdToPhIdMap:];
-[VTKeywordAnalyzerQuasar speechRecognizer:didFinishRecognitionWithError:];
-[VTKeywordAnalyzerQuasar speechRecognizer:didRecognizeFinalResults:];
-[VTKeywordAnalyzerQuasar speechRecognizer:didRecognizePartialResult:];
-[VTKeywordAnalyzerQuasar triggerConfidence];
-[VTKeywordAnalyzerQuasar processAudioBuffer:numSamples:];
```
