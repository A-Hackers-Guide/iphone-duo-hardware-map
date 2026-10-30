# `_UIDynamicAnimationGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDynamicAnimation`
- 3 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
@? _applier;
@"NSMutableArray" _animations;
@"NSMutableArray" _runningAnimations;
```

## Properties

```
@property (T@"NSArray",C,N,V_animations) animations;
```

## Instance methods

```
-[_UIDynamicAnimationGroup animations];
-[_UIDynamicAnimationGroup _stopAnimation];
-[_UIDynamicAnimationGroup dealloc];
-[_UIDynamicAnimationGroup setAnimations:];
-[_UIDynamicAnimationGroup runWithCompletion:];
-[_UIDynamicAnimationGroup addAnimation:];
-[_UIDynamicAnimationGroup removeAnimation:];
-[_UIDynamicAnimationGroup runWithGroupApplier:completion:];
-[_UIDynamicAnimationGroup _animateForInterval:];
-[_UIDynamicAnimationGroup _appendSubclassDescription:atLevel:];
-[_UIDynamicAnimationGroup runWithGroupApplier:completion:forScreen:runLoopMode:];
```
