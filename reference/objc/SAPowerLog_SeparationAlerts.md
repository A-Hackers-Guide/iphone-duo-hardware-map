# `SAPowerLog`

- Image: [`/System/Library/PrivateFrameworks/SeparationAlerts.framework/SeparationAlerts`](../userland/System__Library__PrivateFrameworks__SeparationAlerts.framework__SeparationAlerts.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SAPowerLogServiceProtocol`
- 12 instance variables, 12 properties, 36 instance methods, 0 class methods

## Instance variables

```
B _isReplay;
@"<SATimeServiceProtocol>" _clock;
@"NSHashTable" _clients;
@"NSDate" _startTimestamp;
Q _visitCount;
d _totalVisitDuration;
Q _btScanCount;
Q _geofenceCount;
Q _gpsLocationRequestCount;
Q _wifiLocationRequestCount;
Q _separationAlertsCount;
@"NSMutableSet" _monitoredDevices;
```

## Properties

```
@property (T@"<SATimeServiceProtocol>",&,N,V_clock) clock;
@property (T@"NSHashTable",&,N,V_clients) clients;
@property (T@"NSDate",&,N,V_startTimestamp) startTimestamp;
@property (TQ,N,V_visitCount) visitCount;
@property (Td,N,V_totalVisitDuration) totalVisitDuration;
@property (TQ,N,V_btScanCount) btScanCount;
@property (TQ,N,V_geofenceCount) geofenceCount;
@property (TQ,N,V_gpsLocationRequestCount) gpsLocationRequestCount;
@property (TQ,N,V_wifiLocationRequestCount) wifiLocationRequestCount;
@property (TQ,N,V_separationAlertsCount) separationAlertsCount;
@property (T@"NSMutableSet",&,N,V_monitoredDevices) monitoredDevices;
@property (TB,N,V_isReplay) isReplay;
```

## Instance methods

```
-[SAPowerLog clients];
-[SAPowerLog clock];
-[SAPowerLog setClock:];
-[SAPowerLog ingestTAEvent:];
-[SAPowerLog removeClient:];
-[SAPowerLog setStartTimestamp:];
-[SAPowerLog setClients:];
-[SAPowerLog addClient:];
-[SAPowerLog startTimestamp];
-[SAPowerLog resetStatistics];
-[SAPowerLog visitCount];
-[SAPowerLog setVisitCount:];
-[SAPowerLog increaseGpsLocationRequestCount];
-[SAPowerLog setBtScanCount:];
-[SAPowerLog addMonitoredDevice:];
-[SAPowerLog btScanCount];
-[SAPowerLog geofenceCount];
-[SAPowerLog gpsLocationRequestCount];
-[SAPowerLog increaseBTScanCount];
-[SAPowerLog increaseGeofenceCount];
-[SAPowerLog increaseSeparationAlertsCount:];
-[SAPowerLog increaseWifiLocationRequestCount];
-[SAPowerLog initWithClock:isReplay:];
-[SAPowerLog isReplay];
-[SAPowerLog monitoredDevices];
-[SAPowerLog sendPowerLog];
-[SAPowerLog separationAlertsCount];
-[SAPowerLog setGeofenceCount:];
-[SAPowerLog setGpsLocationRequestCount:];
-[SAPowerLog setIsReplay:];
-[SAPowerLog setMonitoredDevices:];
-[SAPowerLog setSeparationAlertsCount:];
-[SAPowerLog setTotalVisitDuration:];
-[SAPowerLog setWifiLocationRequestCount:];
-[SAPowerLog totalVisitDuration];
-[SAPowerLog wifiLocationRequestCount];
```
