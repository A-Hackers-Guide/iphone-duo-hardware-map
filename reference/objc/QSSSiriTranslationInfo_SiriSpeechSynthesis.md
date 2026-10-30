# `QSSSiriTranslationInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SiriTranslationInfo=[1C]} _root;
```

## Properties

```
@property (T@"QSSRecognitionSausage",R,N) raw_sausage;
@property (T@"NSArray",R,N) raw_nbest_choices;
@property (T@"NSArray",R,N) post_itn_tokens;
@property (T@"NSString",R,N) post_itn_recognition;
@property (T@"NSArray",R,N) itn_alignments;
@property (T@"NSArray",R,N) translation_phrase;
```

## Instance methods

```
-[QSSSiriTranslationInfo copyWithZone:];
-[QSSSiriTranslationInfo addObjectToBuffer:];
-[QSSSiriTranslationInfo flatbuffData];
-[QSSSiriTranslationInfo initAndVerifyWithFlatbuffData:];
-[QSSSiriTranslationInfo initWithFlatbuffData:];
-[QSSSiriTranslationInfo initWithFlatbuffData:root:];
-[QSSSiriTranslationInfo initWithFlatbuffData:root:verify:];
-[QSSSiriTranslationInfo post_itn_tokens];
-[QSSSiriTranslationInfo itn_alignments];
-[QSSSiriTranslationInfo post_itn_recognition];
-[QSSSiriTranslationInfo raw_nbest_choices];
-[QSSSiriTranslationInfo raw_sausage];
-[QSSSiriTranslationInfo translation_phrase];
```
