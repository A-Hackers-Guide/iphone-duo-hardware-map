# `ANMaintenance`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ANMaintenanceUtilitiesDelegate`
- 26 instance variables, 22 properties, 81 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"ANMaintenanceMetrics" _metrics;
@"ANScanCache" _scanCache;
@"NSString" _loi;
B _heleOnly;
i _coexMask;
i _cycles;
i _heartbeats;
B _btOn;
I _maintainable;
I _leashable;
I _helemaintainable;
i _coexStatus;
@"_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator" _proactiveCoordinator;
@"_TtC20AccessoryInteraction20ANBOMScanCoordinator" _bomScanCoordinator;
@"<ANMaintenanceDelegate>" _delegate;
Q _dutyCycleUpgrade;
Q _maintState;
@"ANMaintenanceUtilities" _utils;
@"ANSettings" _settings;
@"NSMutableDictionary" _devices;
@"NSDictionary" _devicesImmutable;
@"NSMutableSet" _activelyMaintaining;
@"NSMutableSet" _evictionCandidates;
@"NSMutableDictionary" _evictionMap;
@"<ANSystemUtilsProtocol>" _systemUtils;
```

## Properties

```
@property (TI,N,V_maintainable) maintainable;
@property (TI,N,V_leashable) leashable;
@property (TI,N,V_helemaintainable) helemaintainable;
@property (TB,N,V_btOn) btOn;
@property (TQ,N,V_dutyCycleUpgrade) dutyCycleUpgrade;
@property (Ti,N,V_coexStatus) coexStatus;
@property (TQ,N,V_maintState) maintState;
@property (T@"ANMaintenanceUtilities",&,N,V_utils) utils;
@property (T@"ANSettings",&,N,V_settings) settings;
@property (T@"NSMutableDictionary",&,N,V_devices) devices;
@property (T@"NSDictionary",&,N,V_devicesImmutable) devicesImmutable;
@property (T@"NSMutableSet",&,N,V_activelyMaintaining) activelyMaintaining;
@property (T@"NSMutableSet",&,N,V_evictionCandidates) evictionCandidates;
@property (T@"NSMutableDictionary",&,N,V_evictionMap) evictionMap;
@property (T@"<ANSystemUtilsProtocol>",&,N,V_systemUtils) systemUtils;
@property (T@"_TtC20AccessoryInteraction33ANProactiveMaintenanceCoordinator",&,N,V_proactiveCoordinator) proactiveCoordinator;
@property (T@"_TtC20AccessoryInteraction20ANBOMScanCoordinator",&,N,V_bomScanCoordinator) bomScanCoordinator;
@property (T@"<ANMaintenanceDelegate>",&,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ANMaintenance compactDictionaryForDevices:];
+[ANMaintenance compactSetForUUIDs:];
+[ANMaintenance shortUUIDString:];
```

## Instance methods

```
-[ANMaintenance dumpState];
-[ANMaintenance handleEvent:];
-[ANMaintenance setDevices:];
-[ANMaintenance setSettings:];
-[ANMaintenance init];
-[ANMaintenance settings];
-[ANMaintenance dealloc];
-[ANMaintenance getQuarterHour];
-[ANMaintenance getMachContinuousTime];
-[ANMaintenance setLoi:];
-[ANMaintenance devices];
-[ANMaintenance setDelegate:];
-[ANMaintenance systemUtils];
-[ANMaintenance utils];
-[ANMaintenance delegate];
-[ANMaintenance submitMaintenanceTimerPowerLog:actualInterval:];
-[ANMaintenance setSystemUtils:];
-[ANMaintenance getDeltaSecondsFromMachTime:];
-[ANMaintenance isStandardMaintenanceForDevice:];
-[ANMaintenance logFaultIfConsistencyCheckFails];
-[ANMaintenance setEvictionMap:];
-[ANMaintenance willDiscoverySpanTheQuarterHour];
-[ANMaintenance activelyMaintaining];
-[ANMaintenance addScanResultAtDate:address:reason:uuid:];
-[ANMaintenance atQuarterHour];
-[ANMaintenance bomScanCoordinator];
-[ANMaintenance btOn];
-[ANMaintenance checkDoneOnDevice:onCondition:];
-[ANMaintenance checkMaintainableDevices:];
-[ANMaintenance checkProactiveOnDevice:forReason:];
-[ANMaintenance checkSkipAll];
-[ANMaintenance coexStatus];
-[ANMaintenance countDeviceCategories];
-[ANMaintenance createMaintList:];
-[ANMaintenance devicesImmutable];
-[ANMaintenance discoveryComplete];
-[ANMaintenance dutyCycleUpgrade];
-[ANMaintenance evictionCandidates];
-[ANMaintenance evictionMap];
-[ANMaintenance finishMaintainingDevice:withReason:andCategory:];
-[ANMaintenance getAddressForDevice:];
-[ANMaintenance getDeviceForUUID:];
-[ANMaintenance getMaintReasonForDevice:];
-[ANMaintenance helemaintainable];
-[ANMaintenance initWithQueue:systemUtils:utils:settings:];
-[ANMaintenance isActiveForUuid:];
-[ANMaintenance isCoexCritical];
-[ANMaintenance isMaintCoex];
-[ANMaintenance isMaintenanceActive];
-[ANMaintenance isNonHeleMaintenanceActive];
-[ANMaintenance isSameMaintQuarterHourForDevice:];
-[ANMaintenance leashable];
-[ANMaintenance maintState];
-[ANMaintenance maintainAllDevices:];
-[ANMaintenance maintainable];
-[ANMaintenance maintenanceTimerFiredWithInterval:];
-[ANMaintenance performProactiveMaintenanceOnDevice:];
-[ANMaintenance proactiveCoordinator];
-[ANMaintenance pruneScanCacheToQuarterHour];
-[ANMaintenance requestDiscovery];
-[ANMaintenance restartMaintenanceConnections];
-[ANMaintenance secondsFromLastQuarterHour];
-[ANMaintenance setActivelyMaintaining:];
-[ANMaintenance setBomScanCoordinator:];
-[ANMaintenance setBtOn:];
-[ANMaintenance setCoex:];
-[ANMaintenance setCoexStatus:];
-[ANMaintenance setDevicesImmutable:];
-[ANMaintenance setDutyCycleUpgrade:];
-[ANMaintenance setEvictionCandidates:];
-[ANMaintenance setHelemaintainable:];
-[ANMaintenance setLeashable:];
-[ANMaintenance setMaintState:];
-[ANMaintenance setMaintainable:];
-[ANMaintenance setProactiveCoordinator:];
-[ANMaintenance setUtils:];
-[ANMaintenance shouldAttemptForcedHeleMaintenanceOnDevice:];
-[ANMaintenance shouldSkipAttemptOnDevice:];
-[ANMaintenance startMaintenanceTimer];
-[ANMaintenance stopMaintenanceTimer];
-[ANMaintenance stopOngoingMaint:];
```
