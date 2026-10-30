# `AVControlCenterModuleState`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 107 instance variables, 17 properties, 81 instance methods, 1 class methods

## Instance variables

```
@"NSString" _bundleID;
@"NSString" _eligibleEffectsKey;
B _isOptedInForBackgroundBlur;
B _isOptedInForStudioLight;
B _isOptedInForReactionEffects;
B _isOptedInForBackgroundReplacement;
B _isOptedInForRingLight;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
B _holdingStateLock;
B _centerStageSupported;
q _centerStageControlMode;
B _centerStageEnabled;
@"NSString" _centerStageControlModeKey;
@"NSString" _centerStageEnabledKey;
@"NSString" _centerStageUnavailableReasonsKey;
B _backgroundBlurSupported;
q _backgroundBlurControlMode;
B _backgroundBlurEnabled;
@"NSString" _backgroundBlurControlModeKey;
@"NSString" _backgroundBlurEnabledKey;
@"NSString" _backgroundBlurUnavailableReasonsKey;
f _backgroundBlurAperture;
@"NSString" _backgroundBlurApertureKey;
B _studioLightingSupported;
q _studioLightingControlMode;
B _studioLightingEnabled;
@"NSString" _studioLightingControlModeKey;
@"NSString" _studioLightingEnabledKey;
@"NSString" _studioLightingUnavailableReasonsKey;
f _studioLightingIntensity;
@"NSString" _studioLightingIntensityKey;
B _reactionEffectsSupported;
B _reactionsEnabled;
@"NSString" _reactionsEnabledKey;
B _gesturesEnabled;
@"NSString" _gesturesEnabledKey;
@"NSString" _gesturesEnabledDefaultKey;
@"NSString" _reactionsUnavailableReasonsKey;
@"NSString" _reactionTriggeredKey;
@"NSMutableDictionary" _previousReactionStateByDeviceIdentifier;
@"NSString" _reactionsInProgressKey;
B _backgroundReplacementSupported;
B _backgroundReplacementEnabled;
@"NSString" _backgroundReplacementEnabledKey;
@"NSString" _backgroundReplacementUnavailableReasonsKey;
@"NSURL" _backgroundReplacementURL;
@"NSString" _backgroundReplacementURLBookmarkKey;
^{__CVBuffer=} _backgroundReplacementPixelBuffer;
i _backgroundReplacementPixelBufferFillWidth;
i _backgroundReplacementPixelBufferFillHeight;
B _ringLightSupported;
B _ringLightEnabled;
B _ringLightActive;
f _ringLightScreenNitsFloor;
f _ringLightWidth;
f _ringLightColor;
B _ringLightAutoSupported;
q _ringLightMode;
q _ringLightOnboardingState;
i _ringLightOnboardingStrikeCount;
@"NSDate" _ringLightOnboardingPreviousTipTimestamp;
q _ringLightWaitTimeBetweenOnboardingTips;
i _ringLightMaxStrikeCounts;
@"NSString" _ringLightSupportedKey;
@"NSString" _ringLightUnavailableReasonsKey;
@"NSString" _ringLightEnabledKey;
@"NSString" _ringLightActiveKey;
@"NSString" _ringLightScreenNitsFloorKey;
@"NSString" _ringLightWidthKey;
@"NSString" _ringLightColorKey;
@"NSString" _ringLightAutoSupportedKey;
@"NSString" _ringLightModeKey;
@"NSString" _ringLightOnboardingStateKey;
@"NSString" _ringLightOnboardingStrikeCountKey;
@"NSString" _ringLightOnboardingPreviousTipTimestampKey;
B _auVoiceIOBypassVoiceProcessing;
@"NSString" _auVoiceIOBypassVoiceProcessingKey;
q _microphoneMode;
q _activeMicrophoneMode;
@"NSString" _microphoneModeKey;
@"NSString" _activeMicrophoneModeKey;
@"NSArray" _supportedMicrophoneModes;
@"NSString" _supportedMicrophoneModesKey;
@"NSArray" _hiddenMicrophoneModes;
@"NSString" _hiddenMicrophoneModesKey;
B _autoMicModeEnabled;
@"NSString" _autoMicModeEnabledKey;
@"NSString" _startPanningAtPointKey;
@"NSString" _panWithTranslationKey;
@"NSString" _manualFramingVideoZoomFactorKey;
@"NSString" _performOneShotFramingKey;
@"NSString" _resetFramingKey;
@"NSString" _oneShotFramingCompletedKey;
@"NSString" _resetFramingCompletedKey;
@"NSString" _panningAnglesKey;
@"NSString" _centerStageFieldOfViewRestrictedToWideKey;
@"NSString" _manualFramingDeviceTypeKey;
@"NSString" _dockedTrackingActiveKey;
d _currentPanningAngleX;
d _currentPanningAngleY;
d _currentOriginalZoomFactor;
q _manualFramingDeviceType;
@"NSDictionary" _zoomFactorConstantsByManualFramingDeviceType;
B _deviceBasedModuleState;
B _deviceSupportsManualFraming;
B _observingManualFramingProprietaryDefaultKeys;
B _observingDockedTrackingProprietaryDefaultKey;
```

## Properties

```
@property (TB,R,GisActive) active;
@property (TB) centerStageSupported;
@property (TB) backgroundBlurSupported;
@property (TB) studioLightingSupported;
@property (TB) reactionEffectsSupported;
@property (TB) backgroundReplacementSupported;
@property (TB) ringLightSupported;
@property (TB,R) micModesSupported;
@property (TB,R,GisAutoMicrophoneModeSupported) autoMicrophoneModeSupported;
@property (T@"NSURL",&,N) backgroundReplacementURL;
@property (TB,R,N) hasBackgroundReplacementBeenToggled;
@property (TB,R) manualFramingIsAtDefault;
@property (TB) centerStageFieldOfViewRestrictedToWide;
@property (Tq) manualFramingDeviceType;
@property (T@"NSDictionary",R) zoomFactorConstantsByManualFramingDeviceType;
@property (TB,R,GisDeviceBasedModuleState) deviceBasedModuleState;
@property (TB,R,GisDeviceBasedModuleStateUpdateToDate) deviceBasedModuleStateUpdateToDate;
```

## Class methods

```
+[AVControlCenterModuleState moduleStateForBundleID:];
```

## Instance methods

```
-[AVControlCenterModuleState reactionEffectsSupported];
-[AVControlCenterModuleState setRingLightColor:];
-[AVControlCenterModuleState activeMicrophoneMode];
-[AVControlCenterModuleState setRingLightSupported:];
-[AVControlCenterModuleState ringLightSupported];
-[AVControlCenterModuleState startPanningAtPoint:];
-[AVControlCenterModuleState dealloc];
-[AVControlCenterModuleState setReactionEffectsSupported:];
-[AVControlCenterModuleState setBackgroundBlurSupported:];
-[AVControlCenterModuleState ringLightColor];
-[AVControlCenterModuleState setBackgroundReplacementURL:];
-[AVControlCenterModuleState centerStageFieldOfViewRestrictedToWide];
-[AVControlCenterModuleState performOneShotFraming];
-[AVControlCenterModuleState resetFraming];
-[AVControlCenterModuleState backgroundReplacementSupported];
-[AVControlCenterModuleState setStudioLightingSupported:];
-[AVControlCenterModuleState panWithTranslation:];
-[AVControlCenterModuleState studioLightingSupported];
-[AVControlCenterModuleState isActive];
-[AVControlCenterModuleState setCenterStageFieldOfViewRestrictedToWide:];
-[AVControlCenterModuleState setBackgroundReplacementSupported:];
-[AVControlCenterModuleState backgroundReplacementURL];
-[AVControlCenterModuleState backgroundBlurSupported];
-[AVControlCenterModuleState ringLightActive];
-[AVControlCenterModuleState _defaultOriginalVideoZoomFactor];
-[AVControlCenterModuleState _checkManualFramingDefaultStateWithNewOriginalZoomFactor:];
-[AVControlCenterModuleState _handleBackPropagatedVideoZoomFactorUpdate:];
-[AVControlCenterModuleState _handlePanningAnglesUpdate:];
-[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:];
-[AVControlCenterModuleState _updateEligibleEffects:];
-[AVControlCenterModuleState backgroundReplacementPixelBufferFillingWidth:height:];
-[AVControlCenterModuleState canShowRingLightOnboardingTip];
-[AVControlCenterModuleState canShowRingLightUI];
-[AVControlCenterModuleState centerStageSupported];
-[AVControlCenterModuleState cleanUpOrphanedSupportedMicModes];
-[AVControlCenterModuleState controlModeForVideoEffect:];
-[AVControlCenterModuleState effectIntensityDefaultForVideoEffect:];
-[AVControlCenterModuleState effectIntensityForVideoEffect:];
-[AVControlCenterModuleState effectIntensityRangeForVideoEffect:];
-[AVControlCenterModuleState enableBlackenFrames:forDeviceUID:];
-[AVControlCenterModuleState getRingLightMode];
-[AVControlCenterModuleState hasBackgroundReplacementBeenToggled];
-[AVControlCenterModuleState hiddenMicrophoneModes];
-[AVControlCenterModuleState initForBundleID:];
-[AVControlCenterModuleState installProprietaryDefaultsHandlers];
-[AVControlCenterModuleState invalidateDeviceBasedModuleStatesIfNeeded];
-[AVControlCenterModuleState isAutoMicrophoneModeEnabled];
-[AVControlCenterModuleState isAutoMicrophoneModeSupported];
-[AVControlCenterModuleState isDeviceBasedModuleState];
-[AVControlCenterModuleState isDeviceBasedModuleStateUpdateToDate];
-[AVControlCenterModuleState isEnabledForVideoEffect:];
-[AVControlCenterModuleState isRingLightAutoSupported];
-[AVControlCenterModuleState manualFramingDeviceType];
-[AVControlCenterModuleState manualFramingEnabledForDevice:];
-[AVControlCenterModuleState manualFramingIsAtDefault];
-[AVControlCenterModuleState manualFramingOriginalVideoZoomFactor];
-[AVControlCenterModuleState micModesSupported];
-[AVControlCenterModuleState microphoneMode];
-[AVControlCenterModuleState performReactionEffect:forCaptureDeviceWithID:];
-[AVControlCenterModuleState ringLightScreenNitsFloor];
-[AVControlCenterModuleState ringLightWidth];
-[AVControlCenterModuleState setAutoMicrophoneModeEnabled:];
-[AVControlCenterModuleState setCenterStageSupported:];
-[AVControlCenterModuleState setEffectIntensityForVideoEffect:forVideoEffect:];
-[AVControlCenterModuleState setEnabled:forVideoEffect:];
-[AVControlCenterModuleState setManualFramingDeviceType:];
-[AVControlCenterModuleState setManualFramingOriginalZoomFactor:convertedZoomFactor:];
-[AVControlCenterModuleState setMicrophoneMode:];
-[AVControlCenterModuleState setRingLightActive:];
-[AVControlCenterModuleState setRingLightMode:];
-[AVControlCenterModuleState setRingLightOnboardingState:];
-[AVControlCenterModuleState setRingLightOnboardingTipResponse:];
-[AVControlCenterModuleState setRingLightWidth:];
-[AVControlCenterModuleState setupDeviceBasedModuleStatesIfNeeded];
-[AVControlCenterModuleState supportedMicrophoneModes];
-[AVControlCenterModuleState supportsVideoEffect:];
-[AVControlCenterModuleState unavailableReasonsForVideoEffect:];
-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:];
-[AVControlCenterModuleState updateCenterStageSupported:backgroundBlurSupported:studioLightingSupported:reactionEffectsSupported:backgroundReplacementSupported:];
-[AVControlCenterModuleState voiceProcessingBypassed];
-[AVControlCenterModuleState zoomFactorConstantsByManualFramingDeviceType];
```
