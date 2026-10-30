# `BWDeepZoomE5InferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWTiledE5InferenceProvider`
- 10 instance variables, 0 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"BWDeepZoomInferenceConfiguration" _inferenceConfig;
@"NSMutableArray" _inputVideoRequirements;
@"BWInferenceVideoRequirement" _outputVideoRequirement;
^{opaqueCMFormatDescription=} _outputFormatDescription;
{?="width"i"height"i} _inputReferencePixelBufferDimensions;
@"<CMIDeepZoomProcessor>" _deepZoomProcessor;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedInputImageFinalCropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _denormalizedSourceCropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _denormalizedDeepTransferLowResROI;
{?="width"i"height"i} _deepTransferLowResBufferDims;
```

## Class methods

```
+[BWDeepZoomE5InferenceProvider initialize];
```

## Instance methods

```
-[BWDeepZoomE5InferenceProvider prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:];
-[BWDeepZoomE5InferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWDeepZoomE5InferenceProvider createInputTiles:withInputs:tileInputInfo:tileOutputInfo:];
-[BWDeepZoomE5InferenceProvider writeOutputFor:to:fromNetworkOutputTiles:withAdditionalPixelBuffers:withInputTilePixelBuffers:withInputFullPixelBuffers:tileInputInfo:tileOutputInfo:];
-[BWDeepZoomE5InferenceProvider prewarmUsingLimitedMemory:];
-[BWDeepZoomE5InferenceProvider dealloc];
-[BWDeepZoomE5InferenceProvider allowedPixelBufferCompressionDirection];
-[BWDeepZoomE5InferenceProvider prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:];
-[BWDeepZoomE5InferenceProvider purgeIntermediateResources];
-[BWDeepZoomE5InferenceProvider preProcessOutputBuffer:forMediaKey:];
-[BWDeepZoomE5InferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWDeepZoomE5InferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:];
-[BWDeepZoomE5InferenceProvider initWithConfiguration:resourceProvider:];
```
