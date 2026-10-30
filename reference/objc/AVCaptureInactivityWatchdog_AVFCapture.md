# `AVCaptureInactivityWatchdog`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
d _timeout;
B _cancelled;
@"NSObject<OS_dispatch_source>" _timer;
@? _handler;
```

## Instance methods

```
-[AVCaptureInactivityWatchdog dealloc];
-[AVCaptureInactivityWatchdog reset];
-[AVCaptureInactivityWatchdog cancel];
-[AVCaptureInactivityWatchdog initWithTimeout:handler:];
-[AVCaptureInactivityWatchdog _handleTimerFired];
```
