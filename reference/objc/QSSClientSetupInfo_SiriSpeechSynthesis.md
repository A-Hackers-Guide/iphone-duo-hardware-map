# `QSSClientSetupInfo`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{ClientSetupInfo=[1C]} _root;
```

## Properties

```
@property (Tf,R,N) endpoint_threshold;
@property (TB,R,N) endpoint_extra_delay;
@property (T@"NSString",R,N) speech_id;
```

## Instance methods

```
-[QSSClientSetupInfo copyWithZone:];
-[QSSClientSetupInfo addObjectToBuffer:];
-[QSSClientSetupInfo flatbuffData];
-[QSSClientSetupInfo initAndVerifyWithFlatbuffData:];
-[QSSClientSetupInfo initWithFlatbuffData:];
-[QSSClientSetupInfo initWithFlatbuffData:root:];
-[QSSClientSetupInfo initWithFlatbuffData:root:verify:];
-[QSSClientSetupInfo speech_id];
-[QSSClientSetupInfo endpoint_extra_delay];
-[QSSClientSetupInfo endpoint_threshold];
```
