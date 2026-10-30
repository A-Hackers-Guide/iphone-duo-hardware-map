# `SBDisplayYoinkingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBSUIDisplayYoinkingSceneHostComponentDelegate`, `SBTapToWakeHandling`, `SBScenePresenting`, `SBSensorActivityObserver`, `PTSettingsKeyPathObserver`, `SBDisplayYoinkingCoordinatorObserver`
- 28 instance variables, 15 properties, 69 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"NSHashTable" _observers;
B _flipActive;
B _yoinkingSliderInteractionInProgressOnOtherDisplay;
B _slidePastTouchBlockingThreshold;
d _lastFlipUptime;
d _lastSwapUptime;
B _flipOverridden;
@"NSTimer" _sliderTimer;
B _swapped;
B _swapPending;
@"SBWindowScene" _windowSceneToRestore;
@"SBSUIDisplayYoinkingSceneHostComponent" _sliderHostComponent;
@"<BSInvalidatable>" _presenterAssertion;
@"<SBScenePresentingDelegate>" _presentingDelegate;
@"SBSensorActivityDataProvider" _sensorActivityDataProvider;
B _cameraSessionActive;
B _shouldRevealYoinkingSlider;
B _canRevealYoinkingSlider;
B _yoinkingSliderVisible;
B _yoinkingSliderInteractionInProgress;
@"<SBDisplayYoinkingControllerDelegate>" _delegate;
@"UIViewController" _yoinkingSliderViewController;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"<BSInvalidatable>" _tapToWakeHandlerAssertion;
@"<BSInvalidatable>" _digitizerActiveDuringSecureIndicatorAssertion;
@"<BSInvalidatable>" _touchSuppressionAssertion;
@"<BSInvalidatable>" _systemGestureDisableAssertion;
```

## Properties

```
@property (TB,N,V_canRevealYoinkingSlider) canRevealYoinkingSlider;
@property (TB,N,V_shouldRevealYoinkingSlider) shouldRevealYoinkingSlider;
@property (T@"UIViewController",&,N,V_yoinkingSliderViewController) yoinkingSliderViewController;
@property (T@"<BSInvalidatable>",&,N,V_stateCaptureAssertion) stateCaptureAssertion;
@property (T@"<BSInvalidatable>",&,N,V_tapToWakeHandlerAssertion) tapToWakeHandlerAssertion;
@property (T@"<BSInvalidatable>",&,N,V_digitizerActiveDuringSecureIndicatorAssertion) digitizerActiveDuringSecureIndicatorAssertion;
@property (T@"<BSInvalidatable>",&,N,V_touchSuppressionAssertion) touchSuppressionAssertion;
@property (T@"<BSInvalidatable>",&,N,V_systemGestureDisableAssertion) systemGestureDisableAssertion;
@property (T@"<SBDisplayYoinkingControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisYoinkingSliderVisible,V_yoinkingSliderVisible) yoinkingSliderVisible;
@property (TB,R,N,GisYoinkingSliderInteractionInProgress,V_yoinkingSliderInteractionInProgress) yoinkingSliderInteractionInProgress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayYoinkingController setPresentingDelegate:];
-[SBDisplayYoinkingController activityDidChangeForSensorActivityDataProvider:];
-[SBDisplayYoinkingController dismissScene:];
-[SBDisplayYoinkingController removeObserver:];
-[SBDisplayYoinkingController setTouchSuppressionAssertion:];
-[SBDisplayYoinkingController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayYoinkingController dealloc];
-[SBDisplayYoinkingController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayYoinkingController presentScene:viewControllerBuilderBlock:];
-[SBDisplayYoinkingController addObserver:];
-[SBDisplayYoinkingController setDelegate:];
-[SBDisplayYoinkingController delegate];
-[SBDisplayYoinkingController description];
-[SBDisplayYoinkingController appendDescriptionToStream:];
-[SBDisplayYoinkingController initWithWindowScene:delegate:];
-[SBDisplayYoinkingController settings:changedValueForKeyPath:];
-[SBDisplayYoinkingController touchSuppressionAssertion];
-[SBDisplayYoinkingController isEligible];
-[SBDisplayYoinkingController displayYoinkingSceneHostComponent:sliderDidCrossSwapThreshold:];
-[SBDisplayYoinkingController displayYoinkingSceneHostComponent:sliderDidCrossTouchBlockingThreshold:];
-[SBDisplayYoinkingController displayYoinkingSceneHostComponentSliderDidBeginInteraction:];
-[SBDisplayYoinkingController displayYoinkingSceneHostComponentSliderDidBeginSlide:];
-[SBDisplayYoinkingController displayYoinkingSceneHostComponentSliderDidCancelSlide:];
-[SBDisplayYoinkingController displayYoinkingSceneHostComponentSliderDidCompleteSlide:];
-[SBDisplayYoinkingController displayYoinkingSceneHostComponentSliderDidEndInteraction:];
-[SBDisplayYoinkingController _endSliderInteractionForReason:];
-[SBDisplayYoinkingController _activeFlipShowsSlider];
-[SBDisplayYoinkingController _addYoinkingSliderScene];
-[SBDisplayYoinkingController _anyCameraSessionCurrentlyActive];
-[SBDisplayYoinkingController _applySliderSettings:];
-[SBDisplayYoinkingController _canYoinkToThisDisplay];
-[SBDisplayYoinkingController _cancelSlide];
-[SBDisplayYoinkingController _removeYoinkingSliderScene];
-[SBDisplayYoinkingController _sceneController];
-[SBDisplayYoinkingController _setListeningToTap:];
-[SBDisplayYoinkingController _setSlidePastTouchBlockingThreshold:];
-[SBDisplayYoinkingController _setTouchesBlocked:];
-[SBDisplayYoinkingController _setYoinkingSliderInteractionInProgress:];
-[SBDisplayYoinkingController _sliderScene];
-[SBDisplayYoinkingController _startOrExtendSliderTimerForReason:];
-[SBDisplayYoinkingController _updateRevealState];
-[SBDisplayYoinkingController _updateSliderSettings];
-[SBDisplayYoinkingController _yoinkToWindowScene:reason:];
-[SBDisplayYoinkingController canRevealYoinkingSlider];
-[SBDisplayYoinkingController currentDisplayIdentity];
-[SBDisplayYoinkingController digitizerActiveDuringSecureIndicatorAssertion];
-[SBDisplayYoinkingController displayYoinkingCoordinator:didChangeFlipActive:];
-[SBDisplayYoinkingController displayYoinkingCoordinator:didChangeFlipOverride:];
-[SBDisplayYoinkingController displayYoinkingCoordinator:didChangeListeningToFlip:];
-[SBDisplayYoinkingController displayYoinkingCoordinator:didChangeSlidePastTouchBlockingThresholdOnOtherDisplay:];
-[SBDisplayYoinkingController displayYoinkingCoordinator:didChangeYoinkingSliderInteractionInProgressOnOtherDisplay:];
-[SBDisplayYoinkingController handleTapToWakeForController:];
-[SBDisplayYoinkingController isVisibleOnScreen];
-[SBDisplayYoinkingController isYoinkingSliderInteractionInProgress];
-[SBDisplayYoinkingController isYoinkingSliderVisible];
-[SBDisplayYoinkingController parentSceneIdentityToken];
-[SBDisplayYoinkingController setCanRevealYoinkingSlider:];
-[SBDisplayYoinkingController setDigitizerActiveDuringSecureIndicatorAssertion:];
-[SBDisplayYoinkingController setShouldRevealYoinkingSlider:];
-[SBDisplayYoinkingController setStateCaptureAssertion:];
-[SBDisplayYoinkingController setSystemGestureDisableAssertion:];
-[SBDisplayYoinkingController setTapToWakeHandlerAssertion:];
-[SBDisplayYoinkingController setYoinkingSliderViewController:];
-[SBDisplayYoinkingController setYoinkingSliderVisible:];
-[SBDisplayYoinkingController shouldRevealYoinkingSlider];
-[SBDisplayYoinkingController stateCaptureAssertion];
-[SBDisplayYoinkingController systemGestureDisableAssertion];
-[SBDisplayYoinkingController tapToWakeHandlerAssertion];
-[SBDisplayYoinkingController yoinkingSliderViewController];
```
