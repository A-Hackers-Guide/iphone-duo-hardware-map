# `TUVideoDeviceController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUVideoDeviceControllerProviderDelegate`
- 18 instance variables, 56 properties, 139 instance methods, 4 class methods

## Instance variables

```
B _secondaryCameraRunning;
B _ignoreStartPreview;
B _wantsPreview;
B _hasRefreshedPreviewAfterError;
B _hasBeganRetryingAfterUninitializedClientError;
B _retryAfterLocalCameraUIDChange;
B _secondaryZoomAvailable;
@"NSString" _primaryCameraOverrideUID;
@"NSString" _secondaryCameraOverrideUID;
@"CALayer" _localFrontLayerHost;
@"CALayer" _localBackLayerHost;
@? _reapplySecondaryCameraZoom;
@? _reapplyCameraZoom;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"<TUVideoDeviceControllerProvider>" _provider;
@"<TUFeatureFlags>" _featureFlags;
@? _previewStartBlock;
q _uninitializedClientRetrySeconds;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_serialQueue) serialQueue;
@property (T@"<TUVideoDeviceControllerProvider>",R,N,V_provider) provider;
@property (T@"<TUFeatureFlags>",R,N,V_featureFlags) featureFlags;
@property (TB,N,V_wantsPreview) wantsPreview;
@property (TB,N,V_hasRefreshedPreviewAfterError) hasRefreshedPreviewAfterError;
@property (T@?,C,N,V_previewStartBlock) previewStartBlock;
@property (TB,N,V_hasBeganRetryingAfterUninitializedClientError) hasBeganRetryingAfterUninitializedClientError;
@property (Tq,N,V_uninitializedClientRetrySeconds) uninitializedClientRetrySeconds;
@property (TB,N,V_retryAfterLocalCameraUIDChange) retryAfterLocalCameraUIDChange;
@property (TB,N,GisSecondaryCameraRunning,V_secondaryCameraRunning) secondaryCameraRunning;
@property (TB,N,V_secondaryZoomAvailable) secondaryZoomAvailable;
@property (T@"NSString",&,N,V_primaryCameraOverrideUID) primaryCameraOverrideUID;
@property (T@"NSString",&,N,V_secondaryCameraOverrideUID) secondaryCameraOverrideUID;
@property (T@"AVCaptureDevice",&,N) currentInputDevice;
@property (Ti,N) currentVideoOrientation;
@property (T@"NSArray",R,C,N) inputDevices;
@property (TB,R,N,GisPreviewRunning) previewRunning;
@property (TB,R,N,GisCinematicFramingEnabled) cinematicFramingEnabled;
@property (TB,R,N) currentInputSupportsCinematicFraming;
@property (TB,N,GisReactionEffectGestureEnabled) reactionEffectGestureEnabled;
@property (TB,N,GisStudioLightEnabled) studioLightEnabled;
@property (TB,R,N) currentInputSupportsStudioLight;
@property (TB,R,N) currentInputIsExternal;
@property (TB,R,N) currentInputSupportsReactionEffects;
@property (TB,R,N) supportsCameraBlur;
@property (TB,N) cameraBlurEnabled;
@property (Ti,N) currentBackgroundBlurControlMode;
@property (TB,R,N) currentInputSupportsTrueDepth;
@property (TB,R,N) currentInputSupportsUltraWide;
@property (TB,N) backgroundReplacementEnabled;
@property (TB,R,N) hasAvailableDeskViewCameras;
@property (T@"CALayer",&,N) localFrontLayer;
@property (T@"CALayer",&,N) localBackLayer;
@property (T@"CALayer",&,N,V_localFrontLayerHost) localFrontLayerHost;
@property (T@"CALayer",&,N,V_localBackLayerHost) localBackLayerHost;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) localScreenContentsRect;
@property (T{CGSize=dd},R,N) localVideoPortraitAspectRatio;
@property (T{CGSize=dd},R,N) localScreenPortraitAspectRatio;
@property (T{CGSize=dd},R,N) localVideoLandscapeAspectRatio;
@property (T{CGSize=dd},R,N) localScreenLandscapeAspectRatio;
@property (T@"NSArray",R,C,N) secondaryInputDevices;
@property (T@"NSString",&,N) secondaryCameraUID;
@property (T{CGSize=dd},R,N) secondaryCameraPortraitAspectRatio;
@property (T{CGSize=dd},R,N) secondaryCameraLandscapeAspectRatio;
@property (TB,R,N) secondaryCameraZoomAvailable;
@property (Td,R,N) secondaryCameraZoomFactor;
@property (Td,R,N) secondaryCameraMaxZoomFactor;
@property (T@?,C,N,V_reapplySecondaryCameraZoom) reapplySecondaryCameraZoom;
@property (TB,N,GisPrimarySessionEnabled) primarySessionEnabled;
@property (TB,N,GisSecondarySessionEnabled) secondarySessionEnabled;
@property (T@?,C,N,V_reapplyCameraZoom) reapplyCameraZoom;
@property (TB,R,N) shouldMirrorMemoji;
@property (TB,R,N) memojiWithoutDepthEnabled;
@property (TB,R,N) dualCameraCaptureSendingSupported;
@property (TB,N,GisFollowSystemCameraEnabled) followSystemCameraEnabled;
@property (TB,N,GshouldIgnoreStartPreview,V_ignoreStartPreview) ignoreStartPreview;
```

## Class methods

```
+[TUVideoDeviceController prewarm];
+[TUVideoDeviceController _aspectRatioForAttributes:landscape:];
+[TUVideoDeviceController _tuOrientationForVideoOrientation:];
+[TUVideoDeviceController _videoOrientationForTUOrientation:];
```

## Instance methods

```
-[TUVideoDeviceController initWithSerialQueue:];
-[TUVideoDeviceController flipCamera];
-[TUVideoDeviceController setCameraZoomFactor:];
-[TUVideoDeviceController isStudioLightEnabled];
-[TUVideoDeviceController isCinematicFramingEnabled];
-[TUVideoDeviceController currentInputSupportsReactionEffects];
-[TUVideoDeviceController backgroundReplacementEnabled];
-[TUVideoDeviceController secondaryZoomAvailable];
-[TUVideoDeviceController setPreviewPresentationOrientation:];
-[TUVideoDeviceController secondaryCameraZoomFactor];
-[TUVideoDeviceController currentInputSupportsStudioLight];
-[TUVideoDeviceController pausePreview];
-[TUVideoDeviceController setBackgroundReplacementEnabled:];
-[TUVideoDeviceController setCurrentInputDevice:];
-[TUVideoDeviceController setFollowSystemCameraEnabled:];
-[TUVideoDeviceController isPreviewRunning];
-[TUVideoDeviceController setReapplySecondaryCameraZoom:];
-[TUVideoDeviceController setCinematicFramingEnabled:];
-[TUVideoDeviceController stopPreview];
-[TUVideoDeviceController memojiWithoutDepthEnabled];
-[TUVideoDeviceController serialQueue];
-[TUVideoDeviceController rampCameraZoomFactor:withRate:];
-[TUVideoDeviceController setSecondaryCameraUID:];
-[TUVideoDeviceController didStartPreviewForProvider:];
-[TUVideoDeviceController startPreview];
-[TUVideoDeviceController setPrimarySessionEnabled:];
-[TUVideoDeviceController debugDescription];
-[TUVideoDeviceController provider:dockKitTrackingDidChange:];
-[TUVideoDeviceController getSnapshot];
-[TUVideoDeviceController setPrimaryCameraUID:secondaryCameraUID:useSquareAspectRatio:isUserPreferred:completionHandler:];
-[TUVideoDeviceController setCurrentInputDevice:isUserPreferred:];
-[TUVideoDeviceController setLocalPortraitAspectRatio:localLandscapeAspectRatio:];
-[TUVideoDeviceController init];
-[TUVideoDeviceController provider:backgroundReplacementEnabledDidChange:];
-[TUVideoDeviceController provider:secondaryCameraZoomAvailabilityDidChange:];
-[TUVideoDeviceController retryPreviewAfterError];
-[TUVideoDeviceController localBackLayer];
-[TUVideoDeviceController isReactionEffectGestureEnabled];
-[TUVideoDeviceController inputDeviceWithUniqueID:];
-[TUVideoDeviceController hasBeganRetryingAfterUninitializedClientError];
-[TUVideoDeviceController reapplySecondaryCameraZoom];
-[TUVideoDeviceController secondaryCameraZoomAvailable];
-[TUVideoDeviceController isSecondarySessionEnabled];
-[TUVideoDeviceController provider:systemPreferredCameraUIDDidChange:];
-[TUVideoDeviceController secondaryCameraMaxZoomFactor];
-[TUVideoDeviceController noteBeginAnimationToPreview];
-[TUVideoDeviceController provider:cameraBlurEnabledDidChange:];
-[TUVideoDeviceController provider:didReceiveErrorFromCameraUniqueID:error:];
-[TUVideoDeviceController provider:userPreferredCameraUIDDidChange:];
-[TUVideoDeviceController setLocalBackLayer:];
-[TUVideoDeviceController didPausePreviewForProvider:];
-[TUVideoDeviceController localVideoPortraitAspectRatio];
-[TUVideoDeviceController provider:cameraZoomAvailabilityDidChange:];
-[TUVideoDeviceController provider];
-[TUVideoDeviceController setSecondarySessionEnabled:];
-[TUVideoDeviceController setPrimaryCameraOverrideUID:];
-[TUVideoDeviceController setReapplyCameraZoom:];
-[TUVideoDeviceController localScreenContentsRect];
-[TUVideoDeviceController localVideoLandscapeAspectRatio];
-[TUVideoDeviceController currentInputSupportsUltraWide];
-[TUVideoDeviceController setCameraBlurEnabled:];
-[TUVideoDeviceController noteEndAnimationToPIP];
-[TUVideoDeviceController localScreenPortraitAspectRatio];
-[TUVideoDeviceController secondaryCameraPortraitAspectRatio];
-[TUVideoDeviceController setPreviewStartBlock:];
-[TUVideoDeviceController setRetryAfterLocalCameraUIDChange:];
-[TUVideoDeviceController setSecondaryCameraOverrideUID:];
-[TUVideoDeviceController provider:cameraDidBecomeInterruptedForForUniqueID:reason:];
-[TUVideoDeviceController setHasBeganRetryingAfterUninitializedClientError:];
-[TUVideoDeviceController currentVideoOrientation];
-[TUVideoDeviceController setIgnoreStartPreview:];
-[TUVideoDeviceController retryAfterLocalCameraUIDChange];
-[TUVideoDeviceController noteBeginAnimationToPIP];
-[TUVideoDeviceController provider:didChangeLocalCameraUID:];
-[TUVideoDeviceController portraitScreenAttributes];
-[TUVideoDeviceController localScreenLandscapeAspectRatio];
-[TUVideoDeviceController provider:didGetSnapshot:];
-[TUVideoDeviceController hasAvailableDeskViewCameras];
-[TUVideoDeviceController reapplyCameraZoom];
-[TUVideoDeviceController setLocalBackLayerHost:];
-[TUVideoDeviceController setSecondaryZoomAvailable:];
-[TUVideoDeviceController uninitializedClientRetrySeconds];
-[TUVideoDeviceController initWithProvider:serialQueue:featureFlags:];
-[TUVideoDeviceController currentInputDevice];
-[TUVideoDeviceController currentInputSupportsCinematicFraming];
-[TUVideoDeviceController setLocalFrontLayerHost:];
-[TUVideoDeviceController setUninitializedClientRetrySeconds:];
-[TUVideoDeviceController localFrontLayerHost];
-[TUVideoDeviceController setSecondaryCameraZoomFactor:];
-[TUVideoDeviceController provider:didReceiveFirstPreviewFrameFromCameraUniqueID:];
-[TUVideoDeviceController _postIsCinematicFramingAvailable:];
-[TUVideoDeviceController rampSecondaryCameraZoomFactor:withRate:];
-[TUVideoDeviceController provider:secondarySessionEnabledDidChange:];
-[TUVideoDeviceController didStopPreviewForProvider:];
-[TUVideoDeviceController secondaryCameraLandscapeAspectRatio];
-[TUVideoDeviceController provider:didChangeLocalVideoAttributes:];
-[TUVideoDeviceController secondaryCameraUID];
-[TUVideoDeviceController localBackLayerHost];
-[TUVideoDeviceController dualCameraCaptureSendingSupported];
-[TUVideoDeviceController noteEndAnimationToPreview];
-[TUVideoDeviceController landscapeScreenAttributes];
-[TUVideoDeviceController shouldMirrorMemoji];
-[TUVideoDeviceController setLocalFrontLayer:];
-[TUVideoDeviceController setWantsPreview:];
-[TUVideoDeviceController secondaryInputDevices];
-[TUVideoDeviceController isFollowSystemCameraEnabled];
-[TUVideoDeviceController primaryCameraOverrideUID];
-[TUVideoDeviceController provider:didChangeSecondaryVideoAttributes:];
-[TUVideoDeviceController cameraBlurEnabled];
-[TUVideoDeviceController isPrimarySessionEnabled];
-[TUVideoDeviceController provider:cameraCinematicFramingEnabledDidChange:];
-[TUVideoDeviceController provider:didReceiveFirstSecondaryFrameFromCameraUniqueID:];
-[TUVideoDeviceController provider:cameraCinematicFramingAvailabilityDidChange:];
-[TUVideoDeviceController currentInputIsExternal];
-[TUVideoDeviceController provider:reactionEffectsEnabledDidChange:];
-[TUVideoDeviceController provider:primarySessionEnabledDidChange:];
-[TUVideoDeviceController setStudioLightEnabled:];
-[TUVideoDeviceController currentBackgroundBlurControlMode];
-[TUVideoDeviceController setReactionEffectGestureEnabled:];
-[TUVideoDeviceController secondaryCameraOverrideUID];
-[TUVideoDeviceController supportsCameraBlur];
-[TUVideoDeviceController wantsPreview];
-[TUVideoDeviceController previewStartBlock];
-[TUVideoDeviceController hasRefreshedPreviewAfterError];
-[TUVideoDeviceController shouldIgnoreStartPreview];
-[TUVideoDeviceController provider:studioLightEnabledDidChange:];
-[TUVideoDeviceController captureDevicesChangedForProvider:];
-[TUVideoDeviceController setCurrentBackgroundBlurControlMode:];
-[TUVideoDeviceController setCurrentVideoOrientation:];
-[TUVideoDeviceController currentInputSupportsTrueDepth];
-[TUVideoDeviceController provider:cameraDidBecomeAvailableForUniqueID:];
-[TUVideoDeviceController provider:didDetectSensitiveContentWithAnalysis:];
-[TUVideoDeviceController updateZoomAvailibility:];
-[TUVideoDeviceController inputDevices];
-[TUVideoDeviceController isSecondaryCameraRunning];
-[TUVideoDeviceController localFrontLayer];
-[TUVideoDeviceController setHasRefreshedPreviewAfterError:];
-[TUVideoDeviceController setSecondaryCameraRunning:];
-[TUVideoDeviceController featureFlags];
```
