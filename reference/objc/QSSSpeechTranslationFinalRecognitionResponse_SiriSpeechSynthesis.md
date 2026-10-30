# `QSSSpeechTranslationFinalRecognitionResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SpeechTranslationFinalRecognitionResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) conversation_id;
@property (T@"NSString",R,N) request_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (T@"NSString",R,N) source_locale;
@property (T@"NSString",R,N) recognition_text;
@property (T@"QSSRecognitionResult",R,N) recognition_result;
```

## Instance methods

```
-[QSSSpeechTranslationFinalRecognitionResponse copyWithZone:];
-[QSSSpeechTranslationFinalRecognitionResponse addObjectToBuffer:];
-[QSSSpeechTranslationFinalRecognitionResponse flatbuffData];
-[QSSSpeechTranslationFinalRecognitionResponse initAndVerifyWithFlatbuffData:];
-[QSSSpeechTranslationFinalRecognitionResponse initWithFlatbuffData:];
-[QSSSpeechTranslationFinalRecognitionResponse initWithFlatbuffData:root:];
-[QSSSpeechTranslationFinalRecognitionResponse initWithFlatbuffData:root:verify:];
-[QSSSpeechTranslationFinalRecognitionResponse conversation_id];
-[QSSSpeechTranslationFinalRecognitionResponse recognition_result];
-[QSSSpeechTranslationFinalRecognitionResponse recognition_text];
-[QSSSpeechTranslationFinalRecognitionResponse request_id];
-[QSSSpeechTranslationFinalRecognitionResponse return_code];
-[QSSSpeechTranslationFinalRecognitionResponse return_str];
-[QSSSpeechTranslationFinalRecognitionResponse source_locale];
```
