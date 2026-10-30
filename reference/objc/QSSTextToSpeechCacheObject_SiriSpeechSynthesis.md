# `QSSTextToSpeechCacheObject`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechCacheObject=[1C]} _root;
```

## Properties

```
@property (T@"NSData",R,N) audio;
@property (T@"NSArray",R,N) word_timing_info;
```

## Instance methods

```
-[QSSTextToSpeechCacheObject audio];
-[QSSTextToSpeechCacheObject copyWithZone:];
-[QSSTextToSpeechCacheObject addObjectToBuffer:];
-[QSSTextToSpeechCacheObject audio:];
-[QSSTextToSpeechCacheObject flatbuffData];
-[QSSTextToSpeechCacheObject initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechCacheObject initWithFlatbuffData:];
-[QSSTextToSpeechCacheObject initWithFlatbuffData:root:];
-[QSSTextToSpeechCacheObject initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechCacheObject word_timing_info];
```
