# `AASystemStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AAServicesXPCClientInterface`, `NSSecureCoding`
- 22 instance variables, 16 properties, 57 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
B _isSREnabled;
B _invalidateCalled;
B _invalidateDone;
B _resetOngoing;
@"NSXPCConnection" _xpcCnx;
B _isSystemEligibleForSiriHijack;
I _clientID;
@"AudioAccessoryDevice" _activeHRMDevice;
@? _activeHRMDeviceChangedHandler;
@? _aaDeviceConnectionChangedHandler;
@? _aaDeviceRouteChangedHandler;
@? _hrmCapableDeviceRoutedStateChangedHandler;
@? _siriHijackEligibilityUpdatedHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _interruptionHandler;
@? _invalidationHandler;
@"AADeviceManager" _connectedDiscovery;
@"NSMutableDictionary" _devicesMap;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
@"AAServicesDaemon" _internalServicesDaemon;
```

## Properties

```
@property (T@"AADeviceManager",&,N,V_connectedDiscovery) connectedDiscovery;
@property (T@"NSMutableDictionary",&,N,V_devicesMap) devicesMap;
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"AAServicesDaemon",&,N,V_internalServicesDaemon) internalServicesDaemon;
@property (TB,R,N) direct;
@property (T@"AudioAccessoryDevice",R,C,N,V_activeHRMDevice) activeHRMDevice;
@property (TB,R,V_isSystemEligibleForSiriHijack) isSystemEligibleForSiriHijack;
@property (T@?,C,V_activeHRMDeviceChangedHandler) activeHRMDeviceChangedHandler;
@property (T@?,C,V_aaDeviceConnectionChangedHandler) aaDeviceConnectionChangedHandler;
@property (T@?,C,V_aaDeviceRouteChangedHandler) aaDeviceRouteChangedHandler;
@property (T@?,C,V_hrmCapableDeviceRoutedStateChangedHandler) hrmCapableDeviceRoutedStateChangedHandler;
@property (T@?,C,V_siriHijackEligibilityUpdatedHandler) siriHijackEligibilityUpdatedHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Class methods

```
+[AASystemStateMonitor supportsSecureCoding];
```

## Instance methods

```
-[AASystemStateMonitor setHrmCapableDeviceRoutedStateChangedHandler:];
-[AASystemStateMonitor testListenerEndpoint];
-[AASystemStateMonitor _invalidateDirect];
-[AASystemStateMonitor setConnectedDiscovery:];
-[AASystemStateMonitor clientID];
-[AASystemStateMonitor dispatchQueue];
-[AASystemStateMonitor _reset];
-[AASystemStateMonitor _ensureXPCStarted];
-[AASystemStateMonitor activateWithCompletion:];
-[AASystemStateMonitor activeHRMDevice];
-[AASystemStateMonitor setTestListenerEndpoint:];
-[AASystemStateMonitor setClientID:];
-[AASystemStateMonitor aaServicesRequireReset];
-[AASystemStateMonitor setActiveHRMDeviceChangedHandler:];
-[AASystemStateMonitor activeHRMDeviceChangedHandler];
-[AASystemStateMonitor setInvalidationHandler:];
-[AASystemStateMonitor init];
-[AASystemStateMonitor _activateXPC:reactivate:];
-[AASystemStateMonitor _activateDirect:];
-[AASystemStateMonitor setAaDeviceRouteChangedHandler:];
-[AASystemStateMonitor isSystemEligibleForSiriHijack];
-[AASystemStateMonitor setInternalServicesDaemon:];
-[AASystemStateMonitor interruptionHandler];
-[AASystemStateMonitor setDispatchQueue:];
-[AASystemStateMonitor siriHijackEligibilityUpdatedHandler];
-[AASystemStateMonitor showFitEducationNotificationForDevice:];
-[AASystemStateMonitor invalidate];
-[AASystemStateMonitor _activate:];
-[AASystemStateMonitor aaDeviceRouteChanged:withAADevice:];
-[AASystemStateMonitor _interrupted];
-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStopped];
-[AASystemStateMonitor aaDeviceRouteChangedHandler];
-[AASystemStateMonitor direct];
-[AASystemStateMonitor encodeWithCoder:];
-[AASystemStateMonitor setSiriHijackEligibilityUpdatedHandler:];
-[AASystemStateMonitor setInterruptionHandler:];
-[AASystemStateMonitor activeHRMDeviceChanged:withSREnabled:];
-[AASystemStateMonitor _reportError:];
-[AASystemStateMonitor siriHijackEligibilityUpdated:];
-[AASystemStateMonitor description];
-[AASystemStateMonitor initWithCoder:];
-[AASystemStateMonitor aaDeviceConnectionChanged:withAADevice:];
-[AASystemStateMonitor invalidationHandler];
-[AASystemStateMonitor _connectedDeviceFound:];
-[AASystemStateMonitor internalServicesDaemon];
-[AASystemStateMonitor fetchPairedHRMDevices:];
-[AASystemStateMonitor _deviceWithIdentifier:];
-[AASystemStateMonitor setAaDeviceConnectionChangedHandler:];
-[AASystemStateMonitor connectedDiscovery];
-[AASystemStateMonitor hrmCapableDeviceRoutedStateChangedHandler];
-[AASystemStateMonitor _invalidated];
-[AASystemStateMonitor _connectedDeviceLost:];
-[AASystemStateMonitor setDevicesMap:];
-[AASystemStateMonitor devicesMap];
-[AASystemStateMonitor fetchHealthKitDataWriteAllowedForDevice:];
-[AASystemStateMonitor aaDeviceConnectionChangedHandler];
-[AASystemStateMonitor _connectedDeviceDiscoveryEnsureStarted];
```
