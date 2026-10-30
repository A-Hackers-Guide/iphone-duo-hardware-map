# `QSSTextToSpeechMeta`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechMeta=[1C]} _root;
```

## Properties

```
@property (T@"QSSTextToSpeechVoice",R,N) voice;
@property (T@"QSSTextToSpeechResource",R,N) resource;
```

## Instance methods

```
-[QSSTextToSpeechMeta voice];
-[QSSTextToSpeechMeta resource];
-[QSSTextToSpeechMeta copyWithZone:];
-[QSSTextToSpeechMeta addObjectToBuffer:];
-[QSSTextToSpeechMeta flatbuffData];
-[QSSTextToSpeechMeta initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechMeta initWithFlatbuffData:];
-[QSSTextToSpeechMeta initWithFlatbuffData:root:];
-[QSSTextToSpeechMeta initWithFlatbuffData:root:verify:];
```
