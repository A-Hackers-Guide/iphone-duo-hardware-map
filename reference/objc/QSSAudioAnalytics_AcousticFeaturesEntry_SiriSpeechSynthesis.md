# `QSSAudioAnalytics_AcousticFeaturesEntry`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{AcousticFeaturesEntry=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) key;
@property (T@"QSSAcousticFeature",R,N) value;
```

## Instance methods

```
-[QSSAudioAnalytics_AcousticFeaturesEntry value];
-[QSSAudioAnalytics_AcousticFeaturesEntry copyWithZone:];
-[QSSAudioAnalytics_AcousticFeaturesEntry key];
-[QSSAudioAnalytics_AcousticFeaturesEntry addObjectToBuffer:];
-[QSSAudioAnalytics_AcousticFeaturesEntry flatbuffData];
-[QSSAudioAnalytics_AcousticFeaturesEntry initAndVerifyWithFlatbuffData:];
-[QSSAudioAnalytics_AcousticFeaturesEntry initWithFlatbuffData:];
-[QSSAudioAnalytics_AcousticFeaturesEntry initWithFlatbuffData:root:];
-[QSSAudioAnalytics_AcousticFeaturesEntry initWithFlatbuffData:root:verify:];
```
