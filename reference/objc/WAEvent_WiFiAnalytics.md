# `WAEvent`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 16 properties, 43 instance methods, 0 class methods

## Instance variables

```
B _bssidAttributionAttempted;
@"NSDate" _eventDate;
@"NSArray" _ccaHistory;
@"NSArray" _rssiHistory;
@"NSArray" _noiseHistory;
@"NSArray" _snrHistory;
@"NSArray" _txPerHistory;
@"NSArray" _txFrameHistory;
@"NSArray" _fwTxPerHistory;
@"NSArray" _fwTxFramesHistory;
@"NSArray" _beaconSchedHistory;
@"NSArray" _beaconPerHistory;
@"NSEntityDescription" _entity;
@"NSString" _bssid;
@"BSSMO" _currentBss;
```

## Properties

```
@property (T@"NSEntityDescription",&,N,V_entity) entity;
@property (T{?=ssssisii},D,N) data;
@property (T@"NSDate",&,N,V_eventDate) eventDate;
@property (T@"NSString",&,N,V_bssid) bssid;
@property (T@"BSSMO",&,N,V_currentBss) currentBss;
@property (TB,N,V_bssidAttributionAttempted) bssidAttributionAttempted;
@property (T@"NSArray",C,N,V_ccaHistory) ccaHistory;
@property (T@"NSArray",C,N,V_rssiHistory) rssiHistory;
@property (T@"NSArray",C,N,V_noiseHistory) noiseHistory;
@property (T@"NSArray",C,N,V_snrHistory) snrHistory;
@property (T@"NSArray",C,N,V_txPerHistory) txPerHistory;
@property (T@"NSArray",C,N,V_txFrameHistory) txFrameHistory;
@property (T@"NSArray",C,N,V_fwTxPerHistory) fwTxPerHistory;
@property (T@"NSArray",C,N,V_fwTxFramesHistory) fwTxFramesHistory;
@property (T@"NSArray",C,N,V_beaconSchedHistory) beaconSchedHistory;
@property (T@"NSArray",C,N,V_beaconPerHistory) beaconPerHistory;
```

## Instance methods

```
-[WAEvent processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEvent dictionaryForCA];
-[WAEvent eventNameForCA];
-[WAEvent caSamplingPercentage];
-[WAEvent setCcaHistory:];
-[WAEvent eventDate];
-[WAEvent txPerHistory];
-[WAEvent noiseHistory];
-[WAEvent updateRecord:];
-[WAEvent setEntity:];
-[WAEvent setTxFrameHistory:];
-[WAEvent beaconPerHistory];
-[WAEvent setBssid:];
-[WAEvent rssiHistory];
-[WAEvent ccaHistory];
-[WAEvent setSnrHistory:];
-[WAEvent txFrameHistory];
-[WAEvent setRssiHistory:];
-[WAEvent beaconSchedHistory];
-[WAEvent entity];
-[WAEvent snrHistory];
-[WAEvent setFwTxFramesHistory:];
-[WAEvent description];
-[WAEvent bssid];
-[WAEvent setFwTxPerHistory:];
-[WAEvent setBeaconSchedHistory:];
-[WAEvent setTxPerHistory:];
-[WAEvent setNoiseHistory:];
-[WAEvent fwTxFramesHistory];
-[WAEvent fwTxPerHistory];
-[WAEvent setBeaconPerHistory:];
-[WAEvent setEventDate:];
-[WAEvent submitEventToCA];
-[WAEvent _processEventOnPersistentContainer:enforceNotNilBssid:withError:];
-[WAEvent _processEventOnPersistentContainer:withError:];
-[WAEvent bssidAttributionAttempted];
-[WAEvent currentBss];
-[WAEvent initWithEntity:bssid:at:withLqmHistory:];
-[WAEvent initWithoutEntityAt:];
-[WAEvent lqmHistoriesDescription];
-[WAEvent processEventOnPersistentContainer:withError:];
-[WAEvent setBssidAttributionAttempted:];
-[WAEvent setCurrentBss:];
```
