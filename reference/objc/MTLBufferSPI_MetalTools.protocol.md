# `MTLBufferSPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLResourceSPI`, `MTLBuffer`
- 0 instance variables, 4 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T^{__IOSurface=},R) iosurface;
@property (TQ,?,R,N) resourceIndex;
@property (TQ,?,N) parentGPUAddress;
@property (TQ,?,N) parentGPUSize;
```

## Instance methods

```
-[MTLBufferSPI didModifyRange:];
-[MTLBufferSPI iosurface];
-[MTLBufferSPI _aneIOSurface];
-[MTLBufferSPI newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:];
-[MTLBufferSPI replaceBackingWithBytesNoCopy:length:deallocator:];
-[MTLBufferSPI resourceIndex];
-[MTLBufferSPI detachBacking];
-[MTLBufferSPI replaceBackingWithRanges:readOnly:];
-[MTLBufferSPI parentGPUAddress];
-[MTLBufferSPI setParentGPUSize:];
-[MTLBufferSPI setParentGPUAddress:];
-[MTLBufferSPI parentGPUSize];
```
