# `SFSpeechSynthesizer`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 10 instance methods, 4 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _serverTaskQueue;
@"NSObject<OS_dispatch_queue>" _deviceTaskQueue;
@"NSObject<OS_dispatch_queue>" _cacheTaskQueue;
B _isVoiceAssetDownloaded;
@"NSLocale" _locale;
@"SFSpeechSynthesisVoice" _voice;
```

## Properties

```
@property (T@"NSLocale",R,C,N,V_locale) locale;
@property (T@"SFSpeechSynthesisVoice",R,N,V_voice) voice;
@property (TB,R,N,V_isVoiceAssetDownloaded) isVoiceAssetDownloaded;
```

## Class methods

```
+[SFSpeechSynthesizer initialize];
+[SFSpeechSynthesizer supportedLocales];
+[SFSpeechSynthesizer getVoiceByName:];
+[SFSpeechSynthesizer supportedVoicesByLocale:];
```

## Instance methods

```
-[SFSpeechSynthesizer voice];
-[SFSpeechSynthesizer init];
-[SFSpeechSynthesizer dealloc];
-[SFSpeechSynthesizer locale];
-[SFSpeechSynthesizer prewarm:];
-[SFSpeechSynthesizer initWithVoice:];
-[SFSpeechSynthesizer startTaskWithRequest:completion:];
-[SFSpeechSynthesizer isVoiceAssetDownloaded];
-[SFSpeechSynthesizer startTaskWithRequest:delegate:];
-[SFSpeechSynthesizer startTaskWithRequest:delegate:completion:];
```
