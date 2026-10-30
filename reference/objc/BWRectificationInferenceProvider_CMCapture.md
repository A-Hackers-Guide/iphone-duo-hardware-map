# `BWRectificationInferenceProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceProvider`, `BWInferenceCacheable`, `BWInferenceSubmittable`
- 50 instance variables, 21 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSString" _customInferenceIdentifier;
@"BWInferenceVideoRequirement" _refInputRequirement;
@"BWInferenceVideoRequirement" _auxInputRequirement;
@"BWInferenceVideoRequirement" _refKeypointsInputRequirement;
@"BWInferenceVideoRequirement" _auxKeypointsInputRequirement;
@"BWInferenceVideoRequirement" _refOutputRequirement;
@"BWInferenceVideoRequirement" _auxOutputRequirement;
@"BWInferenceVideoRequirement" _opticalFlowOutputRequirement;
@"BWInferenceVideoRequirement" _originalRefInputRequirement;
@"BWInferenceVideoRequirement" _originalAuxInputRequirement;
@"LKTKeypointDetector" _lktKeypointDetector;
@"Calibration" _calibration;
@"DisparityTuningParameters" _disparityTuningParameters;
@"Demosaic" _auxiliaryDemosaic;
{?="distortPolynomCoefficients"[8f]"undistortPolynomCoefficients"[8f]"centerX"f"centerY"f"originalImageOriginX"f"originalImageOriginY"f"originalImageWidth"f"originalImageHeight"f"pixelSize"f"homography"[9f]"inverseHomography"[9f]"canvasResolution"{CGSize="width"d"height"d}"applyZTransform"B"samplerType"i"rollingShutterCorrectionHomographies"^{?}"numRollingShutterCorrectionHomographies"i"rollingShutterCorrectionHomographyStep"f"applyRollingShutterCorrection"B"focalLengthPix"f"originalCropRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}} _gdcParametersReference;
{?="distortPolynomCoefficients"[8f]"undistortPolynomCoefficients"[8f]"centerX"f"centerY"f"originalImageOriginX"f"originalImageOriginY"f"originalImageWidth"f"originalImageHeight"f"pixelSize"f"homography"[9f]"inverseHomography"[9f]"canvasResolution"{CGSize="width"d"height"d}"applyZTransform"B"samplerType"i"rollingShutterCorrectionHomographies"^{?}"numRollingShutterCorrectionHomographies"i"rollingShutterCorrectionHomographyStep"f"applyRollingShutterCorrection"B"focalLengthPix"f"originalCropRect"{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}}} _gdcParametersAuxiliary;
@"GDCTransform" _gdcTransform;
^d _adaptiveCorrectionKeypointsReferenceDistorted;
^d _adaptiveCorrectionKeypointsAuxiliaryDistorted;
@"PTDisparityPostProcessing" _disparityPostProcessor;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"FigMetalContext" _metalContext;
@"MTLTextureDescriptor" _refInputDescriptor;
@"MTLTextureDescriptor" _auxInputDescriptor;
@"MTLTextureDescriptor" _refKeypointsInputDescriptor;
@"MTLTextureDescriptor" _auxKeypointsInputDescriptor;
@"MTLTextureDescriptor" _refOutputDescriptor;
@"MTLTextureDescriptor" _auxOutputDescriptor;
@"MTLTextureDescriptor" _opticalFlowDescriptor;
@"NSDictionary" _cameraInfoByPortType;
@"NSDictionary" _calibrationOptions;
@"<MTLCommandQueue>" _commandQueue;
^{__CVBuffer=} _zoomedAux;
Q _calibrationWidth;
Q _calibrationHeight;
I _rectificationWidth;
I _rectificationHeight;
Q _keypointGridWidth;
Q _keypointGridHeight;
B _applyRollingShutterCorrection;
Q _frameIndex;
Q _adcFrameCounter;
i _adcFrequency;
Q _adcMinFramesToConverge;
Q _adcFramesConverged;
B _adcSkipOnConflictWithSmartStyleLearning;
i _numFramesSinceAdcSkipOnConflictWithSmartStyleLearning;
f _oldZoomFactor;
i _oldQuadraBinningFactor;
f _zoomDeltaThreshold;
```

## Properties

```
@property (Ti,R,N) executionTarget;
@property (T@"NSSet",R,C,N) preventionReasons;
@property (T@"NSArray",R,N) inputVideoRequirements;
@property (T@"NSArray",R,N) outputVideoRequirements;
@property (T@"NSArray",R,N) cloneVideoRequirements;
@property (T@"NSArray",R,N) inputMetadataRequirements;
@property (T@"NSArray",R,N) outputMetadataRequirements;
@property (TI,R,N) allowedPixelBufferCompressionDirection;
@property (Ti,R,N) prewarmingSharedResourceType;
@property (T@"NSString",&,N) customInferenceIdentifier;
@property (Ti,R,N) type;
@property (T@"<BWInferenceCacheable>",R,N) cacheable;
@property (T@"<BWInferenceExecutable>",R,N) executable;
@property (T@"<BWInferenceSubmittable>",R,N) submittable;
@property (T@"<BWInferenceSharedResourcePreparatory>",R,N) sharedResourcePreparator;
@property (T@"<BWInferenceExtractable>",R,N) extractable;
@property (T@"<BWInferencePropagatable>",R,N) propagatable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWRectificationInferenceProvider initialize];
```

## Instance methods

```
-[BWRectificationInferenceProvider cacheable];
-[BWRectificationInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:];
-[BWRectificationInferenceProvider extractable];
-[BWRectificationInferenceProvider outputVideoRequirements];
-[BWRectificationInferenceProvider prewarmUsingLimitedMemory:];
-[BWRectificationInferenceProvider dealloc];
-[BWRectificationInferenceProvider reconcileWithPlaceholderProvider:];
-[BWRectificationInferenceProvider setCustomInferenceIdentifier:];
-[BWRectificationInferenceProvider cloneVideoRequirements];
-[BWRectificationInferenceProvider allowedPixelBufferCompressionDirection];
-[BWRectificationInferenceProvider executionTarget];
-[BWRectificationInferenceProvider preventionReasons];
-[BWRectificationInferenceProvider type];
-[BWRectificationInferenceProvider executable];
-[BWRectificationInferenceProvider outputMetadataRequirements];
-[BWRectificationInferenceProvider newStorage];
-[BWRectificationInferenceProvider propagatable];
-[BWRectificationInferenceProvider submittable];
-[BWRectificationInferenceProvider sharedResourcePreparator];
-[BWRectificationInferenceProvider prepareForSubmissionWithWorkQueue:];
-[BWRectificationInferenceProvider customInferenceIdentifier];
-[BWRectificationInferenceProvider inputMetadataRequirements];
-[BWRectificationInferenceProvider inputVideoRequirements];
-[BWRectificationInferenceProvider prewarmingSharedResourceType];
-[BWRectificationInferenceProvider initWithRefInputRequirement:auxInputRequirement:refKeypointsInputRequirement:auxKeypointsInputRequirement:refOutputRequirement:auxOutputRequirement:opticalFlowOutputRequirement:originalRefRequirement:originalAuxRequirement:resourceProvider:configuration:];
```
