# `MTLToolsTextureLayout`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLTextureLayout`
- 0 instance variables, 8 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TQ,R) size;
@property (TQ,R) alignment;
@property (T{?=QQQ},R) copyGranularity;
@property (T{?=[2Q]},R) watermark;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsTextureLayout copyFromTextureMemory:textureSlice:textureLevel:textureRegion:toLinearBytes:linearOffset:linearBytesPerRow:linearBytesPerImage:];
-[MTLToolsTextureLayout initializeTextureMemory:];
-[MTLToolsTextureLayout alignment];
-[MTLToolsTextureLayout size];
-[MTLToolsTextureLayout copyGranularity];
-[MTLToolsTextureLayout finalizeTextureMemory:];
-[MTLToolsTextureLayout copyFromLinearBytes:linearOffset:linearBytesPerRow:linearBytesPerImage:toTextureMemory:textureSlice:textureLevel:textureRegion:];
-[MTLToolsTextureLayout watermark];
```
