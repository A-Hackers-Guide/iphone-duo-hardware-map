# `FigCaptureSessionAttachedSessionManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 1 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigCaptureSession=} _currentPrimarySession;
^{OpaqueFigCaptureSession=} _currentlyStartingSession;
i _currentlyStartingSessionChangeSeed;
@"NSMutableArray" _attachedSessions;
@"NSMutableArray" _detachingSessions;
@"NSMutableArray" _sessionsToStart;
@"NSMutableArray" _incompatibleSessions;
@"NSObject<OS_dispatch_queue>" _queue;
i _changeSeed;
```

## Class methods

```
+[FigCaptureSessionAttachedSessionManager initialize];
```

## Instance methods

```
-[FigCaptureSessionAttachedSessionManager init];
```
