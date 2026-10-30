# `QSSMutableGraphemeToPhonemeResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `QSSGraphemeToPhonemeResponse`
- 0 instance variables, 10 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) session_id;
@property (Ti,N) return_code;
@property (T@"NSString",C,N) return_str;
@property (T@"NSArray",C,N) phonemes;
@property (TB,N) is_pron_guessed;
@property (T@"NSString",C,N) g2p_version;
@property (T@"NSString",C,N) g2p_model_version;
@property (T@"NSString",C,N) phoneset_version;
@property (T@"NSArray",C,N) aot_token_prons;
@property (T@"NSArray",C,N) jit_token_prons;
```

## Instance methods

```
-[QSSMutableGraphemeToPhonemeResponse init];
-[QSSMutableGraphemeToPhonemeResponse copyWithZone:];
-[QSSMutableGraphemeToPhonemeResponse phonemes];
-[QSSMutableGraphemeToPhonemeResponse setPhonemes:];
-[QSSMutableGraphemeToPhonemeResponse session_id];
-[QSSMutableGraphemeToPhonemeResponse setSession_id:];
-[QSSMutableGraphemeToPhonemeResponse jit_token_prons];
-[QSSMutableGraphemeToPhonemeResponse aot_token_prons];
-[QSSMutableGraphemeToPhonemeResponse is_pron_guessed];
-[QSSMutableGraphemeToPhonemeResponse setG2p_version:];
-[QSSMutableGraphemeToPhonemeResponse setReturn_code:];
-[QSSMutableGraphemeToPhonemeResponse g2p_model_version];
-[QSSMutableGraphemeToPhonemeResponse g2p_version];
-[QSSMutableGraphemeToPhonemeResponse phoneset_version];
-[QSSMutableGraphemeToPhonemeResponse return_code];
-[QSSMutableGraphemeToPhonemeResponse return_str];
-[QSSMutableGraphemeToPhonemeResponse setAot_token_prons:];
-[QSSMutableGraphemeToPhonemeResponse setG2p_model_version:];
-[QSSMutableGraphemeToPhonemeResponse setIs_pron_guessed:];
-[QSSMutableGraphemeToPhonemeResponse setJit_token_prons:];
-[QSSMutableGraphemeToPhonemeResponse setPhoneset_version:];
-[QSSMutableGraphemeToPhonemeResponse setReturn_str:];
```
