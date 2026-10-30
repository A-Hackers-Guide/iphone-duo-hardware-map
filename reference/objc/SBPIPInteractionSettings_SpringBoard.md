# `SBPIPInteractionSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 35 instance variables, 35 properties, 71 instance methods, 1 class methods

## Instance variables

```
B _shouldStashOnTransitionToSwitcher;
B _shouldUnstashOnTransitionFromSwitcher;
B _shouldStashOnTransitionToHomescreen;
B _shouldUnstashOnTransitionFromHomescreen;
B _shouldStashOnAppToAppTransitions;
B _usesKeyboards;
B _keyboardDismissesOnTransitionToHomescreen;
B _keyboardDismissesOnOutsideUserInteractionOnHomescreen;
B _keyboardDismissesOnOutsideUserInteractionOutsideHomescreen;
B _alwaysStartAtSmallestSize;
B _panGestureEnabled;
B _edgeResizeGestureEnabled;
B _pinchGestureEnabled;
B _rotationGestureEnabled;
B _stashingEnabled;
@"SBPIPEdgeResizeSettings" _edgeResizeSettings;
Q _freePositioning;
d _defaultContentSizeResetTimeout;
d _inFlightHitTestPadding;
d _maximumSizeSpanForPreferredSizeTuning;
d _minimumSizeSpanBetweenPreferredSizes;
d _positionDecelerationRate;
d _positionExtenderMaximumDistance;
d _positionVelocityYWeightOverVelocityX;
d _rotationExtenderMaximumDistance;
d _rotationPreRecognitionWeight;
d _rotationRubberBandCoefficient;
d _scaleDecelerationRate;
d _scaleExtenderMaximumDistance;
d _scaleLowPassFilterPreviousWeight;
d _stashProgressTabAppearanceThresholdX;
@"SBFFluidBehaviorSettings" _interactiveFluidBehavior;
@"SBFFluidBehaviorSettings" _stashTabFluidBehavior;
@"SBFFluidBehaviorSettings" _rotationFluidBehavior;
@"SBFFluidBehaviorSettings" _regionUpdateFluidBehavior;
```

## Properties

```
@property (T@"SBPIPEdgeResizeSettings",&,N,V_edgeResizeSettings) edgeResizeSettings;
@property (TB,N,V_shouldStashOnTransitionToSwitcher) shouldStashOnTransitionToSwitcher;
@property (TB,N,V_shouldUnstashOnTransitionFromSwitcher) shouldUnstashOnTransitionFromSwitcher;
@property (TB,N,V_shouldStashOnTransitionToHomescreen) shouldStashOnTransitionToHomescreen;
@property (TB,N,V_shouldUnstashOnTransitionFromHomescreen) shouldUnstashOnTransitionFromHomescreen;
@property (TB,N,V_shouldStashOnAppToAppTransitions) shouldStashOnAppToAppTransitions;
@property (TB,N,V_usesKeyboards) usesKeyboards;
@property (TB,N,V_keyboardDismissesOnTransitionToHomescreen) keyboardDismissesOnTransitionToHomescreen;
@property (TB,N,V_keyboardDismissesOnOutsideUserInteractionOnHomescreen) keyboardDismissesOnOutsideUserInteractionOnHomescreen;
@property (TB,N,V_keyboardDismissesOnOutsideUserInteractionOutsideHomescreen) keyboardDismissesOnOutsideUserInteractionOutsideHomescreen;
@property (TB,N,V_alwaysStartAtSmallestSize) alwaysStartAtSmallestSize;
@property (TB,N,V_panGestureEnabled) panGestureEnabled;
@property (TB,N,V_edgeResizeGestureEnabled) edgeResizeGestureEnabled;
@property (TB,N,V_pinchGestureEnabled) pinchGestureEnabled;
@property (TB,N,V_rotationGestureEnabled) rotationGestureEnabled;
@property (TB,N,V_stashingEnabled) stashingEnabled;
@property (TQ,N,V_freePositioning) freePositioning;
@property (Td,N,V_defaultContentSizeResetTimeout) defaultContentSizeResetTimeout;
@property (Td,N,V_inFlightHitTestPadding) inFlightHitTestPadding;
@property (Td,N,V_maximumSizeSpanForPreferredSizeTuning) maximumSizeSpanForPreferredSizeTuning;
@property (Td,N,V_minimumSizeSpanBetweenPreferredSizes) minimumSizeSpanBetweenPreferredSizes;
@property (Td,N,V_positionDecelerationRate) positionDecelerationRate;
@property (Td,N,V_positionExtenderMaximumDistance) positionExtenderMaximumDistance;
@property (Td,N,V_positionVelocityYWeightOverVelocityX) positionVelocityYWeightOverVelocityX;
@property (Td,N,V_rotationExtenderMaximumDistance) rotationExtenderMaximumDistance;
@property (Td,N,V_rotationPreRecognitionWeight) rotationPreRecognitionWeight;
@property (Td,N,V_rotationRubberBandCoefficient) rotationRubberBandCoefficient;
@property (Td,N,V_scaleDecelerationRate) scaleDecelerationRate;
@property (Td,N,V_scaleExtenderMaximumDistance) scaleExtenderMaximumDistance;
@property (Td,N,V_scaleLowPassFilterPreviousWeight) scaleLowPassFilterPreviousWeight;
@property (Td,N,V_stashProgressTabAppearanceThresholdX) stashProgressTabAppearanceThresholdX;
@property (T@"SBFFluidBehaviorSettings",&,N,V_interactiveFluidBehavior) interactiveFluidBehavior;
@property (T@"SBFFluidBehaviorSettings",&,N,V_stashTabFluidBehavior) stashTabFluidBehavior;
@property (T@"SBFFluidBehaviorSettings",&,N,V_rotationFluidBehavior) rotationFluidBehavior;
@property (T@"SBFFluidBehaviorSettings",&,N,V_regionUpdateFluidBehavior) regionUpdateFluidBehavior;
```

## Class methods

```
+[SBPIPInteractionSettings settingsControllerModule];
```

## Instance methods

```
-[SBPIPInteractionSettings setDefaultValues];
-[SBPIPInteractionSettings freePositioning];
-[SBPIPInteractionSettings positionExtenderMaximumDistance];
-[SBPIPInteractionSettings rotationExtenderMaximumDistance];
-[SBPIPInteractionSettings stashingEnabled];
-[SBPIPInteractionSettings alwaysStartAtSmallestSize];
-[SBPIPInteractionSettings defaultContentSizeResetTimeout];
-[SBPIPInteractionSettings edgeResizeGestureEnabled];
-[SBPIPInteractionSettings edgeResizeSettings];
-[SBPIPInteractionSettings inFlightHitTestPadding];
-[SBPIPInteractionSettings interactiveFluidBehavior];
-[SBPIPInteractionSettings keyboardDismissesOnOutsideUserInteractionOnHomescreen];
-[SBPIPInteractionSettings keyboardDismissesOnOutsideUserInteractionOutsideHomescreen];
-[SBPIPInteractionSettings keyboardDismissesOnTransitionToHomescreen];
-[SBPIPInteractionSettings maximumSizeSpanForPreferredSizeTuning];
-[SBPIPInteractionSettings minimumSizeSpanBetweenPreferredSizes];
-[SBPIPInteractionSettings panGestureEnabled];
-[SBPIPInteractionSettings pinchGestureEnabled];
-[SBPIPInteractionSettings positionDecelerationRate];
-[SBPIPInteractionSettings positionVelocityYWeightOverVelocityX];
-[SBPIPInteractionSettings regionUpdateFluidBehavior];
-[SBPIPInteractionSettings rotationFluidBehavior];
-[SBPIPInteractionSettings rotationGestureEnabled];
-[SBPIPInteractionSettings rotationPreRecognitionWeight];
-[SBPIPInteractionSettings rotationRubberBandCoefficient];
-[SBPIPInteractionSettings scaleDecelerationRate];
-[SBPIPInteractionSettings scaleExtenderMaximumDistance];
-[SBPIPInteractionSettings scaleLowPassFilterPreviousWeight];
-[SBPIPInteractionSettings setAlwaysStartAtSmallestSize:];
-[SBPIPInteractionSettings setDefaultContentSizeResetTimeout:];
-[SBPIPInteractionSettings setEdgeResizeGestureEnabled:];
-[SBPIPInteractionSettings setEdgeResizeSettings:];
-[SBPIPInteractionSettings setFreePositioning:];
-[SBPIPInteractionSettings setInFlightHitTestPadding:];
-[SBPIPInteractionSettings setInteractiveFluidBehavior:];
-[SBPIPInteractionSettings setKeyboardDismissesOnOutsideUserInteractionOnHomescreen:];
-[SBPIPInteractionSettings setKeyboardDismissesOnOutsideUserInteractionOutsideHomescreen:];
-[SBPIPInteractionSettings setKeyboardDismissesOnTransitionToHomescreen:];
-[SBPIPInteractionSettings setMaximumSizeSpanForPreferredSizeTuning:];
-[SBPIPInteractionSettings setMinimumSizeSpanBetweenPreferredSizes:];
-[SBPIPInteractionSettings setPanGestureEnabled:];
-[SBPIPInteractionSettings setPinchGestureEnabled:];
-[SBPIPInteractionSettings setPositionDecelerationRate:];
-[SBPIPInteractionSettings setPositionExtenderMaximumDistance:];
-[SBPIPInteractionSettings setPositionVelocityYWeightOverVelocityX:];
-[SBPIPInteractionSettings setRegionUpdateFluidBehavior:];
-[SBPIPInteractionSettings setRotationExtenderMaximumDistance:];
-[SBPIPInteractionSettings setRotationFluidBehavior:];
-[SBPIPInteractionSettings setRotationGestureEnabled:];
-[SBPIPInteractionSettings setRotationPreRecognitionWeight:];
-[SBPIPInteractionSettings setRotationRubberBandCoefficient:];
-[SBPIPInteractionSettings setScaleDecelerationRate:];
-[SBPIPInteractionSettings setScaleExtenderMaximumDistance:];
-[SBPIPInteractionSettings setScaleLowPassFilterPreviousWeight:];
-[SBPIPInteractionSettings setShouldStashOnAppToAppTransitions:];
-[SBPIPInteractionSettings setShouldStashOnTransitionToHomescreen:];
-[SBPIPInteractionSettings setShouldStashOnTransitionToSwitcher:];
-[SBPIPInteractionSettings setShouldUnstashOnTransitionFromHomescreen:];
-[SBPIPInteractionSettings setShouldUnstashOnTransitionFromSwitcher:];
-[SBPIPInteractionSettings setStashProgressTabAppearanceThresholdX:];
-[SBPIPInteractionSettings setStashTabFluidBehavior:];
-[SBPIPInteractionSettings setStashingEnabled:];
-[SBPIPInteractionSettings setUsesKeyboards:];
-[SBPIPInteractionSettings shouldStashOnAppToAppTransitions];
-[SBPIPInteractionSettings shouldStashOnTransitionToHomescreen];
-[SBPIPInteractionSettings shouldStashOnTransitionToSwitcher];
-[SBPIPInteractionSettings shouldUnstashOnTransitionFromHomescreen];
-[SBPIPInteractionSettings shouldUnstashOnTransitionFromSwitcher];
-[SBPIPInteractionSettings stashProgressTabAppearanceThresholdX];
-[SBPIPInteractionSettings stashTabFluidBehavior];
-[SBPIPInteractionSettings usesKeyboards];
```
