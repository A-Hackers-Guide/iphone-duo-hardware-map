# `_UIPassthroughGateGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIScrollEventRespondable`
- 1 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _acceptsFailureRequirements;
```

## Properties

```
@property (T@"<_UIPassthroughGestureDelegate>",W,D,N) delegate;
@property (TB,N,G_acceptsFailureRequirements,S_setAcceptsFailureRequirements:,V_acceptsFailureRequirements) acceptsFailureRequirements;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPassthroughGateGestureRecognizer _supportsTouchContinuation];
```

## Instance methods

```
-[_UIPassthroughGateGestureRecognizer open];
-[_UIPassthroughGateGestureRecognizer shouldReceiveEvent:];
-[_UIPassthroughGateGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIPassthroughGateGestureRecognizer _scrollingChangedWithEvent:];
-[_UIPassthroughGateGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIPassthroughGateGestureRecognizer _shouldReceiveTouch:withEvent:];
-[_UIPassthroughGateGestureRecognizer touchesCancelled:withEvent:];
-[_UIPassthroughGateGestureRecognizer endClosed];
-[_UIPassthroughGateGestureRecognizer initWithTarget:action:];
-[_UIPassthroughGateGestureRecognizer _acceptsFailureRequirements];
-[_UIPassthroughGateGestureRecognizer _setAcceptsFailureRequirements:];
```
