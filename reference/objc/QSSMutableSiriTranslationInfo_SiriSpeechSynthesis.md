# `QSSMutableSiriTranslationInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSSiriTranslationInfo`
- 0 instance variables, 6 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"QSSRecognitionSausage",C,N) raw_sausage;
@property (T@"NSArray",C,N) raw_nbest_choices;
@property (T@"NSArray",C,N) post_itn_tokens;
@property (T@"NSString",C,N) post_itn_recognition;
@property (T@"NSArray",C,N) itn_alignments;
@property (T@"NSArray",C,N) translation_phrase;
```

## Instance methods

```
-[QSSMutableSiriTranslationInfo init];
-[QSSMutableSiriTranslationInfo copyWithZone:];
-[QSSMutableSiriTranslationInfo post_itn_tokens];
-[QSSMutableSiriTranslationInfo setRaw_sausage:];
-[QSSMutableSiriTranslationInfo itn_alignments];
-[QSSMutableSiriTranslationInfo post_itn_recognition];
-[QSSMutableSiriTranslationInfo raw_nbest_choices];
-[QSSMutableSiriTranslationInfo raw_sausage];
-[QSSMutableSiriTranslationInfo setItn_alignments:];
-[QSSMutableSiriTranslationInfo setPost_itn_recognition:];
-[QSSMutableSiriTranslationInfo setPost_itn_tokens:];
-[QSSMutableSiriTranslationInfo setRaw_nbest_choices:];
-[QSSMutableSiriTranslationInfo setTranslation_phrase:];
-[QSSMutableSiriTranslationInfo translation_phrase];
```
