# `MTLTextureLayout` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TQ,R) size;
@property (TQ,R) alignment;
@property (T{?=QQQ},R) copyGranularity;
@property (T{?=[2Q]},R) watermark;
```

## Instance methods

```
-[MTLTextureLayout copyFromTextureMemory:textureSlice:textureLevel:textureRegion:toLinearBytes:linearOffset:linearBytesPerRow:linearBytesPerImage:];
-[MTLTextureLayout alignment];
-[MTLTextureLayout size];
-[MTLTextureLayout copyGranularity];
-[MTLTextureLayout finalizeTextureMemory:];
-[MTLTextureLayout copyFromLinearBytes:linearOffset:linearBytesPerRow:linearBytesPerImage:toTextureMemory:textureSlice:textureLevel:textureRegion:];
-[MTLTextureLayout watermark];
-[MTLTextureLayout initializeTextureMemory:];
```
