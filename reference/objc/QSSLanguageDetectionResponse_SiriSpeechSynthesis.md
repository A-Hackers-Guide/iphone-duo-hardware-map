# `QSSLanguageDetectionResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{LanguageDetectionResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_string;
@property (T@"NSString",R,N) detected_locale;
@property (T@"NSArray",R,N) predictions;
```

## Instance methods

```
-[QSSLanguageDetectionResponse predictions];
-[QSSLanguageDetectionResponse copyWithZone:];
-[QSSLanguageDetectionResponse addObjectToBuffer:];
-[QSSLanguageDetectionResponse flatbuffData];
-[QSSLanguageDetectionResponse initAndVerifyWithFlatbuffData:];
-[QSSLanguageDetectionResponse initWithFlatbuffData:];
-[QSSLanguageDetectionResponse initWithFlatbuffData:root:];
-[QSSLanguageDetectionResponse initWithFlatbuffData:root:verify:];
-[QSSLanguageDetectionResponse session_id];
-[QSSLanguageDetectionResponse speech_id];
-[QSSLanguageDetectionResponse detected_locale];
-[QSSLanguageDetectionResponse return_code];
-[QSSLanguageDetectionResponse return_string];
```
