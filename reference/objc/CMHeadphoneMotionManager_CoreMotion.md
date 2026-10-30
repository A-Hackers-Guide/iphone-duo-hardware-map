# `CMHeadphoneMotionManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"CMHeadphoneMotionManagerInternal" _internal;
@"<CMHeadphoneMotionManagerDelegate>" _delegate;
q _deviceMotionBodyFrame;
```

## Properties

```
@property (Tq,N,V_deviceMotionBodyFrame) deviceMotionBodyFrame;
@property (T@"<CMHeadphoneMotionManagerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,GisConnectionStatusActive) connectionStatusActive;
@property (TB,R,N,GisDeviceMotionAvailable) deviceMotionAvailable;
@property (TB,R,N,GisDeviceMotionActive) deviceMotionActive;
@property (T@"CMDeviceMotion",R) deviceMotion;
```

## Class methods

```
+[CMHeadphoneMotionManager authorizationStatus];
```

## Instance methods

```
-[CMHeadphoneMotionManager init];
-[CMHeadphoneMotionManager stopDeviceMotionUpdates];
-[CMHeadphoneMotionManager dealloc];
-[CMHeadphoneMotionManager isDeviceMotionAvailable];
-[CMHeadphoneMotionManager setDelegate:];
-[CMHeadphoneMotionManager deviceMotion];
-[CMHeadphoneMotionManager delegate];
-[CMHeadphoneMotionManager startDeviceMotionUpdates];
-[CMHeadphoneMotionManager startDeviceMotionUpdatesToQueue:withHandler:];
-[CMHeadphoneMotionManager stopDeviceMotionUpdatesPrivate];
-[CMHeadphoneMotionManager isDeviceMotionActive];
-[CMHeadphoneMotionManager applyInitialReferencePrivate:];
-[CMHeadphoneMotionManager delegateQueuePrivate];
-[CMHeadphoneMotionManager deviceMotionBodyFrame];
-[CMHeadphoneMotionManager hasConnectionClients];
-[CMHeadphoneMotionManager isConnectionStatusActive];
-[CMHeadphoneMotionManager notifyDeviceConnectedEventToClientPrivateWithAvailableReferenceFrames:];
-[CMHeadphoneMotionManager notifyDeviceDisconnectedEventToClientPrivate];
-[CMHeadphoneMotionManager onDeviceMotionPrivate:];
-[CMHeadphoneMotionManager onStatusEventPrivate:];
-[CMHeadphoneMotionManager pauseDeviceMotionStreamingPrivate];
-[CMHeadphoneMotionManager pauseStatusStreamingPrivate];
-[CMHeadphoneMotionManager resumeDeviceMotionStreamingPrivate];
-[CMHeadphoneMotionManager resumeStatusStreamingPrivate];
-[CMHeadphoneMotionManager setDeviceMotionBodyFrame:];
-[CMHeadphoneMotionManager startConnectionStatusUpdates];
-[CMHeadphoneMotionManager startDeviceMotionUpdatesPrivateUsingReferenceFrame:bodyFrame:toQueue:withHandler:];
-[CMHeadphoneMotionManager startStatusUpdatesPrivate];
-[CMHeadphoneMotionManager stopConnectionStatusUpdates];
-[CMHeadphoneMotionManager stopStatusUpdatesPrivate];
```
