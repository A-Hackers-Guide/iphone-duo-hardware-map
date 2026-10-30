# `TUVideoDeviceControllerProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 21 properties, 52 instance methods, 0 class methods

## Properties

```
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
@property (T@"<TUVideoDeviceControllerProviderDelegate>",W,N) delegate;
@property (T@"NSArray",R,C,N) secondaryInputDevices;
@property (T@"NSString",C,N) secondaryCameraUID;
@property (T@"VideoAttributes",C,N) secondaryVideoAttributes;
@property (TB,R,N) secondaryCameraZoomAvailable;
@property (Td,R,N) secondaryCameraZoomFactor;
@property (Td,R,N) secondaryCameraMaxZoomFactor;
@property (TB,N,GisPrimarySessionEnabled) primarySessionEnabled;
@property (TB,N,GisSecondarySessionEnabled) secondarySessionEnabled;
```

## Instance methods

```
-[TUVideoDeviceControllerProvider beginPreviewToPIPAnimation];
-[TUVideoDeviceControllerProvider setCameraZoomFactor:];
-[TUVideoDeviceControllerProvider isStudioLightEnabled];
-[TUVideoDeviceControllerProvider setLocalVideoAttributes:];
-[TUVideoDeviceControllerProvider isCinematicFramingEnabled];
-[TUVideoDeviceControllerProvider setPreviewPresentationOrientation:];
-[TUVideoDeviceControllerProvider secondaryCameraZoomFactor];
-[TUVideoDeviceControllerProvider pausePreview];
-[TUVideoDeviceControllerProvider localVideoAttributes];
-[TUVideoDeviceControllerProvider endPIPToPreviewAnimation];
-[TUVideoDeviceControllerProvider localVideoLayer:];
-[TUVideoDeviceControllerProvider beginPIPToPreviewAnimation];
-[TUVideoDeviceControllerProvider isPreviewRunning];
-[TUVideoDeviceControllerProvider localScreenAttributesForVideoAttributes:];
-[TUVideoDeviceControllerProvider setCinematicFramingEnabled:];
-[TUVideoDeviceControllerProvider stopPreview];
-[TUVideoDeviceControllerProvider memojiWithoutDepthEnabled];
-[TUVideoDeviceControllerProvider localCameraUID];
-[TUVideoDeviceControllerProvider rampCameraZoomFactor:withRate:];
-[TUVideoDeviceControllerProvider setSecondaryCameraUID:];
-[TUVideoDeviceControllerProvider startPreview];
-[TUVideoDeviceControllerProvider setPrimarySessionEnabled:];
-[TUVideoDeviceControllerProvider setLocalScreenAttributes:];
-[TUVideoDeviceControllerProvider endPreviewToPIPAnimation];
-[TUVideoDeviceControllerProvider getSnapshot];
-[TUVideoDeviceControllerProvider setLocalVideoLayerHost:front:];
-[TUVideoDeviceControllerProvider setSecondaryVideoAttributes:];
-[TUVideoDeviceControllerProvider isReactionEffectGestureEnabled];
-[TUVideoDeviceControllerProvider secondaryVideoAttributes];
-[TUVideoDeviceControllerProvider secondaryCameraZoomAvailable];
-[TUVideoDeviceControllerProvider isSecondarySessionEnabled];
-[TUVideoDeviceControllerProvider secondaryCameraMaxZoomFactor];
-[TUVideoDeviceControllerProvider setSecondarySessionEnabled:];
-[TUVideoDeviceControllerProvider setLocalCameraWithUID:];
-[TUVideoDeviceControllerProvider setCameraBlurEnabled:];
-[TUVideoDeviceControllerProvider setLocalVideoLayer:front:];
-[TUVideoDeviceControllerProvider supportsCameraBlurForDevice:];
-[TUVideoDeviceControllerProvider setDelegate:];
-[TUVideoDeviceControllerProvider hasAvailableDeskViewCameras];
-[TUVideoDeviceControllerProvider setSecondaryCameraZoomFactor:];
-[TUVideoDeviceControllerProvider isCameraBlurEnabled];
-[TUVideoDeviceControllerProvider delegate];
-[TUVideoDeviceControllerProvider rampSecondaryCameraZoomFactor:withRate:];
-[TUVideoDeviceControllerProvider secondaryCameraUID];
-[TUVideoDeviceControllerProvider dualCameraCaptureSendingSupported];
-[TUVideoDeviceControllerProvider shouldMirrorMemoji];
-[TUVideoDeviceControllerProvider secondaryInputDevices];
-[TUVideoDeviceControllerProvider setPrimaryCameraUID:secondaryCameraUID:useSquareAspectRatio:completionHandler:];
-[TUVideoDeviceControllerProvider isPrimarySessionEnabled];
-[TUVideoDeviceControllerProvider setStudioLightEnabled:];
-[TUVideoDeviceControllerProvider setReactionEffectGestureEnabled:];
-[TUVideoDeviceControllerProvider inputDevices];
```
