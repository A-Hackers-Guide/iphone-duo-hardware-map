# `QSSBatchTranslationRequest_Paragraph`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{Paragraph=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) paragraph_id;
@property (T@"NSString",R,N) text;
@property (T@"NSArray",R,N) span;
```

## Instance methods

```
-[QSSBatchTranslationRequest_Paragraph text];
-[QSSBatchTranslationRequest_Paragraph copyWithZone:];
-[QSSBatchTranslationRequest_Paragraph span];
-[QSSBatchTranslationRequest_Paragraph addObjectToBuffer:];
-[QSSBatchTranslationRequest_Paragraph flatbuffData];
-[QSSBatchTranslationRequest_Paragraph initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationRequest_Paragraph initWithFlatbuffData:];
-[QSSBatchTranslationRequest_Paragraph initWithFlatbuffData:root:];
-[QSSBatchTranslationRequest_Paragraph initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationRequest_Paragraph paragraph_id];
```
