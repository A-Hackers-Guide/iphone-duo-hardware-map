# `QSSMutableRecoverPronsResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSRecoverPronsResponse`
- 0 instance variables, 6 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) error_code;
@property (T@"NSString",C,N) error_str;
@property (T@"NSArray",C,N) recovery_return_codes;
@property (T@"NSArray",C,N) voc_tokens;
```

## Instance methods

```
-[QSSMutableRecoverPronsResponse init];
-[QSSMutableRecoverPronsResponse copyWithZone:];
-[QSSMutableRecoverPronsResponse error_code];
-[QSSMutableRecoverPronsResponse error_str];
-[QSSMutableRecoverPronsResponse session_id];
-[QSSMutableRecoverPronsResponse setError_code:];
-[QSSMutableRecoverPronsResponse setError_str:];
-[QSSMutableRecoverPronsResponse setSession_id:];
-[QSSMutableRecoverPronsResponse setSpeech_id:];
-[QSSMutableRecoverPronsResponse speech_id];
-[QSSMutableRecoverPronsResponse recovery_return_codes];
-[QSSMutableRecoverPronsResponse setRecovery_return_codes:];
-[QSSMutableRecoverPronsResponse setVoc_tokens:];
-[QSSMutableRecoverPronsResponse voc_tokens];
```
