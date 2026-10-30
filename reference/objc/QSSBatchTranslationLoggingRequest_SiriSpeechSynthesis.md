# `QSSBatchTranslationLoggingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchTranslationLoggingRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) time_to_first_response;
@property (Ti,R,N) time_to_viewport_complete;
@property (Ti,R,N) time_to_page_complete;
```

## Instance methods

```
-[QSSBatchTranslationLoggingRequest copyWithZone:];
-[QSSBatchTranslationLoggingRequest addObjectToBuffer:];
-[QSSBatchTranslationLoggingRequest flatbuffData];
-[QSSBatchTranslationLoggingRequest initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationLoggingRequest initWithFlatbuffData:];
-[QSSBatchTranslationLoggingRequest initWithFlatbuffData:root:];
-[QSSBatchTranslationLoggingRequest initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationLoggingRequest session_id];
-[QSSBatchTranslationLoggingRequest time_to_first_response];
-[QSSBatchTranslationLoggingRequest time_to_page_complete];
-[QSSBatchTranslationLoggingRequest time_to_viewport_complete];
```
