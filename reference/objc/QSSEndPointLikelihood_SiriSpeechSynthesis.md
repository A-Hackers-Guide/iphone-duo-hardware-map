# `QSSEndPointLikelihood`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{EndPointLikelihood=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (Ti,R,N) return_code;
@property (T@"NSString",R,N) return_str;
@property (Ti,R,N) end_point_likelihood;
```

## Instance methods

```
-[QSSEndPointLikelihood copyWithZone:];
-[QSSEndPointLikelihood addObjectToBuffer:];
-[QSSEndPointLikelihood flatbuffData];
-[QSSEndPointLikelihood initAndVerifyWithFlatbuffData:];
-[QSSEndPointLikelihood initWithFlatbuffData:];
-[QSSEndPointLikelihood initWithFlatbuffData:root:];
-[QSSEndPointLikelihood initWithFlatbuffData:root:verify:];
-[QSSEndPointLikelihood session_id];
-[QSSEndPointLikelihood speech_id];
-[QSSEndPointLikelihood end_point_likelihood];
-[QSSEndPointLikelihood return_code];
-[QSSEndPointLikelihood return_str];
```
