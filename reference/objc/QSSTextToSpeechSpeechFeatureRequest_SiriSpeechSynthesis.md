# `QSSTextToSpeechSpeechFeatureRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{TextToSpeechSpeechFeatureRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"QSSTextToSpeechSpeechFeatureModelIdentifier",R,N) model_id;
@property (T@"QSSTextToSpeechSpeechFeatureInputText",R,N) text;
@property (T@"QSSTextToSpeechSpeechFeatureInputWave",R,N) wave_data;
```

## Instance methods

```
-[QSSTextToSpeechSpeechFeatureRequest text];
-[QSSTextToSpeechSpeechFeatureRequest copyWithZone:];
-[QSSTextToSpeechSpeechFeatureRequest addObjectToBuffer:];
-[QSSTextToSpeechSpeechFeatureRequest flatbuffData];
-[QSSTextToSpeechSpeechFeatureRequest initAndVerifyWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureRequest initWithFlatbuffData:];
-[QSSTextToSpeechSpeechFeatureRequest initWithFlatbuffData:root:];
-[QSSTextToSpeechSpeechFeatureRequest initWithFlatbuffData:root:verify:];
-[QSSTextToSpeechSpeechFeatureRequest session_id];
-[QSSTextToSpeechSpeechFeatureRequest speech_id];
-[QSSTextToSpeechSpeechFeatureRequest wave_data];
-[QSSTextToSpeechSpeechFeatureRequest model_id];
```
