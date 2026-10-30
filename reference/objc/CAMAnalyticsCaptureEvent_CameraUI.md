# `CAMAnalyticsCaptureEvent`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMAnalyticsEvent`
- 12 instance variables, 12 properties, 57 instance methods, 0 class methods

## Instance variables

```
B __isStillDuringVideo;
B __outputToExternalStorage;
q __captureMode;
q __captureDevice;
q __captureDevicePosition;
q __captureVideoConfiguration;
q __lightingEffectType;
q __mediaType;
q __videoStabilizationStrength;
q __colorSpace;
q __frontRearSimultaneousVideoPIPInteractionCount;
@"NSMutableSet" __trackedFrontRearSimultaneousVideoAnchors;
```

## Properties

```
@property (Tq,R,N,V__captureMode) _captureMode;
@property (Tq,R,N,V__captureDevice) _captureDevice;
@property (Tq,R,N,V__captureDevicePosition) _captureDevicePosition;
@property (Tq,R,N,V__captureVideoConfiguration) _captureVideoConfiguration;
@property (Tq,N,V__lightingEffectType) _lightingEffectType;
@property (Tq,N,V__mediaType) _mediaType;
@property (TB,N,V__isStillDuringVideo) _isStillDuringVideo;
@property (Tq,R,N,V__videoStabilizationStrength) _videoStabilizationStrength;
@property (TB,N,V__outputToExternalStorage) _outputToExternalStorage;
@property (Tq,R,N,V__colorSpace) _colorSpace;
@property (Tq,N,V__frontRearSimultaneousVideoPIPInteractionCount) _frontRearSimultaneousVideoPIPInteractionCount;
@property (T@"NSMutableSet",&,N,V__trackedFrontRearSimultaneousVideoAnchors) _trackedFrontRearSimultaneousVideoAnchors;
```

## Instance methods

```
-[CAMAnalyticsCaptureEvent set_outputToExternalStorage:];
-[CAMAnalyticsCaptureEvent _lightingEffectType];
-[CAMAnalyticsCaptureEvent populateFromPanoramaCaptureStoppingReason:];
-[CAMAnalyticsCaptureEvent populatePersonalPhotographerIsManualCapture:];
-[CAMAnalyticsCaptureEvent initWithEvent:];
-[CAMAnalyticsCaptureEvent set_lightingEffectType:];
-[CAMAnalyticsCaptureEvent populateFromVideoCaptureResponse:];
-[CAMAnalyticsCaptureEvent _captureDevice];
-[CAMAnalyticsCaptureEvent populatePanoramaDirection:];
-[CAMAnalyticsCaptureEvent set_trackedFrontRearSimultaneousVideoAnchors:];
-[CAMAnalyticsCaptureEvent _trackAnchor:];
-[CAMAnalyticsCaptureEvent set_isStillDuringVideo:];
-[CAMAnalyticsCaptureEvent populateZoomFromDisplayZoomValue:zoomPoints:zoomInteractionType:];
-[CAMAnalyticsCaptureEvent populateZoomFieldOfView:graphConfiguration:smartFramingSource:];
-[CAMAnalyticsCaptureEvent populateObjectResultsWithNumberOfFaces:numberOfCats:numberOfDogs:];
-[CAMAnalyticsCaptureEvent _frontRearSimultaneousVideoPIPInteractionCount];
-[CAMAnalyticsCaptureEvent populateDesiredTorchMode:];
-[CAMAnalyticsCaptureEvent populateFromPanoramaCaptureRequest:];
-[CAMAnalyticsCaptureEvent trackFrontRearSimultaneousVideoPIPMoveToAnchor:];
-[CAMAnalyticsCaptureEvent populateFromStillImageCaptureRequest:burst:preferences:];
-[CAMAnalyticsCaptureEvent didActivateReducedResourceUsageDuringCapture];
-[CAMAnalyticsCaptureEvent populateExposureSliderBias:exposureTapAndBias:totalExposureBias:];
-[CAMAnalyticsCaptureEvent populateFromStillImageCaptureResponse:];
-[CAMAnalyticsCaptureEvent _stringForCoverScreenFeature:];
-[CAMAnalyticsCaptureEvent eventName];
-[CAMAnalyticsCaptureEvent _populateFromCaptureRequest:];
-[CAMAnalyticsCaptureEvent populateContinuousAutoFocusTrackingEnabled:];
-[CAMAnalyticsCaptureEvent populateDuration:];
-[CAMAnalyticsCaptureEvent _captureMode];
-[CAMAnalyticsCaptureEvent populateDesiredNightModeControlMode:resolvedNightModeControlMode:resolvedNightMode:nightModeStatus:];
-[CAMAnalyticsCaptureEvent set_mediaType:];
-[CAMAnalyticsCaptureEvent initWithGraphConfiguration:outputToExternalStorage:];
-[CAMAnalyticsCaptureEvent populateDeviceOrientation:isDeviceOrientationLocked:];
-[CAMAnalyticsCaptureEvent populateDesiredMacroMode:isMacroControlEnabled:isMacroCapture:isMacroSuggested:];
-[CAMAnalyticsCaptureEvent populateReducedResourceActiveAtCaptureStart:];
-[CAMAnalyticsCaptureEvent _isStillDuringVideo];
-[CAMAnalyticsCaptureEvent _zoomRangeStringForDisplayZoomValue:zoomPoints:mode:device:];
-[CAMAnalyticsCaptureEvent populatePortraitStatus:lightingEffectIntensity:apertureValue:zoomFactor:isDepthSuggestionAllowed:request:];
-[CAMAnalyticsCaptureEvent _defaultRangeStringForValue:lowerBound:upperBound:defaultValue:];
-[CAMAnalyticsCaptureEvent populateFromVideoCaptureRequest:preferences:];
-[CAMAnalyticsCaptureEvent _captureDevicePosition];
-[CAMAnalyticsCaptureEvent _outputToExternalStorage];
-[CAMAnalyticsCaptureEvent _videoStabilizationStrength];
-[CAMAnalyticsCaptureEvent _captureVideoConfiguration];
-[CAMAnalyticsCaptureEvent populateZoomFromZoomButtonSymbol:zoomInteractionType:];
-[CAMAnalyticsCaptureEvent set_frontRearSimultaneousVideoPIPInteractionCount:];
-[CAMAnalyticsCaptureEvent _mediaType];
-[CAMAnalyticsCaptureEvent populateAEAFLocked:];
-[CAMAnalyticsCaptureEvent populateDesiredFlashMode:desiredLivePhotoMode:desiredHDRMode:timerDuration:];
-[CAMAnalyticsCaptureEvent populateBurstLength:];
-[CAMAnalyticsCaptureEvent _trackedFrontRearSimultaneousVideoAnchors];
-[CAMAnalyticsCaptureEvent populatePanoramaInstruction:];
-[CAMAnalyticsCaptureEvent populateCoverScreenFeature:];
-[CAMAnalyticsCaptureEvent _colorSpace];
-[CAMAnalyticsCaptureEvent populateForTimelapseCaptureOrientation:captureMirrored:origin:pressType:startDate:];
-[CAMAnalyticsCaptureEvent populatePhoneAltLayout:isYoinked:isSplitScreen:];
-[CAMAnalyticsCaptureEvent populateSharedLibraryMode:autoEnabled:];
```
