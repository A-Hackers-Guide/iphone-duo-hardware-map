# `QSSTextToSpeechSpeechFeatureInputWave`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechSpeechFeatureInputWave=[1C]} _root;
```

## Properties

```
@property (Ti,R,N) sample_rate;
@property (T@"NSData",R,N) pcm_data;
```

## Instance methods

```
-[QSSTextToSpeechSpeechFeatureInputWave copyWithZone:];
-[QSSTextToSpeechSpeechFeatureInputWave addObjectToBuffer:];
-[QSSTextToSpeechSpeechFeatureInputWave flatbuffData];
-[QSSTextToSpeechSpeechFeatureInputWave initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureInputWave initWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureInputWave initWithFlatbuffData:root:];
-[QSSTextToSpeechSpeechFeatureInputWave initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechSpeechFeatureInputWave pcm_data];
-[QSSTextToSpeechSpeechFeatureInputWave pcm_data:];
-[QSSTextToSpeechSpeechFeatureInputWave sample_rate];
```
