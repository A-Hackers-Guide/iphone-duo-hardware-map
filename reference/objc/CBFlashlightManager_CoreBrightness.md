# `CBFlashlightManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
I _cameraService;
^{IONotificationPort=} _ioNotificationPort;
I _ioServiceArrivalIterator;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_os_log>" _logHandle;
Q _samplingTime;
{FlashlightStateSample="isFlashlightOn"B"stateChangeTimestamp"f} _flashlightState;
```

## Properties

```
@property (T{FlashlightStateSample=Bf},R,V_flashlightState) flashlightState;
```

## Instance methods

```
-[CBFlashlightManager stop];
-[CBFlashlightManager dealloc];
-[CBFlashlightManager start];
-[CBFlashlightManager timerCallback];
-[CBFlashlightManager flashlightState];
-[CBFlashlightManager getStrobeState];
-[CBFlashlightManager handleCameraServiceArrival:];
-[CBFlashlightManager initWithQueue:andSamplingTime:];
-[CBFlashlightManager registerForCameraArrivalNotifications];
-[CBFlashlightManager startCameraServiceLookup];
-[CBFlashlightManager unregisterForCameraArrivalNotifications];
```
