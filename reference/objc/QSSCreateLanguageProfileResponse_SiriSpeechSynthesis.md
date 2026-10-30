# `QSSCreateLanguageProfileResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{CreateLanguageProfileResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (T@"QSSUserLanguageProfile",R,N) user_language_profile;
@property (TB,R,N) incomplete_profile;
@property (TB,R,N) recreate_apg_prons;
```

## Instance methods

```
-[QSSCreateLanguageProfileResponse copyWithZone:];
-[QSSCreateLanguageProfileResponse addObjectToBuffer:];
-[QSSCreateLanguageProfileResponse error_code];
-[QSSCreateLanguageProfileResponse error_str];
-[QSSCreateLanguageProfileResponse flatbuffData];
-[QSSCreateLanguageProfileResponse initAndVerifyWithFlatbuffData:];
-[QSSCreateLanguageProfileResponse initWithFlatbuffData:];
-[QSSCreateLanguageProfileResponse initWithFlatbuffData:root:];
-[QSSCreateLanguageProfileResponse initWithFlatbuffData:root:verify:];
-[QSSCreateLanguageProfileResponse session_id];
-[QSSCreateLanguageProfileResponse speech_id];
-[QSSCreateLanguageProfileResponse incomplete_profile];
-[QSSCreateLanguageProfileResponse recreate_apg_prons];
-[QSSCreateLanguageProfileResponse user_language_profile];
```
