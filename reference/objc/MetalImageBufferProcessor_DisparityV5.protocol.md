# `MetalImageBufferProcessor` (protocol)

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `ImageBufferProcessor`
- 0 instance variables, 3 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLCommandQueue>",&,N) metalCommandQueue;
@property (TB,?,R,N) supportsExternalMemoryResource;
@property (T@"CMIExternalMemoryResource",?,&,N) externalMemoryResource;
```

## Instance methods

```
-[MetalImageBufferProcessor setMetalCommandQueue:];
-[MetalImageBufferProcessor metalCommandQueue];
-[MetalImageBufferProcessor externalMemoryResource];
-[MetalImageBufferProcessor supportsExternalMemoryResource];
-[MetalImageBufferProcessor setExternalMemoryResource:];
-[MetalImageBufferProcessor externalMemoryDescriptorForConfiguration:];
```
