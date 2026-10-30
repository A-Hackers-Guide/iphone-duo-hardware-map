# `MTLIOHandleSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLIOFileHandle`
- 0 instance variables, 2 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) globalTraceObjectID;
@property (TI,?,R) vnioID;
```

## Instance methods

```
-[MTLIOHandleSPI globalTraceObjectID];
-[MTLIOHandleSPI decompress:size:offset:stagingBuffer:stagingBufferSize:];
-[MTLIOHandleSPI getHandleOffset:offset:];
-[MTLIOHandleSPI read:size:offset:stagingBuffer:stagingBufferSize:];
-[MTLIOHandleSPI read:size:offset:stagingBuffer:stagingBufferSize:needsDecompress:];
-[MTLIOHandleSPI readIntoStagingBuffer:offset:stagingBuffer:stagingBufferSize:];
-[MTLIOHandleSPI readIntoStagingBuffer:offset:stagingBuffer:stagingBufferSize:needsDecompress:];
-[MTLIOHandleSPI stagingBufferSize:offset:];
-[MTLIOHandleSPI vnioID];
```
