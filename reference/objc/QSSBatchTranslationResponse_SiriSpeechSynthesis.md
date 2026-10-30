# `QSSBatchTranslationResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{BatchTranslationResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) request_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_string;
@property (T@"NSString",R,N) paragraph_id;
@property (T@"NSString",R,N) translated_text;
@property (T@"NSArray",R,N) span;
@property (T@"NSArray",R,N) translated_sentences;
```

## Instance methods

```
-[QSSBatchTranslationResponse copyWithZone:];
-[QSSBatchTranslationResponse span];
-[QSSBatchTranslationResponse addObjectToBuffer:];
-[QSSBatchTranslationResponse flatbuffData];
-[QSSBatchTranslationResponse initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationResponse initWithFlatbuffData:];
-[QSSBatchTranslationResponse initWithFlatbuffData:root:];
-[QSSBatchTranslationResponse initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationResponse translated_text];
-[QSSBatchTranslationResponse paragraph_id];
-[QSSBatchTranslationResponse request_id];
-[QSSBatchTranslationResponse return_code];
-[QSSBatchTranslationResponse return_string];
-[QSSBatchTranslationResponse translated_sentences];
```
