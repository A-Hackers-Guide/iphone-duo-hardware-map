# `VTTranscriber`

- Image: [`/System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger`](../userland/System__Library__PrivateFrameworks__VoiceTrigger.framework__VoiceTrigger.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_EARSpeechRecognitionResultStream`
- 9 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _previousUtteranceTokens;
d _triggerConfidence;
@"NSArray" _triggerTokenList;
@? _callback;
@"_EARSpeechRecognizer" _recognizer;
@"_EARSpeechRecognitionAudioBuffer" _recognizerBuffer;
B _isTriggerFollowedByWords;
B _useKeywordSpotting;
```

## Properties

```
@property (Td,R,V_triggerConfidence) triggerConfidence;
@property (TB,R,V_isTriggerFollowedByWords) isTriggerFollowedByWords;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[VTTranscriber reset];
-[VTTranscriber recognizedTokens];
-[VTTranscriber endAudio];
-[VTTranscriber _getConfidence:];
-[VTTranscriber speechRecognizer:didFinishRecognitionWithError:];
-[VTTranscriber speechRecognizer:didRecognizeFinalResults:];
-[VTTranscriber speechRecognizer:didRecognizePartialResult:];
-[VTTranscriber triggerConfidence];
-[VTTranscriber initWithConfiguration:triggerTokens:useKeywordSpotting:];
-[VTTranscriber isTriggerFollowedByWords];
-[VTTranscriber recognizeWavData:length:];
-[VTTranscriber runRecognitionWithCallback:];
```
