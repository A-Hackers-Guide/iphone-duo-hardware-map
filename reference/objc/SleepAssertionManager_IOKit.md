# `SleepAssertionManager`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`](../userland/System__Library__CoreAccessories__PlugIns__Platform__IOKit.platform__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 36 instance methods, 1 class methods

## Instance variables

```
B _sleepAssertionHeld;
B _eaSleepAssertionHeld;
B _applePencilSleepAssertionHeld;
B _mfi4SleepAssertionHeld;
I _eaSleepAssertionID;
I _applePencilSleepAssertionID;
I _mfi4SleepAssertionID;
@"NSMutableDictionary" _assertions;
@"NSObject<OS_dispatch_queue>" _sleepAssertionsLock;
@"NSObject<OS_dispatch_source>" _applePencilSleepAssertionTimer;
@"NSObject<OS_dispatch_queue>" _applePencilSleepAssertionTimerQueue;
@"NSObject<OS_dispatch_source>" _mfi4SleepAssertionTimer;
@"NSObject<OS_dispatch_queue>" _mfi4SleepAssertionTimerQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_assertions) assertions;
@property (TB,N,V_sleepAssertionHeld) sleepAssertionHeld;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_sleepAssertionsLock) sleepAssertionsLock;
@property (TB,N,V_eaSleepAssertionHeld) eaSleepAssertionHeld;
@property (TI,N,V_eaSleepAssertionID) eaSleepAssertionID;
@property (TB,N,V_applePencilSleepAssertionHeld) applePencilSleepAssertionHeld;
@property (TI,N,V_applePencilSleepAssertionID) applePencilSleepAssertionID;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_applePencilSleepAssertionTimer) applePencilSleepAssertionTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_applePencilSleepAssertionTimerQueue) applePencilSleepAssertionTimerQueue;
@property (TB,N,V_mfi4SleepAssertionHeld) mfi4SleepAssertionHeld;
@property (TI,N,V_mfi4SleepAssertionID) mfi4SleepAssertionID;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_mfi4SleepAssertionTimer) mfi4SleepAssertionTimer;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_mfi4SleepAssertionTimerQueue) mfi4SleepAssertionTimerQueue;
```

## Class methods

```
+[SleepAssertionManager sharedManager];
```

## Instance methods

```
-[SleepAssertionManager setAssertions:];
-[SleepAssertionManager init];
-[SleepAssertionManager dealloc];
-[SleepAssertionManager assertions];
-[SleepAssertionManager removeApplePencilSleepAssertion];
-[SleepAssertionManager createApplePencilSleepAssertion];
-[SleepAssertionManager setApplePencilSleepAssertionID:];
-[SleepAssertionManager applePencilSleepAssertionHeld];
-[SleepAssertionManager applePencilSleepAssertionID];
-[SleepAssertionManager applePencilSleepAssertionTimer];
-[SleepAssertionManager applePencilSleepAssertionTimerQueue];
-[SleepAssertionManager createEASleepAssertion];
-[SleepAssertionManager createMFi4SleepAssertion];
-[SleepAssertionManager createSleepAssertionForUUID:];
-[SleepAssertionManager destroySleepAssertionForUUID:];
-[SleepAssertionManager eaSleepAssertionHeld];
-[SleepAssertionManager eaSleepAssertionID];
-[SleepAssertionManager mfi4SleepAssertionHeld];
-[SleepAssertionManager mfi4SleepAssertionID];
-[SleepAssertionManager mfi4SleepAssertionTimer];
-[SleepAssertionManager mfi4SleepAssertionTimerQueue];
-[SleepAssertionManager removeEASleepAssertion];
-[SleepAssertionManager removeMFi4SleepAssertion];
-[SleepAssertionManager setApplePencilSleepAssertionHeld:];
-[SleepAssertionManager setApplePencilSleepAssertionTimer:];
-[SleepAssertionManager setApplePencilSleepAssertionTimerQueue:];
-[SleepAssertionManager setEaSleepAssertionHeld:];
-[SleepAssertionManager setEaSleepAssertionID:];
-[SleepAssertionManager setMfi4SleepAssertionHeld:];
-[SleepAssertionManager setMfi4SleepAssertionID:];
-[SleepAssertionManager setMfi4SleepAssertionTimer:];
-[SleepAssertionManager setMfi4SleepAssertionTimerQueue:];
-[SleepAssertionManager setSleepAssertionHeld:];
-[SleepAssertionManager setSleepAssertionsLock:];
-[SleepAssertionManager sleepAssertionHeld];
-[SleepAssertionManager sleepAssertionsLock];
```
