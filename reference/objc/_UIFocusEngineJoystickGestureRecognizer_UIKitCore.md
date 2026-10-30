# `_UIFocusEngineJoystickGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 2 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _stickPosition;
{CGPoint="x"d"y"d} _previousStickPosition;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_stickPosition) stickPosition;
@property (T{CGPoint=dd},R,N,V_previousStickPosition) previousStickPosition;
```

## Instance methods

```
-[_UIFocusEngineJoystickGestureRecognizer _shouldReceivePress:];
-[_UIFocusEngineJoystickGestureRecognizer pressesCancelled:withEvent:];
-[_UIFocusEngineJoystickGestureRecognizer pressesEnded:withEvent:];
-[_UIFocusEngineJoystickGestureRecognizer stickPosition];
-[_UIFocusEngineJoystickGestureRecognizer _isGestureType:];
-[_UIFocusEngineJoystickGestureRecognizer reset];
-[_UIFocusEngineJoystickGestureRecognizer previousStickPosition];
-[_UIFocusEngineJoystickGestureRecognizer initWithTarget:action:];
-[_UIFocusEngineJoystickGestureRecognizer pressesBegan:withEvent:];
-[_UIFocusEngineJoystickGestureRecognizer pressesChanged:withEvent:];
-[_UIFocusEngineJoystickGestureRecognizer _calculateStickPositionFromPresses:withEvent:];
```
