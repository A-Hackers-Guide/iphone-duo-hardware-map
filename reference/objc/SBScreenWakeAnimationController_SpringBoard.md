# `SBScreenWakeAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerObserver`, `SBFScreenWakeAnimationControlling`
- 26 instance variables, 5 properties, 31 instance methods, 2 class methods

## Instance variables

```
d _originalDateLeftEdge;
d _originalDateBottomEdge;
d _finalTimeAlpha;
d _finalStatusBarAlpha;
@"<SBFScreenWakeAnimationTarget>" _target;
B _preparingToAnimateWake;
B _animatingForWake;
B _animatingForSleep;
B _insideWakeCompletionBlock;
B _insideSleepCompletionBlock;
i _animationToken;
@? _wakeCompletionBlock;
@? _sleepCompletionBlock;
B _animatingWallpaper;
B _animatingContent;
B _animatingBacklight;
B _ignoringInteractionEvents;
B _waitingForScreenUnblank;
@"SBWindowScene" _windowScene;
q _lastBacklightChangeSource;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarAssertion;
@"SBWindowSceneStatusBarManager" _statusBarManager;
@"SBBacklightController" _backlightController;
@"NSMutableSet" _temporaryDisabledReasons;
@"<BSInvalidatable>" _fadeAnimationOrientationUpdateDeferralAssertion;
@"<SBScreenWakeAnimationControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBScreenWakeAnimationControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBScreenWakeAnimationController _animationSpeedForBacklightChangeSource:isWake:];
+[SBScreenWakeAnimationController backlightFadeDurationForSource:isWake:];
```

## Instance methods

```
-[SBScreenWakeAnimationController backlightController:didTransitionToBacklightState:source:];
-[SBScreenWakeAnimationController _animationSettingsForBacklightChangeSource:isWake:];
-[SBScreenWakeAnimationController succinctDescriptionBuilder];
-[SBScreenWakeAnimationController sleepForSource:completion:];
-[SBScreenWakeAnimationController setScreenWakeTemporarilyDisabled:forReason:];
-[SBScreenWakeAnimationController dealloc];
-[SBScreenWakeAnimationController isWakeAnimationInProgress];
-[SBScreenWakeAnimationController descriptionWithMultilinePrefix:];
-[SBScreenWakeAnimationController _setInteractionEventsIgnored:];
-[SBScreenWakeAnimationController _startWakeAnimationsForWaking:animationSettings:];
-[SBScreenWakeAnimationController _cleanupAnimationWhenInterruptingWaking:];
-[SBScreenWakeAnimationController _cleanupAnimationWhenInterruptingWaking:force:];
-[SBScreenWakeAnimationController _handleAnimationCompletionIfNecessaryForWaking:force:];
-[SBScreenWakeAnimationController prepareToWakeForSource:timeAlpha:statusBarAlpha:target:dateView:completion:];
-[SBScreenWakeAnimationController initWithWindowScene:];
-[SBScreenWakeAnimationController _setLastBacklightChangeSource:];
-[SBScreenWakeAnimationController succinctDescription];
-[SBScreenWakeAnimationController setDelegate:];
-[SBScreenWakeAnimationController _runCompletionHandlerForWake:reason:];
-[SBScreenWakeAnimationController delegate];
-[SBScreenWakeAnimationController isWakeAnimationInProgressForSource:];
-[SBScreenWakeAnimationController description];
-[SBScreenWakeAnimationController _setRelevantLockScreenViewsHidden:];
-[SBScreenWakeAnimationController _startWakeIfNecessary];
-[SBScreenWakeAnimationController _startWakeFromUnblankNotification];
-[SBScreenWakeAnimationController interruptSleepAnimationIfNeeded];
-[SBScreenWakeAnimationController _updateWakeEffectsForWake:animated:completion:];
-[SBScreenWakeAnimationController _handleAnimationCompletionIfNecessaryForWaking:];
-[SBScreenWakeAnimationController sleepForSource:target:completion:];
-[SBScreenWakeAnimationController isSleepAnimationInProgress];
-[SBScreenWakeAnimationController descriptionBuilderWithMultilinePrefix:];
```
