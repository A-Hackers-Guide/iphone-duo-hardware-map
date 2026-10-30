# `BWDeepZoomInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWTiledEspressoInferenceProvider`
- 10 instance variables, 0 properties, 11 instance methods, 1 class methods

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
+[BWDeepZoomInferenceProvider initialize];
```

## Instance methods

```
-[BWDeepZoomInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWDeepZoomInferenceProvider prewarmUsingLimitedMemory:];
-[BWDeepZoomInferenceProvider dealloc];
-[BWDeepZoomInferenceProvider allowedPixelBufferCompressionDirection];
-[BWDeepZoomInferenceProvider purgeIntermediateResources];
-[BWDeepZoomInferenceProvider preProcessOutputBuffer:forMediaKey:];
-[BWDeepZoomInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWDeepZoomInferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:];
-[BWDeepZoomInferenceProvider createInputTiles:withInputs:atPosition:cmdBuffer:];
-[BWDeepZoomInferenceProvider initWithConfiguration:resourceProvider:];
-[BWDeepZoomInferenceProvider writeOutputFor:to:fromNetworkOutputTiles:withAdditionalPixelBuffers:withInputTilePixelBuffers:withInputFullPixelBuffers:atPosition:cmdBuffer:];
```
