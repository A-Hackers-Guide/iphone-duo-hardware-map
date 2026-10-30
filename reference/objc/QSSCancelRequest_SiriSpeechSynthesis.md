# `QSSCancelRequest`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{CancelRequest=[1C]} _root;
```

## Properties

```
@property (T@"NSString",R,N) speech_id;
@property (T@"NSString",R,N) session_id;
@property (T@"NSString",R,N) reason;
```

## Instance methods

```
-[QSSCancelRequest reason];
-[QSSCancelRequest copyWithZone:];
-[QSSCancelRequest addObjectToBuffer:];
-[QSSCancelRequest flatbuffData];
-[QSSCancelRequest initAndVerifyWithFlatbuffData:];
-[QSSCancelRequest initWithFlatbuffData:];
-[QSSCancelRequest initWithFlatbuffData:root:];
-[QSSCancelRequest initWithFlatbuffData:root:verify:];
-[QSSCancelRequest session_id];
-[QSSCancelRequest speech_id];
```
