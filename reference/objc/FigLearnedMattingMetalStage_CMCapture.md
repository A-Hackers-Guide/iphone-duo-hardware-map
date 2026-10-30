# `FigLearnedMattingMetalStage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"FigMetalContext" _metalContext;
@"<MTLComputePipelineState>" _createTileWithScaleKernel;
@"<MTLComputePipelineState>" _pasteTileKernel;
@"<MTLComputePipelineState>" _clearTextureKernel;
^{__CVMetalTextureCache=} _textureCache;
```

## Instance methods

```
-[FigLearnedMattingMetalStage finishProcessing];
-[FigLearnedMattingMetalStage init];
-[FigLearnedMattingMetalStage dealloc];
-[FigLearnedMattingMetalStage initWithMetalContext:];
-[FigLearnedMattingMetalStage clearBuffer:ensureIOFence:];
-[FigLearnedMattingMetalStage createTileFrom:to:withStart:commandBuffer:];
-[FigLearnedMattingMetalStage createTileFrom:to:withStart:withScale:outCommandBuffer:];
-[FigLearnedMattingMetalStage encodeTileCreationFrom:to:withStart:withScale:withTileInputInfo:withTileOutputInfo:];
-[FigLearnedMattingMetalStage encodeTilePasteFrom:to:withStart:withNoOverlapStart:withNoOverlapEnd:withTileInputInfo:withTileOutputInfo:];
-[FigLearnedMattingMetalStage pasteTileFrom:to:withStart:withNoOverlapStart:withNoOverlapEnd:outCommandBuffer:];
```
