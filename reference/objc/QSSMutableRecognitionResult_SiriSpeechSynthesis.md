# `QSSMutableRecognitionResult`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSRecognitionResult`
- 0 instance variables, 6 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"QSSRecognitionSausage",C,N) pre_itn;
@property (T@"QSSRecognitionSausage",C,N) post_itn;
@property (T@"NSArray",C,N) pre_itn_nbest_choices;
@property (T@"NSArray",C,N) post_itn_nbest_choices;
@property (T@"NSArray",C,N) pre_itn_token_to_post_itn_char_alignment;
@property (T@"NSArray",C,N) choice_alignments;
```

## Instance methods

```
-[QSSMutableRecognitionResult init];
-[QSSMutableRecognitionResult copyWithZone:];
-[QSSMutableRecognitionResult pre_itn];
-[QSSMutableRecognitionResult choice_alignments];
-[QSSMutableRecognitionResult post_itn];
-[QSSMutableRecognitionResult post_itn_nbest_choices];
-[QSSMutableRecognitionResult pre_itn_nbest_choices];
-[QSSMutableRecognitionResult pre_itn_token_to_post_itn_char_alignment];
-[QSSMutableRecognitionResult setChoice_alignments:];
-[QSSMutableRecognitionResult setPost_itn:];
-[QSSMutableRecognitionResult setPost_itn_nbest_choices:];
-[QSSMutableRecognitionResult setPre_itn:];
-[QSSMutableRecognitionResult setPre_itn_nbest_choices:];
-[QSSMutableRecognitionResult setPre_itn_token_to_post_itn_char_alignment:];
```
