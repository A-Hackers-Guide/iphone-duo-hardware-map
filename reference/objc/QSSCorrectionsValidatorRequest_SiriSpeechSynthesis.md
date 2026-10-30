# `QSSCorrectionsValidatorRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{CorrectionsValidatorRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"QSSRecognitionResult",R,N) recognition_result;
@property (T@"NSString",R,N) original_utterance;
@property (T@"NSString",R,N) corrected_utterance;
```

## Instance methods

```
-[QSSCorrectionsValidatorRequest language];
-[QSSCorrectionsValidatorRequest copyWithZone:];
-[QSSCorrectionsValidatorRequest addObjectToBuffer:];
-[QSSCorrectionsValidatorRequest flatbuffData];
-[QSSCorrectionsValidatorRequest initAndVerifyWithFlatbuffData:];
-[QSSCorrectionsValidatorRequest initWithFlatbuffData:];
-[QSSCorrectionsValidatorRequest initWithFlatbuffData:root:];
-[QSSCorrectionsValidatorRequest initWithFlatbuffData:root:verify:];
-[QSSCorrectionsValidatorRequest session_id];
-[QSSCorrectionsValidatorRequest speech_id];
-[QSSCorrectionsValidatorRequest corrected_utterance];
-[QSSCorrectionsValidatorRequest original_utterance];
-[QSSCorrectionsValidatorRequest recognition_result];
```
