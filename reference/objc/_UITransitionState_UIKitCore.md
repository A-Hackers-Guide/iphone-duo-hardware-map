# `_UITransitionState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
q _transitionDirection;
@? _completion;
@"NSDate" _beginDate;
```

## Properties

```
@property (Tq,R,N,V_transitionDirection) transitionDirection;
@property (Tq,R,N) effectiveTransitionDirection;
@property (T@"NSDate",R,N,V_beginDate) beginDate;
@property (TB,R,N,GisActive) active;
```

## Instance methods

```
-[_UITransitionState beginDate];
-[_UITransitionState description];
-[_UITransitionState isActive];
-[_UITransitionState cleanupWithFinishedState:completedState:];
-[_UITransitionState effectiveTransitionDirection];
-[_UITransitionState initWithTransitionDirection:completion:];
-[_UITransitionState isCompatibleWithTransitionInDirection:];
-[_UITransitionState markBeginDate];
-[_UITransitionState transitionDirection];
```
