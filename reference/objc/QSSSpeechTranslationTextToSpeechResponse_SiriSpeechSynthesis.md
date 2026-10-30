# `QSSSpeechTranslationTextToSpeechResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SpeechTranslationTextToSpeechResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) conversation_id;
@property (T@"NSString",R,N) request_id;
@property (T@"NSString",R,N) target_locale;
@property (T@"QSSTextToSpeechResponse",R,N) text_to_speech_response;
```

## Instance methods

```
-[QSSSpeechTranslationTextToSpeechResponse copyWithZone:];
-[QSSSpeechTranslationTextToSpeechResponse addObjectToBuffer:];
-[QSSSpeechTranslationTextToSpeechResponse flatbuffData];
-[QSSSpeechTranslationTextToSpeechResponse initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationTextToSpeechResponse initWithFlatbuffData:];
-[QSSSpeechTranslationTextToSpeechResponse initWithFlatbuffData:root:];
-[QSSSpeechTranslationTextToSpeechResponse initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationTextToSpeechResponse conversation_id];
-[QSSSpeechTranslationTextToSpeechResponse request_id];
-[QSSSpeechTranslationTextToSpeechResponse target_locale];
-[QSSSpeechTranslationTextToSpeechResponse text_to_speech_response];
```
