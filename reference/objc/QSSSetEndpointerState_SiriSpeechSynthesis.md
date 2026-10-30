# `QSSSetEndpointerState`

- Image: [`/System/Library/PrivateFrameworks/SiriSpeechSynthesis.framework/SiriSpeechSynthesis`](../userland/System__Library__PrivateFrameworks__SiriSpeechSynthesis.framework__SiriSpeechSynthesis.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FLTBFBufferAccessor`, `NSCopying`
- 3 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _storage;
@"NSData" _data;
r^{SetEndpointerState=[1C]} _root;
```

## Properties

```
@property (TB,R,N) enable_server_side_endpoint;
```

## Instance methods

```
-[QSSSetEndpointerState copyWithZone:];
-[QSSSetEndpointerState addObjectToBuffer:];
-[QSSSetEndpointerState flatbuffData];
-[QSSSetEndpointerState initAndVerifyWithFlatbuffData:];
-[QSSSetEndpointerState initWithFlatbuffData:];
-[QSSSetEndpointerState initWithFlatbuffData:root:];
-[QSSSetEndpointerState initWithFlatbuffData:root:verify:];
-[QSSSetEndpointerState enable_server_side_endpoint];
```
