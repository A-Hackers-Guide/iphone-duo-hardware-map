# `UISplitKeyboardSupport`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIKeyboardMotionSupport`
- Protocols: `UIGestureRecognizerDelegate`, `UIKeyboardKeyplaneTransitionDelegate`
- 14 instance variables, 6 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"UIPanGestureRecognizer" _singleFingerPanRecognizer;
@"UIPanGestureRecognizer" _twoFingerPanRecognizer;
B _isTranslating;
B _isSplitting;
B _splitLockState;
{CGPoint="x"d"y"d} _targetTranslation;
{CGPoint="x"d"y"d} _initialTranslation;
{CGPoint="x"d"y"d} _translationVelocity;
@"CADisplayLink" _displayLink;
d _lastBounceTime;
d _lastTranslationNotificationTime;
@? _bounceCompletionBlock;
B _shouldUpdateKLGForTransition;
B _handedOffTouchesToFloatingTransitionController;
```

## Properties

```
@property (TB,R,N) isTranslating;
@property (TB,R,N) isSplitting;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISplitKeyboardSupport transitionDidFinish:];
-[UISplitKeyboardSupport isTranslating];
-[UISplitKeyboardSupport prepareForTransition];
-[UISplitKeyboardSupport dock];
-[UISplitKeyboardSupport gestureRecognizer:shouldReceiveTouch:];
-[UISplitKeyboardSupport updateProgress:startHeight:endHeight:];
-[UISplitKeyboardSupport _connectController:];
-[UISplitKeyboardSupport isSplitting];
-[UISplitKeyboardSupport completedPlacementFrom:to:forController:];
-[UISplitKeyboardSupport gestureRecognizerShouldBegin:];
-[UISplitKeyboardSupport gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UISplitKeyboardSupport _disconnectingController:];
-[UISplitKeyboardSupport _updatedController];
-[UISplitKeyboardSupport finishTransitionWithCompletion:];
-[UISplitKeyboardSupport _updateBounceAnimation:];
-[UISplitKeyboardSupport _updateKeyboardLayoutGuideForHostFrame:animated:];
-[UISplitKeyboardSupport _updateKeyboardLayoutGuideForSplitTransition:];
-[UISplitKeyboardSupport _updateTrackingProviderForPoint:];
-[UISplitKeyboardSupport _updateTrackingProviderForSplitSize:offset:];
-[UISplitKeyboardSupport _updateTrackingProviderForUndockedFrame:];
-[UISplitKeyboardSupport bounceAnimationDidFinish];
-[UISplitKeyboardSupport cancelBounceAnimation];
-[UISplitKeyboardSupport cancelGestureRecognizers];
-[UISplitKeyboardSupport generateSplitNotificationForNewPlacement:];
-[UISplitKeyboardSupport invalidateDisplayLink];
-[UISplitKeyboardSupport startedPlacementFrom:to:forController:];
-[UISplitKeyboardSupport translateDetected:];
-[UISplitKeyboardSupport undock];
-[UISplitKeyboardSupport updatedControllerApplicator:];
-[UISplitKeyboardSupport willPerformPlacementFrom:to:forController:];
```
