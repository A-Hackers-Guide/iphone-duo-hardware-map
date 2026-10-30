# `ATATranslatorClientDelegate`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ATATranslationClientDelegate`
- 2 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
{weak_ptr<AT::Translation::TranslatorClient>="__ptr_"^{TranslatorClient}"__cntrl_"^{__shared_weak_count}} mImpl;
i mScope;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ATATranslatorClientDelegate audioGenerationDidFinishForClient:];
-[ATATranslatorClientDelegate client:didGenerateTranslatedAudio:];
-[ATATranslatorClientDelegate client:didPauseTranslationWithReason:];
-[ATATranslatorClientDelegate client:didReceiveTranscriptionResult:];
-[ATATranslatorClientDelegate client:didReceiveTranslationResult:];
-[ATATranslatorClientDelegate client:didStopTranslationWithError:];
-[ATATranslatorClientDelegate client:willStartTranslatedAudioWithMetadata:];
-[ATATranslatorClientDelegate initWithWeakImpl:scope:];
-[ATATranslatorClientDelegate serverDidDisconnectForClient:];
-[ATATranslatorClientDelegate translationDidResumeForClient:];
-[ATATranslatorClientDelegate translationDidStartForClient:];
```
