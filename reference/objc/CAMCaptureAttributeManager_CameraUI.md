# `CAMCaptureAttributeManager`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 22 properties, 122 instance methods, 1 class methods

## Instance variables

```
B __needsCustomExposureUpdate;
B __needsCustomWhiteBalanceUpdate;
B __didLockLensApertureForVideoRecording;
f __customLensPosition;
@"<CAMCaptureAttributeTapToFocusDelegate>" _tapToFocusDelegate;
@"<CAMCaptureAttributeDelegate>" _manualControlsDelegate;
@"<CAMCustomExposureCompletionDelegate>" _customExposureCompletionDelegate;
@"<CAMExposureBiasDelegate>" _exposureBiasDelegate;
@"<CAMLensPositionDelegate>" _lensPositionDelegate;
@"CAMCustomExposureValues" __customExposureValues;
q __inFlightCustomExposureCount;
@"CAMCustomWhiteBalanceValues" __customWhiteBalanceValues;
@"<CAMCaptureAttributeManagerCaptureControllerProtocol>" _captureController;
```

## Properties

```
@property (TB,R,N) _shouldSkipAttributeResetForOngoingCapture;
@property (Tf,N,V__customLensPosition) _customLensPosition;
@property (T@"CAMCustomExposureValues",&,N,V__customExposureValues) _customExposureValues;
@property (TB,N,V__needsCustomExposureUpdate) _needsCustomExposureUpdate;
@property (Tq,N,V__inFlightCustomExposureCount) _inFlightCustomExposureCount;
@property (T@"CAMCustomWhiteBalanceValues",&,N,V__customWhiteBalanceValues) _customWhiteBalanceValues;
@property (TB,N,V__needsCustomWhiteBalanceUpdate) _needsCustomWhiteBalanceUpdate;
@property (TB,N,V__didLockLensApertureForVideoRecording) _didLockLensApertureForVideoRecording;
@property (Tq,R,N) _lockedAttributesForTapToFocus;
@property (Tq,R,N) _lockedAttributesForManualControls;
@property (Tq,R,N) _lockedAttributesForAnyDelegate;
@property (T@"<CAMCaptureAttributeManagerCaptureControllerProtocol>",W,N,V_captureController) captureController;
@property (T@"<CAMCaptureAttributeTapToFocusDelegate>",W,N,V_tapToFocusDelegate) tapToFocusDelegate;
@property (T@"<CAMCaptureAttributeDelegate>",W,N,V_manualControlsDelegate) manualControlsDelegate;
@property (T@"<CAMCustomExposureCompletionDelegate>",W,N,V_customExposureCompletionDelegate) customExposureCompletionDelegate;
@property (T@"<CAMExposureBiasDelegate>",W,N,V_exposureBiasDelegate) exposureBiasDelegate;
@property (T@"<CAMLensPositionDelegate>",W,N,V_lensPositionDelegate) lensPositionDelegate;
@property (TB,R,N) shouldAllowUserToChangeFocusAndExposure;
@property (TB,R,N,GisAdjustingCustomExposure) adjustingCustomExposure;
@property (T{?=qiIq},R,N) lockedExposureDurationValue;
@property (Tf,R,N) lockedLensApertureValue;
@property (Tf,R,N) lockedLensPositionValue;
```

## Class methods

```
+[CAMCaptureAttributeManager focusLensPositionCurrentSentinel];
```

## Instance methods

```
-[CAMCaptureAttributeManager _shouldLockWhiteBalanceForActiveVideoRequest];
-[CAMCaptureAttributeManager _scheduleFocusAndExposureResetAfterCaptureIfNecessaryForType:];
-[CAMCaptureAttributeManager set_customLensPosition:];
-[CAMCaptureAttributeManager resetFocusAndExposure];
-[CAMCaptureAttributeManager _isCapturingVideo];
-[CAMCaptureAttributeManager setCinematicFocusForMetadataObject:atPoint:useFixedOpticalFocus:useHardFocus:];
-[CAMCaptureAttributeManager _anyDelegateWantsLockedAttributes:];
-[CAMCaptureAttributeManager _lockedAttributesForAnyDelegate];
-[CAMCaptureAttributeManager updateCaptureAttributesForVideoRecordingStartWithRequest:];
-[CAMCaptureAttributeManager _didLockLensApertureForVideoRecording];
-[CAMCaptureAttributeManager _customWhiteBalanceValues];
-[CAMCaptureAttributeManager setLensPositionDelegate:];
-[CAMCaptureAttributeManager _needsCustomExposureUpdate];
-[CAMCaptureAttributeManager _tapToFocusDelegateWantsLockedAttributes:];
-[CAMCaptureAttributeManager updateCaptureAttributesForPanoramaStart];
-[CAMCaptureAttributeManager _enqueueCustomExposureValues:];
-[CAMCaptureAttributeManager init];
-[CAMCaptureAttributeManager setWhiteBalancePreset:];
-[CAMCaptureAttributeManager _shouldManageFocusForMode:];
-[CAMCaptureAttributeManager _inFlightCustomExposureCount];
-[CAMCaptureAttributeManager manualControlsDelegate];
-[CAMCaptureAttributeManager setExposureISOLockedAtCurrentValue];
-[CAMCaptureAttributeManager updateForActivePrimaryConstituentDeviceChange];
-[CAMCaptureAttributeManager setAutomaticExposureISO];
-[CAMCaptureAttributeManager updateCaptureAttributesForTimelapseStopped];
-[CAMCaptureAttributeManager _invalidateCustomLensPosition];
-[CAMCaptureAttributeManager _requestCustomWhiteBalanceIfNecessary];
-[CAMCaptureAttributeManager dealloc];
-[CAMCaptureAttributeManager _updateCaptureAttributesForVideoRecordingStartForMode:requestWantsLockedWhiteBalance:];
-[CAMCaptureAttributeManager _updateCaptureAttributesForVideoRecordingStoppedForMode:requestWantsLockedWhiteBalance:captureType:];
-[CAMCaptureAttributeManager updateForSessionDidStopRunning];
-[CAMCaptureAttributeManager _lockedAttributesForManualControls];
-[CAMCaptureAttributeManager forceDisableSubjectAreaChangeMonitoring];
-[CAMCaptureAttributeManager _commandForResettingCaptureAttributes:resetSecondaryDevice:cancelDelayedAttributeReset:disableSubjectAreaChangeMonitoring:notifyDelegate:];
-[CAMCaptureAttributeManager _isCapturingTimelapseClassic];
-[CAMCaptureAttributeManager updateCaptureAttributesForLivePhotoRecordingStopped];
-[CAMCaptureAttributeManager setCustomExposureCompletionDelegate:];
-[CAMCaptureAttributeManager _setExposureDuration:];
-[CAMCaptureAttributeManager isAdjustingCustomExposure];
-[CAMCaptureAttributeManager tapToFocusDelegate];
-[CAMCaptureAttributeManager _isCapturingTimelapse];
-[CAMCaptureAttributeManager _resetCaptureAttributesAfterCaptureForType:];
-[CAMCaptureAttributeManager _setExposureISO:];
-[CAMCaptureAttributeManager set_customWhiteBalanceValues:];
-[CAMCaptureAttributeManager _requestCustomExposureIfNecessary];
-[CAMCaptureAttributeManager lockAttributes:];
-[CAMCaptureAttributeManager _customExposureValues];
-[CAMCaptureAttributeManager resetCustomWhiteBalance];
-[CAMCaptureAttributeManager updateForDidChangeFlashActive:];
-[CAMCaptureAttributeManager _isFlashActive];
-[CAMCaptureAttributeManager _lockedAttributesForCaptureStateForReason:];
-[CAMCaptureAttributeManager updateCaptureAttributesForPanoramaStopped];
-[CAMCaptureAttributeManager _shouldLockWhiteBalanceForCTMVideoRequest:];
-[CAMCaptureAttributeManager _useSmoothFocus];
-[CAMCaptureAttributeManager updateCaptureAttributesForCTMVideoRecordingStoppedWithRequest:];
-[CAMCaptureAttributeManager _enqueueCommands:];
-[CAMCaptureAttributeManager _shouldLockFocusForMode:];
-[CAMCaptureAttributeManager _subjectAreaDidChange:];
-[CAMCaptureAttributeManager _manualControlsDelegateWantsLockedAttributes:];
-[CAMCaptureAttributeManager setAutomaticExposureDuration];
-[CAMCaptureAttributeManager updateCaptureAttributesForStillImageCaptureStopped];
-[CAMCaptureAttributeManager _needsCustomWhiteBalanceUpdate];
-[CAMCaptureAttributeManager _enqueueCommand:];
-[CAMCaptureAttributeManager _customLensPosition];
-[CAMCaptureAttributeManager setTapToFocusDelegate:];
-[CAMCaptureAttributeManager lockFocusAtLensPosition:completionBlock:];
-[CAMCaptureAttributeManager setContinuousAutoFocusTrackingLensPositionBias:];
-[CAMCaptureAttributeManager focusAndExposeAtPoint:lockFocus:rectSize:resetExposureTargetBias:enableContinuousAutoFocusTracking:];
-[CAMCaptureAttributeManager set_needsCustomWhiteBalanceUpdate:];
-[CAMCaptureAttributeManager updateForWillChangeToGraphConfiguration:];
-[CAMCaptureAttributeManager _resetCustomExposureValues];
-[CAMCaptureAttributeManager _resetCaptureAttributesIfAppropriateForReason:];
-[CAMCaptureAttributeManager _isCapturingBurst];
-[CAMCaptureAttributeManager setExposureDurationLockedWithValue:];
-[CAMCaptureAttributeManager _lockedAttributesForTapToFocus];
-[CAMCaptureAttributeManager updateCaptureAttributesForBurstStopped];
-[CAMCaptureAttributeManager shouldAllowUserToChangeFocusAndExposure];
-[CAMCaptureAttributeManager _cinematicMetadataObjectIDForMetadataObject:];
-[CAMCaptureAttributeManager _commandForResettingCaptureAttributes:resetSecondaryDevice:];
-[CAMCaptureAttributeManager _shouldLockWhiteBalanceForVideoCaptureRequest:];
-[CAMCaptureAttributeManager updateCaptureAttributesForVideoRecordingStoppedWithRequest:];
-[CAMCaptureAttributeManager _resetCustomExposureIfAllowed];
-[CAMCaptureAttributeManager resetManualFocus];
-[CAMCaptureAttributeManager lockedLensApertureValue];
-[CAMCaptureAttributeManager setAutomaticExposureLensAperture];
-[CAMCaptureAttributeManager setWhiteBalanceTemperature:tint:];
-[CAMCaptureAttributeManager set_needsCustomExposureUpdate:];
-[CAMCaptureAttributeManager _isCapturingPanorama];
-[CAMCaptureAttributeManager updateCaptureAttributesForCTMVideoRecordingStartWithRequest:];
-[CAMCaptureAttributeManager setExposureDurationLockedAtCurrentValue];
-[CAMCaptureAttributeManager _commandInvalidatesCustomLensPosition:];
-[CAMCaptureAttributeManager _lockedAttributesForDelegate:];
-[CAMCaptureAttributeManager _setExposureLensAperture:];
-[CAMCaptureAttributeManager lockedExposureDurationValue];
-[CAMCaptureAttributeManager setExposureISOLockedWithValue:];
-[CAMCaptureAttributeManager setManualControlsDelegate:];
-[CAMCaptureAttributeManager lockedLensPositionValue];
-[CAMCaptureAttributeManager _modificationReasonForResetReason:];
-[CAMCaptureAttributeManager setExposureBiasDelegate:];
-[CAMCaptureAttributeManager _resetCustomWhiteBalanceValues];
-[CAMCaptureAttributeManager customExposureCompletionDelegate];
-[CAMCaptureAttributeManager updateCaptureAttributesForTimelapseStart];
-[CAMCaptureAttributeManager exposureBiasDelegate];
-[CAMCaptureAttributeManager _resetStateForConfigurationChange];
-[CAMCaptureAttributeManager set_inFlightCustomExposureCount:];
-[CAMCaptureAttributeManager _resetCaptureAttributesAfterCapture];
-[CAMCaptureAttributeManager setExposureLensApertureLockedWithValue:];
-[CAMCaptureAttributeManager setExposureLensApertureLockedAtCurrentValue];
-[CAMCaptureAttributeManager lensPositionDelegate];
-[CAMCaptureAttributeManager _shouldLockLensApertureForVideoRecordingForMode:];
-[CAMCaptureAttributeManager updateForDidChangeToGraphConfiguration:];
-[CAMCaptureAttributeManager _shouldSkipAttributeResetForOngoingCapture];
-[CAMCaptureAttributeManager set_didLockLensApertureForVideoRecording:];
-[CAMCaptureAttributeManager changeExposureTargetBias:];
-[CAMCaptureAttributeManager set_customExposureValues:];
-[CAMCaptureAttributeManager cancelDelayedFocusAndExposureReset];
-[CAMCaptureAttributeManager setCaptureController:];
-[CAMCaptureAttributeManager setCinematicFocusAtPoint:useFixedOpticalFocus:useHardFocus:];
-[CAMCaptureAttributeManager captureController];
-[CAMCaptureAttributeManager focusAtCenterForVideoRecording];
-[CAMCaptureAttributeManager updateCaptureAttributesForBurstStart];
-[CAMCaptureAttributeManager _isCapturingTimeWarp];
```
