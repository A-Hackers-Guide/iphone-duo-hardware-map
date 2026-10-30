# `AVCaptureMetadataOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureOutput`
- Protocols: `AVCaptureDataOutputDelegateOverride`
- 1 instance variables, 12 properties, 113 instance methods, 3 class methods

## Instance variables

```
@"AVCaptureMetadataOutputInternal" _internal;
```

## Properties

```
@property (T@"<AVCaptureMetadataOutputObjectsDelegate>",R,N) metadataObjectsDelegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) metadataObjectsCallbackQueue;
@property (T@"NSArray",R,N) availableMetadataObjectTypes;
@property (T@"NSArray",C,N) metadataObjectTypes;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) rectOfInterest;
@property (T@"NSArray",R,N) requiredMetadataObjectTypesForCinematicVideoCapture;
@property (T@,R,N) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateOverrideCallbackQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureMetadataOutput initialize];
+[AVCaptureMetadataOutput new];
+[AVCaptureMetadataOutput _metadataConstantValueToName:];
```

## Instance methods

```
-[AVCaptureMetadataOutput setRawFrameDeliveryEnabled:];
-[AVCaptureMetadataOutput canAddConnection:failureReason:];
-[AVCaptureMetadataOutput isFaceOcclusionDetectionEnabled];
-[AVCaptureMetadataOutput setEmitsEmptyObjectDetectionMetadata:];
-[AVCaptureMetadataOutput setMetadataObjectTypesForPerceptionThumbnailChannel:];
-[AVCaptureMetadataOutput emitsEmptyObjectDetectionMetadata];
-[AVCaptureMetadataOutput _metadataIdentifiersForPerceptionThumbnailChannel];
-[AVCaptureMetadataOutput _handleNotification:payload:];
-[AVCaptureMetadataOutput setFaceTrackingMetadataObjectTypesAvailable:];
-[AVCaptureMetadataOutput rawFrameDeliverySupported];
-[AVCaptureMetadataOutput _processSampleBuffer:];
-[AVCaptureMetadataOutput metadataObjectTypesForMetadataIdentifiers:];
-[AVCaptureMetadataOutput setLightSourceEstimationAmbientLuminance:];
-[AVCaptureMetadataOutput maxSynchronizationFrameDelay];
-[AVCaptureMetadataOutput _newEmitTimerForSynchronizedMetadataCollections:];
-[AVCaptureMetadataOutput setOfflineVideoStabilizationMotionMetadataObjectTypesAvailable:];
-[AVCaptureMetadataOutput isAppClipCodeMetadataObjectTypeAvailable];
-[AVCaptureMetadataOutput motionToWakeTargetFrameRate];
-[AVCaptureMetadataOutput init];
-[AVCaptureMetadataOutput _handleLocalQueueMessage:];
-[AVCaptureMetadataOutput setAttentionDetectionEnabled:];
-[AVCaptureMetadataOutput isSceneClassificationMetadataSupported];
-[AVCaptureMetadataOutput setSceneClassificationMetadataObjectTypeAvailable:];
-[AVCaptureMetadataOutput lightSourceEstimationAmbientLuminance];
-[AVCaptureMetadataOutput isAppClipCodeMetadataSupported];
-[AVCaptureMetadataOutput detachSafelyFromFigCaptureSession:];
-[AVCaptureMetadataOutput dealloc];
-[AVCaptureMetadataOutput isSceneClassificationMetadataObjectTypeAvailable];
-[AVCaptureMetadataOutput _metadataIdentifiers];
-[AVCaptureMetadataOutput deviceProximityDetectionDeviceTypes];
-[AVCaptureMetadataOutput _removeMetadataObjectTypesFromMetadataObjectTypes:];
-[AVCaptureMetadataOutput metadataObjectTypesSupportingZeroFrameDelaySynchronization];
-[AVCaptureMetadataOutput _emitSyncedCollections:];
-[AVCaptureMetadataOutput isAttentionDetectionEnabled];
-[AVCaptureMetadataOutput setRectOfInterest:];
-[AVCaptureMetadataOutput setTextRegionMetadataObjectTypeAvailable:];
-[AVCaptureMetadataOutput _processSynchronizationWithCollections:withCorrespondingMetadataObjectTypes:];
-[AVCaptureMetadataOutput setMetadataObjectsDelegate:queue:];
-[AVCaptureMetadataOutput isHeadMetadataObjectTypesAvailable];
-[AVCaptureMetadataOutput setHumanHandMetadataObjectTypeAvailable:];
-[AVCaptureMetadataOutput isPeriocularForFaceIDReadinessEnabled];
-[AVCaptureMetadataOutput captureFaceIDBracketWithConfiguration:];
-[AVCaptureMetadataOutput setMetadataObjectTypes:];
-[AVCaptureMetadataOutput isHumanHandMetadataSupported];
-[AVCaptureMetadataOutput lightSourceEstimationTargetFrameRate];
-[AVCaptureMetadataOutput _updateRemoteQueue:];
-[AVCaptureMetadataOutput setHeadMetadataObjectTypesAvailable:];
-[AVCaptureMetadataOutput setAttentionForFaceIDReadinessRequired:];
-[AVCaptureMetadataOutput _updateSynchronizationEnabledStatus];
-[AVCaptureMetadataOutput isFaceTrackingPlusEnabled];
-[AVCaptureMetadataOutput isFaceTrackingUsingFaceRecognition];
-[AVCaptureMetadataOutput isFaceTrackingSuspended];
-[AVCaptureMetadataOutput supportedMetadataObjectTypesForFrameRateControl];
-[AVCaptureMetadataOutput supportedMetadataObjectTypesForPerceptionThumbnailChannel];
-[AVCaptureMetadataOutput isHeadMetadataSupported];
-[AVCaptureMetadataOutput handleChangedActiveFormat:forDevice:];
-[AVCaptureMetadataOutput isHumanHandMetadataObjectTypeAvailable];
-[AVCaptureMetadataOutput setMaxSynchronizationFrameDelay:];
-[AVCaptureMetadataOutput deviceProximityDetectionTargetFrameRate];
-[AVCaptureMetadataOutput faceIDConfiguration];
-[AVCaptureMetadataOutput rawFrameDeliveryEnabled];
-[AVCaptureMetadataOutput _activeVideoMaxFrameDurationInSeconds];
-[AVCaptureMetadataOutput isFaceTrackingMetadataObjectTypesAvailable];
-[AVCaptureMetadataOutput isSynchronizationEnabled];
-[AVCaptureMetadataOutput isFaceOcclusionDetectionSupported];
-[AVCaptureMetadataOutput isAttentionDetectionSupported];
-[AVCaptureMetadataOutput isOfflineVideoStabilizationMotionMetadataObjectTypesAvailable];
-[AVCaptureMetadataOutput setAppClipCodeMetadataObjectTypeAvailable:];
-[AVCaptureMetadataOutput requiredMetadataObjectTypesForCinematicVideoCapture];
-[AVCaptureMetadataOutput isTextRegionMetadataSupported];
-[AVCaptureMetadataOutput setDeviceProximityDetectionDeviceTypes:];
-[AVCaptureMetadataOutput setFaceTrackingSuspended:];
-[AVCaptureMetadataOutput _flushSynchronizedMetadataCollectionsQueue];
-[AVCaptureMetadataOutput faceTrackingFailureFieldOfViewModifier];
-[AVCaptureMetadataOutput isFaceTrackingSupported];
-[AVCaptureMetadataOutput _removeMetadataObjectTypeFromMetadataObjectTypes:];
-[AVCaptureMetadataOutput setSynchronizationEnabled:];
-[AVCaptureMetadataOutput setPerceptionTestModeEnabled:];
-[AVCaptureMetadataOutput setFaceTrackingPlusEnabled:];
-[AVCaptureMetadataOutput rectOfInterest];
-[AVCaptureMetadataOutput _setSynchronizationEnabledBySynchronizer:];
-[AVCaptureMetadataOutput _handleRemoteQueueOperation:];
-[AVCaptureMetadataOutput connectionMediaTypes];
-[AVCaptureMetadataOutput setFaceOcclusionDetectionEnabled:];
-[AVCaptureMetadataOutput setFaceTrackingFailureFieldOfViewModifier:];
-[AVCaptureMetadataOutput metadataObjectTypesForPerceptionThumbnailChannel];
-[AVCaptureMetadataOutput setFaceTrackingUsesFaceRecognition:];
-[AVCaptureMetadataOutput _updateLocalQueue:];
-[AVCaptureMetadataOutput _emitCollections:];
-[AVCaptureMetadataOutput availableMetadataObjectTypes];
-[AVCaptureMetadataOutput setVideoPreviewHistogramMetadataObjectTypesAvailable:];
-[AVCaptureMetadataOutput perceptionTestModeEnabled];
-[AVCaptureMetadataOutput setPeriocularForFaceIDReadinessEnabled:];
-[AVCaptureMetadataOutput delegateOverrideCallbackQueue];
-[AVCaptureMetadataOutput setFaceIDConfiguration:];
-[AVCaptureMetadataOutput isVideoPreviewHistogramMetadataSupported];
-[AVCaptureMetadataOutput setFaceTrackingNetworkFailureThresholdMultiplier:];
-[AVCaptureMetadataOutput attachSafelyToFigCaptureSession:];
-[AVCaptureMetadataOutput isTextRegionMetadataObjectTypeAvailable];
-[AVCaptureMetadataOutput setFaceTrackingMaxFaces:];
-[AVCaptureMetadataOutput isOfflineVideoStabilizationMotionMetadataSupported];
-[AVCaptureMetadataOutput setDelegateOverride:delegateOverrideCallbackQueue:];
-[AVCaptureMetadataOutput metadataIdentifiersForMetadataObjectTypes:];
-[AVCaptureMetadataOutput setTargetFrameRate:forMetadataObjectType:];
-[AVCaptureMetadataOutput isVideoPreviewHistogramMetadataObjectTypesAvailable];
-[AVCaptureMetadataOutput faceTrackingNetworkFailureThresholdMultiplier];
-[AVCaptureMetadataOutput isAttentionForFaceIDReadinessRequired];
-[AVCaptureMetadataOutput metadataObjectsDelegate];
-[AVCaptureMetadataOutput metadataObjectTypes];
-[AVCaptureMetadataOutput objectDetectionTargetFrameRate];
-[AVCaptureMetadataOutput faceTrackingMaxFaces];
-[AVCaptureMetadataOutput delegateOverride];
-[AVCaptureMetadataOutput metadataObjectsCallbackQueue];
```
