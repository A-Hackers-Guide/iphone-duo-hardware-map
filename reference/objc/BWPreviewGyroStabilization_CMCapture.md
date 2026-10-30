# `BWPreviewGyroStabilization`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 45 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
{PreviewGyroStabilizationTransformContext="width"i"height"i"imageCenter"{CGPoint="x"d"y"d}"pixelsPerMicron"f"finalCropRect"{?="origin"{?="x"i"y"i}"size"{?="width"i"height"i}}"limitFactor"f"prevTransformLimited"B"forceIdentity"B} _transformContext;
{?="fusedRingIndex"i"fusedRingTime"[256d]"fusedRingQuaternion"[256{?="w"d"x"d"y"d"z"d}]"motionTimeShift"d"ignoreMotionDataForPowerTest"C"relaxMotionDataLoggingThreshold"C"didHaveMotionData"C"prevDidHaveMotionData"C"usingMotionDataFromISP"C} _motionData;
{?="fusedRingIndex"[2i]"fusedRingTime"[2[512d]]"fusedRingHallPosition"[2[512{?="x"f"y"f}]]"fusedRingSagPosition"[2^{?}]"hallTimeShift"d"isFirstSample"[2C]"bypassHighPassFilter"C"lowpassParameter"f"lowpassHallPosition"[2{?="x"f"y"f}]} _hallData;
{?="w"d"x"d"y"d"z"d} _extrinsicAlignmentPose;
B _isFirstFrame;
[4{?="w"d"x"d"y"d"z"d}] _stabilizedCenterQuaternion;
[4{?="w"d"x"d"y"d"z"d}] _stabilizedCenterQuaternionAdjusted;
{?="w"d"x"d"y"d"z"d} _lowpassQuaternionsInstant;
{?="w"d"x"d"y"d"z"d} _correctionQuaternion;
{?="x"f"y"f} _oisOffsetInput;
{?="x"f"y"f} _sagPosition;
[9f] _baseVector;
{?="x"f"y"f} _currentShift;
f _lowpassParameter;
f _lowpassParameterCascade;
d _frameRateNormalizationFactor;
d _deltaFrameTime;
d _previousCaptureTime;
d _quaternionThreshold;
f _physicalTripodRate;
f _panningSpeedLimitingThreshold;
B _enableCascadeFilter;
i _sagRemovalMethod;
f _lowpassParameterOverride;
B _isStillImagePreview;
f _ispMotionDataGroupDelay;
@"BWPreviewGyroStabilizationPanningDetection" _previewPanningDetection;
@"BWPreviewGyroStabilizationTripodDetection" _previewTripodDetection;
f _maxSmoothParameter;
f _defaultSmoothParameter;
f _defaultSmoothParameterSlope;
f _tripodSmoothParameter;
f _tripodSmoothParameterSlope;
i _tripodRampUpFrames;
i _tripodRampDownFrames;
i _tripodSlowPanningRampDownFrames;
i _tripodFastPanningRampDownFrames;
f _panningOverscanPercentage;
f _panningSpeedThreshold;
f _tripodMaxAngleThresholdAccumulate;
f _tripodMaxAngleThresholdInstant;
f _physicalTripodLikelyMaxAngleThreshold;
f _physicalTripodMinSmoothParameter;
f _physicalTripodGuaranteedMaxAngleThreshold;
f _slowPanningSpeedThreshold;
```

## Instance methods

```
-[BWPreviewGyroStabilization dealloc];
-[BWPreviewGyroStabilization _adjustQuaternionForSagRemoval:focalLength:];
-[BWPreviewGyroStabilization _adjustSmoothParameterWithQuaternion:cameraMetadata:reduceSmoothParameterForLowLight:];
-[BWPreviewGyroStabilization _applyCascadeFiltering:quaternion:lowpassParameter:cascadeLevel:];
-[BWPreviewGyroStabilization _computeMotionStatisticsWithQuaternion:focalLength:maxAngleAccumulateOut:maxAngleInstantOut:translationOut:];
-[BWPreviewGyroStabilization _computeSmoothParameterForNonStationaryCaseWithPanningStatus:frameIsSphereStabilized:previousLowPassParameter:rampDownRate:rampUpRate:targetSmoothParameter:];
-[BWPreviewGyroStabilization _computeSmoothParameterForPhysicalTripod:lowpassParameter:previousLowPassParameter:frameRateNormalization:];
-[BWPreviewGyroStabilization _computeSmoothParameterForStationaryCaseWithPanningStatus:translation:previousLowPassParameter:rampDownRate:rampUpRate:targetSmoothParameter:];
-[BWPreviewGyroStabilization _extractMetadataFromTopToBottomRowsFromDictionary:cameraMetadata:quaternion:];
-[BWPreviewGyroStabilization _getAllMetadataFromDictionary:cameraMetadata:];
-[BWPreviewGyroStabilization _limitSmoothParameterToOverscanWithQuaternion:cameraMetadata:minSmoothParameter:smoothParameterInOut:];
-[BWPreviewGyroStabilization _setDefaultParametersForStillImagePreview:isFrontCamera:];
-[BWPreviewGyroStabilization _updateTripodSmoothParametersWithSphereVideoEnabled:frameRateNormalization:];
-[BWPreviewGyroStabilization computeStabilizationShiftUsingMetadata:pixelBufferDimensions:pixelSizeInMicrons:useISPFrameCorrectionShift:stabilizationShiftOut:];
-[BWPreviewGyroStabilization initForStillImagePreview:];
```
