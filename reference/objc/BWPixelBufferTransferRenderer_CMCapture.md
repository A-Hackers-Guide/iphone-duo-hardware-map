# `BWPixelBufferTransferRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"BWPixelBufferPool" _intermediateBufferPool;
@"FigM2MController" _alignmentM2MController;
B _useGPUForAlignmentRendering;
B _useMSRBorderFill;
B _useCPUForAlignedBlackFill;
@"NSData" _histogramData;
B _fractionalSourceRectEnabled;
^{__CVBuffer=} _blackFillPlaceholderPixelBuffer;
^{__CVBuffer=} _scalingIntermediatePixelBuffer;
@"FigMetalContext" _metalContext;
@"NSObject<OS_dispatch_queue>" _metalCompletionQueue;
@"NSObject<OS_dispatch_queue>" _metalSubmissionQueue;
@"<MTLRenderPipelineState>" _metalRenderPipelineState_pixelTransfer;
@"<MTLRenderPipelineState>" _metalRenderPipelineState_blackFill;
@"<MTLSamplerState>" _metalSamplerState;
^{__CVMetalTextureCache=} _metalTextureCache;
```

## Class methods

```
+[BWPixelBufferTransferRenderer initialize];
+[BWPixelBufferTransferRenderer supportsAcceleratedBorderFill];
```

## Instance methods

```
-[BWPixelBufferTransferRenderer dealloc];
-[BWPixelBufferTransferRenderer histogramData];
-[BWPixelBufferTransferRenderer borderBlackFillPixelBuffer:validRect:];
-[BWPixelBufferTransferRenderer doPixelRotationTransferWithSession:sourceBuffer:sourceRect:destinationBuffer:destinationRect:blackFillUnalignedEdges:];
-[BWPixelBufferTransferRenderer initWithIntermediateBufferPool:fractionalSourceRectEnabled:compressedFormatEnabled:];
```
