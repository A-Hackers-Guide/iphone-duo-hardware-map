# `MTLGPUDebugBlitCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsBlitCommandEncoder`
- Protocols: `MTLGPUDebugCommandEncoder`
- 1 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
I _encoderID;
```

## Properties

```
@property (TI,R,V_encoderID) encoderID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLGPUDebugBlitCommandEncoder optimizeIndirectCommandBuffer:withRange:];
-[MTLGPUDebugBlitCommandEncoder copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:];
-[MTLGPUDebugBlitCommandEncoder copyFromInternalBuffer:sourceOffset:toInternalBuffer:destinationOffset:size:];
-[MTLGPUDebugBlitCommandEncoder encoderID];
-[MTLGPUDebugBlitCommandEncoder initWithBlitCommandEncoder:parent:descriptor:encoderID:];
-[MTLGPUDebugBlitCommandEncoder temporaryBufferWithBytes:length:];
-[MTLGPUDebugBlitCommandEncoder temporaryBufferWithLength:];
```
