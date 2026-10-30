# `QSSSpeechTranslationPartialRecognitionResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SpeechTranslationPartialRecognitionResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) conversation_id;
@property (T@"NSString",R,N) request_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSString",R,N) source_locale;
@property (T@"NSString",R,N) recognition_text;
@property (Ti,R,N) confidence;
@property (TB,R,N) is_stable_result;
```

## Instance methods

```
-[QSSSpeechTranslationPartialRecognitionResponse copyWithZone:];
-[QSSSpeechTranslationPartialRecognitionResponse confidence];
-[QSSSpeechTranslationPartialRecognitionResponse addObjectToBuffer:];
-[QSSSpeechTranslationPartialRecognitionResponse flatbuffData];
-[QSSSpeechTranslationPartialRecognitionResponse initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationPartialRecognitionResponse initWithFlatbuffData:];
-[QSSSpeechTranslationPartialRecognitionResponse initWithFlatbuffData:root:];
-[QSSSpeechTranslationPartialRecognitionResponse initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationPartialRecognitionResponse conversation_id];
-[QSSSpeechTranslationPartialRecognitionResponse is_stable_result];
-[QSSSpeechTranslationPartialRecognitionResponse recognition_text];
-[QSSSpeechTranslationPartialRecognitionResponse request_id];
-[QSSSpeechTranslationPartialRecognitionResponse return_code];
-[QSSSpeechTranslationPartialRecognitionResponse return_str];
-[QSSSpeechTranslationPartialRecognitionResponse source_locale];
```
