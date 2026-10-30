# `_MTLCommandBufferEncoderInfo`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLCommandBufferEncoderInfo`
- 5 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
Q _uniqueID;
Q _globalTraceObjectID;
@"NSString" _label;
@"NSArray" _debugSignposts;
q _errorState;
```

## Properties

```
@property (TQ,N,V_uniqueID) uniqueID;
@property (TQ,N,V_globalTraceObjectID) globalTraceObjectID;
@property (T@"NSString",&,N,V_label) label;
@property (T@"NSArray",&,N,V_debugSignposts) debugSignposts;
@property (Tq,N,V_errorState) errorState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLCommandBufferEncoderInfo label];
-[_MTLCommandBufferEncoderInfo setLabel:];
-[_MTLCommandBufferEncoderInfo globalTraceObjectID];
-[_MTLCommandBufferEncoderInfo dealloc];
-[_MTLCommandBufferEncoderInfo uniqueID];
-[_MTLCommandBufferEncoderInfo setErrorState:];
-[_MTLCommandBufferEncoderInfo description];
-[_MTLCommandBufferEncoderInfo setUniqueID:];
-[_MTLCommandBufferEncoderInfo debugSignposts];
-[_MTLCommandBufferEncoderInfo errorState];
-[_MTLCommandBufferEncoderInfo setDebugSignposts:];
-[_MTLCommandBufferEncoderInfo setGlobalTraceObjectID:];
```
