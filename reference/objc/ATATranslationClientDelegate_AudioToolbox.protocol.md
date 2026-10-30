# `ATATranslationClientDelegate` (protocol)

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance methods

```
-[ATATranslationClientDelegate client:didStopTranslationWithError:];
-[ATATranslationClientDelegate serverDidDisconnectForClient:];
-[ATATranslationClientDelegate audioGenerationDidFinishForClient:];
-[ATATranslationClientDelegate client:didGenerateTranslatedAudio:];
-[ATATranslationClientDelegate client:didPauseTranslationWithReason:];
-[ATATranslationClientDelegate client:didReceiveTranscriptionResult:];
-[ATATranslationClientDelegate client:didReceiveTranslationResult:];
-[ATATranslationClientDelegate client:willStartTranslatedAudioWithMetadata:];
-[ATATranslationClientDelegate translationDidResumeForClient:];
-[ATATranslationClientDelegate translationDidStartForClient:];
```
