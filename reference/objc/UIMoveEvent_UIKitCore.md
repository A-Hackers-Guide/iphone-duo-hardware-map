# `UIMoveEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIWindow" _windowFromHIDEvent;
q _moveDirection;
Q _focusHeading;
```

## Properties

```
@property (Tq,N,S_setMoveDirection:,V_moveDirection) _moveDirection;
@property (TQ,N,S_setFocusHeading:,V_focusHeading) _focusHeading;
```

## Instance methods

```
-[UIMoveEvent _allWindows];
-[UIMoveEvent _cleanupAfterDispatch];
-[UIMoveEvent _setHIDEvent:];
-[UIMoveEvent _sendEventToResponder:];
-[UIMoveEvent type];
-[UIMoveEvent _focusHeading];
-[UIMoveEvent _moveDirection];
-[UIMoveEvent _setFocusHeading:];
-[UIMoveEvent _setMoveDirection:];
```
