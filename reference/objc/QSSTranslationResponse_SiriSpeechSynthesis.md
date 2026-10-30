# `QSSTranslationResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TranslationResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) request_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_string;
@property (T@"NSArray",R,N) n_best_translated_phrases;
@property (T@"NSString",R,N) engine_input;
@property (T@"NSArray",R,N) engine_output;
@property (T@"NSString",R,N) sequence_id;
@property (TB,R,N) final_message;
```

## Instance methods

```
-[QSSTranslationResponse copyWithZone:];
-[QSSTranslationResponse addObjectToBuffer:];
-[QSSTranslationResponse flatbuffData];
-[QSSTranslationResponse initAndVerifyWithFlatbuffData:];
-[QSSTranslationResponse initWithFlatbuffData:];
-[QSSTranslationResponse initWithFlatbuffData:root:];
-[QSSTranslationResponse initWithFlatbuffData:root:verify:];
-[QSSTranslationResponse speech_id];
-[QSSTranslationResponse engine_input];
-[QSSTranslationResponse engine_output];
-[QSSTranslationResponse final_message];
-[QSSTranslationResponse n_best_translated_phrases];
-[QSSTranslationResponse request_id];
-[QSSTranslationResponse return_code];
-[QSSTranslationResponse return_string];
-[QSSTranslationResponse sequence_id];
```
