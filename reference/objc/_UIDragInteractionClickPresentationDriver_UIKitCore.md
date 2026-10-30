# `_UIDragInteractionClickPresentationDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDragInteractionDriver`
- 5 instance variables, 0 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSSet" _touches;
@? _itemIterator;
@? _sessionHandler;
@? _liftCompletion;
@"UIDelayedAction" _delayedLift;
```

## Instance methods

```
-[_UIDragInteractionClickPresentationDriver didTransitionToInactiveState];
-[_UIDragInteractionClickPresentationDriver isLifted];
-[_UIDragInteractionClickPresentationDriver beginDragWithTouches:itemIterator:beginningSessionHandler:];
-[_UIDragInteractionClickPresentationDriver didTransitionToInflightState];
-[_UIDragInteractionClickPresentationDriver beginLiftAtLocation:useDefaultLiftAnimation:delay:completion:];
-[_UIDragInteractionClickPresentationDriver didTransitionToBeginState];
-[_UIDragInteractionClickPresentationDriver _performDelayedLift];
-[_UIDragInteractionClickPresentationDriver canBeginLiftAtLocation:];
-[_UIDragInteractionClickPresentationDriver cancel];
-[_UIDragInteractionClickPresentationDriver isPreparingToDrag];
```
