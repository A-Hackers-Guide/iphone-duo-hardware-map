# `BWTiledEspressoInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _forceSynchronousInference;
@"<MTLCommandQueue>" _metalCommandQueue;
@"NSString" _pipelineProcessingContext;
C _tileBufferCount;
I _anefIntermediateBufferSizeMultiplierHint;
```

## Properties

```
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (TB,N,V_forceSynchronousInference) forceSynchronousInference;
@property (TC,N,V_tileBufferCount) tileBufferCount;
@property (T@"NSString",&,N,V_pipelineProcessingContext) pipelineProcessingContext;
@property (TI,N,V_anefIntermediateBufferSizeMultiplierHint) anefIntermediateBufferSizeMultiplierHint;
```

## Instance methods

```
-[BWTiledEspressoInferenceConfiguration setMetalCommandQueue:];
-[BWTiledEspressoInferenceConfiguration pipelineProcessingContext];
-[BWTiledEspressoInferenceConfiguration metalCommandQueue];
-[BWTiledEspressoInferenceConfiguration setPipelineProcessingContext:];
-[BWTiledEspressoInferenceConfiguration initWithInferenceType:];
-[BWTiledEspressoInferenceConfiguration dealloc];
-[BWTiledEspressoInferenceConfiguration anefIntermediateBufferSizeMultiplierHint];
-[BWTiledEspressoInferenceConfiguration setAnefIntermediateBufferSizeMultiplierHint:];
-[BWTiledEspressoInferenceConfiguration tileBufferCount];
-[BWTiledEspressoInferenceConfiguration forceSynchronousInference];
-[BWTiledEspressoInferenceConfiguration initWithInferenceType:metalCommandQueue:];
-[BWTiledEspressoInferenceConfiguration setForceSynchronousInference:];
-[BWTiledEspressoInferenceConfiguration setTileBufferCount:];
```
