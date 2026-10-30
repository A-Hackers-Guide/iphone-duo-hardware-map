# `SBPanSystemGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPanGestureRecognizer`
- 5 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _initialTouchReceived;
d _initialTouchReceivedTime;
B _failsPastMaximumPressDurationWithoutHysteresis;
d _maximumPressDuration;
@"NSTimer" _noHysterisisCancellationTimer;
```

## Properties

```
@property (T@"NSTimer",&,N,V_noHysterisisCancellationTimer) noHysterisisCancellationTimer;
@property (T@"<SBPanSystemGestureRecognizerDelegate>",W,D,N) delegate;
@property (TB,N,V_failsPastMaximumPressDurationWithoutHysteresis) failsPastMaximumPressDurationWithoutHysteresis;
@property (Td,N,V_maximumPressDuration) maximumPressDuration;
```

## Instance methods

```
-[SBPanSystemGestureRecognizer setFailsPastMaximumPressDurationWithoutHysteresis:];
-[SBPanSystemGestureRecognizer setState:];
-[SBPanSystemGestureRecognizer failsPastMaximumPressDurationWithoutHysteresis];
-[SBPanSystemGestureRecognizer setupNoHysterisisCancellationTimerIfNeeded];
-[SBPanSystemGestureRecognizer maximumPressDuration];
-[SBPanSystemGestureRecognizer setNoHysterisisCancellationTimer:];
-[SBPanSystemGestureRecognizer dealloc];
-[SBPanSystemGestureRecognizer noHysterisisCancellationTimer];
-[SBPanSystemGestureRecognizer reset];
-[SBPanSystemGestureRecognizer touchesBegan:withEvent:];
-[SBPanSystemGestureRecognizer initWithTarget:action:];
-[SBPanSystemGestureRecognizer invalidateNoHysterisisCancellationTimer];
-[SBPanSystemGestureRecognizer setMaximumPressDuration:];
```
