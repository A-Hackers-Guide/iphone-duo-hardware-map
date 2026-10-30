# `MTLCountersCommandBuffer`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsCommandBuffer`
- 1 instance variables, 1 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"MTLCountersTraceCommandBuffer" _traceBuffer;
```

## Properties

```
@property (T@"MTLCountersTraceCommandBuffer",R,N,V_traceBuffer) traceBuffer;
```

## Instance methods

```
-[MTLCountersCommandBuffer waitUntilScheduled];
-[MTLCountersCommandBuffer blitCommandEncoderWithDescriptor:];
-[MTLCountersCommandBuffer waitUntilCompleted];
-[MTLCountersCommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLCountersCommandBuffer computeCommandEncoderWithDispatchType:];
-[MTLCountersCommandBuffer resourceStateCommandEncoderWithDescriptor:];
-[MTLCountersCommandBuffer sampledComputeCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLCountersCommandBuffer presentDrawable:];
-[MTLCountersCommandBuffer computeCommandEncoderWithDescriptor:];
-[MTLCountersCommandBuffer sampledBlitCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTLCountersCommandBuffer sampledBlitCommandEncoder:capacity:];
-[MTLCountersCommandBuffer sampledComputeCommandEncoderWithProgramInfoBuffer:capacity:];
-[MTLCountersCommandBuffer sampledComputeCommandEncoderWithDispatchType:programInfoBuffer:capacity:];
-[MTLCountersCommandBuffer presentDrawable:atTime:];
-[MTLCountersCommandBuffer computeCommandEncoder];
-[MTLCountersCommandBuffer dealloc];
-[MTLCountersCommandBuffer addPurgedResource:];
-[MTLCountersCommandBuffer addPurgedHeap:];
-[MTLCountersCommandBuffer blitCommandEncoder];
-[MTLCountersCommandBuffer renderCommandEncoderWithDescriptor:];
-[MTLCountersCommandBuffer parallelRenderCommandEncoderWithDescriptor:];
-[MTLCountersCommandBuffer resourceStateCommandEncoder];
-[MTLCountersCommandBuffer initWithCommandBuffer:commandQueue:descriptor:];
-[MTLCountersCommandBuffer traceBuffer];
```
