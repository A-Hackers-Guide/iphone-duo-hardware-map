# `QSSTranslationRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 15 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TranslationRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) request_id;
@property (T@"NSString",R,N) task;
@property (T@"NSString",R,N) source_language;
@property (T@"NSString",R,N) target_language;
@property (T@"NSArray",R,N) translation_phrase;
@property (T@"QSSSiriTranslationInfo",R,N) siri_translation_info;
@property (T@"QSSSpeechTranslationInfo",R,N) speech_translation_info;
@property (T@"QSSSiriPayloadTranslationInfo",R,N) siri_payload_translation_info;
@property (T@"NSString",R,N) sequence_id;
@property (T@"QSSWebTranslationInfo",R,N) web_translation_info;
@property (TB,R,N) disable_log;
@property (Tq,R,N) opt_in_status;
@property (T@"NSString",R,N) app_id;
@property (T@"NSString",R,N) use_case;
```

## Instance methods

```
-[QSSTranslationRequest task];
-[QSSTranslationRequest copyWithZone:];
-[QSSTranslationRequest addObjectToBuffer:];
-[QSSTranslationRequest app_id];
-[QSSTranslationRequest flatbuffData];
-[QSSTranslationRequest initAndVerifyWithFlatbuffData:];
-[QSSTranslationRequest initWithFlatbuffData:];
-[QSSTranslationRequest initWithFlatbuffData:root:];
-[QSSTranslationRequest initWithFlatbuffData:root:verify:];
-[QSSTranslationRequest speech_id];
-[QSSTranslationRequest source_language];
-[QSSTranslationRequest target_language];
-[QSSTranslationRequest disable_log];
-[QSSTranslationRequest opt_in_status];
-[QSSTranslationRequest request_id];
-[QSSTranslationRequest sequence_id];
-[QSSTranslationRequest siri_payload_translation_info];
-[QSSTranslationRequest siri_translation_info];
-[QSSTranslationRequest speech_translation_info];
-[QSSTranslationRequest translation_phrase];
-[QSSTranslationRequest use_case];
-[QSSTranslationRequest web_translation_info];
```
