# `QSSBatchTranslationStreamingResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchTranslationStreamingResponse=[1C]} _root;
```

## Properties

```
@property (Tq,R,N) content_type;
@property (T@"QSSBatchTranslationResponse",R,N) contentAsQSSBatchTranslationResponse;
@property (T@"QSSFinalBlazarResponse",R,N) contentAsQSSFinalBlazarResponse;
@property (T@"QSSTranslationSupportedLanguagesResponse",R,N) contentAsQSSTranslationSupportedLanguagesResponse;
```

## Instance methods

```
-[QSSBatchTranslationStreamingResponse copyWithZone:];
-[QSSBatchTranslationStreamingResponse addObjectToBuffer:];
-[QSSBatchTranslationStreamingResponse content_type];
-[QSSBatchTranslationStreamingResponse flatbuffData];
-[QSSBatchTranslationStreamingResponse initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationStreamingResponse initWithFlatbuffData:];
-[QSSBatchTranslationStreamingResponse initWithFlatbuffData:root:];
-[QSSBatchTranslationStreamingResponse initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationStreamingResponse contentAsQSSFinalBlazarResponse];
-[QSSBatchTranslationStreamingResponse contentAsQSSBatchTranslationResponse];
-[QSSBatchTranslationStreamingResponse contentAsQSSTranslationSupportedLanguagesResponse];
```
