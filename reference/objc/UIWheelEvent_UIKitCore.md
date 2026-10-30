# `UIWheelEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- 4 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _recentScrollDistance;
@"NSMutableArray" _recentScrollEvents;
q lastSubtype;
@"UIWindow" _windowFromHIDEvent;
```

## Instance methods

```
-[UIWheelEvent _allWindows];
-[UIWheelEvent _cleanupAfterDispatch];
-[UIWheelEvent _setHIDEvent:];
-[UIWheelEvent subtype];
-[UIWheelEvent _sendEventToResponder:];
-[UIWheelEvent type];
-[UIWheelEvent _canHaveVelocity];
-[UIWheelEvent _wheelVelocity];
```
