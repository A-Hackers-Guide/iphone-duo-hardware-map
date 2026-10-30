# `WiFiP2PNANStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PNANStateMonitorXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 2 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@? _channelSequenceUpdatedEventHandler;
```

## Properties

```
@property (T@?,C,N,V_channelSequenceUpdatedEventHandler) channelSequenceUpdatedEventHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiP2PNANStateMonitor beginMonitoring];
-[WiFiP2PNANStateMonitor startConnectionUsingProxy:completionHandler:];
-[WiFiP2PNANStateMonitor init];
-[WiFiP2PNANStateMonitor exportedInterface];
-[WiFiP2PNANStateMonitor endMonitoring];
-[WiFiP2PNANStateMonitor exportedObject];
-[WiFiP2PNANStateMonitor setChannelSequenceUpdatedEventHandler:];
-[WiFiP2PNANStateMonitor channelSequenceUpdatedEventHandler];
-[WiFiP2PNANStateMonitor channelSequenceChangedEvent:map1Channels:];
-[WiFiP2PNANStateMonitor updatedNANAvailability:];
-[WiFiP2PNANStateMonitor updatedNANAvailabilityWithChangedOptions:changedOptions:];
-[WiFiP2PNANStateMonitor updatedNANAvailabilityWithChangedOptions:changedOptions:forceAllChangedOptions:];
-[WiFiP2PNANStateMonitor updatedNANDpState:];
-[WiFiP2PNANStateMonitor updatedNANDpStateWithChangedOptions:changedOptions:];
-[WiFiP2PNANStateMonitor updatedNANDpStateWithChangedOptions:changedOptions:forceAllChangedOptions:];
-[WiFiP2PNANStateMonitor updatedNANPeerAvail:];
-[WiFiP2PNANStateMonitor updatedNANPeerAvailWithChangedOptions:changedOptions:];
-[WiFiP2PNANStateMonitor updatedNANPeerAvailWithChangedOptions:changedOptions:forceAllChangedOptions:];
-[WiFiP2PNANStateMonitor updatedNANRealtimeMode:];
-[WiFiP2PNANStateMonitor updatedNANSrvInfo:];
-[WiFiP2PNANStateMonitor updatedNANSrvInfoWithChangedOptions:changedOptions:];
-[WiFiP2PNANStateMonitor updatedNANSrvInfoWithChangedOptions:changedOptions:forceAllChangedOptions:];
-[WiFiP2PNANStateMonitor updatedNANState:];
-[WiFiP2PNANStateMonitor updatedNANStateWithChangedOptions:changedOptions:];
-[WiFiP2PNANStateMonitor updatedNANStateWithChangedOptions:changedOptions:forceAllChangedOptions:];
```
