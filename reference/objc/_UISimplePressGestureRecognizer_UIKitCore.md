# `_UISimplePressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 3 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UIDelayedAction" _delayedAction;
@"NSValue" _activeTrigger;
@"NSArray" _triggers;
```

## Properties

```
@property (T@"UIDelayedAction",&,N,V_delayedAction) delayedAction;
@property (T@"NSArray",&,N,V_triggers) triggers;
@property (T@"NSValue",R,N,V_activeTrigger) activeTrigger;
@property (T@"NSArray",C,N) allowedTouchTypes;
@property (T@"NSArray",C,N) allowedPressTypes;
```

## Instance methods

```
-[_UISimplePressGestureRecognizer setTriggers:];
-[_UISimplePressGestureRecognizer _begin];
-[_UISimplePressGestureRecognizer pressesCancelled:withEvent:];
-[_UISimplePressGestureRecognizer pressesEnded:withEvent:];
-[_UISimplePressGestureRecognizer dealloc];
-[_UISimplePressGestureRecognizer reset];
-[_UISimplePressGestureRecognizer initWithTarget:action:];
-[_UISimplePressGestureRecognizer triggers];
-[_UISimplePressGestureRecognizer _endOrFail];
-[_UISimplePressGestureRecognizer pressesBegan:withEvent:];
-[_UISimplePressGestureRecognizer _cancelOrFail];
-[_UISimplePressGestureRecognizer activeTrigger];
-[_UISimplePressGestureRecognizer setDelayedAction:];
-[_UISimplePressGestureRecognizer delayedAction];
```
