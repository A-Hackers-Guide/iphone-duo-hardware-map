# `ANMaintenanceMetrics`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _groupMaintDeltas;
@"NSMutableDictionary" _maintainedReasonCountDictionary;
@"NSMutableDictionary" _maintainedCategoryCountDictionary;
B _neededDiscovery;
i _coex;
i _devices;
i _leashable;
d _referenceTime;
d _timeBetweenTriggers;
d _duration;
d _assertionDuration;
@"NSString" _deviceTypes;
@"NSString" _forceReason;
@"NSString" _loiType;
```

## Properties

```
@property (Td,N,V_referenceTime) referenceTime;
@property (Td,N,V_timeBetweenTriggers) timeBetweenTriggers;
@property (Td,N,V_duration) duration;
@property (Td,N,V_assertionDuration) assertionDuration;
@property (TB,N,V_neededDiscovery) neededDiscovery;
@property (Ti,N,V_coex) coex;
@property (Ti,N,V_devices) devices;
@property (Ti,N,V_leashable) leashable;
@property (T@"NSString",&,N,V_deviceTypes) deviceTypes;
@property (T@"NSString",&,N,V_forceReason) forceReason;
@property (T@"NSString",&,N,V_loiType) loiType;
@property (T@"NSDictionary",R,N,V_groupMaintDeltas) groupMaintDeltas;
@property (T@"NSDictionary",R,N) maintainedReasonCountDictionary;
@property (T@"NSDictionary",R,N) maintainedCategoryCountDictionary;
```

## Instance methods

```
-[ANMaintenanceMetrics setDevices:];
-[ANMaintenanceMetrics setLoiType:];
-[ANMaintenanceMetrics init];
-[ANMaintenanceMetrics dealloc];
-[ANMaintenanceMetrics deviceTypes];
-[ANMaintenanceMetrics duration];
-[ANMaintenanceMetrics devices];
-[ANMaintenanceMetrics setDuration:];
-[ANMaintenanceMetrics loiType];
-[ANMaintenanceMetrics referenceTime];
-[ANMaintenanceMetrics setReferenceTime:];
-[ANMaintenanceMetrics setDeviceTypes:];
-[ANMaintenanceMetrics neededDiscovery];
-[ANMaintenanceMetrics startNewMaintEventWithCount:leashable:deviceTypes:coex:loiType:];
-[ANMaintenanceMetrics maintainedReasonCountDictionary];
-[ANMaintenanceMetrics setForceReason:];
-[ANMaintenanceMetrics accumulateMaintainedReasonCountWithReason:andCategory:];
-[ANMaintenanceMetrics assertionDuration];
-[ANMaintenanceMetrics coex];
-[ANMaintenanceMetrics forceReason];
-[ANMaintenanceMetrics groupMaintDeltas];
-[ANMaintenanceMetrics leashable];
-[ANMaintenanceMetrics maintainedCategoryCountDictionary];
-[ANMaintenanceMetrics resetWithTime:];
-[ANMaintenanceMetrics setAssertionDuration:];
-[ANMaintenanceMetrics setCoex:];
-[ANMaintenanceMetrics setGroupMaintDelta:forUUID:];
-[ANMaintenanceMetrics setLeashable:];
-[ANMaintenanceMetrics setNeededDiscovery:];
-[ANMaintenanceMetrics setTimeBetweenTriggers:];
-[ANMaintenanceMetrics timeBetweenTriggers];
```
