# `TUVideoDeviceControllerProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVConferencePreviewClientDelegate`, `AVCPreviewCameraSessionDelegate`, `TUVideoDeviceControllerProvider`
- 8 instance variables, 27 properties, 88 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _cachedInputDevices;
@"NSArray" _cachedSecondaryInputDevices;
B _primarySessionEnabled;
B _secondarySessionEnabled;
B _isAVCaptureDeviceReady;
@"<TUVideoDeviceControllerProviderDelegate>" _delegate;
@"AVConferencePreview" _preview;
@"TUFeatureFlags" _featureFlags;
```

## Properties

```
@property (T@"AVConferencePreview",R,N,V_preview) preview;
@property (T@"TUFeatureFlags",R,N,V_featureFlags) featureFlags;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisPreviewRunning) previewRunning;
@property (T@"NSString",R,C,N) localCameraUID;
@property (T@"NSArray",R,C,N) inputDevices;
@property (T@"VideoAttributes",C,N) localVideoAttributes;
@property (TB,N,GisCinematicFramingEnabled) cinematicFramingEnabled;
@property (TB,N,GisReactionEffectGestureEnabled) reactionEffectGestureEnabled;
@property (TB,N,GisStudioLightEnabled) studioLightEnabled;
@property (TB,N,GisCameraBlurEnabled) cameraBlurEnabled;
@property (TB,R,N) hasAvailableDeskViewCameras;
@property (TB,R,N) shouldMirrorMemoji;
@property (TB,R,N) memojiWithoutDepthEnabled;
@property (TB,R,N) dualCameraCaptureSendingSupported;
@property (T@"<TUVideoDeviceControllerProviderDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,C,N) secondaryInputDevices;
@property (T@"NSString",C,N) secondaryCameraUID;
@property (T@"VideoAttributes",C,N) secondaryVideoAttributes;
@property (TB,R,N) secondaryCameraZoomAvailable;
@property (Td,R,N) secondaryCameraZoomFactor;
@property (Td,R,N) secondaryCameraMaxZoomFactor;
@property (TB,N,GisPrimarySessionEnabled) primarySessionEnabled;
@property (TB,N,GisSecondarySessionEnabled) secondarySessionEnabled;
```

## Class methods

```
+[TUVideoDeviceControllerProvider prewarm];
```

## Instance methods

```
-[TUVideoDeviceControllerProvider beginPreviewToPIPAnimation];
-[TUVideoDeviceControllerProvider preview];
-[TUVideoDeviceControllerProvider setCameraZoomFactor:];
-[TUVideoDeviceControllerProvider isStudioLightEnabled];
-[TUVideoDeviceControllerProvider setLocalVideoAttributes:];
-[TUVideoDeviceControllerProvider isCinematicFramingEnabled];
-[TUVideoDeviceControllerProvider notifyCenterStageEnabled:];
-[TUVideoDeviceControllerProvider didChangeLocalVideoAttributes:];
-[TUVideoDeviceControllerProvider setPreviewPresentationOrientation:];
-[TUVideoDeviceControllerProvider secondaryCameraZoomFactor];
-[TUVideoDeviceControllerProvider didStartPreview];
-[TUVideoDeviceControllerProvider didGetSnapshot:];
-[TUVideoDeviceControllerProvider pausePreview];
-[TUVideoDeviceControllerProvider setBackgroundReplacementEnabled:];
-[TUVideoDeviceControllerProvider localVideoAttributes];
-[TUVideoDeviceControllerProvider endPIPToPreviewAnimation];
-[TUVideoDeviceControllerProvider cameraDidBecomeAvailableForUniqueID:];
-[TUVideoDeviceControllerProvider localVideoLayer:];
-[TUVideoDeviceControllerProvider didPausePreview];
-[TUVideoDeviceControllerProvider beginPIPToPreviewAnimation];
-[TUVideoDeviceControllerProvider isPreviewRunning];
-[TUVideoDeviceControllerProvider localScreenAttributesForVideoAttributes:];
-[TUVideoDeviceControllerProvider setCinematicFramingEnabled:];
-[TUVideoDeviceControllerProvider stopPreview];
-[TUVideoDeviceControllerProvider memojiWithoutDepthEnabled];
-[TUVideoDeviceControllerProvider localCameraUID];
-[TUVideoDeviceControllerProvider rampCameraZoomFactor:withRate:];
-[TUVideoDeviceControllerProvider setSecondaryCameraUID:];
-[TUVideoDeviceControllerProvider didStopPreview];
-[TUVideoDeviceControllerProvider startPreview];
-[TUVideoDeviceControllerProvider setPrimarySessionEnabled:];
-[TUVideoDeviceControllerProvider observeValueForKeyPath:ofObject:change:context:];
-[TUVideoDeviceControllerProvider setLocalScreenAttributes:];
-[TUVideoDeviceControllerProvider endPreviewToPIPAnimation];
-[TUVideoDeviceControllerProvider didChangeLocalCameraUID:];
-[TUVideoDeviceControllerProvider getSnapshot];
-[TUVideoDeviceControllerProvider cameraDidBecomeInterruptedForForUniqueID:reason:];
-[TUVideoDeviceControllerProvider setLocalVideoLayerHost:front:];
-[TUVideoDeviceControllerProvider init];
-[TUVideoDeviceControllerProvider setSecondaryVideoAttributes:];
-[TUVideoDeviceControllerProvider isReactionEffectGestureEnabled];
-[TUVideoDeviceControllerProvider queryAVCaptureDeviceIfNeeded];
-[TUVideoDeviceControllerProvider secondaryVideoAttributes];
-[TUVideoDeviceControllerProvider secondaryCameraZoomAvailable];
-[TUVideoDeviceControllerProvider dealloc];
-[TUVideoDeviceControllerProvider isSecondarySessionEnabled];
-[TUVideoDeviceControllerProvider secondaryCameraMaxZoomFactor];
-[TUVideoDeviceControllerProvider cameraSession:didUpdateZoomAvailability:zoomFactor:maxZoomFactor:];
-[TUVideoDeviceControllerProvider didReceiveFirstPreviewFrameForCameraSession:];
-[TUVideoDeviceControllerProvider setSecondarySessionEnabled:];
-[TUVideoDeviceControllerProvider setLocalCameraWithUID:];
-[TUVideoDeviceControllerProvider didReceiveErrorFromCameraUniqueID:error:];
-[TUVideoDeviceControllerProvider setCameraBlurEnabled:];
-[TUVideoDeviceControllerProvider cameraSession:didEnableCapture:error:];
-[TUVideoDeviceControllerProvider setLocalVideoLayer:front:];
-[TUVideoDeviceControllerProvider cameraSession:didSetCameraUID:error:];
-[TUVideoDeviceControllerProvider supportsCameraBlurForDevice:];
-[TUVideoDeviceControllerProvider cameraSession:didUpdateZoomAvailability:];
-[TUVideoDeviceControllerProvider setDelegate:];
-[TUVideoDeviceControllerProvider hasAvailableDeskViewCameras];
-[TUVideoDeviceControllerProvider invalidateInputDevicesCache];
-[TUVideoDeviceControllerProvider cameraCinematicFramingAvailabilityDidChange:];
-[TUVideoDeviceControllerProvider didReceiveFirstPreviewFrameFromCameraUniqueID:];
-[TUVideoDeviceControllerProvider setSecondaryCameraZoomFactor:];
-[TUVideoDeviceControllerProvider isCameraBlurEnabled];
-[TUVideoDeviceControllerProvider didDetectSensitiveContentWithAnalysis:];
-[TUVideoDeviceControllerProvider delegate];
-[TUVideoDeviceControllerProvider rampSecondaryCameraZoomFactor:withRate:];
-[TUVideoDeviceControllerProvider secondaryCameraUID];
-[TUVideoDeviceControllerProvider dualCameraCaptureSendingSupported];
-[TUVideoDeviceControllerProvider queryAVCaptureDeviceWithType:mediaType:position:];
-[TUVideoDeviceControllerProvider shouldMirrorMemoji];
-[TUVideoDeviceControllerProvider secondaryInputDevices];
-[TUVideoDeviceControllerProvider captureDevicesChanged:];
-[TUVideoDeviceControllerProvider setPrimaryCameraUID:secondaryCameraUID:useSquareAspectRatio:completionHandler:];
-[TUVideoDeviceControllerProvider isPrimarySessionEnabled];
-[TUVideoDeviceControllerProvider cameraSession:didUpdateVideoAttributes:];
-[TUVideoDeviceControllerProvider setStudioLightEnabled:];
-[TUVideoDeviceControllerProvider appendFriendModeCamerasToDevices:];
-[TUVideoDeviceControllerProvider currentBackgroundBlurControlMode];
-[TUVideoDeviceControllerProvider setReactionEffectGestureEnabled:];
-[TUVideoDeviceControllerProvider cameraSession:didReceiveError:];
-[TUVideoDeviceControllerProvider centerStageAvailableChangedNotification:];
-[TUVideoDeviceControllerProvider cameraZoomAvailabilityDidChange:];
-[TUVideoDeviceControllerProvider setCurrentBackgroundBlurControlMode:];
-[TUVideoDeviceControllerProvider isBackgroundReplacementEnabled];
-[TUVideoDeviceControllerProvider inputDevices];
-[TUVideoDeviceControllerProvider featureFlags];
```
