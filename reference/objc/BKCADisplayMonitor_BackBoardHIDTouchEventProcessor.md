# `BKCADisplayMonitor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 10 instance variables, 4 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"<BKCADisplayProvider>" _displayProvider;
@"NSObject<OS_os_log>" _log;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _displayLock;
@"BSCompoundAssertion" _displayLock_observerAssertion;
@"BSCompoundAssertion" _displayLock_diffObserverAssertion;
@"NSMutableDictionary" _displayLock_displayUUIDKeyToImmutableCADisplay;
@"NSMutableDictionary" _displayLock_displayIndexToDisplayUUID;
B _displayLock_isInvalid;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _filterPredicateLock;
@? _filterPredicateLock_displayFilterPredicate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKCADisplayMonitor sharedDisplayProvider];
```

## Instance methods

```
-[BKCADisplayMonitor init];
-[BKCADisplayMonitor dealloc];
-[BKCADisplayMonitor initWithLog:];
-[BKCADisplayMonitor addObserver:];
-[BKCADisplayMonitor invalidate];
-[BKCADisplayMonitor _filterDisplays:usingPredicate:];
-[BKCADisplayMonitor _filterDisplay:usingPredicate:];
-[BKCADisplayMonitor _immutableDisplays];
-[BKCADisplayMonitor addDiffObserver:];
-[BKCADisplayMonitor displayUUIDIsActive:];
-[BKCADisplayMonitor initWithDisplayProvider:log:filterPredicate:];
-[BKCADisplayMonitor initWithLog:filterPredicate:];
-[BKCADisplayMonitor reevaluateActiveDisplaysWithReason:];
-[BKCADisplayMonitor setDisplayFilterPredicate:];
```
