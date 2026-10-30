# `MTLIndirectCommandBufferSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLIndirectCommandBuffer`
- 0 instance variables, 5 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TQ,R) uniqueIdentifier;
@property (TQ,R) storageMode;
@property (TQ,?,R,N) gpuAddress;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,R) gpuHandle;
```

## Instance methods

```
-[MTLIndirectCommandBufferSPI storageMode];
-[MTLIndirectCommandBufferSPI uniqueIdentifier];
-[MTLIndirectCommandBufferSPI gpuHandle];
-[MTLIndirectCommandBufferSPI getHeader:headerSize:];
-[MTLIndirectCommandBufferSPI resourceIndex];
-[MTLIndirectCommandBufferSPI gpuAddress];
```
