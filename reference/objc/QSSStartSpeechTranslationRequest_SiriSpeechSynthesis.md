# `QSSStartSpeechTranslationRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 10 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StartSpeechTranslationRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) conversation_id;
@property (T@"NSString",R,N) request_id;
@property (T@"NSArray",R,N) translation_locale_pairs;
@property (T@"QSSStartSpeechRequest",R,N) start_speech_request;
@property (T@"QSSTranslationRequest",R,N) translation_request;
@property (T@"NSArray",R,N) text_to_speech_requests;
@property (TB,R,N) restricted_mode;
@property (T@"NSString",R,N) app_id;
@property (Tq,R,N) opt_in_status;
@property (TB,R,N) streaming_mode;
```

## Instance methods

```
-[QSSStartSpeechTranslationRequest copyWithZone:];
-[QSSStartSpeechTranslationRequest addObjectToBuffer:];
-[QSSStartSpeechTranslationRequest app_id];
-[QSSStartSpeechTranslationRequest flatbuffData];
-[QSSStartSpeechTranslationRequest initAndVerifyWithFlatbuffData:];
-[QSSStartSpeechTranslationRequest initWithFlatbuffData:];
-[QSSStartSpeechTranslationRequest initWithFlatbuffData:root:];
-[QSSStartSpeechTranslationRequest initWithFlatbuffData:root:verify:];
-[QSSStartSpeechTranslationRequest conversation_id];
-[QSSStartSpeechTranslationRequest restricted_mode];
-[QSSStartSpeechTranslationRequest opt_in_status];
-[QSSStartSpeechTranslationRequest request_id];
-[QSSStartSpeechTranslationRequest start_speech_request];
-[QSSStartSpeechTranslationRequest streaming_mode];
-[QSSStartSpeechTranslationRequest text_to_speech_requests];
-[QSSStartSpeechTranslationRequest translation_locale_pairs];
-[QSSStartSpeechTranslationRequest translation_request];
```
