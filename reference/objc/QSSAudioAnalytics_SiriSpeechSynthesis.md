# `QSSAudioAnalytics`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{AudioAnalytics=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) speech_recognition_features;
@property (T@"NSArray",R,N) acoustic_features;
```

## Instance methods

```
-[QSSAudioAnalytics copyWithZone:];
-[QSSAudioAnalytics addObjectToBuffer:];
-[QSSAudioAnalytics flatbuffData];
-[QSSAudioAnalytics initAndVerifyWithFlatbuffData:];
-[QSSAudioAnalytics initWithFlatbuffData:];
-[QSSAudioAnalytics initWithFlatbuffData:root:];
-[QSSAudioAnalytics initWithFlatbuffData:root:verify:];
-[QSSAudioAnalytics acoustic_features];
-[QSSAudioAnalytics speech_recognition_features];
```
