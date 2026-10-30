# `AVExternalStorageDeviceDiscoverySession`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 8 instance methods, 3 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _lock;
@"AVWeakReference" _weakReference;
^{OpaqueFigExternalStorageDeviceManager=} _externalStorageDeviceManager;
@"NSMutableArray" _externalStorageDevices;
@"NSMutableArray" _uuidOfExternalStorageDevice;
```

## Properties

```
@property (T@"NSArray",R,V_externalStorageDevices) externalStorageDevices;
```

## Class methods

```
+[AVExternalStorageDeviceDiscoverySession initialize];
+[AVExternalStorageDeviceDiscoverySession sharedSession];
+[AVExternalStorageDeviceDiscoverySession isSupported];
```

## Instance methods

```
-[AVExternalStorageDeviceDiscoverySession init];
-[AVExternalStorageDeviceDiscoverySession dealloc];
-[AVExternalStorageDeviceDiscoverySession _checkAuthorizationStatus];
-[AVExternalStorageDeviceDiscoverySession _reconnectToServer];
-[AVExternalStorageDeviceDiscoverySession _requestAuthorization:];
-[AVExternalStorageDeviceDiscoverySession _setupExternalStorageDeviceDiscoverySession];
-[AVExternalStorageDeviceDiscoverySession _tearDownExternalStorageDeviceDiscoverySessionToReconnectToServer:];
-[AVExternalStorageDeviceDiscoverySession externalStorageDevices];
```
