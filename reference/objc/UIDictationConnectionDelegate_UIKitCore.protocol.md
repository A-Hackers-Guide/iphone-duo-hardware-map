# `UIDictationConnectionDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance methods

```
-[UIDictationConnectionDelegate dictationConnection:didStartRecordingWithOptions:];
-[UIDictationConnectionDelegate dictationConnectionDidCancel:];
-[UIDictationConnectionDelegate dictationConnection:didDetectLanguage:];
-[UIDictationConnectionDelegate dictationConnection:updateOptions:];
-[UIDictationConnectionDelegate dictationConnnectionDidChangeAvailability:];
-[UIDictationConnectionDelegate dictationConnectionDidEndRecording:];
-[UIDictationConnectionDelegate dictationConnection:didFailRecognitionWithError:];
-[UIDictationConnectionDelegate dictationConnectionDidCancelRecording:];
-[UIDictationConnectionDelegate dictationConnection:didReceivePartialPackage:nluResult:languageModel:];
-[UIDictationConnectionDelegate dictationConnectionDidCancelIncompatibleLocalRecognizer:];
-[UIDictationConnectionDelegate dictationConnection:finalizePhrases:languageModel:correctionIdentifier:secureInput:finalResult:];
-[UIDictationConnectionDelegate dictationConnectionDidStartRecording:];
-[UIDictationConnectionDelegate dictationConnectionDidFinish:];
-[UIDictationConnectionDelegate dictationConnection:didReceiveVoiceCommandCandidatePackage:nluResult:];
-[UIDictationConnectionDelegate dictationConnection:didReceiveSearchResults:recognizedText:stable:final:];
-[UIDictationConnectionDelegate dictationConnectionWillStartRecording:];
-[UIDictationConnectionDelegate dictationConnection:didReceiveCandidateDictationSerializableResults:];
-[UIDictationConnectionDelegate dictationConnection:didFailRecordingWithError:];
-[UIDictationConnectionDelegate dictationConnection:didBeginLocalRecognitionWithModelInfo:];
-[UIDictationConnectionDelegate dictationConnection:receivedInterpretation:languageModel:secureInput:];
```
