# `SBCaptureButtonSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 45 instance variables, 45 properties, 92 instance methods, 1 class methods

## Instance variables

```
B _visionIntelligenceKeylineScreenBlendMode;
B _visionIntelligenceKeylineRimIsSoft;
B _enableZoomUpBlur;
B _dosidoUsesHomeScreenBlur;
B _enablesStationaryDetectionForUnlocked;
d _launchAfterButtonUpGracePeriod;
d _ignoreFaceDownAfterDuration;
d _longPressVisionIntelligenceDelay;
d _directLaunchAfterUnsuppressGracePeriod;
d _preludeDropletRadius;
d _preludeCornerRadius;
d _preludeScreenEdgeInset;
@"SBFFluidBehaviorSettings" _preludePresentationTranslationSettings;
d _visionIntelligenceKeylineAlpha;
d _visionIntelligenceKeylineLargeBlurRadius;
d _visionIntelligenceKeylineLargeAmount;
d _visionIntelligenceKeylineLargeStart;
d _visionIntelligenceKeylineLargeEnd;
d _visionIntelligenceKeylineSmallWidth;
d _visionIntelligenceKeylineFadeLength;
d _visionIntelligenceKeylineFadeStart;
d _visionIntelligenceKeylineFadeEnd;
d _visionIntelligenceKeylineEDRGain;
@"SBFFluidBehaviorSettings" _visionIntelligenceBehaviorSettings;
@"SBFFluidBehaviorSettings" _visionIntelligenceHintBehaviorSettings;
d _zoomUpDropletRadius;
d _disableDropletEffectDelay;
d _zoomUpYAndScaleDelay;
@"SBFFluidBehaviorSettings" _zoomUpPositionXSettings;
@"SBFFluidBehaviorSettings" _zoomUpPositionYSettings;
@"SBFFluidBehaviorSettings" _zoomUpScaleSettings;
@"SBFFluidBehaviorSettings" _zoomUpCornerRadiusSettings;
@"SBFFluidBehaviorSettings" _zoomUpDropletRadiusAnimationSettings;
@"SBFFluidBehaviorSettings" _zoomUpBackgroundDimAnimationSettings;
@"SBFFluidBehaviorSettings" _zoomUpDisableDropletEffectFiltersSettings;
d _zoomUpBlurStartProgress;
d _zoomUpBackgroundDimStartProgress;
d _dosidoTargetScale;
@"SBFFluidBehaviorSettings" _dosidoLayoutAndPositionSettings;
@"SBFFluidBehaviorSettings" _dosidoScaleSettings;
d _accidentalPreventionStationaryThreshold;
d _accidentalPreventionPickUpBuffer;
d _coachingUIDismissalInterval;
d _stationaryDetectionDebounceInterval;
d _displaySwapMitigationGracePeriod;
```

## Properties

```
@property (Td,N,V_launchAfterButtonUpGracePeriod) launchAfterButtonUpGracePeriod;
@property (Td,N,V_ignoreFaceDownAfterDuration) ignoreFaceDownAfterDuration;
@property (Td,N,V_longPressVisionIntelligenceDelay) longPressVisionIntelligenceDelay;
@property (Td,N,V_directLaunchAfterUnsuppressGracePeriod) directLaunchAfterUnsuppressGracePeriod;
@property (Td,N,V_preludeDropletRadius) preludeDropletRadius;
@property (Td,N,V_preludeCornerRadius) preludeCornerRadius;
@property (Td,N,V_preludeScreenEdgeInset) preludeScreenEdgeInset;
@property (T@"SBFFluidBehaviorSettings",&,N,V_preludePresentationTranslationSettings) preludePresentationTranslationSettings;
@property (TB,N,V_visionIntelligenceKeylineScreenBlendMode) visionIntelligenceKeylineScreenBlendMode;
@property (TB,N,V_visionIntelligenceKeylineRimIsSoft) visionIntelligenceKeylineRimIsSoft;
@property (Td,N,V_visionIntelligenceKeylineAlpha) visionIntelligenceKeylineAlpha;
@property (Td,N,V_visionIntelligenceKeylineLargeBlurRadius) visionIntelligenceKeylineLargeBlurRadius;
@property (Td,N,V_visionIntelligenceKeylineLargeAmount) visionIntelligenceKeylineLargeAmount;
@property (Td,N,V_visionIntelligenceKeylineLargeStart) visionIntelligenceKeylineLargeStart;
@property (Td,N,V_visionIntelligenceKeylineLargeEnd) visionIntelligenceKeylineLargeEnd;
@property (Td,N,V_visionIntelligenceKeylineSmallWidth) visionIntelligenceKeylineSmallWidth;
@property (Td,N,V_visionIntelligenceKeylineFadeLength) visionIntelligenceKeylineFadeLength;
@property (Td,N,V_visionIntelligenceKeylineFadeStart) visionIntelligenceKeylineFadeStart;
@property (Td,N,V_visionIntelligenceKeylineFadeEnd) visionIntelligenceKeylineFadeEnd;
@property (Td,N,V_visionIntelligenceKeylineEDRGain) visionIntelligenceKeylineEDRGain;
@property (T@"SBFFluidBehaviorSettings",&,N,V_visionIntelligenceBehaviorSettings) visionIntelligenceBehaviorSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_visionIntelligenceHintBehaviorSettings) visionIntelligenceHintBehaviorSettings;
@property (Td,N,V_zoomUpDropletRadius) zoomUpDropletRadius;
@property (Td,N,V_disableDropletEffectDelay) disableDropletEffectDelay;
@property (Td,N,V_zoomUpYAndScaleDelay) zoomUpYAndScaleDelay;
@property (T@"SBFFluidBehaviorSettings",&,N,V_zoomUpPositionXSettings) zoomUpPositionXSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_zoomUpPositionYSettings) zoomUpPositionYSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_zoomUpScaleSettings) zoomUpScaleSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_zoomUpCornerRadiusSettings) zoomUpCornerRadiusSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_zoomUpDropletRadiusAnimationSettings) zoomUpDropletRadiusAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_zoomUpBackgroundDimAnimationSettings) zoomUpBackgroundDimAnimationSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_zoomUpDisableDropletEffectFiltersSettings) zoomUpDisableDropletEffectFiltersSettings;
@property (TB,N,V_enableZoomUpBlur) enableZoomUpBlur;
@property (Td,N,V_zoomUpBlurStartProgress) zoomUpBlurStartProgress;
@property (Td,N,V_zoomUpBackgroundDimStartProgress) zoomUpBackgroundDimStartProgress;
@property (Td,N,V_dosidoTargetScale) dosidoTargetScale;
@property (T@"SBFFluidBehaviorSettings",&,N,V_dosidoLayoutAndPositionSettings) dosidoLayoutAndPositionSettings;
@property (T@"SBFFluidBehaviorSettings",&,N,V_dosidoScaleSettings) dosidoScaleSettings;
@property (TB,N,V_dosidoUsesHomeScreenBlur) dosidoUsesHomeScreenBlur;
@property (TB,N,V_enablesStationaryDetectionForUnlocked) enablesStationaryDetectionForUnlocked;
@property (Td,N,V_accidentalPreventionStationaryThreshold) accidentalPreventionStationaryThreshold;
@property (Td,N,V_accidentalPreventionPickUpBuffer) accidentalPreventionPickUpBuffer;
@property (Td,N,V_coachingUIDismissalInterval) coachingUIDismissalInterval;
@property (Td,N,V_stationaryDetectionDebounceInterval) stationaryDetectionDebounceInterval;
@property (Td,N,V_displaySwapMitigationGracePeriod) displaySwapMitigationGracePeriod;
```

## Class methods

```
+[SBCaptureButtonSettings settingsControllerModule];
```

## Instance methods

```
-[SBCaptureButtonSettings setDefaultValues];
-[SBCaptureButtonSettings dosidoLayoutAndPositionSettings];
-[SBCaptureButtonSettings setCoachingUIDismissalInterval:];
-[SBCaptureButtonSettings setIgnoreFaceDownAfterDuration:];
-[SBCaptureButtonSettings _configureSettings:withDamping:mass:stiffness:];
-[SBCaptureButtonSettings accidentalPreventionPickUpBuffer];
-[SBCaptureButtonSettings accidentalPreventionStationaryThreshold];
-[SBCaptureButtonSettings coachingUIDismissalInterval];
-[SBCaptureButtonSettings directLaunchAfterUnsuppressGracePeriod];
-[SBCaptureButtonSettings disableDropletEffectDelay];
-[SBCaptureButtonSettings displaySwapMitigationGracePeriod];
-[SBCaptureButtonSettings dosidoScaleSettings];
-[SBCaptureButtonSettings dosidoTargetScale];
-[SBCaptureButtonSettings dosidoUsesHomeScreenBlur];
-[SBCaptureButtonSettings enableZoomUpBlur];
-[SBCaptureButtonSettings enablesStationaryDetectionForUnlocked];
-[SBCaptureButtonSettings ignoreFaceDownAfterDuration];
-[SBCaptureButtonSettings launchAfterButtonUpGracePeriod];
-[SBCaptureButtonSettings longPressVisionIntelligenceDelay];
-[SBCaptureButtonSettings preludeCornerRadius];
-[SBCaptureButtonSettings preludeDropletRadius];
-[SBCaptureButtonSettings preludePresentationTranslationSettings];
-[SBCaptureButtonSettings preludeScreenEdgeInset];
-[SBCaptureButtonSettings setAccidentalPreventionPickUpBuffer:];
-[SBCaptureButtonSettings setAccidentalPreventionStationaryThreshold:];
-[SBCaptureButtonSettings setDirectLaunchAfterUnsuppressGracePeriod:];
-[SBCaptureButtonSettings setDisableDropletEffectDelay:];
-[SBCaptureButtonSettings setDisplaySwapMitigationGracePeriod:];
-[SBCaptureButtonSettings setDosidoLayoutAndPositionSettings:];
-[SBCaptureButtonSettings setDosidoScaleSettings:];
-[SBCaptureButtonSettings setDosidoTargetScale:];
-[SBCaptureButtonSettings setDosidoUsesHomeScreenBlur:];
-[SBCaptureButtonSettings setEnableZoomUpBlur:];
-[SBCaptureButtonSettings setEnablesStationaryDetectionForUnlocked:];
-[SBCaptureButtonSettings setLaunchAfterButtonUpGracePeriod:];
-[SBCaptureButtonSettings setLongPressVisionIntelligenceDelay:];
-[SBCaptureButtonSettings setPreludeCornerRadius:];
-[SBCaptureButtonSettings setPreludeDropletRadius:];
-[SBCaptureButtonSettings setPreludePresentationTranslationSettings:];
-[SBCaptureButtonSettings setPreludeScreenEdgeInset:];
-[SBCaptureButtonSettings setStationaryDetectionDebounceInterval:];
-[SBCaptureButtonSettings setVisionIntelligenceBehaviorSettings:];
-[SBCaptureButtonSettings setVisionIntelligenceHintBehaviorSettings:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineAlpha:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineEDRGain:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineFadeEnd:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineFadeLength:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineFadeStart:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineLargeAmount:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineLargeBlurRadius:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineLargeEnd:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineLargeStart:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineRimIsSoft:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineScreenBlendMode:];
-[SBCaptureButtonSettings setVisionIntelligenceKeylineSmallWidth:];
-[SBCaptureButtonSettings setZoomUpBackgroundDimAnimationSettings:];
-[SBCaptureButtonSettings setZoomUpBackgroundDimStartProgress:];
-[SBCaptureButtonSettings setZoomUpBlurStartProgress:];
-[SBCaptureButtonSettings setZoomUpCornerRadiusSettings:];
-[SBCaptureButtonSettings setZoomUpDisableDropletEffectFiltersSettings:];
-[SBCaptureButtonSettings setZoomUpDropletRadius:];
-[SBCaptureButtonSettings setZoomUpDropletRadiusAnimationSettings:];
-[SBCaptureButtonSettings setZoomUpPositionXSettings:];
-[SBCaptureButtonSettings setZoomUpPositionYSettings:];
-[SBCaptureButtonSettings setZoomUpScaleSettings:];
-[SBCaptureButtonSettings setZoomUpYAndScaleDelay:];
-[SBCaptureButtonSettings stationaryDetectionDebounceInterval];
-[SBCaptureButtonSettings visionIntelligenceBehaviorSettings];
-[SBCaptureButtonSettings visionIntelligenceHintBehaviorSettings];
-[SBCaptureButtonSettings visionIntelligenceKeylineAlpha];
-[SBCaptureButtonSettings visionIntelligenceKeylineEDRGain];
-[SBCaptureButtonSettings visionIntelligenceKeylineFadeEnd];
-[SBCaptureButtonSettings visionIntelligenceKeylineFadeLength];
-[SBCaptureButtonSettings visionIntelligenceKeylineFadeStart];
-[SBCaptureButtonSettings visionIntelligenceKeylineLargeAmount];
-[SBCaptureButtonSettings visionIntelligenceKeylineLargeBlurRadius];
-[SBCaptureButtonSettings visionIntelligenceKeylineLargeEnd];
-[SBCaptureButtonSettings visionIntelligenceKeylineLargeStart];
-[SBCaptureButtonSettings visionIntelligenceKeylineRimIsSoft];
-[SBCaptureButtonSettings visionIntelligenceKeylineScreenBlendMode];
-[SBCaptureButtonSettings visionIntelligenceKeylineSmallWidth];
-[SBCaptureButtonSettings zoomUpBackgroundDimAnimationSettings];
-[SBCaptureButtonSettings zoomUpBackgroundDimStartProgress];
-[SBCaptureButtonSettings zoomUpBlurStartProgress];
-[SBCaptureButtonSettings zoomUpCornerRadiusSettings];
-[SBCaptureButtonSettings zoomUpDisableDropletEffectFiltersSettings];
-[SBCaptureButtonSettings zoomUpDropletRadius];
-[SBCaptureButtonSettings zoomUpDropletRadiusAnimationSettings];
-[SBCaptureButtonSettings zoomUpPositionXSettings];
-[SBCaptureButtonSettings zoomUpPositionYSettings];
-[SBCaptureButtonSettings zoomUpScaleSettings];
-[SBCaptureButtonSettings zoomUpYAndScaleDelay];
```
