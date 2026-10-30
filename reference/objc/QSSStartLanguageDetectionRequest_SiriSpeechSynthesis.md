# `QSSStartLanguageDetectionRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{StartLanguageDetectionRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSArray",R,N) locales;
@property (Tq,R,N) codec;
```

## Instance methods

```
-[QSSStartLanguageDetectionRequest locales];
-[QSSStartLanguageDetectionRequest codec];
-[QSSStartLanguageDetectionRequest copyWithZone:];
-[QSSStartLanguageDetectionRequest addObjectToBuffer:];
-[QSSStartLanguageDetectionRequest flatbuffData];
-[QSSStartLanguageDetectionRequest initAndVerifyWithFlatbuffData:];
-[QSSStartLanguageDetectionRequest initWithFlatbuffData:];
-[QSSStartLanguageDetectionRequest initWithFlatbuffData:root:];
-[QSSStartLanguageDetectionRequest initWithFlatbuffData:root:verify:];
-[QSSStartLanguageDetectionRequest session_id];
-[QSSStartLanguageDetectionRequest speech_id];
```
