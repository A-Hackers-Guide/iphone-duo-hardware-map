# `BWAdaptiveCorrectionPreviewRegistration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 0 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"BWAdaptiveCorrectionPreviewRegistrationTuningParameters" _tuningParameters;
@"FigRegToolboxGPU" _keypointDetector;
@"FigMetalContext" _metalContext;
^{?=ffffff} _keypointList;
^{OpaqueVTPixelRotationSession=} _cropAndScaleSession;
@"NSDictionary" _staticParametersByPortType;
{CalModel="focalLengthPix"[2d]"opticalCenterX"[2d]"opticalCenterY"[2d]"extrinRotRefefenceToAuxiliary"[12d]"canonicalDisparityScale"d"calibrationDimensions"[2d]"pixelSize_um"[2d]} _correctedCalibration;
[2^d] _validKeypointsInSensorResolution;
I _validKeypointsCount;
[2^d] _transposedKeypoints;
^d _keypointDepths;
[3^d] _keypointWeights;
{?="narrowerToWiderTransforms"[3{?="columns"[3]}]} _registrationTransform;
@"BWPixelBufferPool" _registrationPool;
@"BWMemoryPoolFlushAssertion" _registrationPoolReadyAssertion;
B _resourcesCleaned;
B _excludeExtrinsicsCorrectionFromWideTeleAlignment;
B _excludeEstimatedSagFromWideTeleAlignment;
f _sagEstimationAlpha;
@"NSMutableDictionary" _estimatedSagPositionsByPortType;
{?="value"q"timescale"i"flags"I"epoch"q} _lastNarrowerFramePTS;
^? _fullCorrectionFunction;
^? _computeVerticalBaselineTransformFunction;
^? _rotateCalModelFunction;
^? _transformPointsWithMatrixFunction;
^v _disparityLib;
```

## Class methods

```
+[BWAdaptiveCorrectionPreviewRegistration initialize];
+[BWAdaptiveCorrectionPreviewRegistration flattenNarrowerToWiderTransforms:narrowerDimensions:narrowerFinalCropRect:atNarrowerToWiderCameraScale:useAnchorAtCenter:useHorizontalEdges:];
```

## Instance methods

```
-[BWAdaptiveCorrectionPreviewRegistration dealloc];
-[BWAdaptiveCorrectionPreviewRegistration cleanupResources];
-[BWAdaptiveCorrectionPreviewRegistration allocateResourcesWithVideoFormat:metalContext:];
-[BWAdaptiveCorrectionPreviewRegistration computeAlignmentFromWiderSampleBuffer:narrowerSampleBuffer:narrowerToWiderTransformsOut:];
-[BWAdaptiveCorrectionPreviewRegistration computeApproximateCorrectionForWiderCamera:narrowerCameraPortType:narrowerPixelBufferDimensions:narrowerToWiderCameraScale:narrowerToWiderTransformsOut:];
-[BWAdaptiveCorrectionPreviewRegistration initWithCameraInfoByPortType:excludeStaticComponentFromAlignmentShifts:];
-[BWAdaptiveCorrectionPreviewRegistration registerWiderSampleBufferUsingADC:narrowerSampleBuffer:narrowerRect:macroTransitionType:registerHorizontalEdges:narrowerToWiderTransformsOut:];
```
