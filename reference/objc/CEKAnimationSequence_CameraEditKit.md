# `CEKAnimationSequence`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" __animations;
@? __completionHandler;
@"CEKAnimationGenerator" __animationGenerator;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V__animations) _animations;
@property (T@?,C,N,V__completionHandler) _completionHandler;
@property (T@"CEKAnimationGenerator",&,N,V__animationGenerator) _animationGenerator;
```

## Instance methods

```
-[CEKAnimationSequence _animations];
-[CEKAnimationSequence start];
-[CEKAnimationSequence _completionHandler];
-[CEKAnimationSequence initWithAnimations:completionHandler:];
-[CEKAnimationSequence stopAllAnimations];
-[CEKAnimationSequence _animationGenerator];
-[CEKAnimationSequence _notifyCompletionWithSuccess:];
-[CEKAnimationSequence _startNextAnimation];
-[CEKAnimationSequence set_animationGenerator:];
-[CEKAnimationSequence set_completionHandler:];
```
