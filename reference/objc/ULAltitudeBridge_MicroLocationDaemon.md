# `ULAltitudeBridge`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULAltitudeSource`
- 4 instance variables, 8 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _backgroundUpdatesRunning;
@"NSObject<OS_dispatch_queue>" _queue;
@"<ULAltitudeDelegate>" _delegate;
@"CMAltimeter" _altimeter;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<ULAltitudeDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_backgroundUpdatesRunning) backgroundUpdatesRunning;
@property (T@"CMAltimeter",&,N,V_altimeter) altimeter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULAltitudeBridge isAvailable];
```

## Instance methods

```
-[ULAltitudeBridge queue];
-[ULAltitudeBridge stopBackgroundUpdates];
-[ULAltitudeBridge setDelegate:];
-[ULAltitudeBridge delegate];
-[ULAltitudeBridge startBackgroundUpdates];
-[ULAltitudeBridge setQueue:];
-[ULAltitudeBridge altimeter];
-[ULAltitudeBridge setAltimeter:];
-[ULAltitudeBridge initWithDelegateQueue:delegate:];
-[ULAltitudeBridge backgroundUpdatesRunning];
-[ULAltitudeBridge handleAltitudeMeasurement:error:];
-[ULAltitudeBridge setBackgroundUpdatesRunning:];
```
