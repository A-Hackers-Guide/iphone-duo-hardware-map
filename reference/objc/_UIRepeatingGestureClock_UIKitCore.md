# `_UIRepeatingGestureClock`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q _delayIndex;
B _timerOn;
@"<_UIRepeatingGestureClockDelegate>" _delegate;
```

## Properties

```
@property (T@"<_UIRepeatingGestureClockDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[_UIRepeatingGestureClock _scheduleTimer];
-[_UIRepeatingGestureClock dealloc];
-[_UIRepeatingGestureClock _cancelTimer];
-[_UIRepeatingGestureClock setDelegate:];
-[_UIRepeatingGestureClock delegate];
-[_UIRepeatingGestureClock _createTick:];
-[_UIRepeatingGestureClock _performTick:];
-[_UIRepeatingGestureClock startClock];
-[_UIRepeatingGestureClock stopClock];
```
