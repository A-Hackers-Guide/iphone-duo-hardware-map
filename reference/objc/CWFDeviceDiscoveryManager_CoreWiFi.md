# `CWFDeviceDiscoveryManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 45 instance methods, 0 class methods

## Instance variables

```
Q _setupReason;
@"RPCompanionLinkClient" _rapportClient;
Q _rapportClientActivationFailCount;
@"NSMutableSet" _activeDevices;
@"NSMutableDictionary" _retryDevices;
@"NSObject<OS_dispatch_source>" _wifiInfoRetryRequestTimer;
@"NSObject<OS_dispatch_source>" _rapportTeardownTimer;
@"NSObject<OS_dispatch_queue>" _rapportQueue;
@"NSString" _thisDeviceMACAddress;
@"NSMutableSet" _delegates;
@"NSRegularExpression" _rapportErrorRegex;
```

## Properties

```
@property (TQ,N,V_setupReason) setupReason;
@property (T@"RPCompanionLinkClient",&,N,V_rapportClient) rapportClient;
@property (TQ,N,V_rapportClientActivationFailCount) rapportClientActivationFailCount;
@property (T@"NSMutableSet",&,N,V_activeDevices) activeDevices;
@property (T@"NSMutableDictionary",&,N,V_retryDevices) retryDevices;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_wifiInfoRetryRequestTimer) wifiInfoRetryRequestTimer;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_rapportTeardownTimer) rapportTeardownTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_rapportQueue) rapportQueue;
@property (T@"NSString",C,N,V_thisDeviceMACAddress) thisDeviceMACAddress;
@property (T@"NSMutableSet",&,N,V_delegates) delegates;
@property (T@"NSRegularExpression",&,N,V_rapportErrorRegex) rapportErrorRegex;
```

## Instance methods

```
-[CWFDeviceDiscoveryManager setDelegates:];
-[CWFDeviceDiscoveryManager delegates];
-[CWFDeviceDiscoveryManager init];
-[CWFDeviceDiscoveryManager unregisterDelegate:];
-[CWFDeviceDiscoveryManager invalidate];
-[CWFDeviceDiscoveryManager registerDelegate:];
-[CWFDeviceDiscoveryManager activeDevices];
-[CWFDeviceDiscoveryManager rapportClient];
-[CWFDeviceDiscoveryManager rapportQueue];
-[CWFDeviceDiscoveryManager setActiveDevices:];
-[CWFDeviceDiscoveryManager setRapportQueue:];
-[CWFDeviceDiscoveryManager setSetupReason:];
-[CWFDeviceDiscoveryManager _invalidateRapportTeardownTimer];
-[CWFDeviceDiscoveryManager _fetchAndUpdateActiveDevicesInfo];
-[CWFDeviceDiscoveryManager _fetchWiFiInfoForDevice:rapportDevice:];
-[CWFDeviceDiscoveryManager _fetchWiFiInfoForRapportDevice:completion:];
-[CWFDeviceDiscoveryManager _interfaceForModel:];
-[CWFDeviceDiscoveryManager _invalidateWiFiInfoRetryRequestTimer];
-[CWFDeviceDiscoveryManager _isRapportTeardownTimerValid];
-[CWFDeviceDiscoveryManager _isSupportedModel:];
-[CWFDeviceDiscoveryManager _isWiFiInfoRequestTimerValid];
-[CWFDeviceDiscoveryManager _registerExtractWiFiInfo];
-[CWFDeviceDiscoveryManager _reportFaultEventForDevices:];
-[CWFDeviceDiscoveryManager _resetRapportClientWithInvalidation:];
-[CWFDeviceDiscoveryManager _sendRapportMessageToDevice:requestID:request:options:completion:];
-[CWFDeviceDiscoveryManager _sendRapportMessageToDevice:withRequestID:request:options:completion:];
-[CWFDeviceDiscoveryManager _setupRapportClientWithReason:];
-[CWFDeviceDiscoveryManager _wifiInfo];
-[CWFDeviceDiscoveryManager fetchActiveDevices];
-[CWFDeviceDiscoveryManager fetchWiFiInfoForDevice:];
-[CWFDeviceDiscoveryManager rapportClientActivationFailCount];
-[CWFDeviceDiscoveryManager rapportErrorRegex];
-[CWFDeviceDiscoveryManager rapportTeardownTimer];
-[CWFDeviceDiscoveryManager retryDevices];
-[CWFDeviceDiscoveryManager setRapportClient:];
-[CWFDeviceDiscoveryManager setRapportClientActivationFailCount:];
-[CWFDeviceDiscoveryManager setRapportErrorRegex:];
-[CWFDeviceDiscoveryManager setRapportTeardownTimer:];
-[CWFDeviceDiscoveryManager setRetryDevices:];
-[CWFDeviceDiscoveryManager setThisDeviceMACAddress:];
-[CWFDeviceDiscoveryManager setWifiInfoRetryRequestTimer:];
-[CWFDeviceDiscoveryManager setupReason];
-[CWFDeviceDiscoveryManager startDiscoveringDevicesIfNeeded:withReason:];
-[CWFDeviceDiscoveryManager thisDeviceMACAddress];
-[CWFDeviceDiscoveryManager wifiInfoRetryRequestTimer];
```
