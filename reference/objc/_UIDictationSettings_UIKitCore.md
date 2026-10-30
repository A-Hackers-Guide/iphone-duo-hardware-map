# `_UIDictationSettings`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 34 instance variables, 34 properties, 69 instance methods, 6 class methods

## Instance variables

```
B _glowEffectEnabled;
B _pulseAnimationEnabled;
B _trailAnimationEnabled;
B _soundReactiveCursorEnabled;
B _commandHapticFeedbackEnabled;
B _voiceCommandsInIWorkEnabled;
d _minimumRadius;
d _cursorGlowBlurRadius;
d _trailingGlowBlurRadius;
@"NSString" _lightModeCompositingFiler;
@"NSString" _darkModeCompositingFiler;
d _trailingGlowDuration;
d _tailHeight;
d _headHeight;
d _trailingGlowAlpha;
d _cursorGlowAlphaMin;
d _cursorGlowAlphaMax;
d _revealFadeTime;
d _typewriterEffectFramesPerSecond;
d _typewriterEffectStreamingCharacterInsertionRate;
d _typewriterEffectMinDurationBetweenHypotheses;
d _pulseFrameRate;
d _trailFrameRate;
d _audioPollingRate;
d _audioWidthMaxBump;
d _audioHeightMaxBump;
d _audioScaleAnimationDampingRatio;
d _audioScaleAnimationResponse;
q _impactStyle;
d _impactIntensity;
d _pulseWidthMaxBump;
d _pulseHeightMaxBump;
d _pulseDuration;
d _cursorGlowBorderPadding;
```

## Properties

```
@property (Td,N,V_minimumRadius) minimumRadius;
@property (Td,N,V_cursorGlowBlurRadius) cursorGlowBlurRadius;
@property (Td,N,V_trailingGlowBlurRadius) trailingGlowBlurRadius;
@property (T@"NSString",&,N,V_lightModeCompositingFiler) lightModeCompositingFiler;
@property (T@"NSString",&,N,V_darkModeCompositingFiler) darkModeCompositingFiler;
@property (Td,N,V_trailingGlowDuration) trailingGlowDuration;
@property (Td,N,V_tailHeight) tailHeight;
@property (Td,N,V_headHeight) headHeight;
@property (Td,N,V_trailingGlowAlpha) trailingGlowAlpha;
@property (Td,N,V_cursorGlowAlphaMin) cursorGlowAlphaMin;
@property (Td,N,V_cursorGlowAlphaMax) cursorGlowAlphaMax;
@property (Td,N,V_revealFadeTime) revealFadeTime;
@property (Td,N,V_typewriterEffectFramesPerSecond) typewriterEffectFramesPerSecond;
@property (Td,N,V_typewriterEffectStreamingCharacterInsertionRate) typewriterEffectStreamingCharacterInsertionRate;
@property (Td,N,V_typewriterEffectMinDurationBetweenHypotheses) typewriterEffectMinDurationBetweenHypotheses;
@property (TB,N,V_glowEffectEnabled) glowEffectEnabled;
@property (TB,N,V_pulseAnimationEnabled) pulseAnimationEnabled;
@property (TB,N,V_trailAnimationEnabled) trailAnimationEnabled;
@property (Td,N,V_pulseFrameRate) pulseFrameRate;
@property (Td,N,V_trailFrameRate) trailFrameRate;
@property (TB,N,V_soundReactiveCursorEnabled) soundReactiveCursorEnabled;
@property (Td,N,V_audioPollingRate) audioPollingRate;
@property (Td,N,V_audioWidthMaxBump) audioWidthMaxBump;
@property (Td,N,V_audioHeightMaxBump) audioHeightMaxBump;
@property (Td,N,V_audioScaleAnimationDampingRatio) audioScaleAnimationDampingRatio;
@property (Td,N,V_audioScaleAnimationResponse) audioScaleAnimationResponse;
@property (TB,N,V_commandHapticFeedbackEnabled) commandHapticFeedbackEnabled;
@property (Tq,N,V_impactStyle) impactStyle;
@property (Td,N,V_impactIntensity) impactIntensity;
@property (Td,N,V_pulseWidthMaxBump) pulseWidthMaxBump;
@property (Td,N,V_pulseHeightMaxBump) pulseHeightMaxBump;
@property (Td,N,V_pulseDuration) pulseDuration;
@property (TB,N,V_voiceCommandsInIWorkEnabled) voiceCommandsInIWorkEnabled;
@property (Td,N,V_cursorGlowBorderPadding) cursorGlowBorderPadding;
```

## Class methods

```
+[_UIDictationSettings frameRatesTitles];
+[_UIDictationSettings settingsControllerModule];
+[_UIDictationSettings impactStylesTitles];
+[_UIDictationSettings impactStyles];
+[_UIDictationSettings compositingFilters];
+[_UIDictationSettings frameRates];
```

## Instance methods

```
-[_UIDictationSettings setMinimumRadius:];
-[_UIDictationSettings minimumRadius];
-[_UIDictationSettings setAudioWidthMaxBump:];
-[_UIDictationSettings pulseFrameRate];
-[_UIDictationSettings trailAnimationEnabled];
-[_UIDictationSettings typewriterEffectMinDurationBetweenHypotheses];
-[_UIDictationSettings tailHeight];
-[_UIDictationSettings setCursorGlowBlurRadius:];
-[_UIDictationSettings cursorGlowAlphaMin];
-[_UIDictationSettings cursorGlowBorderPadding];
-[_UIDictationSettings setCursorGlowAlphaMin:];
-[_UIDictationSettings revealFadeTime];
-[_UIDictationSettings setPulseHeightMaxBump:];
-[_UIDictationSettings glowEffectEnabled];
-[_UIDictationSettings audioScaleAnimationResponse];
-[_UIDictationSettings setAudioScaleAnimationResponse:];
-[_UIDictationSettings setCursorGlowAlphaMax:];
-[_UIDictationSettings setTrailingGlowBlurRadius:];
-[_UIDictationSettings setTrailingGlowAlpha:];
-[_UIDictationSettings typewriterEffectStreamingCharacterInsertionRate];
-[_UIDictationSettings cursorGlowAlphaMax];
-[_UIDictationSettings setRevealFadeTime:];
-[_UIDictationSettings setDarkModeCompositingFiler:];
-[_UIDictationSettings soundReactiveCursorEnabled];
-[_UIDictationSettings setTypewriterEffectMinDurationBetweenHypotheses:];
-[_UIDictationSettings darkModeCompositingFiler];
-[_UIDictationSettings setGlowEffectEnabled:];
-[_UIDictationSettings trailingGlowBlurRadius];
-[_UIDictationSettings setPulseWidthMaxBump:];
-[_UIDictationSettings setVoiceCommandsInIWorkEnabled:];
-[_UIDictationSettings trailingGlowAlpha];
-[_UIDictationSettings setDefaultValues];
-[_UIDictationSettings pulseWidthMaxBump];
-[_UIDictationSettings pulseAnimationEnabled];
-[_UIDictationSettings audioWidthMaxBump];
-[_UIDictationSettings setTrailAnimationEnabled:];
-[_UIDictationSettings headHeight];
-[_UIDictationSettings setCursorGlowBorderPadding:];
-[_UIDictationSettings setLightModeCompositingFiler:];
-[_UIDictationSettings setTrailFrameRate:];
-[_UIDictationSettings impactIntensity];
-[_UIDictationSettings setPulseAnimationEnabled:];
-[_UIDictationSettings setTypewriterEffectFramesPerSecond:];
-[_UIDictationSettings audioScaleAnimationDampingRatio];
-[_UIDictationSettings setAudioHeightMaxBump:];
-[_UIDictationSettings trailingGlowDuration];
-[_UIDictationSettings setTailHeight:];
-[_UIDictationSettings lightModeCompositingFiler];
-[_UIDictationSettings audioPollingRate];
-[_UIDictationSettings setAudioScaleAnimationDampingRatio:];
-[_UIDictationSettings cursorGlowBlurRadius];
-[_UIDictationSettings setPulseFrameRate:];
-[_UIDictationSettings audioHeightMaxBump];
-[_UIDictationSettings setImpactIntensity:];
-[_UIDictationSettings setHeadHeight:];
-[_UIDictationSettings typewriterEffectFramesPerSecond];
-[_UIDictationSettings setTypewriterEffectStreamingCharacterInsertionRate:];
-[_UIDictationSettings pulseDuration];
-[_UIDictationSettings setImpactStyle:];
-[_UIDictationSettings commandHapticFeedbackEnabled];
-[_UIDictationSettings setTrailingGlowDuration:];
-[_UIDictationSettings voiceCommandsInIWorkEnabled];
-[_UIDictationSettings setPulseDuration:];
-[_UIDictationSettings setSoundReactiveCursorEnabled:];
-[_UIDictationSettings pulseHeightMaxBump];
-[_UIDictationSettings trailFrameRate];
-[_UIDictationSettings impactStyle];
-[_UIDictationSettings setCommandHapticFeedbackEnabled:];
-[_UIDictationSettings setAudioPollingRate:];
```
