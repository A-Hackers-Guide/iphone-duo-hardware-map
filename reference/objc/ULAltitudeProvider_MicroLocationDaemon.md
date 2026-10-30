# `ULAltitudeProvider`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULAltitudeDelegate`
- 8 instance variables, 12 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _hasDeliveredNonZeroStatus;
@"NSObject<OS_dispatch_queue>" _queue;
@"<ULAltitudeProviderDelegate>" _delegate;
@"<ULAltitudeSource>" _altitudeSource;
@"NSUUID" _altitudeSessionUUID;
@"NSNumber" _referenceAltitudeMeters;
@"NSNumber" _lastReportedAltitudeMeters;
@"NSDate" _previousStatusUpdateDate;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<ULAltitudeProviderDelegate>",W,N,V_delegate) delegate;
@property (T@"<ULAltitudeSource>",&,N,V_altitudeSource) altitudeSource;
@property (T@"NSUUID",&,N,V_altitudeSessionUUID) altitudeSessionUUID;
@property (T@"NSNumber",&,N,V_referenceAltitudeMeters) referenceAltitudeMeters;
@property (T@"NSNumber",&,N,V_lastReportedAltitudeMeters) lastReportedAltitudeMeters;
@property (T@"NSDate",&,N,V_previousStatusUpdateDate) previousStatusUpdateDate;
@property (TB,N,V_hasDeliveredNonZeroStatus) hasDeliveredNonZeroStatus;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULAltitudeProvider isAltitudeAvailable];
```

## Instance methods

```
-[ULAltitudeProvider hasDeliveredNonZeroStatus];
-[ULAltitudeProvider referenceAltitudeMeters];
-[ULAltitudeProvider _resetTrajectory];
-[ULAltitudeProvider didReceiveAltitudeProviderStateIsAvailable:];
-[ULAltitudeProvider setPreviousStatusUpdateDate:];
-[ULAltitudeProvider didReceiveAltitudeUpdate:withError:];
-[ULAltitudeProvider lastReportedAltitudeMeters];
-[ULAltitudeProvider _checkIfAltitudeExceedsThreshold:];
-[ULAltitudeProvider initWithQueue:delegate:];
-[ULAltitudeProvider queue];
-[ULAltitudeProvider setReferenceAltitudeMeters:];
-[ULAltitudeProvider stopBackgroundUpdates];
-[ULAltitudeProvider setLastReportedAltitudeMeters:];
-[ULAltitudeProvider setDelegate:];
-[ULAltitudeProvider _getTimestampFromState:];
-[ULAltitudeProvider setAltitudeSessionUUID:];
-[ULAltitudeProvider delegate];
-[ULAltitudeProvider setHasDeliveredNonZeroStatus:];
-[ULAltitudeProvider setAltitudeSource:];
-[ULAltitudeProvider altitudeSessionUUID];
-[ULAltitudeProvider startBackgroundUpdates];
-[ULAltitudeProvider altitudeSource];
-[ULAltitudeProvider previousStatusUpdateDate];
-[ULAltitudeProvider _resetReferenceAltitude];
-[ULAltitudeProvider setQueue:];
```
