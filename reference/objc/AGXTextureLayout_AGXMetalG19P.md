# `AGXTextureLayout`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOGPUMetalTextureLayout`
- Protocols: `MTLTextureLayout`
- 1 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
^v _impl;
```

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
-[AGXTextureLayout copyFromTextureMemory:textureSlice:textureLevel:textureRegion:toLinearBytes:linearOffset:linearBytesPerRow:linearBytesPerImage:];
-[AGXTextureLayout initializeTextureMemory:];
-[AGXTextureLayout dealloc];
-[AGXTextureLayout alignment];
-[AGXTextureLayout size];
-[AGXTextureLayout copyGranularity];
-[AGXTextureLayout finalizeTextureMemory:];
-[AGXTextureLayout copyFromLinearBytes:linearOffset:linearBytesPerRow:linearBytesPerImage:toTextureMemory:textureSlice:textureLevel:textureRegion:];
-[AGXTextureLayout watermark];
-[AGXTextureLayout initWithDevice:descriptor:isHeapOrBufferBacked:];
```
