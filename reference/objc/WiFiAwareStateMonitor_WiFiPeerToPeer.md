# `WiFiAwareStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PNANStateMonitorXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 18 instance variables, 19 properties, 74 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@"<WiFiP2PNANStateMonitorXPCDelegate>" _remoteProxy;
@"WiFiAwareStateMonitorConfiguration" _lastConfiguration;
@? _stateUpdatedHandler;
@? _dpStateUpdatedHandler;
@? _availUpdatedHandler;
@? _srvInfoUpdatedHandler;
@? _peerAvailInfoUpdatedHandler;
@? _realtimeModeUpdatedHandler;
@? _dpSetupInProgressHandler;
@"NSArray" _lastStateChangedOptions;
@"NSArray" _lastDataPathStateChangedOptions;
@"NSArray" _lastRadioScheduleChangedOptions;
@"WiFiAwareRadioSchedule" _lastRadioSchedule;
@"NSArray" _lastSrvInfoChangedOptions;
@"WiFiAwareSrvInfo" _lastSrvInfo;
@"NSArray" _lastPeerAvailChangedOptions;
@"WiFiAwarePeerAvailInfo" _lastPeerAvailInfo;
```

## Properties

```
@property (T@"NSArray",&,N,V_lastStateChangedOptions) lastStateChangedOptions;
@property (T@"NSArray",&,N,V_lastDataPathStateChangedOptions) lastDataPathStateChangedOptions;
@property (T@"NSArray",&,N,V_lastRadioScheduleChangedOptions) lastRadioScheduleChangedOptions;
@property (T@"WiFiAwareRadioSchedule",&,N,V_lastRadioSchedule) lastRadioSchedule;
@property (T@"NSArray",&,N,V_lastSrvInfoChangedOptions) lastSrvInfoChangedOptions;
@property (T@"WiFiAwareSrvInfo",&,N,V_lastSrvInfo) lastSrvInfo;
@property (T@"NSArray",&,N,V_lastPeerAvailChangedOptions) lastPeerAvailChangedOptions;
@property (T@"WiFiAwarePeerAvailInfo",&,N,V_lastPeerAvailInfo) lastPeerAvailInfo;
@property (T@?,C,N,V_stateUpdatedHandler) stateUpdatedHandler;
@property (T@?,C,N,V_dpStateUpdatedHandler) dpStateUpdatedHandler;
@property (T@?,C,N,V_availUpdatedHandler) availUpdatedHandler;
@property (T@?,C,N,V_srvInfoUpdatedHandler) srvInfoUpdatedHandler;
@property (T@?,C,N,V_peerAvailInfoUpdatedHandler) peerAvailInfoUpdatedHandler;
@property (T@?,C,N,V_realtimeModeUpdatedHandler) realtimeModeUpdatedHandler;
@property (T@?,C,N,V_dpSetupInProgressHandler) dpSetupInProgressHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiAwareStateMonitor beginMonitoring];
-[WiFiAwareStateMonitor stateUpdatedHandler];
-[WiFiAwareStateMonitor startConnectionUsingProxy:completionHandler:];
-[WiFiAwareStateMonitor init];
-[WiFiAwareStateMonitor realtimeModeUpdatedHandler];
-[WiFiAwareStateMonitor setStateUpdatedHandler:];
-[WiFiAwareStateMonitor exportedInterface];
-[WiFiAwareStateMonitor endMonitoring];
-[WiFiAwareStateMonitor exportedObject];
-[WiFiAwareStateMonitor setRealtimeModeUpdatedHandler:];
-[WiFiAwareStateMonitor beginAvailabilityMonitoring];
-[WiFiAwareStateMonitor getFormattedSrvInfoDescription:];
-[WiFiAwareStateMonitor lastRadioScheduleChangedOptions];
-[WiFiAwareStateMonitor queryNANEnabled];
-[WiFiAwareStateMonitor setLastSrvInfo:];
-[WiFiAwareStateMonitor lastDataPathStateChangedOptions];
-[WiFiAwareStateMonitor setLastPeerAvailChangedOptions:];
-[WiFiAwareStateMonitor setPeerAvailInfoUpdatedHandler:];
-[WiFiAwareStateMonitor availUpdatedHandler];
-[WiFiAwareStateMonitor beginDataPathMonitoring];
-[WiFiAwareStateMonitor beginPeerAvailMonitoring];
-[WiFiAwareStateMonitor beginSrvInfoMonitoring];
-[WiFiAwareStateMonitor channelSequenceChangedEvent:map1Channels:];
-[WiFiAwareStateMonitor dpSetupInProgressHandler];
-[WiFiAwareStateMonitor dpStateUpdatedHandler];
-[WiFiAwareStateMonitor endAvailabilityMonitoring];
-[WiFiAwareStateMonitor endDataPathMonitoring];
-[WiFiAwareStateMonitor endPeerAvailMonitoring];
-[WiFiAwareStateMonitor endSrvInfoMonitoring];
-[WiFiAwareStateMonitor getFormattedDataPathStateDescription:];
-[WiFiAwareStateMonitor getFormattedPeerAvailInfoDescription:];
-[WiFiAwareStateMonitor getFormattedRadioScheduleDescription:];
-[WiFiAwareStateMonitor getFormattedStateDescription:];
-[WiFiAwareStateMonitor handleConnectionEstablishedWithProxy:];
-[WiFiAwareStateMonitor lastPeerAvailChangedOptions];
-[WiFiAwareStateMonitor lastPeerAvailInfo];
-[WiFiAwareStateMonitor lastRadioSchedule];
-[WiFiAwareStateMonitor lastSrvInfo];
-[WiFiAwareStateMonitor lastSrvInfoChangedOptions];
-[WiFiAwareStateMonitor lastStateChangedOptions];
-[WiFiAwareStateMonitor peerAvailInfoUpdatedHandler];
-[WiFiAwareStateMonitor queryNANAvail];
-[WiFiAwareStateMonitor queryNANDataPathState];
-[WiFiAwareStateMonitor queryNANPeerAvail];
-[WiFiAwareStateMonitor queryNANSrv];
-[WiFiAwareStateMonitor queryNANState];
-[WiFiAwareStateMonitor setAvailUpdatedHandler:];
-[WiFiAwareStateMonitor setDpSetupInProgressHandler:];
-[WiFiAwareStateMonitor setDpStateUpdatedHandler:];
-[WiFiAwareStateMonitor setLastDataPathStateChangedOptions:];
-[WiFiAwareStateMonitor setLastPeerAvailInfo:];
-[WiFiAwareStateMonitor setLastRadioSchedule:];
-[WiFiAwareStateMonitor setLastRadioScheduleChangedOptions:];
-[WiFiAwareStateMonitor setLastSrvInfoChangedOptions:];
-[WiFiAwareStateMonitor setLastStateChangedOptions:];
-[WiFiAwareStateMonitor setSrvInfoUpdatedHandler:];
-[WiFiAwareStateMonitor srvInfoUpdatedHandler];
-[WiFiAwareStateMonitor updatedNANAvailability:];
-[WiFiAwareStateMonitor updatedNANAvailabilityWithChangedOptions:changedOptions:];
-[WiFiAwareStateMonitor updatedNANAvailabilityWithChangedOptions:changedOptions:forceAllChangedOptions:];
-[WiFiAwareStateMonitor updatedNANDPInProgress:];
-[WiFiAwareStateMonitor updatedNANDpState:];
-[WiFiAwareStateMonitor updatedNANDpStateWithChangedOptions:changedOptions:];
-[WiFiAwareStateMonitor updatedNANDpStateWithChangedOptions:changedOptions:forceAllChangedOptions:];
-[WiFiAwareStateMonitor updatedNANPeerAvail:];
-[WiFiAwareStateMonitor updatedNANPeerAvailWithChangedOptions:changedOptions:];
-[WiFiAwareStateMonitor updatedNANPeerAvailWithChangedOptions:changedOptions:forceAllChangedOptions:];
-[WiFiAwareStateMonitor updatedNANRealtimeMode:];
-[WiFiAwareStateMonitor updatedNANSrvInfo:];
-[WiFiAwareStateMonitor updatedNANSrvInfoWithChangedOptions:changedOptions:];
-[WiFiAwareStateMonitor updatedNANSrvInfoWithChangedOptions:changedOptions:forceAllChangedOptions:];
-[WiFiAwareStateMonitor updatedNANState:];
-[WiFiAwareStateMonitor updatedNANStateWithChangedOptions:changedOptions:];
-[WiFiAwareStateMonitor updatedNANStateWithChangedOptions:changedOptions:forceAllChangedOptions:];
```
