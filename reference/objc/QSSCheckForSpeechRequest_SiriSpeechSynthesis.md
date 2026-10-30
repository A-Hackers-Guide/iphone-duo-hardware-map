# `QSSCheckForSpeechRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{CheckForSpeechRequest=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) start_speech_time;
@property (Tq,R,N) end_speech_time;
```

## Instance methods

```
-[QSSCheckForSpeechRequest copyWithZone:];
-[QSSCheckForSpeechRequest addObjectToBuffer:];
-[QSSCheckForSpeechRequest flatbuffData];
-[QSSCheckForSpeechRequest initAndVerifyWithFlatbuffData:];
-[QSSCheckForSpeechRequest initWithFlatbuffData:];
-[QSSCheckForSpeechRequest initWithFlatbuffData:root:];
-[QSSCheckForSpeechRequest initWithFlatbuffData:root:verify:];
-[QSSCheckForSpeechRequest end_speech_time];
-[QSSCheckForSpeechRequest start_speech_time];
```
