# `CMMagicPoseManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"CMDeviceStateManager" _manager;
@"NSOperationQueue" fClientQueue;
@? fClientHandler;
@"NSOperationQueue" fInternalQueue;
@? fInternalHandler;
```

## Class methods

```
+[CMMagicPoseManager isAvailable];
+[CMMagicPoseManager sharedManager];
+[CMMagicPoseManager orientationForMagicPose:deviceSurface:];
```

## Instance methods

```
-[CMMagicPoseManager init];
-[CMMagicPoseManager dealloc];
-[CMMagicPoseManager stopUpdates];
-[CMMagicPoseManager initWithName:];
-[CMMagicPoseManager createInternalHandlerForManager];
-[CMMagicPoseManager createDeviceStateEventFromMagicPoseEvent:];
-[CMMagicPoseManager createMagicPoseEventFromDeviceStateEvent:];
-[CMMagicPoseManager dispatchMagicPoseEvent:error:onQueue:toHandler:];
-[CMMagicPoseManager startUpdatesToQueue:withHandler:];
-[CMMagicPoseManager startUpdatesWithProgressToQueue:withHandler:];
-[CMMagicPoseManager updateClientQueue:handler:];
```
