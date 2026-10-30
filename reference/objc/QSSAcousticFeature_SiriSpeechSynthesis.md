# `QSSAcousticFeature`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{AcousticFeature=[1C]} _root;
```

## Properties

```
@property (T@"NSArray",R,N) acoustic_feature_per_frame;
@property (Tf,R,N) frame_duration;
```

## Instance methods

```
-[QSSAcousticFeature copyWithZone:];
-[QSSAcousticFeature addObjectToBuffer:];
-[QSSAcousticFeature flatbuffData];
-[QSSAcousticFeature initAndVerifyWithFlatbuffData:];
-[QSSAcousticFeature initWithFlatbuffData:];
-[QSSAcousticFeature initWithFlatbuffData:root:];
-[QSSAcousticFeature initWithFlatbuffData:root:verify:];
-[QSSAcousticFeature acoustic_feature_per_frame];
-[QSSAcousticFeature frame_duration];
```
