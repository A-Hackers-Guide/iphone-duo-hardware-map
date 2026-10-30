# `BWPreviewStitcherRenderer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 75 instance variables, 5 properties, 47 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _cameraInfo;
@"BWPreviewStitcherCameraInfo" _superWideCameraInfo;
@"BWPreviewStitcherCameraInfo" _wideCameraInfo;
@"BWPreviewStitcherCameraInfo" _teleCameraInfo;
B _multiCameraStitchingEnabled;
B _fractionalSourceRectEnabled;
B _inputBuffersHaveHorizontalOverscanOnly;
B _superWideSensorCenterOffsetEnabled;
B _parallaxMitigationBasedOnZoomFactorEnabled;
B _superWideCompensateForMissingFOV;
B _hideSuperWideStitchingWhenTooClose;
B _cameraTransitionBrightnessCompensationEnabled;
f _cameraTransitionBrightnessCompensationInsetPercentage;
f _dynamicCameraScaleMSRMarginPercentage;
f _superMacroEdgeFeatheringBlurInset;
B _superMacroEdgeFeatheringShowBlurMask;
B _borderBlurEnabled;
f _borderBlurStrength;
B _borderStretchEnabled;
f _borderStretchScaleFactor;
f _borderStretchNextNarrowerBaseZoomFactorMultiplier;
f _edgeFeatheringAspectCompensation;
f _zoomInFeatheringInnerRadiusStart;
f _zoomInFeatheringInnerRadiusEnd;
f _zoomInFeatheringOuterRadiusStart;
f _zoomInFeatheringOuterRadiusEnd;
f _zoomOutFeatheringInnerRadiusStart;
f _zoomOutFeatheringInnerRadiusEnd;
f _zoomOutFeatheringOuterRadiusStart;
f _zoomOutFeatheringOuterRadiusEnd;
f _zoomInFeatheringInnerRadiusInterim;
f _zoomInFeatheringOuterRadiusInterim;
f _zoomInFeatheringInnerRadiusExpanded;
f _zoomInFeatheringOuterRadiusExpanded;
B _cameraTransitionBorderEdgeFeatheringEnabled;
i _cameraTransitionEdgeFeatheringZoomInStartSigma;
i _cameraTransitionEdgeFeatheringZoomInEndSigma;
i _cameraTransitionEdgeFeatheringZoomOutStartSigma;
i _cameraTransitionEdgeFeatheringZoomOutEndSigma;
i _cameraTransitionEdgeFeatheringBorderInsetFactor;
@"BWVideoFormat" _outputVideoFormat;
@"BWPixelBufferPool" _livePixelBufferPool;
i _rotationDegrees;
B _flipHorizontal;
B _flipVertical;
B _generatesHistogram;
B _inputIsHDR;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _outputTransform;
^{OpaqueVTPixelRotationSession=} _outputRotationSession;
^{OpaqueVTPixelRotationSession=} _intermediateRotationSession;
i _screenScale;
@"BWPixelBufferPool" _ciPreheatingBufferPool;
@"BWPixelBufferPool" _compressedFormatIntermediatePool;
@"BWMemoryPoolFlushAssertion" _ciPreheatingBufferPoolReadyAssertion;
@"CIContext" _cameraTransitionCIContext;
@"NSURL" _coreImageMetalLibraryURL;
@"NSObject<OS_dispatch_queue>" _metalCompletionQueue;
@"NSObject<OS_dispatch_queue>" _metalSubmissionQueue;
@"NSObject<OS_dispatch_queue>" _ciPreheatingQueue;
@"NSObject<OS_dispatch_group>" _ciPreheatingGroup;
B _havePreheatedCI;
@"NSMutableDictionary" _blackFilledBorderRectsBySurfaceID;
B _forceBlackFillBorderEnabled;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _widerCameraFoVFillsOverCapture;
{BWSmartCameraScene="enabled"B"confident"B"confidenceFilterRatio"f"filteredConfidence"f"confidenceThreshold"f"confidenceHysteresisValueLag"f"confidenceHysteresisTemporalLagBeforeConfident"s"confidenceHysteresisTemporalLagBeforeNotConfident"s"currentTemporalHysteresis"s"resetTemporalHysteresisAndFilteringOnNextUpdate"B"name"*} _narrowerCameraFoVFillsOverCapture;
B _superWideOccludedByWide;
B _superWideDrawingSuspendedUntilFocusImproves;
{?="value"q"timescale"i"flags"I"epoch"q} _firstFramePTS;
f _uiZoomFactor;
B _showFeatherGradient;
B _rebuildingGraphForTrueVideoTransition;
B _trueVideoCaptureEnabled;
B _thermalPressureIsCritical;
@"BWPixelBufferTransferRenderer" _pixelBufferTransferRenderer;
B _appliesOverCaptureToLongerDimension;
```

## Properties

```
@property (TB,N) forceBlackFillBorderEnabled;
@property (TB,N,V_rebuildingGraphForTrueVideoTransition) rebuildingGraphForTrueVideoTransition;
@property (TB,N,V_trueVideoCaptureEnabled) trueVideoCaptureEnabled;
@property (TB,N,V_thermalPressureIsCritical) thermalPressureIsCritical;
@property (TB,N,V_appliesOverCaptureToLongerDimension) appliesOverCaptureToLongerDimension;
```

## Class methods

```
+[BWPreviewStitcherRenderer initialize];
```

## Instance methods

```
-[BWPreviewStitcherRenderer setTrueVideoCaptureEnabled:];
-[BWPreviewStitcherRenderer trueVideoCaptureEnabled];
-[BWPreviewStitcherRenderer _rectangularFeatheredImageWithNarrowerCameraImage:widerCameraImage:narrowerCameraClipRect:zoomingIn:progress:rampCameraTransition:transitionCoordinator:];
-[BWPreviewStitcherRenderer _compressedFormatIntermediatePool];
-[BWPreviewStitcherRenderer _preheatCIRenderingAsyncIfNecessaryWithTransitionCoordinator:];
-[BWPreviewStitcherRenderer _featheredImageWithNarrowerCameraImage:widerCameraImage:narrowerCameraClipRect:widerCameraClipRect:zoomingIn:progress:featherEdges:rampCameraTransition:renderEnhancedFeathering:transitionCoordinator:];
-[BWPreviewStitcherRenderer setForceBlackFillBorderEnabled:];
-[BWPreviewStitcherRenderer dealloc];
-[BWPreviewStitcherRenderer _cameraTransitionEdgeFeatheringZoomInStartSigma];
-[BWPreviewStitcherRenderer _scaleFactorAppliedForPixelBuffer:usedSourceRect:primaryCaptureRectAspectRatio:metadata:];
-[BWPreviewStitcherRenderer _imageWithCIImage:bounds:shift:];
-[BWPreviewStitcherRenderer waitForPreheatingToFinish];
-[BWPreviewStitcherRenderer _cameraTransitionEdgeFeatheringZoomOutEndSigma];
-[BWPreviewStitcherRenderer initWithCameraInfoArray:multiCameraStitchingEnabled:fractionalSourceRectEnabled:inputBuffersHaveHorizontalOverscanOnly:superWideSensorCenterOffsetEnabled:parallaxMitigationBasedOnZoomFactorEnabled:];
-[BWPreviewStitcherRenderer thermalPressureIsCritical];
-[BWPreviewStitcherRenderer _transferPixelBuffer:rect:intoPixelBuffer:rect:isFinalOutput:withInputShift:scale:excludeOutputRect:outputAlignment:inputSourceRectOut:blackFillUnalignedEdges:];
-[BWPreviewStitcherRenderer _transitionRampImageWithWiderCameraImage:widerCameraBounds:narrowerCameraImage:zoomingIn:progress:narrowerCameraBounds:narrowerCameraShift:featherEdges:rampCameraTransition:renderEnhancedFeathering:renderBrightnessCompensation:transitionCoordinator:unrotatedOutputDimensions:];
-[BWPreviewStitcherRenderer _coreImageMetalLibraryURL];
-[BWPreviewStitcherRenderer forceBlackFillBorderEnabled];
-[BWPreviewStitcherRenderer _applyBrightnessCompensationToImage:referenceImage:bounds:compensationLevel:];
-[BWPreviewStitcherRenderer appliesOverCaptureToLongerDimension];
-[BWPreviewStitcherRenderer renderStitchedPixelBuffer:fromFramePairInfo:alignmentCoordinator:transitionCoordinator:renderParameters:renderInfoOut:];
-[BWPreviewStitcherRenderer setAppliesOverCaptureToLongerDimension:];
-[BWPreviewStitcherRenderer cleanupResources];
-[BWPreviewStitcherRenderer _initCameraTransitionCIContextWithColorManagementEnabled:];
-[BWPreviewStitcherRenderer _getInputRect:outputRect:inputShiftAppliedInOutputRect:toTransferPixelBuffer:rect:intoPixelBufferDimensions:rect:withInputShift:shiftOutsideBoundingRectAllowed:scale:forFinalOutput:];
-[BWPreviewStitcherRenderer _compensateForMissingFOVUsingPixelBuffer:sourceRect:destinationContainingRect:destinationInsetRect:outputPixelBuffer:];
-[BWPreviewStitcherRenderer _imageWithCVPixelBuffer:sourceRect:destinationDimensions:destinationRect:useSDRToneMap:];
-[BWPreviewStitcherRenderer _metalSubmissionQueue];
-[BWPreviewStitcherRenderer _metalCompletionQueue];
-[BWPreviewStitcherRenderer _ciPreheatingBufferPool];
-[BWPreviewStitcherRenderer rebuildingGraphForTrueVideoTransition];
-[BWPreviewStitcherRenderer _cameraTransitionBrightnessCompensationEnabled];
-[BWPreviewStitcherRenderer prepareWithBWNodeOutput:transitionCoordinator:rotationDegrees:flipHorizontal:flipVertical:generatesHistogram:inputIsHDR:];
-[BWPreviewStitcherRenderer _cameraTransitionBorderEdgeFeatheringEnabled];
-[BWPreviewStitcherRenderer _imageByBlendingHDRImage:withSDRImage:bounds:progress:];
-[BWPreviewStitcherRenderer setRebuildingGraphForTrueVideoTransition:];
-[BWPreviewStitcherRenderer _usesCIPreheating];
-[BWPreviewStitcherRenderer _cameraTransitionEdgeFeatheringBorderInsetFactor];
-[BWPreviewStitcherRenderer _borderBlackFillPixelBuffer:validPixelRect:];
-[BWPreviewStitcherRenderer _cameraTransitionEdgeFeatheringZoomOutStartSigma];
-[BWPreviewStitcherRenderer _renderCIImage:toRenderDestination:sourceRect:destinationRect:];
-[BWPreviewStitcherRenderer _cameraTransitionEdgeFeatheringZoomInEndSigma];
-[BWPreviewStitcherRenderer _imageByTransformingImage:sourceRect:intoDestinationRect:rotationDegrees:flipX:flipY:highQualityDownsample:];
-[BWPreviewStitcherRenderer histogramData];
-[BWPreviewStitcherRenderer setThermalPressureIsCritical:];
-[BWPreviewStitcherRenderer _cameraTransitionBrightnessCompensationInsetPercentage];
```
