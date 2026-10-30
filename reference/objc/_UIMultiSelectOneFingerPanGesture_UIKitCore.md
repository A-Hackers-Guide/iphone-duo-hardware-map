# `_UIMultiSelectOneFingerPanGesture`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPanGestureRecognizer`
- 3 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UITouch" _activeTouch;
@"UIEvent" _activeEvent;
@"<_UIMultiSelectOneFingerPanGestureDelegate>" _oneFingerPanDelegate;
```

## Properties

```
@property (T@"UITouch",R,N,V_activeTouch) activeTouch;
@property (T@"UIEvent",R,N,V_activeEvent) activeEvent;
@property (T@"<_UIMultiSelectOneFingerPanGestureDelegate>",W,N,V_oneFingerPanDelegate) oneFingerPanDelegate;
```

## Instance methods

```
-[_UIMultiSelectOneFingerPanGesture canPreventGestureRecognizer:];
-[_UIMultiSelectOneFingerPanGesture _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIMultiSelectOneFingerPanGesture canBePreventedByGestureRecognizer:];
-[_UIMultiSelectOneFingerPanGesture _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIMultiSelectOneFingerPanGesture _canCancelGestureRecognizer:];
-[_UIMultiSelectOneFingerPanGesture activeTouch];
-[_UIMultiSelectOneFingerPanGesture activeEvent];
-[_UIMultiSelectOneFingerPanGesture reset];
-[_UIMultiSelectOneFingerPanGesture touchesBegan:withEvent:];
-[_UIMultiSelectOneFingerPanGesture shouldBeRequiredToFailByGestureRecognizer:];
-[_UIMultiSelectOneFingerPanGesture setOneFingerPanDelegate:];
-[_UIMultiSelectOneFingerPanGesture oneFingerPanDelegate];
-[_UIMultiSelectOneFingerPanGesture _preventsDragInteractionGestures];
```
