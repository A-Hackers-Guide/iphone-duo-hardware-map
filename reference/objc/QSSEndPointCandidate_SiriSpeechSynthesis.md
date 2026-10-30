# `QSSEndPointCandidate`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{EndPointCandidate=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (Ti,R,N) end_point_likelihood;
@property (Ti,R,N) processed_audio_duration_ms;
```

## Instance methods

```
-[QSSEndPointCandidate copyWithZone:];
-[QSSEndPointCandidate addObjectToBuffer:];
-[QSSEndPointCandidate flatbuffData];
-[QSSEndPointCandidate initAndVerifyWithFlatbuffData:];
-[QSSEndPointCandidate initWithFlatbuffData:];
-[QSSEndPointCandidate initWithFlatbuffData:root:];
-[QSSEndPointCandidate initWithFlatbuffData:root:verify:];
-[QSSEndPointCandidate session_id];
-[QSSEndPointCandidate speech_id];
-[QSSEndPointCandidate end_point_likelihood];
-[QSSEndPointCandidate processed_audio_duration_ms];
-[QSSEndPointCandidate return_code];
-[QSSEndPointCandidate return_str];
```
