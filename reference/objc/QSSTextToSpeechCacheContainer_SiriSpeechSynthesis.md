# `QSSTextToSpeechCacheContainer`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechCacheContainer=[1C]} _root;
```

## Properties

```
@property (T@"QSSTextToSpeechCacheMetaInfo",R,N) cache_meta_info;
@property (T@"NSArray",R,N) cache_object;
```

## Instance methods

```
-[QSSTextToSpeechCacheContainer copyWithZone:];
-[QSSTextToSpeechCacheContainer addObjectToBuffer:];
-[QSSTextToSpeechCacheContainer flatbuffData];
-[QSSTextToSpeechCacheContainer initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechCacheContainer initWithFlatbuffData:];
-[QSSTextToSpeechCacheContainer initWithFlatbuffData:root:];
-[QSSTextToSpeechCacheContainer initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechCacheContainer cache_meta_info];
-[QSSTextToSpeechCacheContainer cache_object];
```
