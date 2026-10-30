# `QSSTextToSpeechRequestMeta`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechRequestMeta=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) channel_type;
@property (T@"NSString",R,N) app_id;
@property (TB,R,N) is_synthesis;
```

## Instance methods

```
-[QSSTextToSpeechRequestMeta copyWithZone:];
-[QSSTextToSpeechRequestMeta addObjectToBuffer:];
-[QSSTextToSpeechRequestMeta app_id];
-[QSSTextToSpeechRequestMeta channel_type];
-[QSSTextToSpeechRequestMeta flatbuffData];
-[QSSTextToSpeechRequestMeta initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechRequestMeta initWithFlatbuffData:];
-[QSSTextToSpeechRequestMeta initWithFlatbuffData:root:];
-[QSSTextToSpeechRequestMeta initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechRequestMeta is_synthesis];
```
