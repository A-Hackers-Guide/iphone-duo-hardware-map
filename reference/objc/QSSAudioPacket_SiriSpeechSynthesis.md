# `QSSAudioPacket`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{AudioPacket=[1C]} _root;
```

## Properties

```
@property (T@"NSData",R,N) audio_bytes;
```

## Instance methods

```
-[QSSAudioPacket copyWithZone:];
-[QSSAudioPacket addObjectToBuffer:];
-[QSSAudioPacket flatbuffData];
-[QSSAudioPacket initAndVerifyWithFlatbuffData:];
-[QSSAudioPacket initWithFlatbuffData:];
-[QSSAudioPacket initWithFlatbuffData:root:];
-[QSSAudioPacket initWithFlatbuffData:root:verify:];
-[QSSAudioPacket audio_bytes];
-[QSSAudioPacket audio_bytes:];
```
