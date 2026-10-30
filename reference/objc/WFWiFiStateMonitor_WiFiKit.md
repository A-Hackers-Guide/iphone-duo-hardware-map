# `WFWiFiStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 58 instance methods, 0 class methods

## Instance variables

```
B _monitoring;
B _associatedToCarPlayOnly;
B _useStateMonitor;
q _state;
@? _handler;
@"WFLinkQuality" _linkQuality;
@"NSString" _identifier;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"NSObject<OS_dispatch_queue>" _wifiUIStateFlagsQueue;
@"CWFScanResult" _currentNetwork;
@"WFClient" _client;
@"NSRunLoop" _callbackRunLoop;
@"NSThread" _callbackThread;
@"NSString" _bundleIdentifier;
@"_TtC7WiFiKit12StateMonitor" _stateMonitor;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (T@"NSObject<OS_dispatch_queue>",&,V_internalQueue) internalQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,V_wifiUIStateFlagsQueue) wifiUIStateFlagsQueue;
@property (T@"WFLinkQuality",C,N,V_linkQuality) linkQuality;
@property (T@"CWFScanResult",&,N,V_currentNetwork) currentNetwork;
@property (TB,V_monitoring) monitoring;
@property (TB,V_associatedToCarPlayOnly) associatedToCarPlayOnly;
@property (T@"WFClient",&,N,V_client) client;
@property (T@"NSRunLoop",V_callbackRunLoop) callbackRunLoop;
@property (T@"NSThread",&,N,V_callbackThread) callbackThread;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"_TtC7WiFiKit12StateMonitor",&,N,V_stateMonitor) stateMonitor;
@property (TB,V_useStateMonitor) useStateMonitor;
@property (T@?,C,V_handler) handler;
@property (T@"NSString",C,N,V_identifier) identifier;
```

## Instance methods

```
-[WFWiFiStateMonitor startMonitoring];
-[WFWiFiStateMonitor setCurrentNetwork:];
-[WFWiFiStateMonitor currentNetwork];
-[WFWiFiStateMonitor _updateState];
-[WFWiFiStateMonitor setStateMonitor:];
-[WFWiFiStateMonitor setState:];
-[WFWiFiStateMonitor setCallbackThread:];
-[WFWiFiStateMonitor isPowerModificationDisabled];
-[WFWiFiStateMonitor identifier];
-[WFWiFiStateMonitor init];
-[WFWiFiStateMonitor setCallbackRunLoop:];
-[WFWiFiStateMonitor dealloc];
-[WFWiFiStateMonitor setHandler:];
-[WFWiFiStateMonitor bundleIdentifier];
-[WFWiFiStateMonitor setLinkQuality:];
-[WFWiFiStateMonitor setClient:];
-[WFWiFiStateMonitor stopMonitoring];
-[WFWiFiStateMonitor stateMonitor];
-[WFWiFiStateMonitor setIdentifier:];
-[WFWiFiStateMonitor linkQuality];
-[WFWiFiStateMonitor _runManagerCallbackThread];
-[WFWiFiStateMonitor handler];
-[WFWiFiStateMonitor description];
-[WFWiFiStateMonitor _powerStateDidChange:];
-[WFWiFiStateMonitor callbackThread];
-[WFWiFiStateMonitor setBundleIdentifier:];
-[WFWiFiStateMonitor setInternalQueue:];
-[WFWiFiStateMonitor callbackRunLoop];
-[WFWiFiStateMonitor client];
-[WFWiFiStateMonitor internalQueue];
-[WFWiFiStateMonitor state];
-[WFWiFiStateMonitor _updateState:];
-[WFWiFiStateMonitor _scheduleStateUpdate];
-[WFWiFiStateMonitor monitoring];
-[WFWiFiStateMonitor setMonitoring:];
-[WFWiFiStateMonitor initWithClient:handler:];
-[WFWiFiStateMonitor _linkDidChange:];
-[WFWiFiStateMonitor useStateMonitor];
-[WFWiFiStateMonitor _asyncGetCurrentNetwork:];
-[WFWiFiStateMonitor _autoJoinStateChanged:];
-[WFWiFiStateMonitor _carPlayNetworkTypeDidChange:];
-[WFWiFiStateMonitor _clientConnectionRestarted:];
-[WFWiFiStateMonitor _convertStateMonitorStateToWFWiFiState:];
-[WFWiFiStateMonitor _hostAPStateChanged:];
-[WFWiFiStateMonitor _interfaceBecameAvailable:];
-[WFWiFiStateMonitor _linkQualityDidChange:];
-[WFWiFiStateMonitor _notifyStateChanged:newState:];
-[WFWiFiStateMonitor _outrankStateDidChange:];
-[WFWiFiStateMonitor _performDebounceStateUpdate];
-[WFWiFiStateMonitor _registerInterfaceObserversForInterface:];
-[WFWiFiStateMonitor _spawnManagerCallbackThread];
-[WFWiFiStateMonitor _updateWiFiUIState:];
-[WFWiFiStateMonitor _wifiUIFlagsStateChanged:];
-[WFWiFiStateMonitor associatedToCarPlayOnly];
-[WFWiFiStateMonitor setAssociatedToCarPlayOnly:];
-[WFWiFiStateMonitor setUseStateMonitor:];
-[WFWiFiStateMonitor setWifiUIStateFlagsQueue:];
-[WFWiFiStateMonitor wifiUIStateFlagsQueue];
```
