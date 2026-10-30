# `QSSTextNormalizationRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextNormalizationRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) language;
@property (T@"NSString",R,N) text;
@property (Ti,R,N) nbest_variants_max;
```

## Instance methods

```
-[QSSTextNormalizationRequest language];
-[QSSTextNormalizationRequest text];
-[QSSTextNormalizationRequest copyWithZone:];
-[QSSTextNormalizationRequest addObjectToBuffer:];
-[QSSTextNormalizationRequest flatbuffData];
-[QSSTextNormalizationRequest initAndVerifyWithFlatbuffData:];
-[QSSTextNormalizationRequest initWithFlatbuffData:];
-[QSSTextNormalizationRequest initWithFlatbuffData:root:];
-[QSSTextNormalizationRequest initWithFlatbuffData:root:verify:];
-[QSSTextNormalizationRequest session_id];
-[QSSTextNormalizationRequest speech_id];
-[QSSTextNormalizationRequest nbest_variants_max];
```
