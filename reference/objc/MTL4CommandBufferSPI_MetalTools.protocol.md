# `MTL4CommandBufferSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4CommandBuffer`
- 0 instance variables, 1 properties, 4 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) currentGeneration;
```

## Instance methods

```
-[MTL4CommandBufferSPI sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[MTL4CommandBufferSPI currentGeneration];
-[MTL4CommandBufferSPI resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:];
-[MTL4CommandBufferSPI sampledComputeCommandEncoder:capacity:];
```
