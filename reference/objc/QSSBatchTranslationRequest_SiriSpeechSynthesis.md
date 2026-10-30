# `QSSBatchTranslationRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchTranslationRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) request_id;
@property (T@"NSString",R,N) task;
@property (T@"NSString",R,N) source_language;
@property (T@"NSString",R,N) target_language;
@property (T@"NSArray",R,N) paragraphs;
@property (T@"NSString",R,N) app_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) url;
@property (Tq,R,N) opt_in_status;
```

## Instance methods

```
-[QSSBatchTranslationRequest task];
-[QSSBatchTranslationRequest copyWithZone:];
-[QSSBatchTranslationRequest url];
-[QSSBatchTranslationRequest paragraphs];
-[QSSBatchTranslationRequest addObjectToBuffer:];
-[QSSBatchTranslationRequest app_id];
-[QSSBatchTranslationRequest flatbuffData];
-[QSSBatchTranslationRequest initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationRequest initWithFlatbuffData:];
-[QSSBatchTranslationRequest initWithFlatbuffData:root:];
-[QSSBatchTranslationRequest initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationRequest session_id];
-[QSSBatchTranslationRequest source_language];
-[QSSBatchTranslationRequest target_language];
-[QSSBatchTranslationRequest opt_in_status];
-[QSSBatchTranslationRequest request_id];
```
