# `QSSTextToSpeechSpeechFeatureResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechSpeechFeatureResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
@property (T@"NSArray",R,N) features;
```

## Instance methods

```
-[QSSTextToSpeechSpeechFeatureResponse features];
-[QSSTextToSpeechSpeechFeatureResponse copyWithZone:];
-[QSSTextToSpeechSpeechFeatureResponse addObjectToBuffer:];
-[QSSTextToSpeechSpeechFeatureResponse error_code];
-[QSSTextToSpeechSpeechFeatureResponse error_str];
-[QSSTextToSpeechSpeechFeatureResponse flatbuffData];
-[QSSTextToSpeechSpeechFeatureResponse initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureResponse initWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureResponse initWithFlatbuffData:root:];
-[QSSTextToSpeechSpeechFeatureResponse initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechSpeechFeatureResponse session_id];
-[QSSTextToSpeechSpeechFeatureResponse speech_id];
```
