# `WAEventLQMHistory`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _ccaHistory;
@"NSMutableArray" _rssiHistory;
@"NSMutableArray" _noiseHistory;
@"NSMutableArray" _snrHistory;
@"NSMutableArray" _txPerHistory;
@"NSMutableArray" _txFrameHistory;
@"NSMutableArray" _fwTxPerHistory;
@"NSMutableArray" _fwTxFramesHistory;
@"NSMutableArray" _beaconSchedHistory;
@"NSMutableArray" _beaconPerHistory;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_ccaHistory) ccaHistory;
@property (T@"NSMutableArray",&,N,V_rssiHistory) rssiHistory;
@property (T@"NSMutableArray",&,N,V_noiseHistory) noiseHistory;
@property (T@"NSMutableArray",&,N,V_snrHistory) snrHistory;
@property (T@"NSMutableArray",&,N,V_txPerHistory) txPerHistory;
@property (T@"NSMutableArray",&,N,V_txFrameHistory) txFrameHistory;
@property (T@"NSMutableArray",&,N,V_fwTxPerHistory) fwTxPerHistory;
@property (T@"NSMutableArray",&,N,V_fwTxFramesHistory) fwTxFramesHistory;
@property (T@"NSMutableArray",&,N,V_beaconSchedHistory) beaconSchedHistory;
@property (T@"NSMutableArray",&,N,V_beaconPerHistory) beaconPerHistory;
```

## Instance methods

```
-[WAEventLQMHistory setCcaHistory:];
-[WAEventLQMHistory txPerHistory];
-[WAEventLQMHistory noiseHistory];
-[WAEventLQMHistory setTxFrameHistory:];
-[WAEventLQMHistory init];
-[WAEventLQMHistory beaconPerHistory];
-[WAEventLQMHistory rssiHistory];
-[WAEventLQMHistory ccaHistory];
-[WAEventLQMHistory setSnrHistory:];
-[WAEventLQMHistory txFrameHistory];
-[WAEventLQMHistory setRssiHistory:];
-[WAEventLQMHistory beaconSchedHistory];
-[WAEventLQMHistory snrHistory];
-[WAEventLQMHistory setFwTxFramesHistory:];
-[WAEventLQMHistory setFwTxPerHistory:];
-[WAEventLQMHistory setBeaconSchedHistory:];
-[WAEventLQMHistory setTxPerHistory:];
-[WAEventLQMHistory setNoiseHistory:];
-[WAEventLQMHistory fwTxFramesHistory];
-[WAEventLQMHistory fwTxPerHistory];
-[WAEventLQMHistory setBeaconPerHistory:];
```
