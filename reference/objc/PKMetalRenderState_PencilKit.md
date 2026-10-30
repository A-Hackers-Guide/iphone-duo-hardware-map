# `PKMetalRenderState`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 30 instance variables, 0 properties, 1 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _commandBuffers;
@"NSMutableSet" _purgeableFramebuffers;
@"NSMutableSet" _extendedLifetimeObjects;
{PKShaderPipelineConfig="framebufferPixelFormats"[8C]} _defaultPipelineConfig;
B _liveRendering;
B _waitUntilCompletedOnCommit;
B _msaaRendering;
B _renderOnPaper;
B _needRenderMask;
B _renderGroupMaskedRendering;
B _useAccumulatorsAsPaintFramebuffers;
B _needPaintAccumulator;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLCommandBuffer>" _commandBuffer;
@"<MTLCommandBuffer>" _computeCommandBuffer;
@"<MTLCommandBuffer>" _maskCommandBuffer;
@"<MTLRenderCommandEncoder>" _renderEncoder;
@"<MTLComputeCommandEncoder>" _computeEncoder;
@"<MTLRenderCommandEncoder>" _maskRenderEncoder;
Q _vertexEncodeCount;
@"<MTLTexture>" _destinationTexture;
@"<MTLTexture>" _multiplyDestinationTexture;
Q _destinationColorAttachmentIndex;
Q _sixChannelMultiplyLayerColorAttachmentIndex;
Q _sixChannelRenderModeAddMultiplyLayersColorAttachmentIndexOffset;
q _sixChannelRenderMode;
@"<MTLTexture>" _sixChannelContentTexture;
Q _numPaintFramebuffers;
{?="x"Q"y"Q"width"Q"height"Q} _scissorRect;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _renderTextureTexCoordTransform;
```

## Class methods

```
+[PKMetalRenderState renderTargetBarrierForRenderEncoder:];
```

## Instance methods

```
-[PKMetalRenderState dealloc];
```
