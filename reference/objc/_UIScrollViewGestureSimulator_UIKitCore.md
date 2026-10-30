# `_UIScrollViewGestureSimulator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
^{__CFRunLoopSource=} _mainThreadRunLoopSource;
@"NSMutableArray" _simulatedGestures;
@"NSThread" _workThread;
@"CADisplayLink" _displayLink;
@"NSTimer" _timer;
B _hasSimulatedGestures;
d _lastWakeUpTime;
```

## Class methods

```
+[_UIScrollViewGestureSimulator sharedInstance];
```

## Instance methods

```
-[_UIScrollViewGestureSimulator init];
-[_UIScrollViewGestureSimulator dealloc];
-[_UIScrollViewGestureSimulator _update];
-[_UIScrollViewGestureSimulator _displayLinkDidFire:];
-[_UIScrollViewGestureSimulator _setHasSimulatedGestures:];
-[_UIScrollViewGestureSimulator _signalMainThreadIfNecessary];
-[_UIScrollViewGestureSimulator _threadMain];
-[_UIScrollViewGestureSimulator simulateGestureWithDuration:begin:update:end:];
```
