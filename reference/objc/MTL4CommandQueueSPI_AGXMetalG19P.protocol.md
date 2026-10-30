# `MTL4CommandQueueSPI` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTL4CommandQueue`
- 0 instance variables, 2 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"<MTL4CommandBuffer>",R,N) lastCommittedCommandBuffer;
@property (TQ,R,N) lastCommittedCommandBufferGeneration;
```

## Instance methods

```
-[MTL4CommandQueueSPI setGPUPriority:];
-[MTL4CommandQueueSPI getBackgroundGPUPriority];
-[MTL4CommandQueueSPI getGPUPriority];
-[MTL4CommandQueueSPI setBackgroundGPUPriority:];
-[MTL4CommandQueueSPI lastCommittedCommandBuffer];
-[MTL4CommandQueueSPI lastCommittedCommandBufferGeneration];
```
