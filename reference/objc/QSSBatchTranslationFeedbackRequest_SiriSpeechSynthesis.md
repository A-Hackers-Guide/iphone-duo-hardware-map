# `QSSBatchTranslationFeedbackRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchTranslationFeedbackRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) source_content;
@property (T@"NSString",R,N) translated_content;
@property (T@"NSString",R,N) url;
@property (T@"NSString",R,N) errors;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) source_language;
@property (T@"NSString",R,N) target_language;
@property (T@"NSString",R,N) safari_version;
@property (T@"NSString",R,N) app_id;
@property (T@"NSString",R,N) os_version;
@property (T@"NSString",R,N) device_type;
```

## Instance methods

```
-[QSSBatchTranslationFeedbackRequest errors];
-[QSSBatchTranslationFeedbackRequest device_type];
-[QSSBatchTranslationFeedbackRequest copyWithZone:];
-[QSSBatchTranslationFeedbackRequest url];
-[QSSBatchTranslationFeedbackRequest safari_version];
-[QSSBatchTranslationFeedbackRequest addObjectToBuffer:];
-[QSSBatchTranslationFeedbackRequest app_id];
-[QSSBatchTranslationFeedbackRequest flatbuffData];
-[QSSBatchTranslationFeedbackRequest initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationFeedbackRequest initWithFlatbuffData:];
-[QSSBatchTranslationFeedbackRequest initWithFlatbuffData:root:];
-[QSSBatchTranslationFeedbackRequest initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationFeedbackRequest session_id];
-[QSSBatchTranslationFeedbackRequest source_language];
-[QSSBatchTranslationFeedbackRequest target_language];
-[QSSBatchTranslationFeedbackRequest os_version];
-[QSSBatchTranslationFeedbackRequest source_content];
-[QSSBatchTranslationFeedbackRequest translated_content];
```
