# `BKSAccelerometer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 8 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<BKSAccelerometerDelegate>" _delegate;
^{__CFRunLoopSource=} _accelerometerEventsSource;
^{__CFRunLoop=} _accelerometerEventsRunLoop;
d _updateInterval;
@"NSLock" _lock;
i _orientationCheckToken;
i _orientationNotificationsToken;
@"NSThread" _orientationEventsThread;
I _orientationPort;
B _passiveOrientationEvents;
B _orientationEventsEnabled;
f _xThreshold;
f _yThreshold;
f _zThreshold;
```

## Properties

```
@property (TB,N) accelerometerEventsEnabled;
@property (Td,N,V_updateInterval) updateInterval;
@property (Tf,N,V_xThreshold) xThreshold;
@property (Tf,N,V_yThreshold) yThreshold;
@property (Tf,N,V_zThreshold) zThreshold;
@property (TB,N,V_passiveOrientationEvents) passiveOrientationEvents;
@property (TB,N,V_orientationEventsEnabled) orientationEventsEnabled;
@property (T@"<BKSAccelerometerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[BKSAccelerometer _checkOut];
-[BKSAccelerometer orientationEventsEnabled];
-[BKSAccelerometer _orientationDidChange];
-[BKSAccelerometer init];
-[BKSAccelerometer xThreshold];
-[BKSAccelerometer dealloc];
-[BKSAccelerometer currentDeviceOrientation];
-[BKSAccelerometer setPassiveOrientationEvents:];
-[BKSAccelerometer setOrientationEventsEnabled:];
-[BKSAccelerometer _orientationEventsThread];
-[BKSAccelerometer setAccelerometerEventsEnabled:];
-[BKSAccelerometer setDelegate:];
-[BKSAccelerometer accelerometerEventsEnabled];
-[BKSAccelerometer yThreshold];
-[BKSAccelerometer setUpdateInterval:];
-[BKSAccelerometer _registerForOrientationNotifications];
-[BKSAccelerometer setYThreshold:];
-[BKSAccelerometer _serverWasRestarted];
-[BKSAccelerometer delegate];
-[BKSAccelerometer passiveOrientationEvents];
-[BKSAccelerometer _checkIn];
-[BKSAccelerometer zThreshold];
-[BKSAccelerometer _updateOrientationServer];
-[BKSAccelerometer setZThreshold:];
-[BKSAccelerometer setXThreshold:];
-[BKSAccelerometer updateInterval];
```
