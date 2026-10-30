# `QSSRecognitionResult`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{RecognitionResult=[1C]} _root;
```

## Properties

```
@property (T@"QSSRecognitionSausage",R,N) pre_itn;
@property (T@"QSSRecognitionSausage",R,N) post_itn;
@property (T@"NSArray",R,N) pre_itn_nbest_choices;
@property (T@"NSArray",R,N) post_itn_nbest_choices;
@property (T@"NSArray",R,N) pre_itn_token_to_post_itn_char_alignment;
@property (T@"NSArray",R,N) choice_alignments;
```

## Instance methods

```
-[QSSRecognitionResult copyWithZone:];
-[QSSRecognitionResult addObjectToBuffer:];
-[QSSRecognitionResult flatbuffData];
-[QSSRecognitionResult initAndVerifyWithFlatbuffData:];
-[QSSRecognitionResult initWithFlatbuffData:];
-[QSSRecognitionResult initWithFlatbuffData:root:];
-[QSSRecognitionResult initWithFlatbuffData:root:verify:];
-[QSSRecognitionResult pre_itn];
-[QSSRecognitionResult choice_alignments];
-[QSSRecognitionResult post_itn];
-[QSSRecognitionResult post_itn_nbest_choices];
-[QSSRecognitionResult pre_itn_nbest_choices];
-[QSSRecognitionResult pre_itn_token_to_post_itn_char_alignment];
```
