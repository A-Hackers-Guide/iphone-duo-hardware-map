# `STSpeechTranslatorClientDelegate` (protocol)

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance methods

```
-[STSpeechTranslatorClientDelegate client:didStopTranslationWithError:];
-[STSpeechTranslatorClientDelegate serverDidDisconnectForClient:];
-[STSpeechTranslatorClientDelegate audioGenerationDidFinishForClient:];
-[STSpeechTranslatorClientDelegate client:didGenerateTranslatedAudio:];
-[STSpeechTranslatorClientDelegate client:didPauseTranslationWithReason:];
-[STSpeechTranslatorClientDelegate client:didReceiveTranscriptionResult:];
-[STSpeechTranslatorClientDelegate client:didReceiveTranslationResult:];
-[STSpeechTranslatorClientDelegate client:willStartTranslatedAudioWithMetadata:];
-[STSpeechTranslatorClientDelegate translationDidResumeForClient:];
-[STSpeechTranslatorClientDelegate translationDidStartForClient:];
```
