# `QSSTextNormalizationResponse`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextNormalizationResponse=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSArray",R,N) tokens;
@property (Ti,R,N) error_code;
@property (T@"NSString",R,N) error_str;
```

## Instance methods

```
-[QSSTextNormalizationResponse tokens];
-[QSSTextNormalizationResponse copyWithZone:];
-[QSSTextNormalizationResponse addObjectToBuffer:];
-[QSSTextNormalizationResponse error_code];
-[QSSTextNormalizationResponse error_str];
-[QSSTextNormalizationResponse flatbuffData];
-[QSSTextNormalizationResponse initAndVerifyWithFlatbuffData:];
-[QSSTextNormalizationResponse initWithFlatbuffData:];
-[QSSTextNormalizationResponse initWithFlatbuffData:root:];
-[QSSTextNormalizationResponse initWithFlatbuffData:root:verify:];
-[QSSTextNormalizationResponse session_id];
-[QSSTextNormalizationResponse speech_id];
```
