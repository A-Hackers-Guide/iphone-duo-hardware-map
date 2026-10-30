# `QSSMutableCreateLanguageProfileResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSCreateLanguageProfileResponse`
- 0 instance variables, 7 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) speech_id;
@property (T@"NSString",C,N) session_id;
@property (Ti,N) error_code;
@property (T@"NSString",C,N) error_str;
@property (T@"QSSUserLanguageProfile",C,N) user_language_profile;
@property (TB,N) incomplete_profile;
@property (TB,N) recreate_apg_prons;
```

## Instance methods

```
-[QSSMutableCreateLanguageProfileResponse init];
-[QSSMutableCreateLanguageProfileResponse copyWithZone:];
-[QSSMutableCreateLanguageProfileResponse error_code];
-[QSSMutableCreateLanguageProfileResponse error_str];
-[QSSMutableCreateLanguageProfileResponse session_id];
-[QSSMutableCreateLanguageProfileResponse setError_code:];
-[QSSMutableCreateLanguageProfileResponse setError_str:];
-[QSSMutableCreateLanguageProfileResponse setSession_id:];
-[QSSMutableCreateLanguageProfileResponse setSpeech_id:];
-[QSSMutableCreateLanguageProfileResponse speech_id];
-[QSSMutableCreateLanguageProfileResponse incomplete_profile];
-[QSSMutableCreateLanguageProfileResponse recreate_apg_prons];
-[QSSMutableCreateLanguageProfileResponse setIncomplete_profile:];
-[QSSMutableCreateLanguageProfileResponse setRecreate_apg_prons:];
-[QSSMutableCreateLanguageProfileResponse setUser_language_profile:];
-[QSSMutableCreateLanguageProfileResponse user_language_profile];
```
