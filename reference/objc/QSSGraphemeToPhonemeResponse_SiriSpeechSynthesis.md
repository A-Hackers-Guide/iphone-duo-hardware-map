# `QSSGraphemeToPhonemeResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{GraphemeToPhonemeResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSArray",R,N) phonemes;
@property (TB,R,N) is_pron_guessed;
@property (T@"NSString",R,N) g2p_version;
@property (T@"NSString",R,N) g2p_model_version;
@property (T@"NSString",R,N) phoneset_version;
@property (T@"NSArray",R,N) aot_token_prons;
@property (T@"NSArray",R,N) jit_token_prons;
```

## Instance methods

```
-[QSSGraphemeToPhonemeResponse copyWithZone:];
-[QSSGraphemeToPhonemeResponse phonemes];
-[QSSGraphemeToPhonemeResponse addObjectToBuffer:];
-[QSSGraphemeToPhonemeResponse flatbuffData];
-[QSSGraphemeToPhonemeResponse initAndVerifyWithFlatbuffData:];
-[QSSGraphemeToPhonemeResponse initWithFlatbuffData:];
-[QSSGraphemeToPhonemeResponse initWithFlatbuffData:root:];
-[QSSGraphemeToPhonemeResponse initWithFlatbuffData:root:verify:];
-[QSSGraphemeToPhonemeResponse session_id];
-[QSSGraphemeToPhonemeResponse jit_token_prons];
-[QSSGraphemeToPhonemeResponse aot_token_prons];
-[QSSGraphemeToPhonemeResponse is_pron_guessed];
-[QSSGraphemeToPhonemeResponse g2p_model_version];
-[QSSGraphemeToPhonemeResponse g2p_version];
-[QSSGraphemeToPhonemeResponse phoneset_version];
-[QSSGraphemeToPhonemeResponse return_code];
-[QSSGraphemeToPhonemeResponse return_str];
```
