# `SBPerformTransitionSwitcherEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEventResponse`
- 2 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _gestureInitiated;
@"SBSwitcherTransitionRequest" _transitionRequest;
```

## Properties

```
@property (T@"SBSwitcherTransitionRequest",R,N,V_transitionRequest) transitionRequest;
@property (TB,R,N,GisGestureInitiated,V_gestureInitiated) gestureInitiated;
```

## Instance methods

```
-[SBPerformTransitionSwitcherEventResponse isGestureInitiated];
-[SBPerformTransitionSwitcherEventResponse type];
-[SBPerformTransitionSwitcherEventResponse descriptionBuilderWithMultilinePrefix:];
-[SBPerformTransitionSwitcherEventResponse initWithTransitionRequest:gestureInitiated:];
-[SBPerformTransitionSwitcherEventResponse transitionRequest];
```
