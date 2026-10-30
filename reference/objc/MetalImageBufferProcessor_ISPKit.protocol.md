# `MetalImageBufferProcessor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
