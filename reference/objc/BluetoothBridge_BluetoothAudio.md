# `BluetoothBridge`

- Image: [`/System/Library/PrivateFrameworks/BluetoothAudio.framework/BluetoothAudio`](../userland/System__Library__PrivateFrameworks__BluetoothAudio.framework__BluetoothAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 38 instance methods, 1 class methods

## Instance variables

```
B _targetUserSession;
B _noHFPSupport;
@"NSObject<OS_dispatch_semaphore>" _connectedSemaphore;
^{OpaqueFigEndpointManager=} _manager;
@"CBDiscovery" _deviceDiscovery;
@"CUSystemMonitor" _systemMonitor;
@"NSObject<OS_dispatch_queue>" _queue;
@? _lowerScanRate;
@? _activation;
@? _activationTimeoutBlock;
@"NSMutableDictionary" _lecaSessionIDCache;
```

## Properties

```
@property (TB,N,V_noHFPSupport) noHFPSupport;
@property (T@"NSMutableDictionary",&,N,V_lecaSessionIDCache) lecaSessionIDCache;
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_connectedSemaphore) connectedSemaphore;
@property (T^{OpaqueFigEndpointManager=},N,V_manager) manager;
@property (T@"CBDiscovery",&,V_deviceDiscovery) deviceDiscovery;
@property (TB,V_targetUserSession) targetUserSession;
@property (T@"CUSystemMonitor",&,V_systemMonitor) systemMonitor;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@?,C,V_lowerScanRate) lowerScanRate;
@property (T@?,C,V_activation) activation;
@property (T@?,C,V_activationTimeoutBlock) activationTimeoutBlock;
```

## Class methods

```
+[BluetoothBridge sharedBluetoothBridge];
```

## Instance methods

```
-[BluetoothBridge systemMonitor];
-[BluetoothBridge targetUserSession];
-[BluetoothBridge setTargetUserSession:];
-[BluetoothBridge init];
-[BluetoothBridge setManager:];
-[BluetoothBridge deviceFromIdentifier:];
-[BluetoothBridge queue];
-[BluetoothBridge manager];
-[BluetoothBridge setSystemMonitor:];
-[BluetoothBridge setQueue:];
-[BluetoothBridge isConnected:];
-[BluetoothBridge activation];
-[BluetoothBridge setActivation:];
-[BluetoothBridge deviceDiscovery];
-[BluetoothBridge setDeviceDiscovery:];
-[BluetoothBridge nameFromDevice:];
-[BluetoothBridge activationTimeoutBlock];
-[BluetoothBridge addListeners];
-[BluetoothBridge addressFromDevice:];
-[BluetoothBridge connectToAddress:completionHandler:];
-[BluetoothBridge connectedSemaphore];
-[BluetoothBridge createDescriptionWithDevice:];
-[BluetoothBridge getHFPSupportStatus];
-[BluetoothBridge isHALPublished:device:];
-[BluetoothBridge lecaSessionIDCache];
-[BluetoothBridge lowerScanRate];
-[BluetoothBridge noHFPSupport];
-[BluetoothBridge removeDeviceFromFigE:];
-[BluetoothBridge setActivationTimeoutBlock:];
-[BluetoothBridge setConnectedSemaphore:];
-[BluetoothBridge setLecaSessionIDCache:];
-[BluetoothBridge setLowerScanRate:];
-[BluetoothBridge setNoHFPSupport:];
-[BluetoothBridge shouldRemoveDevice:];
-[BluetoothBridge startLEScanning:];
-[BluetoothBridge stopLEScanning];
-[BluetoothBridge supportedFormats:];
-[BluetoothBridge uidFromDevice:];
```
