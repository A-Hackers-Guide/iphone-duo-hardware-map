# `_TtCE5UIKitCSo6UIView22HybridPropertyAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIViewHybridPropertyAnimator`
- 16 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 backgroundProgressValue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 mainProgressValue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isProgressValueReversed;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 springBehavior;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 springBehaviorWhenContinued;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 completionPosition;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 propertyAnimator;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 c2Animations;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 completionHandlers;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 keyframes;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isC2Finished;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _fractionComplete;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _state;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _isRunning;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _isReversed;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _pausesOnCompletion;
```

## Properties

```
@property (T@"UIViewFloatAnimatableProperty",N,R) progressValue;
@property (Tq,N,R) state;
@property (TB,N,R) running;
@property (TB,N) reversed;
@property (Td,N) fractionComplete;
@property (TB,N,R) _canAddAnimations;
```

## Instance methods

```
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator _canAddAnimations];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator addAnimations:delayFactor:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator setReversed:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator setFractionComplete:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator isRunning];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator fractionComplete];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator pauseAnimation];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator addAnimations:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator isReversed];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator startAnimation];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator addCompletion:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator continueAnimationWithTimingParameters:durationFactor:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator stopAnimation:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator finishAnimationAtPosition:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator startAnimationAfterDelay:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator init];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator dealloc];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator state];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator addInProcessProgressAnimations:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator _continueAnimationWithStartingVelocity:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator addInProcessProgressKeyframeWithRelativeStartTime:relativeDuration:animations:];
-[_TtCE5UIKitCSo6UIView22HybridPropertyAnimator progressValue];
```
