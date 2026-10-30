# `QSSMutablePronGuessResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSPronGuessResponse`
- 0 instance variables, 8 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) error_code;
@property (T@"NSString",C,N) error_str;
@property (T@"NSString",C,N) apg_id;
@property (T@"QSSVocToken",C,N) voc_token;
@property (T@"NSArray",C,N) tts_pronunciations;
@property (T@"NSArray",C,N) human_readable_prons;
```

## Instance methods

```
-[QSSMutablePronGuessResponse init];
-[QSSMutablePronGuessResponse copyWithZone:];
-[QSSMutablePronGuessResponse error_code];
-[QSSMutablePronGuessResponse error_str];
-[QSSMutablePronGuessResponse session_id];
-[QSSMutablePronGuessResponse setError_code:];
-[QSSMutablePronGuessResponse setError_str:];
-[QSSMutablePronGuessResponse setSession_id:];
-[QSSMutablePronGuessResponse setSpeech_id:];
-[QSSMutablePronGuessResponse speech_id];
-[QSSMutablePronGuessResponse apg_id];
-[QSSMutablePronGuessResponse human_readable_prons];
-[QSSMutablePronGuessResponse setApg_id:];
-[QSSMutablePronGuessResponse setHuman_readable_prons:];
-[QSSMutablePronGuessResponse setTts_pronunciations:];
-[QSSMutablePronGuessResponse setVoc_token:];
-[QSSMutablePronGuessResponse tts_pronunciations];
-[QSSMutablePronGuessResponse voc_token];
```
