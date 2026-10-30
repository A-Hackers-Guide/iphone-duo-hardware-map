# `FigCaptureSystemStatus`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
^{IONotificationPort=} _ioNotificationPort;
I _serviceNotification;
AQ _systemState;
^{IONotificationPort=} _powerNotificationPort;
I _powerNotifier;
I _powerNotifierConnect;
```

## Properties

```
@property (TQ,R) systemState;
```

## Class methods

```
+[FigCaptureSystemStatus sharedInstance];
+[FigCaptureSystemStatus initialize];
+[FigCaptureSystemStatus clamshellIsClosed];
```

## Instance methods

```
-[FigCaptureSystemStatus systemState];
-[FigCaptureSystemStatus initWithQueue:];
-[FigCaptureSystemStatus dealloc];
-[FigCaptureSystemStatus _setupClamshellStateChangeHandler];
-[FigCaptureSystemStatus _setupPowerStateChangeHandler];
-[FigCaptureSystemStatus clamshellStateChangeHandler:];
-[FigCaptureSystemStatus powerStateChangeHandler:args:];
```
