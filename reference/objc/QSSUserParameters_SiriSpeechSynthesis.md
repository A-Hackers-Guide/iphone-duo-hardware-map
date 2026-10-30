# `QSSUserParameters`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{UserParameters=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) fork_id;
```

## Instance methods

```
-[QSSUserParameters copyWithZone:];
-[QSSUserParameters addObjectToBuffer:];
-[QSSUserParameters flatbuffData];
-[QSSUserParameters initAndVerifyWithFlatbuffData:];
-[QSSUserParameters initWithFlatbuffData:];
-[QSSUserParameters initWithFlatbuffData:root:];
-[QSSUserParameters initWithFlatbuffData:root:verify:];
-[QSSUserParameters speech_id];
-[QSSUserParameters fork_id];
```
