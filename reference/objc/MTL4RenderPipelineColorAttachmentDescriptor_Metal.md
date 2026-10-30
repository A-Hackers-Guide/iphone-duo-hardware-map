# `MTL4RenderPipelineColorAttachmentDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
Q _pixelFormat;
q _blendingState;
Q _sourceRGBBlendFactor;
Q _destinationRGBBlendFactor;
Q _rgbBlendOperation;
Q _sourceAlphaBlendFactor;
Q _destinationAlphaBlendFactor;
Q _alphaBlendOperation;
Q _writeMask;
```

## Properties

```
@property (TQ,N,V_pixelFormat) pixelFormat;
@property (Tq,N,V_blendingState) blendingState;
@property (TQ,N,V_sourceRGBBlendFactor) sourceRGBBlendFactor;
@property (TQ,N,V_destinationRGBBlendFactor) destinationRGBBlendFactor;
@property (TQ,N,V_rgbBlendOperation) rgbBlendOperation;
@property (TQ,N,V_sourceAlphaBlendFactor) sourceAlphaBlendFactor;
@property (TQ,N,V_destinationAlphaBlendFactor) destinationAlphaBlendFactor;
@property (TQ,N,V_alphaBlendOperation) alphaBlendOperation;
@property (TQ,N,V_writeMask) writeMask;
```

## Instance methods

```
-[MTL4RenderPipelineColorAttachmentDescriptor setRgbBlendOperation:];
-[MTL4RenderPipelineColorAttachmentDescriptor setDestinationRGBBlendFactor:];
-[MTL4RenderPipelineColorAttachmentDescriptor sourceRGBBlendFactor];
-[MTL4RenderPipelineColorAttachmentDescriptor init];
-[MTL4RenderPipelineColorAttachmentDescriptor rgbBlendOperation];
-[MTL4RenderPipelineColorAttachmentDescriptor setSourceAlphaBlendFactor:];
-[MTL4RenderPipelineColorAttachmentDescriptor reset];
-[MTL4RenderPipelineColorAttachmentDescriptor setAlphaBlendOperation:];
-[MTL4RenderPipelineColorAttachmentDescriptor alphaBlendOperation];
-[MTL4RenderPipelineColorAttachmentDescriptor setSourceRGBBlendFactor:];
-[MTL4RenderPipelineColorAttachmentDescriptor writeMask];
-[MTL4RenderPipelineColorAttachmentDescriptor destinationAlphaBlendFactor];
-[MTL4RenderPipelineColorAttachmentDescriptor setDestinationAlphaBlendFactor:];
-[MTL4RenderPipelineColorAttachmentDescriptor setWriteMask:];
-[MTL4RenderPipelineColorAttachmentDescriptor hash];
-[MTL4RenderPipelineColorAttachmentDescriptor pixelFormat];
-[MTL4RenderPipelineColorAttachmentDescriptor copyWithZone:];
-[MTL4RenderPipelineColorAttachmentDescriptor setPixelFormat:];
-[MTL4RenderPipelineColorAttachmentDescriptor isEqual:];
-[MTL4RenderPipelineColorAttachmentDescriptor destinationRGBBlendFactor];
-[MTL4RenderPipelineColorAttachmentDescriptor sourceAlphaBlendFactor];
-[MTL4RenderPipelineColorAttachmentDescriptor blendingState];
-[MTL4RenderPipelineColorAttachmentDescriptor setBlendingState:];
```
