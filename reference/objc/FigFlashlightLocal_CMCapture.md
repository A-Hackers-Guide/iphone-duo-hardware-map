# `FigFlashlightLocal`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigFlashlight`
- 31 instance variables, 0 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _notificationPostingQueue;
@"NSObject<OS_dispatch_queue>" _ambientLightSensorReadingQueue;
@"NSObject<OS_dispatch_queue>" _availabilityListenerQueue;
@ _availabilityChangedNotificationToken;
f _level;
f _levelSentInPowerEvent;
f _beamWidth;
B _lowCurrentTorchEnabled;
i _deviceVendorClientID;
i _deviceVendorClientPriority;
B _deviceVendorClientCanStealFromClientsWithSamePriority;
B _deviceSharingWithOtherClientsAllowed;
@"BWFigCaptureDevice" _device;
@"BWFigCaptureStream" _stream;
q _clientType;
^{OpaqueFigSimpleMutex=} _lock;
@"FigCaptureThermalMonitor" _thermalMonitor;
i _clientPID;
{?="val"[8I]} _clientAuditToken;
@"NSString" _clientApplicationID;
* _loggingPrefix;
@"FigCaptureOSStateHandle" _osStateHandle;
I _lastLevelIndex;
q _lastLevelChangedTime;
[11q] _usageTimeOfLevel;
q _totalUsageTime;
i _lastBeamWidthIndex;
[11q] _usageTimeOfBeamWidth;
q _lastBeamWidthChangedTime;
@"BWAmbientLightSensor" _ambientLightSensor;
i _luxLevel;
```

## Class methods

```
+[FigFlashlightLocal initialize];
```

## Instance methods

```
-[FigFlashlightLocal powerOn];
-[FigFlashlightLocal isAvailable];
-[FigFlashlightLocal dealloc];
-[FigFlashlightLocal level];
-[FigFlashlightLocal setLevel:];
-[FigFlashlightLocal setLowCurrentTorchEnabled:];
-[FigFlashlightLocal isOverheated];
-[FigFlashlightLocal beamWidth];
-[FigFlashlightLocal setBeamWidth:];
-[FigFlashlightLocal notifyForCurrentState];
-[FigFlashlightLocal powerOff];
-[FigFlashlightLocal _handleDeviceAvailabilityChangedNotification:withWeakReference:];
-[FigFlashlightLocal _createDeviceAndStream];
-[FigFlashlightLocal _handleDeviceAvailabilityChangedNotification:];
-[FigFlashlightLocal _handleMaxTorchLevelChange:];
-[FigFlashlightLocal _logBeamWidthAnalytics:forceUpdate:];
-[FigFlashlightLocal _logLevelAnalytics:];
-[FigFlashlightLocal _osStateData];
-[FigFlashlightLocal _postNotification:withValue:];
-[FigFlashlightLocal _setBeamWidthInternal:];
-[FigFlashlightLocal _setLevelInternal:];
-[FigFlashlightLocal _setUpDevice];
-[FigFlashlightLocal _teardownDeviceAndNotify:];
-[FigFlashlightLocal initWithClientType:clientAuditToken:clientApplicationID:];
```
