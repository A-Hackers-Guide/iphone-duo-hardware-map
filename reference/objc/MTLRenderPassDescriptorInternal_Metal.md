# `MTLRenderPassDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLRenderPassDescriptor`
- 1 instance variables, 0 properties, 56 instance methods, 1 class methods

## Instance variables

```
{MTLRenderPassDescriptorPrivate="attachments"@"MTLRenderPassColorAttachmentDescriptorArrayInternal""visibilityResultBuffer"@"<MTLBuffer>""renderTargetWidth"Q"renderTargetHeight"Q"defaultColorSampleCount"Q"fineGrainedBackgroundVisibilityEnabled"B"skipEmptyTilesOnClearEnabled"B"ditherEnabled"B"openGLModeEnabled"B"renderTargetArrayLength"Q"tileWidth"Q"tileHeight"Q""(?="defaultSampleCount"Q"defaultRasterSampleCount"Q)"imageBlockSampleLength"Q"threadgroupMemoryLength"Q"customSamplePositions"[8{?="x"f"y"f}]"numCustomSamplePositions"Q"rasterizationRateMap"@"<MTLRasterizationRateMap>""sampleBufferAttachments"@"MTLRenderPassSampleBufferAttachmentDescriptorArrayInternal""pointCoordYFlipEnabled"B"visibilityResultType"q"supportColorAttachmentMapping"B"useExplicitRenderTargetDimensions"B} _private;
```

## Class methods

```
+[MTLRenderPassDescriptorInternal renderPassDescriptor];
```

## Instance methods

```
-[MTLRenderPassDescriptorInternal openGLModeEnabled];
-[MTLRenderPassDescriptorInternal setOpenGLModeEnabled:];
-[MTLRenderPassDescriptorInternal renderTargetHeight];
-[MTLRenderPassDescriptorInternal colorAttachments];
-[MTLRenderPassDescriptorInternal setRenderTargetArrayLength:];
-[MTLRenderPassDescriptorInternal stencilAttachment];
-[MTLRenderPassDescriptorInternal setUseExplicitRenderTargetDimensions:];
-[MTLRenderPassDescriptorInternal imageblockSampleLength];
-[MTLRenderPassDescriptorInternal renderTargetArrayLength];
-[MTLRenderPassDescriptorInternal setVisibilityResultType:];
-[MTLRenderPassDescriptorInternal formattedDescription:];
-[MTLRenderPassDescriptorInternal setSkipEmptyTilesOnClearEnabled:];
-[MTLRenderPassDescriptorInternal init];
-[MTLRenderPassDescriptorInternal sampleBufferAttachments];
-[MTLRenderPassDescriptorInternal defaultRasterSampleCount];
-[MTLRenderPassDescriptorInternal setDitherEnabled:];
-[MTLRenderPassDescriptorInternal dealloc];
-[MTLRenderPassDescriptorInternal setFineGrainedBackgroundVisibilityEnabled:];
-[MTLRenderPassDescriptorInternal useExplicitRenderTargetDimensions];
-[MTLRenderPassDescriptorInternal visibilityResultBuffer];
-[MTLRenderPassDescriptorInternal skipEmptyTilesOnClearEnabled];
-[MTLRenderPassDescriptorInternal setThreadgroupMemoryLength:];
-[MTLRenderPassDescriptorInternal setSamplePositions:count:];
-[MTLRenderPassDescriptorInternal validate:width:height:];
-[MTLRenderPassDescriptorInternal setTileWidth:];
-[MTLRenderPassDescriptorInternal setRenderTargetWidth:];
-[MTLRenderPassDescriptorInternal defaultColorSampleCount];
-[MTLRenderPassDescriptorInternal _descriptorPrivate];
-[MTLRenderPassDescriptorInternal tileHeight];
-[MTLRenderPassDescriptorInternal tileWidth];
-[MTLRenderPassDescriptorInternal fineGrainedBackgroundVisibilityEnabled];
-[MTLRenderPassDescriptorInternal setPointCoordYFlipEnabled:];
-[MTLRenderPassDescriptorInternal setVisibilityResultBuffer:];
-[MTLRenderPassDescriptorInternal validate:width:height:hasOverriddenRenderTargetDimension:];
-[MTLRenderPassDescriptorInternal setSupportColorAttachmentMapping:];
-[MTLRenderPassDescriptorInternal setDepthAttachment:];
-[MTLRenderPassDescriptorInternal hash];
-[MTLRenderPassDescriptorInternal threadgroupMemoryLength];
-[MTLRenderPassDescriptorInternal depthAttachment];
-[MTLRenderPassDescriptorInternal setStencilAttachment:];
-[MTLRenderPassDescriptorInternal description];
-[MTLRenderPassDescriptorInternal setTileHeight:];
-[MTLRenderPassDescriptorInternal setDefaultRasterSampleCount:];
-[MTLRenderPassDescriptorInternal ditherEnabled];
-[MTLRenderPassDescriptorInternal setRasterizationRateMap:];
-[MTLRenderPassDescriptorInternal setImageblockSampleLength:];
-[MTLRenderPassDescriptorInternal copyWithZone:];
-[MTLRenderPassDescriptorInternal renderTargetWidth];
-[MTLRenderPassDescriptorInternal pointCoordYFlipEnabled];
-[MTLRenderPassDescriptorInternal isEqual:];
-[MTLRenderPassDescriptorInternal supportColorAttachmentMapping];
-[MTLRenderPassDescriptorInternal setDefaultColorSampleCount:];
-[MTLRenderPassDescriptorInternal rasterizationRateMap];
-[MTLRenderPassDescriptorInternal setRenderTargetHeight:];
-[MTLRenderPassDescriptorInternal getSamplePositions:count:];
-[MTLRenderPassDescriptorInternal visibilityResultType];
```
