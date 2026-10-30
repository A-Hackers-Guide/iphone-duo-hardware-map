# `CBLowPowerMode`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PMPowerMitigationsObserver`, `CBLowPowerModeObservable`
- 6 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSMutableSet" _observers;
{map<void *, void (^)(PMMitigationLevel), std::less<void *>, std::allocator<std::pair<void *const, void (^)(PMMitigationLevel)>>>="__tree_"{__tree<std::__value_type<void *, void (^)(PMMitigationLevel)>, std::__map_value_compare<void *, std::pair<void *const, void (^)(PMMitigationLevel)>, std::less<void *>>, std::allocator<std::pair<void *const, void (^)(PMMitigationLevel)>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _notificationBlocks;
B _started;
q lastLevel;
@"<PMPowerMitigationsObservable>" _observable;
```

## Properties

```
@property (T@"<PMPowerMitigationsObservable>",&,V_observable) observable;
@property (TB,R,V_started) started;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,VlastLevel) lastLevel;
@property (TB,R) isAmbrosiaLevel;
```

## Class methods

```
+[CBLowPowerMode levelToString:];
```

## Instance methods

```
-[CBLowPowerMode init];
-[CBLowPowerMode stop];
-[CBLowPowerMode dealloc];
-[CBLowPowerMode started];
-[CBLowPowerMode setObservable:];
-[CBLowPowerMode start];
-[CBLowPowerMode observable];
-[CBLowPowerMode registerObserver:];
-[CBLowPowerMode publishUpdate:];
-[CBLowPowerMode initWithObservable:];
-[CBLowPowerMode isAmbrosiaLevel];
-[CBLowPowerMode deregisterNotificationBlockForCaller:];
-[CBLowPowerMode deregisterObserver:];
-[CBLowPowerMode didChangeToMitigations:withSessionInfo:];
-[CBLowPowerMode forceMitigationLevel:];
-[CBLowPowerMode lastLevel];
-[CBLowPowerMode refreshSystemState];
-[CBLowPowerMode registerNotificationBlock:forCaller:];
-[CBLowPowerMode setLastLevel:];
```
