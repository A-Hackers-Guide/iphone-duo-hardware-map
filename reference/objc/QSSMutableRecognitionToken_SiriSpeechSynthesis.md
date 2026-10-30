# `QSSMutableRecognitionToken`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSRecognitionToken`
- 0 instance variables, 8 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) token_text;
@property (Ti,N) start_milli_seconds;
@property (Ti,N) end_milli_seconds;
@property (Ti,N) silence_start_milli_seconds;
@property (Ti,N) confidence;
@property (TB,N) add_space_after;
@property (T@"NSString",C,N) phone_seq;
@property (T@"NSString",C,N) ipa_phone_seq;
```

## Instance methods

```
-[QSSMutableRecognitionToken init];
-[QSSMutableRecognitionToken setConfidence:];
-[QSSMutableRecognitionToken copyWithZone:];
-[QSSMutableRecognitionToken confidence];
-[QSSMutableRecognitionToken add_space_after];
-[QSSMutableRecognitionToken setSilence_start_milli_seconds:];
-[QSSMutableRecognitionToken end_milli_seconds];
-[QSSMutableRecognitionToken ipa_phone_seq];
-[QSSMutableRecognitionToken phone_seq];
-[QSSMutableRecognitionToken setAdd_space_after:];
-[QSSMutableRecognitionToken setEnd_milli_seconds:];
-[QSSMutableRecognitionToken setIpa_phone_seq:];
-[QSSMutableRecognitionToken setPhone_seq:];
-[QSSMutableRecognitionToken setStart_milli_seconds:];
-[QSSMutableRecognitionToken setToken_text:];
-[QSSMutableRecognitionToken silence_start_milli_seconds];
-[QSSMutableRecognitionToken start_milli_seconds];
-[QSSMutableRecognitionToken token_text];
```
