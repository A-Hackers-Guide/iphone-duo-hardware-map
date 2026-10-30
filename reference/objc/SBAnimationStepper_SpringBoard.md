# `SBAnimationStepper`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAAnimationDelegate`, `SBUIAnimationStepping`
- 20 instance variables, 10 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"BSAnimationSettings" _animationSettings;
@"NSMutableSet" _views;
@"NSMutableSet" _finishedAnimatingViews;
@"CADisplayLink" _displayLink;
@? _completion;
d _percentage;
B _invalidated;
B _completed;
B _finishingForward;
B _finishingBackward;
B _animatingToStepPercent;
d _animatedSteppingTimestamp;
d _animatedSteppingStartPercent;
d _animatedSteppingTargetPercent;
d _finishBackwardTimestamp;
d _finishBackwardDuration;
d _finishBackwardPercentage;
B _adjustsDurationForLongestAnimation;
d _duration;
d _finishSpeed;
```

## Properties

```
@property (Td,N,V_finishSpeed) finishSpeed;
@property (T@"NSArray",R,D,N) views;
@property (Td,R,N,V_duration) duration;
@property (TB,N,V_adjustsDurationForLongestAnimation) adjustsDurationForLongestAnimation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisStepped) stepped;
@property (Td,N) stepPercentage;
```

## Instance methods

```
-[SBAnimationStepper views];
-[SBAnimationStepper _displayLinkFired:];
-[SBAnimationStepper animationDidStop:finished:];
-[SBAnimationStepper succinctDescriptionBuilder];
-[SBAnimationStepper init];
-[SBAnimationStepper dealloc];
-[SBAnimationStepper descriptionWithMultilinePrefix:];
-[SBAnimationStepper duration];
-[SBAnimationStepper succinctDescription];
-[SBAnimationStepper invalidate];
-[SBAnimationStepper descriptionBuilderWithMultilinePrefix:];
-[SBAnimationStepper initWithAnimationSettings:];
-[SBAnimationStepper _updateAnimationSteppingTarget:];
-[SBAnimationStepper _nextCommitTime];
-[SBAnimationStepper setFinishSpeed:];
-[SBAnimationStepper _adjustDurationForLongestAnimation];
-[SBAnimationStepper _checkForCompletion];
-[SBAnimationStepper _displayLinkFiredForBackwardToStart:];
-[SBAnimationStepper _makeSubviewTree:fromView:];
-[SBAnimationStepper _setStepPercentage:];
-[SBAnimationStepper adjustsDurationForLongestAnimation];
-[SBAnimationStepper finishSpeed];
-[SBAnimationStepper finishSteppingBackwardToStart];
-[SBAnimationStepper finishSteppingBackwardToStartWithCompletion:];
-[SBAnimationStepper finishSteppingForwardToEnd];
-[SBAnimationStepper finishSteppingForwardToEndWithCompletion:];
-[SBAnimationStepper isStepped];
-[SBAnimationStepper setAdjustsDurationForLongestAnimation:];
-[SBAnimationStepper setStepPercentage:];
-[SBAnimationStepper startSteppingAnimationsInView:];
-[SBAnimationStepper stepPercentage];
```
