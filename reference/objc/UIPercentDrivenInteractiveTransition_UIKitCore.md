# `UIPercentDrivenInteractiveTransition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerInteractiveTransitioning`
- 13 instance variables, 15 properties, 37 instance methods, 0 class methods

## Instance variables

```
d _duration;
B _didCommitAnimations;
@"<UIViewImplicitlyAnimating>" _interruptibleAnimator;
@"NSUUID" _animationTrackingAnimatorUUID;
B _wantsInteractiveStart;
B __transitionInterrupted;
B __usesPacedFractionComplete;
B __clampsPercentComplete;
d _completionSpeed;
q _completionCurve;
@"<UITimingCurveProvider>" _timingCurve;
@"NSString" __originalFillMode;
@"NSUUID" __uuid;
```

## Properties

```
@property (T@"NSString",&,N,S_setOriginalFillMode:,V__originalFillMode) _originalFillMode;
@property (T@"NSUUID",&,N,S_setUuid:,V__uuid) _uuid;
@property (TB,N,G_isTransitionInterrupted,S_setTransitionInterrupted:,V__transitionInterrupted) _transitionInterrupted;
@property (TB,N,S_setUsesPacedFractionComplete:,V__usesPacedFractionComplete) _usesPacedFractionComplete;
@property (TB,N,S_setClampsPercentComplete:,V__clampsPercentComplete) _clampsPercentComplete;
@property (Td,R) duration;
@property (Td,R) percentComplete;
@property (Td,N,V_completionSpeed) completionSpeed;
@property (Tq,N,V_completionCurve) completionCurve;
@property (T@"<UITimingCurveProvider>",&,N,V_timingCurve) timingCurve;
@property (TB,N,V_wantsInteractiveStart) wantsInteractiveStart;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPercentDrivenInteractiveTransition updateInteractiveTransition:];
-[UIPercentDrivenInteractiveTransition percentComplete];
-[UIPercentDrivenInteractiveTransition init];
-[UIPercentDrivenInteractiveTransition startInteractiveTransition:];
-[UIPercentDrivenInteractiveTransition _setDuration:];
-[UIPercentDrivenInteractiveTransition _resetInteractionController];
-[UIPercentDrivenInteractiveTransition cancelInteractiveTransition];
-[UIPercentDrivenInteractiveTransition pauseInteractiveTransition];
-[UIPercentDrivenInteractiveTransition duration];
-[UIPercentDrivenInteractiveTransition finishInteractiveTransition];
-[UIPercentDrivenInteractiveTransition wantsInteractiveStart];
-[UIPercentDrivenInteractiveTransition completionCurve];
-[UIPercentDrivenInteractiveTransition _stopInteractiveTransition];
-[UIPercentDrivenInteractiveTransition _startingVelocity];
-[UIPercentDrivenInteractiveTransition completionSpeed];
-[UIPercentDrivenInteractiveTransition setTimingCurve:];
-[UIPercentDrivenInteractiveTransition _clampsPercentComplete];
-[UIPercentDrivenInteractiveTransition _continueInterruptibleTransitionFromPercentComplete:reversed:];
-[UIPercentDrivenInteractiveTransition _durationFactorForPercentComplete:reversed:];
-[UIPercentDrivenInteractiveTransition _isTransitionInterrupted];
-[UIPercentDrivenInteractiveTransition _originalFillMode];
-[UIPercentDrivenInteractiveTransition _setClampsPercentComplete:];
-[UIPercentDrivenInteractiveTransition _setOriginalFillMode:];
-[UIPercentDrivenInteractiveTransition _setTransitionInterrupted:];
-[UIPercentDrivenInteractiveTransition _setUsesPacedFractionComplete:];
-[UIPercentDrivenInteractiveTransition _setUuid:];
-[UIPercentDrivenInteractiveTransition _startInterruptibleTransition:];
-[UIPercentDrivenInteractiveTransition _stopInteractiveTransition:];
-[UIPercentDrivenInteractiveTransition _updateInteractiveTransition:percent:isFinished:didComplete:];
-[UIPercentDrivenInteractiveTransition _useAnimatorTrackingToDriveTransition];
-[UIPercentDrivenInteractiveTransition _usesPacedFractionComplete];
-[UIPercentDrivenInteractiveTransition _uuid];
-[UIPercentDrivenInteractiveTransition setCompletionCurve:];
-[UIPercentDrivenInteractiveTransition setCompletionSpeed:];
-[UIPercentDrivenInteractiveTransition setWantsInteractiveStart:];
-[UIPercentDrivenInteractiveTransition startInteractiveTransition:containerViews:animation:];
-[UIPercentDrivenInteractiveTransition timingCurve];
```
