# `MTLCommandBuffer` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 12 properties, 39 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"<MTLCommandQueue>",R) commandQueue;
@property (TB,R) retainedReferences;
@property (TQ,R) errorOptions;
@property (T@"NSString",C) label;
@property (Td,R) kernelStartTime;
@property (Td,R) kernelEndTime;
@property (T@"<MTLLogContainer>",R) logs;
@property (Td,R) GPUStartTime;
@property (Td,R) GPUEndTime;
@property (TQ,R) status;
@property (T@"NSError",R) error;
```

## Instance methods

```
-[MTLCommandBuffer GPUEndTime];
-[MTLCommandBuffer presentDrawable:afterMinimumDuration:];
-[MTLCommandBuffer addCompletedHandler:];
-[MTLCommandBuffer waitUntilScheduled];
-[MTLCommandBuffer errorOptions];
-[MTLCommandBuffer blitCommandEncoderWithDescriptor:];
-[MTLCommandBuffer waitUntilCompleted];
-[MTLCommandBuffer pushDebugGroup:];
-[MTLCommandBuffer useResidencySet:];
-[MTLCommandBuffer addScheduledHandler:];
-[MTLCommandBuffer computeCommandEncoderWithDispatchType:];
-[MTLCommandBuffer resourceStateCommandEncoderWithDescriptor:];
-[MTLCommandBuffer enqueue];
-[MTLCommandBuffer kernelStartTime];
-[MTLCommandBuffer commit];
-[MTLCommandBuffer presentDrawable:];
-[MTLCommandBuffer retainedReferences];
-[MTLCommandBuffer computeCommandEncoderWithDescriptor:];
-[MTLCommandBuffer useResidencySets:count:];
-[MTLCommandBuffer logs];
-[MTLCommandBuffer presentDrawable:atTime:];
-[MTLCommandBuffer popDebugGroup];
-[MTLCommandBuffer GPUStartTime];
-[MTLCommandBuffer accelerationStructureCommandEncoderWithDescriptor:];
-[MTLCommandBuffer kernelEndTime];
-[MTLCommandBuffer accelerationStructureCommandEncoder];
-[MTLCommandBuffer encodeSignalEvent:value:];
-[MTLCommandBuffer device];
-[MTLCommandBuffer computeCommandEncoder];
-[MTLCommandBuffer label];
-[MTLCommandBuffer setLabel:];
-[MTLCommandBuffer status];
-[MTLCommandBuffer error];
-[MTLCommandBuffer commandQueue];
-[MTLCommandBuffer encodeWaitForEvent:value:];
-[MTLCommandBuffer blitCommandEncoder];
-[MTLCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTLCommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[MTLCommandBuffer resourceStateCommandEncoder];
```
