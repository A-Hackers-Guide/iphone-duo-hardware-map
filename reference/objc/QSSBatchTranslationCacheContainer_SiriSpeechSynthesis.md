# `QSSBatchTranslationCacheContainer`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchTranslationCacheContainer=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) request_id;
@property (T@"NSString",R,N) translated_text;
@property (T@"NSArray",R,N) spans;
@property (Ti,R,N) sentence_count;
```

## Instance methods

```
-[QSSBatchTranslationCacheContainer copyWithZone:];
-[QSSBatchTranslationCacheContainer spans];
-[QSSBatchTranslationCacheContainer addObjectToBuffer:];
-[QSSBatchTranslationCacheContainer flatbuffData];
-[QSSBatchTranslationCacheContainer initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationCacheContainer initWithFlatbuffData:];
-[QSSBatchTranslationCacheContainer initWithFlatbuffData:root:];
-[QSSBatchTranslationCacheContainer initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationCacheContainer translated_text];
-[QSSBatchTranslationCacheContainer request_id];
-[QSSBatchTranslationCacheContainer sentence_count];
```
