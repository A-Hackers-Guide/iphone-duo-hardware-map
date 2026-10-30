# `AVCaptureVisionDataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- Protocols: `AVCaptureDataOutputDelegateOverride`
- 1 instance variables, 34 properties, 75 instance methods, 2 class methods

## Instance variables

```
@"AVCaptureVisionDataOutputInternal" _internal;
```

## Properties

```
@property (T@"<AVCaptureVisionDataOutputDelegate>",R,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateCallbackQueue;
@property (T{?=qiIq},N) minFrameDuration;
@property (T{?=qiIq},N) minBurstFrameDuration;
@property (T{?=qiIq},N) maxBurstDuration;
@property (TQ,N) gaussianPyramidOctavesCount;
@property (Tf,N) gaussianPyramidBaseOctaveDownscalingFactor;
@property (TQ,N) maxKeypointsCount;
@property (TB,N,GisFeatureBinningEnabled) featureBinningEnabled;
@property (TB,N,GisFeatureOrientationAssignmentEnabled) featureOrientationAssignmentEnabled;
@property (TB,R,N,GisDynamicThresholdingSupported) dynamicThresholdingSupported;
@property (TB,N,GisDynamicThresholdingEnabled) dynamicThresholdingEnabled;
@property (TQ,N) keypointDetectionFlowType;
@property (TB,R,N,GisSubPixelThresholdSupported) subPixelThresholdSupported;
@property (TQ,N) subPixelThreshold;
@property (TB,R,N,GisFeatureMatchingSupported) featureMatchingSupported;
@property (TB,N,GisFeatureMatchingEnabled) featureMatchingEnabled;
@property (TQ,N) featureMatchingDescriptorSize;
@property (TB,R,N,GisOrientationDistanceThresholdSupported) orientationDistanceThresholdSupported;
@property (Tf,N) orientationDistanceThreshold;
@property (TB,R,N,GisSigmaDistanceThresholdSupported) sigmaDistanceThresholdSupported;
@property (Tf,N) sigmaDistanceThreshold;
@property (TB,R,N,GisSquareDistanceDisparityFractionSupported) squareDistanceDisparityFractionSupported;
@property (Tf,N) squareDistanceDisparityFraction;
@property (TB,R,N,GisHammingDistanceThresholdSupported) hammingDistanceThresholdSupported;
@property (TQ,N) hammingDistanceThreshold;
@property (TB,R,N,GisLACCConfigAndMetadataSupported) laccConfigAndMetadataSupported;
@property (T@"NSData",&,N) laccConfigAndMetadata;
@property (T@,R,N) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateOverrideCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureVisionDataOutput initialize];
+[AVCaptureVisionDataOutput new];
```

## Instance methods

```
-[AVCaptureVisionDataOutput canAddConnection:failureReason:];
-[AVCaptureVisionDataOutput isDynamicThresholdingEnabled];
-[AVCaptureVisionDataOutput _handleNotification:payload:];
-[AVCaptureVisionDataOutput setOrientationDistanceThreshold:];
-[AVCaptureVisionDataOutput _processSampleBuffer:];
-[AVCaptureVisionDataOutput appliesOrientationWithPhysicalRotationForConnection:];
-[AVCaptureVisionDataOutput laccConfigAndMetadata];
-[AVCaptureVisionDataOutput minFrameDuration];
-[AVCaptureVisionDataOutput init];
-[AVCaptureVisionDataOutput _handleLocalQueueMessage:];
-[AVCaptureVisionDataOutput appliesMirroringWithPhysicalFlipForConnection:];
-[AVCaptureVisionDataOutput setMinFrameDuration:];
-[AVCaptureVisionDataOutput gaussianPyramidBaseOctaveDownscalingFactor];
-[AVCaptureVisionDataOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureVisionDataOutput dealloc];
-[AVCaptureVisionDataOutput maxKeypointsCount];
-[AVCaptureVisionDataOutput orientationDistanceThreshold];
-[AVCaptureVisionDataOutput setFeatureMatchingEnabled:];
-[AVCaptureVisionDataOutput maxBurstDuration];
-[AVCaptureVisionDataOutput setMaxKeypointsCount:];
-[AVCaptureVisionDataOutput _updateRemoteQueue:];
-[AVCaptureVisionDataOutput setLaccConfigAndMetadata:];
-[AVCaptureVisionDataOutput keypointDetectionThreshold];
-[AVCaptureVisionDataOutput isFeatureMatchingEnabled];
-[AVCaptureVisionDataOutput setKeypointDetectionFlowType:];
-[AVCaptureVisionDataOutput handleChangedActiveFormat:forDevice:];
-[AVCaptureVisionDataOutput setMaxBurstDuration:];
-[AVCaptureVisionDataOutput setFeatureMatchingDescriptorSize:];
-[AVCaptureVisionDataOutput squareDistanceDisparityFraction];
-[AVCaptureVisionDataOutput featureMatchingDescriptorSize];
-[AVCaptureVisionDataOutput gaussianPyramidOctavesCount];
-[AVCaptureVisionDataOutput setSubPixelThreshold:];
-[AVCaptureVisionDataOutput delegate];
-[AVCaptureVisionDataOutput setGaussianPyramidBaseOctaveDownscalingFactor:];
-[AVCaptureVisionDataOutput setHammingDistanceThreshold:];
-[AVCaptureVisionDataOutput setKeypointDetectionThreshold:];
-[AVCaptureVisionDataOutput delegateCallbackQueue];
-[AVCaptureVisionDataOutput _handleRemoteQueueOperation:];
-[AVCaptureVisionDataOutput connectionMediaTypes];
-[AVCaptureVisionDataOutput sigmaDistanceThreshold];
-[AVCaptureVisionDataOutput removeConnection:];
-[AVCaptureVisionDataOutput _updateLocalQueue:];
-[AVCaptureVisionDataOutput setFeatureOrientationAssignmentEnabled:];
-[AVCaptureVisionDataOutput subPixelThreshold];
-[AVCaptureVisionDataOutput delegateOverrideCallbackQueue];
-[AVCaptureVisionDataOutput attachSafelyToFigCaptureSession:];
-[AVCaptureVisionDataOutput keypointDetectionFlowType];
-[AVCaptureVisionDataOutput setFeatureBinningEnabled:];
-[AVCaptureVisionDataOutput setDelegateOverride:delegateOverrideCallbackQueue:];
-[AVCaptureVisionDataOutput setRuntimeUpdates:];
-[AVCaptureVisionDataOutput setSigmaDistanceThreshold:];
-[AVCaptureVisionDataOutput setDynamicThresholdingEnabled:];
-[AVCaptureVisionDataOutput setGaussianPyramidOctavesCount:];
-[AVCaptureVisionDataOutput hammingDistanceThreshold];
-[AVCaptureVisionDataOutput setSquareDistanceDisparityFraction:];
-[AVCaptureVisionDataOutput addConnection:error:];
-[AVCaptureVisionDataOutput delegateOverride];
-[AVCaptureVisionDataOutput _initializeClientVisiblePropertiesForSourceDevice:];
-[AVCaptureVisionDataOutput _isPropertySupported:];
-[AVCaptureVisionDataOutput areRuntimeUpdatesSupported];
-[AVCaptureVisionDataOutput isDynamicThresholdingSupported];
-[AVCaptureVisionDataOutput isFeatureBinningEnabled];
-[AVCaptureVisionDataOutput isFeatureMatchingSupported];
-[AVCaptureVisionDataOutput isFeatureOrientationAssignmentEnabled];
-[AVCaptureVisionDataOutput isHammingDistanceThresholdSupported];
-[AVCaptureVisionDataOutput isKeypointDetectionFlowTypeSupported:];
-[AVCaptureVisionDataOutput isLACCConfigAndMetadataSupported];
-[AVCaptureVisionDataOutput isOrientationDistanceThresholdSupported];
-[AVCaptureVisionDataOutput isSigmaDistanceThresholdSupported];
-[AVCaptureVisionDataOutput isSquareDistanceDisparityFractionSupported];
-[AVCaptureVisionDataOutput isSubPixelThresholdSupported];
-[AVCaptureVisionDataOutput minBurstFrameDuration];
-[AVCaptureVisionDataOutput setDelegate:callbackQueue:];
-[AVCaptureVisionDataOutput setMinBurstFrameDuration:];
-[AVCaptureVisionDataOutput triggerBurst];
```
