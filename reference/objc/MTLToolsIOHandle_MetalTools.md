# `MTLToolsIOHandle`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLIOHandleSPI`
- 0 instance variables, 7 properties, 14 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) globalTraceObjectID;
@property (TI,?,R) vnioID;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsIOHandle label];
-[MTLToolsIOHandle setLabel:];
-[MTLToolsIOHandle globalTraceObjectID];
-[MTLToolsIOHandle dealloc];
-[MTLToolsIOHandle length];
-[MTLToolsIOHandle decompress:size:offset:stagingBuffer:stagingBufferSize:];
-[MTLToolsIOHandle getHandleOffset:offset:];
-[MTLToolsIOHandle initWithBaseObject:parent:];
-[MTLToolsIOHandle read:size:offset:stagingBuffer:stagingBufferSize:];
-[MTLToolsIOHandle read:size:offset:stagingBuffer:stagingBufferSize:needsDecompress:];
-[MTLToolsIOHandle readIntoStagingBuffer:offset:stagingBuffer:stagingBufferSize:];
-[MTLToolsIOHandle readIntoStagingBuffer:offset:stagingBuffer:stagingBufferSize:needsDecompress:];
-[MTLToolsIOHandle stagingBufferSize:offset:];
-[MTLToolsIOHandle vnioID];
```
