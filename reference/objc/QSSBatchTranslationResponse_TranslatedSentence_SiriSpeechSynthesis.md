# `QSSBatchTranslationResponse_TranslatedSentence`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TranslatedSentence=[1C]} _root;
```

## Properties

```
@property (T@"QSSSpan",R,N) source_span;
@property (T@"NSString",R,N) engine_input;
@property (T@"QSSSpan",R,N) target_span;
@property (T@"NSArray",R,N) n_best_choices;
```

## Instance methods

```
-[QSSBatchTranslationResponse_TranslatedSentence copyWithZone:];
-[QSSBatchTranslationResponse_TranslatedSentence addObjectToBuffer:];
-[QSSBatchTranslationResponse_TranslatedSentence flatbuffData];
-[QSSBatchTranslationResponse_TranslatedSentence initAndVerifyWithFlatbuffData:];
-[QSSBatchTranslationResponse_TranslatedSentence initWithFlatbuffData:];
-[QSSBatchTranslationResponse_TranslatedSentence initWithFlatbuffData:root:];
-[QSSBatchTranslationResponse_TranslatedSentence initWithFlatbuffData:root:verify:];
-[QSSBatchTranslationResponse_TranslatedSentence engine_input];
-[QSSBatchTranslationResponse_TranslatedSentence n_best_choices];
-[QSSBatchTranslationResponse_TranslatedSentence source_span];
-[QSSBatchTranslationResponse_TranslatedSentence target_span];
```
