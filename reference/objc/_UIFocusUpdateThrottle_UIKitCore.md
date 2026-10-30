# `_UIFocusUpdateThrottle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
Q _nilUpdateCount;
d _lastUpdate;
d _currentTimeout;
B _updateIsScheduled;
@"NSTimer" _updateTimer;
@? _updateHandler;
```

## Instance methods

```
-[_UIFocusUpdateThrottle initWithUpdateHandler:];
-[_UIFocusUpdateThrottle reset];
-[_UIFocusUpdateThrottle teardown];
-[_UIFocusUpdateThrottle scheduleProgrammaticFocusUpdate];
-[_UIFocusUpdateThrottle _performScheduledUpdate];
-[_UIFocusUpdateThrottle didCreateProgrammaticFocusUpdateContext:];
```
