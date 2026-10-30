# `WFInterface`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 23 instance variables, 23 properties, 87 instance methods, 0 class methods

## Instance variables

```
B _ipv4SelfAssigned;
B _hasNoGatewayIP;
B _currentNetworkIsDirected;
B _monitoringEvents;
B _scanning;
B _associatedOnIRInterface;
i _ipState;
@"NSString" _interfaceName;
@"WFNetworkScanRecord" _currentNetwork;
@"WFIPMonitor" _ipMonitor;
@"NSArray" _deviceScanChannels;
@"NSArray" _deviceScanChannelsPerCurLocale;
@"NSSet" _currentNetworkIssues;
@"WFNetworkScanRecord" _coreWiFiCurrentNetwork;
@"NSObject<OS_dispatch_queue>" _currentNetworkQueue;
@"NSObject<OS_dispatch_queue>" _networkProcessingQueue;
^{__WiFiDeviceClient=} _device;
@"NSOperationQueue" _joinQueue;
@"NSThread" _callbackThread;
@"NSRunLoop" _callbackRunLoop;
@"WFClient" _wifiClient;
@"CWFInterface" _cInterface;
@"CWFInterface" _irInterface;
```

## Properties

```
@property (T@"NSSet",&,N,V_currentNetworkIssues) currentNetworkIssues;
@property (T@"WFNetworkScanRecord",&,N,V_currentNetwork) currentNetwork;
@property (T@"WFNetworkScanRecord",&,N,V_coreWiFiCurrentNetwork) coreWiFiCurrentNetwork;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"WFIPMonitor",&,N,V_ipMonitor) ipMonitor;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_currentNetworkQueue) currentNetworkQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_networkProcessingQueue) networkProcessingQueue;
@property (T^{__WiFiDeviceClient=},N,V_device) device;
@property (T@"NSOperationQueue",&,N,V_joinQueue) joinQueue;
@property (T@"NSArray",&,N,V_deviceScanChannels) deviceScanChannels;
@property (T@"NSArray",&,N,V_deviceScanChannelsPerCurLocale) deviceScanChannelsPerCurLocale;
@property (Ti,N,V_ipState) ipState;
@property (TB,N,V_ipv4SelfAssigned) ipv4SelfAssigned;
@property (TB,N,V_hasNoGatewayIP) hasNoGatewayIP;
@property (TB,N,V_currentNetworkIsDirected) currentNetworkIsDirected;
@property (T@"NSThread",&,N,V_callbackThread) callbackThread;
@property (T@"NSRunLoop",&,N,V_callbackRunLoop) callbackRunLoop;
@property (TB,V_monitoringEvents) monitoringEvents;
@property (TB,V_scanning) scanning;
@property (T@"WFClient",W,N,V_wifiClient) wifiClient;
@property (T@"CWFInterface",&,N,V_cInterface) cInterface;
@property (T@"CWFInterface",&,N,V_irInterface) irInterface;
@property (TB,N,V_associatedOnIRInterface) associatedOnIRInterface;
```

## Instance methods

```
-[WFInterface setScanning:];
-[WFInterface setCurrentNetwork:];
-[WFInterface IPv4SubnetMasks];
-[WFInterface _currentInterface];
-[WFInterface IPv4Addresses];
-[WFInterface IPv4RouterAddress];
-[WFInterface currentNetwork];
-[WFInterface scanning];
-[WFInterface _linkQualityChanged:];
-[WFInterface isReadyForConnectionVelocityTest];
-[WFInterface disassociateFromCurrentNetworkWithReason:];
-[WFInterface IPv6Addresses];
-[WFInterface setIrInterface:];
-[WFInterface setAssociatedOnIRInterface:];
-[WFInterface joinQueue];
-[WFInterface currentKnownNetworkProfile];
-[WFInterface IPv4ARPResolvedIPAddress];
-[WFInterface IPv6RouterAddress];
-[WFInterface initWithDevice:];
-[WFInterface setCallbackThread:];
-[WFInterface setHasNoGatewayIP:];
-[WFInterface setWifiClient:];
-[WFInterface setDevice:];
-[WFInterface _carPlayNetworkTypeChangedCallback:];
-[WFInterface _initCurrentNetwork];
-[WFInterface device];
-[WFInterface setDeviceScanChannels:];
-[WFInterface _wifiManagerRestarted:];
-[WFInterface asyncAssociateToNetwork:password:reply:];
-[WFInterface _currentNetworkDidChangeWithReason:previousNetwork:];
-[WFInterface hasValidIPAddress];
-[WFInterface setInterfaceName:];
-[WFInterface _linkChangedWithInfo:];
-[WFInterface setCallbackRunLoop:];
-[WFInterface dealloc];
-[WFInterface deviceScanChannels];
-[WFInterface interfaceName];
-[WFInterface hasPrimaryIPConfiguration];
-[WFInterface setCoreWiFiCurrentNetwork:];
-[WFInterface currentNetworkIssues];
-[WFInterface wifiClient];
-[WFInterface associatedOnIRInterface];
-[WFInterface createNANInterface];
-[WFInterface setMonitoringEvents:];
-[WFInterface hasNoGatewayIP];
-[WFInterface networkProcessingQueue];
-[WFInterface setCInterface:];
-[WFInterface setIpv4SelfAssigned:];
-[WFInterface deviceScanChannelsPerCurLocale];
-[WFInterface coreWiFiCurrentNetwork];
-[WFInterface monitoringEvents];
-[WFInterface initWithDevice:coreWiFiInterface:];
-[WFInterface _startMonitoringWiFiEvents];
-[WFInterface _updateCurrentNetworkWithNetwork:callback:];
-[WFInterface cInterface];
-[WFInterface asyncScanRequest:reply:];
-[WFInterface setJoinQueue:];
-[WFInterface updateDeviceScanChannelsPerCurLocale];
-[WFInterface _stopMonitoringWiFiEvents];
-[WFInterface setDeviceScanChannelsPerCurLocale:];
-[WFInterface setIpState:];
-[WFInterface setCurrentNetworkIsDirected:];
-[WFInterface _hostAPStateDidChange:];
-[WFInterface ipState];
-[WFInterface asyncCurrentScanResult:];
-[WFInterface ipv4SelfAssigned];
-[WFInterface disassociateFromCarPlayUserConfiguredNetwork];
-[WFInterface setNetworkProcessingQueue:];
-[WFInterface currentNetworkQueue];
-[WFInterface asyncHS20Supported:];
-[WFInterface callbackThread];
-[WFInterface notifyNoNetworksFound];
-[WFInterface disassociateFromCurrentNetwork];
-[WFInterface setIpMonitor:];
-[WFInterface irInterface];
-[WFInterface callbackRunLoop];
-[WFInterface asyncCurrentNetwork:];
-[WFInterface asyncAssociateToNetwork:profile:reply:];
-[WFInterface setCurrentNetworkIssues:];
-[WFInterface disassociateFromCurrentNetworkWithCompletion:];
-[WFInterface _updateCurrentNetworkWithNetwork:forceUpdateNetwork:callback:userInfo:];
-[WFInterface initWithDevice:coreWiFiInterface:interfaceName:];
-[WFInterface currentNetworkIsDirected];
-[WFInterface setCurrentNetworkQueue:];
-[WFInterface _resetCurrentNetworkStates];
-[WFInterface _debugLQMString:];
-[WFInterface ipMonitor];
```
