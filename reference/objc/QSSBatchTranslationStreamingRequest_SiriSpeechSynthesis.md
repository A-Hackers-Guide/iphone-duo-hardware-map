# `QSSBatchTranslationStreamingRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchTranslationStreamingRequest=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSBatchTranslationRequest",R,N) contentAsQSSBatchTranslationRequest;
@property (T@"QSSBatchTranslationFeedbackRequest",R,N) contentAsQSSBatchTranslationFeedbackRequest;
@property (T@"QSSBatchTranslationLoggingRequest",R,N) contentAsQSSBatchTranslationLoggingRequest;
@property (T@"QSSTranslationSupportedLanguagesRequest",R,N) contentAsQSSTranslationSupportedLanguagesRequest;
```

## Instance methods

```
-[QSSBatchTranslationStreamingRequest copyWithZone:];
-[QSSBatchTranslationStreamingRequest addObjectToBuffer:];
-[QSSBatchTranslationStreamingRequest content_type];
-[QSSBatchTranslationStreamingRequest flatbuffData];
-[QSSBatchTranslationStreamingRequest initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationStreamingRequest initWithFlatbuffData:];
-[QSSBatchTranslationStreamingRequest initWithFlatbuffData:root:];
-[QSSBatchTranslationStreamingRequest initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationStreamingRequest contentAsQSSBatchTranslationFeedbackRequest];
-[QSSBatchTranslationStreamingRequest contentAsQSSBatchTranslationLoggingRequest];
-[QSSBatchTranslationStreamingRequest contentAsQSSBatchTranslationRequest];
-[QSSBatchTranslationStreamingRequest contentAsQSSTranslationSupportedLanguagesRequest];
```
