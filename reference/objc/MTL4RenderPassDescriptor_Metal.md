# `MTL4RenderPassDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 15 properties, 43 instance methods, 0 class methods

## Instance variables

```
{MTLRenderPassDescriptorPrivate="attachments"@"MTLRenderPassColorAttachmentDescriptorArrayInternal""visibilityResultBuffer"@"<MTLBuffer>""renderTargetWidth"Q"renderTargetHeight"Q"defaultColorSampleCount"Q"fineGrainedBackgroundVisibilityEnabled"B"skipEmptyTilesOnClearEnabled"B"ditherEnabled"B"openGLModeEnabled"B"renderTargetArrayLength"Q"tileWidth"Q"tileHeight"Q""(?="defaultSampleCount"Q"defaultRasterSampleCount"Q)"imageBlockSampleLength"Q"threadgroupMemoryLength"Q"customSamplePositions"[8{?="x"f"y"f}]"numCustomSamplePositions"Q"rasterizationRateMap"@"<MTLRasterizationRateMap>""sampleBufferAttachments"@"MTLRenderPassSampleBufferAttachmentDescriptorArrayInternal""pointCoordYFlipEnabled"B"visibilityResultType"q"supportColorAttachmentMapping"B"useExplicitRenderTargetDimensions"B} _private;
```

## Properties

```
@property (T@"MTLRenderPassColorAttachmentDescriptorArray",R) colorAttachments;
@property (T@"MTLRenderPassDepthAttachmentDescriptor",C,N) depthAttachment;
@property (T@"MTLRenderPassStencilAttachmentDescriptor",C,N) stencilAttachment;
@property (TQ,N) renderTargetArrayLength;
@property (TQ,N) imageblockSampleLength;
@property (TQ,N) threadgroupMemoryLength;
@property (TQ,N) tileWidth;
@property (TQ,N) tileHeight;
@property (TQ,N) defaultRasterSampleCount;
@property (TQ,N) renderTargetWidth;
@property (TQ,N) renderTargetHeight;
@property (T@"<MTLRasterizationRateMap>",&,N) rasterizationRateMap;
@property (T@"<MTLBuffer>",&,N) visibilityResultBuffer;
@property (Tq,N) visibilityResultType;
@property (TB,N) supportColorAttachmentMapping;
```

## Instance methods

```
-[MTL4RenderPassDescriptor renderTargetHeight];
-[MTL4RenderPassDescriptor colorAttachments];
-[MTL4RenderPassDescriptor setRenderTargetArrayLength:];
-[MTL4RenderPassDescriptor stencilAttachment];
-[MTL4RenderPassDescriptor setUseExplicitRenderTargetDimensions:];
-[MTL4RenderPassDescriptor imageblockSampleLength];
-[MTL4RenderPassDescriptor renderTargetArrayLength];
-[MTL4RenderPassDescriptor setVisibilityResultType:];
-[MTL4RenderPassDescriptor init];
-[MTL4RenderPassDescriptor defaultRasterSampleCount];
-[MTL4RenderPassDescriptor dealloc];
-[MTL4RenderPassDescriptor useExplicitRenderTargetDimensions];
-[MTL4RenderPassDescriptor visibilityResultBuffer];
-[MTL4RenderPassDescriptor setThreadgroupMemoryLength:];
-[MTL4RenderPassDescriptor setSamplePositions:count:];
-[MTL4RenderPassDescriptor validate:width:height:];
-[MTL4RenderPassDescriptor setTileWidth:];
-[MTL4RenderPassDescriptor setRenderTargetWidth:];
-[MTL4RenderPassDescriptor defaultColorSampleCount];
-[MTL4RenderPassDescriptor _descriptorPrivate];
-[MTL4RenderPassDescriptor tileHeight];
-[MTL4RenderPassDescriptor tileWidth];
-[MTL4RenderPassDescriptor setVisibilityResultBuffer:];
-[MTL4RenderPassDescriptor validate:width:height:hasOverriddenRenderTargetDimension:];
-[MTL4RenderPassDescriptor setSupportColorAttachmentMapping:];
-[MTL4RenderPassDescriptor setDepthAttachment:];
-[MTL4RenderPassDescriptor hash];
-[MTL4RenderPassDescriptor threadgroupMemoryLength];
-[MTL4RenderPassDescriptor depthAttachment];
-[MTL4RenderPassDescriptor setStencilAttachment:];
-[MTL4RenderPassDescriptor setTileHeight:];
-[MTL4RenderPassDescriptor setDefaultRasterSampleCount:];
-[MTL4RenderPassDescriptor setRasterizationRateMap:];
-[MTL4RenderPassDescriptor setImageblockSampleLength:];
-[MTL4RenderPassDescriptor copyWithZone:];
-[MTL4RenderPassDescriptor renderTargetWidth];
-[MTL4RenderPassDescriptor isEqual:];
-[MTL4RenderPassDescriptor supportColorAttachmentMapping];
-[MTL4RenderPassDescriptor setDefaultColorSampleCount:];
-[MTL4RenderPassDescriptor rasterizationRateMap];
-[MTL4RenderPassDescriptor setRenderTargetHeight:];
-[MTL4RenderPassDescriptor getSamplePositions:count:];
-[MTL4RenderPassDescriptor visibilityResultType];
```
