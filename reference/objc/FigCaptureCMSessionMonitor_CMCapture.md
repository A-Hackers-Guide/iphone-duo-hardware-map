# `FigCaptureCMSessionMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _lock;
@"FigCaptureCMSession" _session;
i _clientPID;
@"<FigCaptureCMSessionObserver>" _observer;
@ _applicationStateChangeNotificationToken;
@ _interruptionStateChangeNotificationToken;
B _invalidated;
```

## Class methods

```
+[FigCaptureCMSessionMonitor initialize];
```

## Instance methods

```
-[FigCaptureCMSessionMonitor debugDescription];
-[FigCaptureCMSessionMonitor dealloc];
-[FigCaptureCMSessionMonitor invalidate];
-[FigCaptureCMSessionMonitor description];
-[FigCaptureCMSessionMonitor _initWithFigCaptureCMSession:clientPID:observer:];
-[FigCaptureCMSessionMonitor initWithCMSession:clientPID:observer:];
```
