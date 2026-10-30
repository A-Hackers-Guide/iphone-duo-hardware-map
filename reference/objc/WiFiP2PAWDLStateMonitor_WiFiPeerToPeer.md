# `WiFiP2PAWDLStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PAWDLStateMonitorXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 10 instance variables, 12 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@"NSMutableArray" _interestedUniqueIdentifiers;
@? _stateUpdatedHandler;
@? _statisticsUpdatedHandler;
@? _lowLatencyStatisticsUpdatedHandler;
@? _realtimeModeUpdatedHandler;
@? _threadCoexistenceEventHandler;
@? _softAPChannelChangedEventHandler;
@? _channelSequenceUpdatedEventHandler;
@? _serviceAvailabilityUpdatedHandler;
```

## Properties

```
@property (T@?,C,N,V_stateUpdatedHandler) stateUpdatedHandler;
@property (T@?,C,N,V_statisticsUpdatedHandler) statisticsUpdatedHandler;
@property (T@?,C,N,V_lowLatencyStatisticsUpdatedHandler) lowLatencyStatisticsUpdatedHandler;
@property (T@?,C,N,V_realtimeModeUpdatedHandler) realtimeModeUpdatedHandler;
@property (T@?,C,N,V_threadCoexistenceEventHandler) threadCoexistenceEventHandler;
@property (T@?,C,N,V_softAPChannelChangedEventHandler) softAPChannelChangedEventHandler;
@property (T@?,C,N,V_channelSequenceUpdatedEventHandler) channelSequenceUpdatedEventHandler;
@property (T@?,C,N,V_serviceAvailabilityUpdatedHandler) serviceAvailabilityUpdatedHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiP2PAWDLStateMonitor beginMonitoring];
-[WiFiP2PAWDLStateMonitor stateUpdatedHandler];
-[WiFiP2PAWDLStateMonitor startConnectionUsingProxy:completionHandler:];
-[WiFiP2PAWDLStateMonitor copyStatistics];
-[WiFiP2PAWDLStateMonitor registerAvailabilityUpdatesForService:];
-[WiFiP2PAWDLStateMonitor updateLTERestrictedChannels:error:];
-[WiFiP2PAWDLStateMonitor threadCoexistenceEvent:];
-[WiFiP2PAWDLStateMonitor init];
-[WiFiP2PAWDLStateMonitor realtimeModeUpdatedHandler];
-[WiFiP2PAWDLStateMonitor setLowLatencyStatisticsUpdatedHandler:];
-[WiFiP2PAWDLStateMonitor setStateUpdatedHandler:];
-[WiFiP2PAWDLStateMonitor copyActiveServiceUniqueIdentifiers];
-[WiFiP2PAWDLStateMonitor serviceAvailabilityUpdatedHandler];
-[WiFiP2PAWDLStateMonitor exportedInterface];
-[WiFiP2PAWDLStateMonitor copyLowLatencyStatistics];
-[WiFiP2PAWDLStateMonitor threadCoexistenceEventHandler];
-[WiFiP2PAWDLStateMonitor setThreadCoexistenceEventHandler:];
-[WiFiP2PAWDLStateMonitor softAPChannelChangedEvent:channelNumber:];
-[WiFiP2PAWDLStateMonitor lowLatencyStatisticsDifferenceBetweenPrevious:current:];
-[WiFiP2PAWDLStateMonitor updatedStatistics];
-[WiFiP2PAWDLStateMonitor endMonitoring];
-[WiFiP2PAWDLStateMonitor exportedObject];
-[WiFiP2PAWDLStateMonitor copySidecarStatistics];
-[WiFiP2PAWDLStateMonitor lowLatencyStatisticsUpdatedHandler];
-[WiFiP2PAWDLStateMonitor setStatisticsUpdatedHandler:];
-[WiFiP2PAWDLStateMonitor setChannelSequenceUpdatedEventHandler:];
-[WiFiP2PAWDLStateMonitor setRealtimeModeUpdatedHandler:];
-[WiFiP2PAWDLStateMonitor queryAverageRSSIForPeer:];
-[WiFiP2PAWDLStateMonitor setSoftAPChannelChangedEventHandler:];
-[WiFiP2PAWDLStateMonitor updatedRealtimeMode:];
-[WiFiP2PAWDLStateMonitor availabilityUpdatedForService:error:];
-[WiFiP2PAWDLStateMonitor queryPeerDatabase];
-[WiFiP2PAWDLStateMonitor setServiceAvailabilityUpdatedHandler:];
-[WiFiP2PAWDLStateMonitor updatedAWDLState:];
-[WiFiP2PAWDLStateMonitor fetchAWDLActiveServices:withActivePorts:error:];
-[WiFiP2PAWDLStateMonitor channelSequenceUpdatedEventHandler];
-[WiFiP2PAWDLStateMonitor statisticsUpdatedHandler];
-[WiFiP2PAWDLStateMonitor channelSequenceChangedEvent:];
-[WiFiP2PAWDLStateMonitor softAPChannelChangedEventHandler];
-[WiFiP2PAWDLStateMonitor updatedLowLatencyStatistics];
```
