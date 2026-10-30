# `AVCaptureVideoPreviewLayer`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- Protocols: `AVCapturePreviewMonitor`
- 1 instance variables, 15 properties, 116 instance methods, 3 class methods

## Instance variables

```
@"AVCaptureVideoPreviewLayerInternal" _internal;
```

## Properties

```
@property (T@"AVCaptureSession",&,N) session;
@property (T@"AVCaptureConnection",R,N) connection;
@property (T@"NSString",C) videoGravity;
@property (TB,R,N,GisPreviewing) previewing;
@property (TB,R,N,GisOrientationSupported) orientationSupported;
@property (Tq,N) orientation;
@property (TB,R,N,GisMirroringSupported) mirroringSupported;
@property (TB,N) automaticallyAdjustsMirroring;
@property (TB,N,GisMirrored) mirrored;
@property (TB,R,N,GisDeferredStartSupported) deferredStartSupported;
@property (TB,N,GisDeferredStartEnabled) deferredStartEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureVideoPreviewLayer initialize];
+[AVCaptureVideoPreviewLayer layerWithSession:];
+[AVCaptureVideoPreviewLayer layerWithSessionWithNoConnection:];
```

## Instance methods

```
-[AVCaptureVideoPreviewLayer setOrientation:];
-[AVCaptureVideoPreviewLayer canAddConnection:failureReason:];
-[AVCaptureVideoPreviewLayer didUpdatePreviewFormatDescription:];
-[AVCaptureVideoPreviewLayer isPortraitAutoSuggestEnabled];
-[AVCaptureVideoPreviewLayer isPaused];
-[AVCaptureVideoPreviewLayer captureDevicePointOfInterestForPoint:];
-[AVCaptureVideoPreviewLayer _setSensorAndEstimatedPreviewSizes];
-[AVCaptureVideoPreviewLayer didUpdatePreviewImageQueueSlot:imageQueue:rotationDegrees:size:];
-[AVCaptureVideoPreviewLayer _handleNotification:payload:];
-[AVCaptureVideoPreviewLayer _updatePreviewTransforms];
-[AVCaptureVideoPreviewLayer transformedMetadataObjectForMetadataObject:];
-[AVCaptureVideoPreviewLayer observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureVideoPreviewLayer weakReference];
-[AVCaptureVideoPreviewLayer rectForMetadataOutputRectOfInterest:];
-[AVCaptureVideoPreviewLayer _updateTransformForMetadataOutputCorrections:];
-[AVCaptureVideoPreviewLayer changeSeed];
-[AVCaptureVideoPreviewLayer setSemanticStyleRenderingEnabled:];
-[AVCaptureVideoPreviewLayer imageQueueSlot];
-[AVCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:applyDynamicAspectRatio:];
-[AVCaptureVideoPreviewLayer init];
-[AVCaptureVideoPreviewLayer centerSublayer:];
-[AVCaptureVideoPreviewLayer clientShowingViewfinder:];
-[AVCaptureVideoPreviewLayer _isMirrored];
-[AVCaptureVideoPreviewLayer didBeginGraphBuild];
-[AVCaptureVideoPreviewLayer isPortraitAutoSuggestSupported];
-[AVCaptureVideoPreviewLayer orientation];
-[AVCaptureVideoPreviewLayer detachSafelyFromFigCaptureSession:];
-[AVCaptureVideoPreviewLayer _zoomPictureInPictureOverlaySupported];
-[AVCaptureVideoPreviewLayer dealloc];
-[AVCaptureVideoPreviewLayer viewfinderClosedForReconfiguring];
-[AVCaptureVideoPreviewLayer _initWithSession:makeConnection:];
-[AVCaptureVideoPreviewLayer _orientation];
-[AVCaptureVideoPreviewLayer willStartRunningSession];
-[AVCaptureVideoPreviewLayer didStopRunningSession];
-[AVCaptureVideoPreviewLayer _previewMonitorTimeout];
-[AVCaptureVideoPreviewLayer _updatePreferredDynamicRangeForFirstPreviewFrameDisplayed:];
-[AVCaptureVideoPreviewLayer _updateCaptureDeviceTransform];
-[AVCaptureVideoPreviewLayer setVideoPreviewFilters:];
-[AVCaptureVideoPreviewLayer setCaptureDeviceTransformNeedsUpdate];
-[AVCaptureVideoPreviewLayer metadataOutputRectOfInterestForRect:];
-[AVCaptureVideoPreviewLayer clientWantsPreviewDisplayedBySession:];
-[AVCaptureVideoPreviewLayer initWithLayer:];
-[AVCaptureVideoPreviewLayer _updateZoomPIPOverlayRect:];
-[AVCaptureVideoPreviewLayer isDeferredStartEnabled];
-[AVCaptureVideoPreviewLayer isMirrored];
-[AVCaptureVideoPreviewLayer setBounds:];
-[AVCaptureVideoPreviewLayer setZoomPictureInPictureOverlayEnabled:];
-[AVCaptureVideoPreviewLayer _updateSemanticStyleRenderingSupported];
-[AVCaptureVideoPreviewLayer _previewMonitorDidDisplayFirstPreviewFrame];
-[AVCaptureVideoPreviewLayer bumpChangeSeed];
-[AVCaptureVideoPreviewLayer isZoomPictureInPictureOverlayEnabled];
-[AVCaptureVideoPreviewLayer isFilterRenderingEnabled];
-[AVCaptureVideoPreviewLayer setSession:];
-[AVCaptureVideoPreviewLayer setPaused:];
-[AVCaptureVideoPreviewLayer videoPreviewFilters];
-[AVCaptureVideoPreviewLayer _filtersAreOptimized:exceptionReason:];
-[AVCaptureVideoPreviewLayer _previewMonitorPreviewDisplaying];
-[AVCaptureVideoPreviewLayer isOrientationSupported];
-[AVCaptureVideoPreviewLayer layerDidBecomeVisible:];
-[AVCaptureVideoPreviewLayer setMirrored:];
-[AVCaptureVideoPreviewLayer handleChangedActiveFormat:forDevice:];
-[AVCaptureVideoPreviewLayer isSemanticStyleRenderingEnabled];
-[AVCaptureVideoPreviewLayer isDepthDataDeliveryEnabled];
-[AVCaptureVideoPreviewLayer undimLayerWithAnimationDuration:];
-[AVCaptureVideoPreviewLayer _previewMonitorExpectingPreviewDisplayed];
-[AVCaptureVideoPreviewLayer semanticStyle];
-[AVCaptureVideoPreviewLayer sessionWantsPreviewStopped];
-[AVCaptureVideoPreviewLayer setSessionWithNoConnection:];
-[AVCaptureVideoPreviewLayer detachFromFigCaptureSession:];
-[AVCaptureVideoPreviewLayer videoGravity];
-[AVCaptureVideoPreviewLayer connection];
-[AVCaptureVideoPreviewLayer setSemanticStyle:animated:];
-[AVCaptureVideoPreviewLayer setUnoptimizedFilterRenderingEnabled:];
-[AVCaptureVideoPreviewLayer isDepthDataDeliverySupported];
-[AVCaptureVideoPreviewLayer layoutSublayers];
-[AVCaptureVideoPreviewLayer enableLaunchTelemetry];
-[AVCaptureVideoPreviewLayer initWithSessionWithNoConnection:];
-[AVCaptureVideoPreviewLayer setAutomaticallyAdjustsMirroring:];
-[AVCaptureVideoPreviewLayer _activatePreviewMonitorTimeoutTimerIfNeeded];
-[AVCaptureVideoPreviewLayer isZoomPictureInPictureOverlaySupported];
-[AVCaptureVideoPreviewLayer setFilterRenderingEnabled:];
-[AVCaptureVideoPreviewLayer previewRotationDegrees];
-[AVCaptureVideoPreviewLayer _automaticallyAdjustsMirroring];
-[AVCaptureVideoPreviewLayer _updateDepthDataDeliverySupported];
-[AVCaptureVideoPreviewLayer initWithSession:];
-[AVCaptureVideoPreviewLayer setVideoGravity:];
-[AVCaptureVideoPreviewLayer setDepthDataDeliveryEnabled:];
-[AVCaptureVideoPreviewLayer connectionMediaTypes];
-[AVCaptureVideoPreviewLayer attachToFigCaptureSession:];
-[AVCaptureVideoPreviewLayer _setPortraitLightingEffectStrengthFromDeviceInput];
-[AVCaptureVideoPreviewLayer removeConnection:];
-[AVCaptureVideoPreviewLayer setSinkID:];
-[AVCaptureVideoPreviewLayer performFigCaptureSessionOperationSafelyUsingBlock:];
-[AVCaptureVideoPreviewLayer session];
-[AVCaptureVideoPreviewLayer _setVideoPreviewFilters:checkForExceptionalInput:exceptionReason:];
-[AVCaptureVideoPreviewLayer pointForCaptureDevicePointOfInterest:];
-[AVCaptureVideoPreviewLayer _setSimulatedApertureFromDeviceInput];
-[AVCaptureVideoPreviewLayer setDeferredStartEnabled:];
-[AVCaptureVideoPreviewLayer _input];
-[AVCaptureVideoPreviewLayer isDeferredStartSupported];
-[AVCaptureVideoPreviewLayer isUnoptimizedFilterRenderingEnabled];
-[AVCaptureVideoPreviewLayer attachSafelyToFigCaptureSession:];
-[AVCaptureVideoPreviewLayer sinkID];
-[AVCaptureVideoPreviewLayer previewMonitor];
-[AVCaptureVideoPreviewLayer isPreviewing];
-[AVCaptureVideoPreviewLayer setPortraitAutoSuggestEnabled:];
-[AVCaptureVideoPreviewLayer _updatePortraitAutoSuggestSupported];
-[AVCaptureVideoPreviewLayer _updateZoomPictureInPictureOverlaySupported];
-[AVCaptureVideoPreviewLayer zoomPictureInPictureOverlayRect];
-[AVCaptureVideoPreviewLayer automaticallyAdjustsMirroring];
-[AVCaptureVideoPreviewLayer isMirroringSupported];
-[AVCaptureVideoPreviewLayer dimLayerWithAnimationDuration:undimOnNextFirstPreviewFrame:];
-[AVCaptureVideoPreviewLayer addConnection:error:];
-[AVCaptureVideoPreviewLayer _activatePreviewMonitorTimeoutTimer];
-[AVCaptureVideoPreviewLayer isSemanticStyleRenderingSupported];
-[AVCaptureVideoPreviewLayer _cancelPreviewMonitorTimeoutTimer];
```
