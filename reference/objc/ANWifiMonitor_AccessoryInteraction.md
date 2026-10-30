# `ANWifiMonitor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
^{__WiFiManagerClient=} _wifiManager;
^{__WiFiDeviceClient=} _wifiDevice;
^{__WiFiNetwork=} _wifiNetwork;
i _channel;
B _isAssociated;
B _isOn2GHzNetwork;
B _isInCriticalState;
B _isAssociatedTo2GHzWiFi;
@? _criticalStateUpdateHandler;
@? _isOn2GHzNetworkUpdateHandler;
```

## Properties

```
@property (TB,R,V_isInCriticalState) isInCriticalState;
@property (TB,R,V_isAssociatedTo2GHzWiFi) isAssociatedTo2GHzWiFi;
@property (TB,R,V_isOn2GHzNetwork) isOn2GHzNetwork;
@property (T@?,C,V_criticalStateUpdateHandler) criticalStateUpdateHandler;
@property (T@?,C,V_isOn2GHzNetworkUpdateHandler) isOn2GHzNetworkUpdateHandler;
```

## Instance methods

```
-[ANWifiMonitor initWithQueue:];
-[ANWifiMonitor dealloc];
-[ANWifiMonitor isOn2GHzNetwork];
-[ANWifiMonitor criticalStateUpdateHandler];
-[ANWifiMonitor getChangedNetwork:];
-[ANWifiMonitor getChannelNumberFromNetwork:];
-[ANWifiMonitor getLinkDownStatus:];
-[ANWifiMonitor isAssociatedTo2GHzWiFi];
-[ANWifiMonitor isInCriticalState];
-[ANWifiMonitor isOn2GHzNetworkUpdateHandler];
-[ANWifiMonitor onWiFiDeviceClient:extendedLinkCallback:];
-[ANWifiMonitor onWiFiDeviceClient:networkInCriticalState:];
-[ANWifiMonitor setCriticalStateUpdateHandler:];
-[ANWifiMonitor setIsOn2GHzNetworkUpdateHandler:];
-[ANWifiMonitor setupWifiBits];
```
