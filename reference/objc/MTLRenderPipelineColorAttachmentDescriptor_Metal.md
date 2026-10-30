# `MTLRenderPipelineColorAttachmentDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 0 instance variables, 9 properties, 2 instance methods, 2 class methods

## Properties

```
@property (TQ,D,N) pixelFormat;
@property (TB,D,N,GisBlendingEnabled) blendingEnabled;
@property (TQ,D,N) sourceRGBBlendFactor;
@property (TQ,D,N) destinationRGBBlendFactor;
@property (TQ,D,N) rgbBlendOperation;
@property (TQ,D,N) sourceAlphaBlendFactor;
@property (TQ,D,N) destinationAlphaBlendFactor;
@property (TQ,D,N) alphaBlendOperation;
@property (TQ,D,N) writeMask;
```

## Class methods

```
+[MTLRenderPipelineColorAttachmentDescriptor allocWithZone:];
+[MTLRenderPipelineColorAttachmentDescriptor alloc];
```

## Instance methods

```
-[MTLRenderPipelineColorAttachmentDescriptor reset];
-[MTLRenderPipelineColorAttachmentDescriptor copyWithZone:];
```
