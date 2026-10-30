# `AVExternalSyncDeviceDiscoverySession`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 10 instance methods, 3 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _deviceLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _sourceLock;
@"NSMutableArray" _devices;
@"AVWeakReference" _weakReference;
^{OpaqueFigCaptureSource=} _fcs;
@ _serverDiedObserver;
```

## Properties

```
@property (T@"NSArray",R) devices;
```

## Class methods

```
+[AVExternalSyncDeviceDiscoverySession initialize];
+[AVExternalSyncDeviceDiscoverySession sharedSession];
+[AVExternalSyncDeviceDiscoverySession isSupported];
```

## Instance methods

```
-[AVExternalSyncDeviceDiscoverySession observeValueForKeyPath:ofObject:change:context:];
-[AVExternalSyncDeviceDiscoverySession init];
-[AVExternalSyncDeviceDiscoverySession dealloc];
-[AVExternalSyncDeviceDiscoverySession devices];
-[AVExternalSyncDeviceDiscoverySession _handleNotification:dict:];
-[AVExternalSyncDeviceDiscoverySession _updateDevicesEvent:];
-[AVExternalSyncDeviceDiscoverySession setupNotifications];
-[AVExternalSyncDeviceDiscoverySession setupSource];
-[AVExternalSyncDeviceDiscoverySession teardownNotifications];
-[AVExternalSyncDeviceDiscoverySession teardownSource];
```
