# `BWStillImageNodeConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 24 properties, 50 instance methods, 0 class methods

## Instance variables

```
i _stillImageProcessingMode;
@"NSString" _pipelineProcessingContext;
@"<MTLCommandQueue>" _metalCommandQueue;
I _figThreadPriority;
i _depthDataType;
i _pearlModuleType;
i _depthDataToRGBRotationAngle;
@"BWInferenceScheduler" _inferenceScheduler;
i _maxLossyCompressionLevel;
B _deferredCaptureSupportEnabled;
B _deferredPhotoProcessorEnabled;
{?="width"i"height"i} _enhancedResolutionDimensions;
{?="width"i"height"i} _downgradedDeepFusionEnhancedResolutionDimensions;
B _optimizedEnhancedResolutionDepthPipelineEnabled;
B _filterRenderingEnabled;
{?="width"i"height"i} _constantColorConfidenceMapDimensions;
{?="width"i"height"i} _stereoPhotoOutputDimensions;
{?="width"i"height"i} _depthDataOutputDimensions;
B _optimizedProcessingForZoomFOVSupported;
B _preferNRFDownscaleToTargetDimensions;
@"NSDictionary" _cameraSensorOrientationCompensationDegreesCWByPortType;
B _documentScanningEnabled;
B _smartStylesInFilterNodeEnabled;
B _secureSigningPhotoCaptureSupportEnabled;
```

## Properties

```
@property (Ti,N,V_stillImageProcessingMode) stillImageProcessingMode;
@property (T@"NSString",&,N,V_pipelineProcessingContext) pipelineProcessingContext;
@property (T@"<MTLCommandQueue>",&,N,V_metalCommandQueue) metalCommandQueue;
@property (TI,N,V_figThreadPriority) figThreadPriority;
@property (Ti,N,V_depthDataType) depthDataType;
@property (Ti,N,V_pearlModuleType) pearlModuleType;
@property (Ti,N,V_depthDataToRGBRotationAngle) depthDataToRGBRotationAngle;
@property (T@"BWInferenceScheduler",&,N,V_inferenceScheduler) inferenceScheduler;
@property (Ti,N,V_maxLossyCompressionLevel) maxLossyCompressionLevel;
@property (TB,N,V_deferredCaptureSupportEnabled) deferredCaptureSupportEnabled;
@property (TB,N,V_deferredPhotoProcessorEnabled) deferredPhotoProcessorEnabled;
@property (T{?=ii},N,V_enhancedResolutionDimensions) enhancedResolutionDimensions;
@property (T{?=ii},N,V_downgradedDeepFusionEnhancedResolutionDimensions) downgradedDeepFusionEnhancedResolutionDimensions;
@property (TB,N,V_optimizedEnhancedResolutionDepthPipelineEnabled) optimizedEnhancedResolutionDepthPipelineEnabled;
@property (TB,N,V_filterRenderingEnabled) filterRenderingEnabled;
@property (T{?=ii},N,V_constantColorConfidenceMapDimensions) constantColorConfidenceMapDimensions;
@property (T{?=ii},N,V_stereoPhotoOutputDimensions) stereoPhotoOutputDimensions;
@property (T{?=ii},N,V_depthDataOutputDimensions) depthDataOutputDimensions;
@property (TB,N,V_optimizedProcessingForZoomFOVSupported) optimizedProcessingForZoomFOVSupported;
@property (TB,N,V_preferNRFDownscaleToTargetDimensions) preferNRFDownscaleToTargetDimensions;
@property (T@"NSDictionary",&,N,V_cameraSensorOrientationCompensationDegreesCWByPortType) cameraSensorOrientationCompensationDegreesCWByPortType;
@property (TB,N,V_documentScanningEnabled) documentScanningEnabled;
@property (TB,N,V_smartStylesInFilterNodeEnabled) smartStylesInFilterNodeEnabled;
@property (TB,N,V_secureSigningPhotoCaptureSupportEnabled) secureSigningPhotoCaptureSupportEnabled;
```

## Instance methods

```
-[BWStillImageNodeConfiguration pearlModuleType];
-[BWStillImageNodeConfiguration cameraSensorOrientationCompensationDegreesCWByPortType];
-[BWStillImageNodeConfiguration setDowngradedDeepFusionEnhancedResolutionDimensions:];
-[BWStillImageNodeConfiguration setDepthDataOutputDimensions:];
-[BWStillImageNodeConfiguration smartStylesInFilterNodeEnabled];
-[BWStillImageNodeConfiguration setMetalCommandQueue:];
-[BWStillImageNodeConfiguration pipelineProcessingContext];
-[BWStillImageNodeConfiguration setDeferredCaptureSupportEnabled:];
-[BWStillImageNodeConfiguration inferenceScheduler];
-[BWStillImageNodeConfiguration depthDataType];
-[BWStillImageNodeConfiguration enhancedResolutionDimensions];
-[BWStillImageNodeConfiguration optimizedEnhancedResolutionDepthPipelineEnabled];
-[BWStillImageNodeConfiguration metalCommandQueue];
-[BWStillImageNodeConfiguration setCameraSensorOrientationCompensationDegreesCWByPortType:];
-[BWStillImageNodeConfiguration secureSigningPhotoCaptureSupportEnabled];
-[BWStillImageNodeConfiguration setPipelineProcessingContext:];
-[BWStillImageNodeConfiguration setEnhancedResolutionDimensions:];
-[BWStillImageNodeConfiguration setConstantColorConfidenceMapDimensions:];
-[BWStillImageNodeConfiguration preferNRFDownscaleToTargetDimensions];
-[BWStillImageNodeConfiguration setSmartStylesInFilterNodeEnabled:];
-[BWStillImageNodeConfiguration setDocumentScanningEnabled:];
-[BWStillImageNodeConfiguration setStereoPhotoOutputDimensions:];
-[BWStillImageNodeConfiguration setFigThreadPriority:];
-[BWStillImageNodeConfiguration downgradedDeepFusionEnhancedResolutionDimensions];
-[BWStillImageNodeConfiguration stillImageProcessingMode];
-[BWStillImageNodeConfiguration setDepthDataToRGBRotationAngle:];
-[BWStillImageNodeConfiguration setPearlModuleType:];
-[BWStillImageNodeConfiguration depthDataToRGBRotationAngle];
-[BWStillImageNodeConfiguration depthDataOutputDimensions];
-[BWStillImageNodeConfiguration deferredCaptureSupportEnabled];
-[BWStillImageNodeConfiguration deferredPhotoProcessorEnabled];
-[BWStillImageNodeConfiguration setPreferNRFDownscaleToTargetDimensions:];
-[BWStillImageNodeConfiguration setDepthDataType:];
-[BWStillImageNodeConfiguration stereoPhotoOutputDimensions];
-[BWStillImageNodeConfiguration setMaxLossyCompressionLevel:];
-[BWStillImageNodeConfiguration maxLossyCompressionLevel];
-[BWStillImageNodeConfiguration constantColorConfidenceMapDimensions];
-[BWStillImageNodeConfiguration setDeferredPhotoProcessorEnabled:];
-[BWStillImageNodeConfiguration setSecureSigningPhotoCaptureSupportEnabled:];
-[BWStillImageNodeConfiguration dealloc];
-[BWStillImageNodeConfiguration setOptimizedProcessingForZoomFOVSupported:];
-[BWStillImageNodeConfiguration documentScanningEnabled];
-[BWStillImageNodeConfiguration setStillImageProcessingMode:];
-[BWStillImageNodeConfiguration setOptimizedEnhancedResolutionDepthPipelineEnabled:];
-[BWStillImageNodeConfiguration setFilterRenderingEnabled:];
-[BWStillImageNodeConfiguration initWithNodeConfiguration:];
-[BWStillImageNodeConfiguration optimizedProcessingForZoomFOVSupported];
-[BWStillImageNodeConfiguration setInferenceScheduler:];
-[BWStillImageNodeConfiguration figThreadPriority];
-[BWStillImageNodeConfiguration filterRenderingEnabled];
```
