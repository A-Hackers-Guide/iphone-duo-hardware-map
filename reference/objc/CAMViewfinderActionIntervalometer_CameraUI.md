# `CAMViewfinderActionIntervalometer`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<CAMViewfinderActionIntervalometerDelegate>" _delegate;
d _interval;
d _delay;
q _maximumCount;
q __remaining;
@"CAMPreciseTimer" __timer;
@"CAMViewfinderViewController" __viewfinderViewController;
```

## Properties

```
@property (Tq,N,V__remaining) _remaining;
@property (T@"CAMPreciseTimer",R,N,V__timer) _timer;
@property (T@"CAMViewfinderViewController",R,N,V__viewfinderViewController) _viewfinderViewController;
@property (T@"<CAMViewfinderActionIntervalometerDelegate>",R,W,N,V_delegate) delegate;
@property (Td,R,N,V_interval) interval;
@property (Td,R,N,V_delay) delay;
@property (Tq,R,N,V_maximumCount) maximumCount;
@property (TQ,R,N) successfullActionCount;
```

## Instance methods

```
-[CAMViewfinderActionIntervalometer _timer];
-[CAMViewfinderActionIntervalometer interval];
-[CAMViewfinderActionIntervalometer init];
-[CAMViewfinderActionIntervalometer delay];
-[CAMViewfinderActionIntervalometer delegate];
-[CAMViewfinderActionIntervalometer maximumCount];
-[CAMViewfinderActionIntervalometer _attemptViewfinderActions];
-[CAMViewfinderActionIntervalometer _remaining];
-[CAMViewfinderActionIntervalometer _viewfinderViewController];
-[CAMViewfinderActionIntervalometer initWithDelegate:interval:delay:maximumCount:viewfinderViewController:];
-[CAMViewfinderActionIntervalometer manuallyGenerateRequest];
-[CAMViewfinderActionIntervalometer set_remaining:];
-[CAMViewfinderActionIntervalometer startGeneratingRequests];
-[CAMViewfinderActionIntervalometer stopAttemptingActions];
-[CAMViewfinderActionIntervalometer successfullActionCount];
```
