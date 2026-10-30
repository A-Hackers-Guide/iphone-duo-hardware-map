# `MTLRenderPassDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 16 properties, 13 instance methods, 3 class methods

## Instance variables

```
B _supportColorAttachmentMapping;
Q _imageblockSampleLength;
Q _threadgroupMemoryLength;
Q _tileWidth;
Q _tileHeight;
```

## Properties

```
@property (T@"MTLRenderPassColorAttachmentDescriptorArray",R,D) colorAttachments;
@property (T@"MTLRenderPassDepthAttachmentDescriptor",C,D,N) depthAttachment;
@property (T@"MTLRenderPassStencilAttachmentDescriptor",C,D,N) stencilAttachment;
@property (T@"<MTLBuffer>",&,D,N) visibilityResultBuffer;
@property (TQ,D,N) renderTargetArrayLength;
@property (TQ,N,V_imageblockSampleLength) imageblockSampleLength;
@property (TQ,N,V_threadgroupMemoryLength) threadgroupMemoryLength;
@property (TQ,N,V_tileWidth) tileWidth;
@property (TQ,N,V_tileHeight) tileHeight;
@property (TQ,D,N) defaultRasterSampleCount;
@property (TQ,D,N) renderTargetWidth;
@property (TQ,D,N) renderTargetHeight;
@property (T@"<MTLRasterizationRateMap>",&,D,N) rasterizationRateMap;
@property (T@"MTLRenderPassSampleBufferAttachmentDescriptorArray",R,D) sampleBufferAttachments;
@property (Tq,D,N) visibilityResultType;
@property (TB,N,V_supportColorAttachmentMapping) supportColorAttachmentMapping;
```

## Class methods

```
+[MTLRenderPassDescriptor allocWithZone:];
+[MTLRenderPassDescriptor alloc];
+[MTLRenderPassDescriptor renderPassDescriptor];
```

## Instance methods

```
-[MTLRenderPassDescriptor imageblockSampleLength];
-[MTLRenderPassDescriptor setThreadgroupMemoryLength:];
-[MTLRenderPassDescriptor setSamplePositions:count:];
-[MTLRenderPassDescriptor setTileWidth:];
-[MTLRenderPassDescriptor tileHeight];
-[MTLRenderPassDescriptor tileWidth];
-[MTLRenderPassDescriptor setSupportColorAttachmentMapping:];
-[MTLRenderPassDescriptor threadgroupMemoryLength];
-[MTLRenderPassDescriptor setTileHeight:];
-[MTLRenderPassDescriptor setImageblockSampleLength:];
-[MTLRenderPassDescriptor copyWithZone:];
-[MTLRenderPassDescriptor supportColorAttachmentMapping];
-[MTLRenderPassDescriptor getSamplePositions:count:];
```
