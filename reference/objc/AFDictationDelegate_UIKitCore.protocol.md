# `AFDictationDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 29 instance methods, 0 class methods

## Instance methods

```
-[AFDictationDelegate dictationConnection:speechRecordingDidFail:];
-[AFDictationDelegate dictationConnection:didRecognizeVoiceCommandCandidatePackage:nluResult:];
-[AFDictationDelegate dictationConnection:didRecognizePhrases:languageModel:correctionIdentifier:];
-[AFDictationDelegate dictationConnection:didRecognizeFinalResultCandidatePackage:];
-[AFDictationDelegate dictationConnnectionDidChangeAvailability:];
-[AFDictationDelegate dictationConnectionSpeechRecognitionDidSucceed:];
-[AFDictationDelegate dictationConnection:didRecognizeTokens:languageModel:];
-[AFDictationDelegate dictationConnection:didRecognizePartialPackage:nluResult:languageModel:];
-[AFDictationDelegate dictationConnectionSpeechRecordingDidBegin:];
-[AFDictationDelegate dictationConnection:didRecognizePartialResult:];
-[AFDictationDelegate dictationConnectionDidPauseRecognition:];
-[AFDictationDelegate dictationConnection:languageDetectorFailedWithError:];
-[AFDictationDelegate dictationConnectionSpeechRecordingWillBegin:];
-[AFDictationDelegate dictationConnection:speechRecordingDidBeginWithOptions:];
-[AFDictationDelegate dictationConnection:didRecognizeMultilingualSpeech:];
-[AFDictationDelegate dictationConnection:didReceiveSearchResults:recognizedText:stable:final:];
-[AFDictationDelegate dictationConnection:didDetectLanguage:confidenceScores:isConfident:];
-[AFDictationDelegate dictationConnectionSpeechRecordingDidEnd:];
-[AFDictationDelegate dictationConnectionSpeechRecordingDidCancel:];
-[AFDictationDelegate dictationConnection:speechRecognitionDidFail:];
-[AFDictationDelegate dictationConnection:didBeginLocalRecognitionWithModelInfo:];
-[AFDictationDelegate dictationConnection:didRecognizeTokens:nluResult:languageModel:];
-[AFDictationDelegate dictationConnection:didDetectLanguage:confidenceScores:];
-[AFDictationDelegate dictationConnection:didFinishWritingAudioFile:error:];
-[AFDictationDelegate dictationConnection:didProcessAudioDuration:];
-[AFDictationDelegate dictationConnection:didRecognizePackage:];
-[AFDictationDelegate dictationConnection:didRecognizePackage:nluResult:];
-[AFDictationDelegate dictationConnection:didRecognizePhrases:languageModel:correctionIdentifier:replacingPreviousPhrasesCount:];
-[AFDictationDelegate dictationConnection:didRecognizeTranscriptionObjects:languageModel:];
```
