# `CWFRemoteInterfaceManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"CWFInterface" _interface;
@"NSObject<OS_dispatch_queue>" _requestQueue;
@"NSObject<OS_dispatch_source>" _interfaceDeactivationTimer;
Q _requestsInProgress;
```

## Properties

```
@property (T@"CWFInterface",&,N,V_interface) interface;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_requestQueue) requestQueue;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_interfaceDeactivationTimer) interfaceDeactivationTimer;
@property (TQ,N,V_requestsInProgress) requestsInProgress;
```

## Class methods

```
+[CWFRemoteInterfaceManager sharedInstance];
```

## Instance methods

```
-[CWFRemoteInterfaceManager requestQueue];
-[CWFRemoteInterfaceManager init];
-[CWFRemoteInterfaceManager setInterface:];
-[CWFRemoteInterfaceManager interface];
-[CWFRemoteInterfaceManager setRequestQueue:];
-[CWFRemoteInterfaceManager scanAvailableNetworksWithCompletion:];
-[CWFRemoteInterfaceManager _activateInterface];
-[CWFRemoteInterfaceManager _deactivateInterface];
-[CWFRemoteInterfaceManager _defaultScanParameters];
-[CWFRemoteInterfaceManager _invalidateInterfaceDeactivationTimer];
-[CWFRemoteInterfaceManager _isInterfaceDeactivationTimerValid];
-[CWFRemoteInterfaceManager _startInterfaceDeactivationTimerIfNeeded];
-[CWFRemoteInterfaceManager associateNetwork:password:completion:];
-[CWFRemoteInterfaceManager interfaceDeactivationTimer];
-[CWFRemoteInterfaceManager requestsInProgress];
-[CWFRemoteInterfaceManager setInterfaceDeactivationTimer:];
-[CWFRemoteInterfaceManager setRequestsInProgress:];
-[CWFRemoteInterfaceManager wifiStatusWithCompletion:];
```
