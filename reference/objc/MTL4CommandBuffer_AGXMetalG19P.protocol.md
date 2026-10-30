# `MTL4CommandBuffer` (protocol)

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
```

## Instance methods

```
-[MTL4CommandBuffer pushDebugGroup:];
-[MTL4CommandBuffer useResidencySet:];
-[MTL4CommandBuffer useResidencySets:count:];
-[MTL4CommandBuffer popDebugGroup];
-[MTL4CommandBuffer device];
-[MTL4CommandBuffer computeCommandEncoder];
-[MTL4CommandBuffer label];
-[MTL4CommandBuffer setLabel:];
-[MTL4CommandBuffer renderCommandEncoderWithDescriptor:];
-[MTL4CommandBuffer writeTimestampIntoHeap:atIndex:];
-[MTL4CommandBuffer beginCommandBufferWithAllocator:];
-[MTL4CommandBuffer beginCommandBufferWithAllocator:options:];
-[MTL4CommandBuffer endCommandBuffer];
-[MTL4CommandBuffer machineLearningCommandEncoder];
-[MTL4CommandBuffer renderCommandEncoderWithDescriptor:options:];
-[MTL4CommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:];
```
