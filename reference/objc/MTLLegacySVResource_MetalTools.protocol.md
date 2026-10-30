# `MTLLegacySVResource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResourceSPI`
- 0 instance variables, 4 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLResource>",R,N) baseObject;
@property (TQ,R,N) length;
@property (TQ,R,N) gpuAddress;
@property (TQ,R,N) underlyingGPUAddress;
```

## Instance methods

```
-[MTLLegacySVResource gpuAddress];
-[MTLLegacySVResource length];
-[MTLLegacySVResource baseObject];
-[MTLLegacySVResource handleForOffset:];
-[MTLLegacySVResource underlyingGPUAddress];
-[MTLLegacySVResource useWithComputeEncoder:usage:];
-[MTLLegacySVResource useWithRenderEncoder:usage:stages:];
```
