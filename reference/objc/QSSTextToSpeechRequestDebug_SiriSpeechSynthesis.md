# `QSSTextToSpeechRequestDebug`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechRequestDebug=[1C]} _root;
```

## Properties

```
@property (TB,R,N) force_use_tts_service;
@property (TB,R,N) disable_cache;
```

## Instance methods

```
-[QSSTextToSpeechRequestDebug copyWithZone:];
-[QSSTextToSpeechRequestDebug addObjectToBuffer:];
-[QSSTextToSpeechRequestDebug disable_cache];
-[QSSTextToSpeechRequestDebug flatbuffData];
-[QSSTextToSpeechRequestDebug force_use_tts_service];
-[QSSTextToSpeechRequestDebug initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechRequestDebug initWithFlatbuffData:];
-[QSSTextToSpeechRequestDebug initWithFlatbuffData:root:];
-[QSSTextToSpeechRequestDebug initWithFlatbuffData:root:verify:];
```
