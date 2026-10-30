# `QSSPronGuessResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{PronGuessResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (T@"NSString",R,N) apg_id;
@property (T@"QSSVocToken",R,N) voc_token;
@property (T@"NSArray",R,N) tts_pronunciations;
@property (T@"NSArray",R,N) human_readable_prons;
```

## Instance methods

```
-[QSSPronGuessResponse copyWithZone:];
-[QSSPronGuessResponse addObjectToBuffer:];
-[QSSPronGuessResponse error_code];
-[QSSPronGuessResponse error_str];
-[QSSPronGuessResponse flatbuffData];
-[QSSPronGuessResponse initAndVerifyWithFlatbuffData:];
-[QSSPronGuessResponse initWithFlatbuffData:];
-[QSSPronGuessResponse initWithFlatbuffData:root:];
-[QSSPronGuessResponse initWithFlatbuffData:root:verify:];
-[QSSPronGuessResponse session_id];
-[QSSPronGuessResponse speech_id];
-[QSSPronGuessResponse apg_id];
-[QSSPronGuessResponse human_readable_prons];
-[QSSPronGuessResponse tts_pronunciations];
-[QSSPronGuessResponse voc_token];
```
