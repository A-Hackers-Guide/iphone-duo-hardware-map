# `MPSCaptureCommandEncoder`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `MTLComputeCommandEncoder`
- 3 instance variables, 7 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<MTLComputeCommandEncoder>" _encoder;
@"MPSGraphCaptureContext" _captureContext;
^v _encoderContext;
```

## Properties

```
@property (TQ,R) dispatchType;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MPSCaptureCommandEncoder waitForFence:];
-[MPSCaptureCommandEncoder setBuffers:offsets:withRange:];
-[MPSCaptureCommandEncoder executeCommandsInBuffer:indirectBuffer:indirectBufferOffset:];
-[MPSCaptureCommandEncoder setBuffer:offset:atIndex:];
-[MPSCaptureCommandEncoder updateFence:];
-[MPSCaptureCommandEncoder executeCommandsInBuffer:withRange:];
-[MPSCaptureCommandEncoder memoryBarrierWithScope:];
-[MPSCaptureCommandEncoder dispatchThreadgroups:threadsPerThreadgroup:];
-[MPSCaptureCommandEncoder setTexture:atIndex:];
-[MPSCaptureCommandEncoder setSamplerState:atIndex:];
-[MPSCaptureCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:];
-[MPSCaptureCommandEncoder setBytes:length:atIndex:];
-[MPSCaptureCommandEncoder dealloc];
-[MPSCaptureCommandEncoder setThreadgroupMemoryLength:atIndex:];
-[MPSCaptureCommandEncoder setStageInRegion:];
-[MPSCaptureCommandEncoder setSamplerState:lodMinClamp:lodMaxClamp:atIndex:];
-[MPSCaptureCommandEncoder forwardingTargetForSelector:];
-[MPSCaptureCommandEncoder setStageInRegionWithIndirectBuffer:indirectBufferOffset:];
-[MPSCaptureCommandEncoder setBufferOffset:atIndex:];
-[MPSCaptureCommandEncoder dispatchThreads:threadsPerThreadgroup:];
-[MPSCaptureCommandEncoder setSamplerStates:withRange:];
-[MPSCaptureCommandEncoder setComputePipelineState:];
-[MPSCaptureCommandEncoder setTextures:withRange:];
-[MPSCaptureCommandEncoder memoryBarrierWithResources:count:];
-[MPSCaptureCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:];
-[MPSCaptureCommandEncoder initWithCommandEncoder:captureContext:];
```
