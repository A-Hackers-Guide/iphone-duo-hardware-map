# `QSSTextToSpeechSpeechFeatureOutputFeature`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechSpeechFeatureOutputFeature=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) phone_name;
@property (Tf,R,N) begin_time;
@property (Tf,R,N) end_time;
@property (Tf,R,N) duration;
@property (Tf,R,N) pitch;
@property (Tf,R,N) energy;
```

## Instance methods

```
-[QSSTextToSpeechSpeechFeatureOutputFeature pitch];
-[QSSTextToSpeechSpeechFeatureOutputFeature energy];
-[QSSTextToSpeechSpeechFeatureOutputFeature duration];
-[QSSTextToSpeechSpeechFeatureOutputFeature copyWithZone:];
-[QSSTextToSpeechSpeechFeatureOutputFeature addObjectToBuffer:];
-[QSSTextToSpeechSpeechFeatureOutputFeature flatbuffData];
-[QSSTextToSpeechSpeechFeatureOutputFeature initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureOutputFeature initWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureOutputFeature initWithFlatbuffData:root:];
-[QSSTextToSpeechSpeechFeatureOutputFeature initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechSpeechFeatureOutputFeature begin_time];
-[QSSTextToSpeechSpeechFeatureOutputFeature end_time];
-[QSSTextToSpeechSpeechFeatureOutputFeature phone_name];
```
