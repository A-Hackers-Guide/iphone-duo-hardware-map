# `SBDoNotDisturbStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DNDStateUpdateListener`
- 4 instance variables, 5 properties, 6 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSHashTable" _lock_observers;
@"DNDState" _lock_state;
@"DNDStateService" _stateService;
```

## Properties

```
@property (T@"DNDState",R,C,N) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBDoNotDisturbStateMonitor sharedInstance];
```

## Instance methods

```
-[SBDoNotDisturbStateMonitor stateService:didReceiveDoNotDisturbStateUpdate:];
-[SBDoNotDisturbStateMonitor removeObserver:];
-[SBDoNotDisturbStateMonitor init];
-[SBDoNotDisturbStateMonitor addObserver:];
-[SBDoNotDisturbStateMonitor state];
-[SBDoNotDisturbStateMonitor _noteNewDNDState:];
```
