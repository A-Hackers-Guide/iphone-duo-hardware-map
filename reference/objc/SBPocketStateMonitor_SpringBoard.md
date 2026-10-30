# `SBPocketStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CMPocketStateDelegate`
- 4 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"CMPocketStateManager" _pocketStateManager;
q _pocketState;
@"NSHashTable" _observers;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
```

## Properties

```
@property (Tq,R,N,V_pocketState) pocketState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBPocketStateMonitor sharedInstance];
```

## Instance methods

```
-[SBPocketStateMonitor removeObserver:];
-[SBPocketStateMonitor init];
-[SBPocketStateMonitor dealloc];
-[SBPocketStateMonitor addObserver:];
-[SBPocketStateMonitor pocketStateManager:didUpdateState:];
-[SBPocketStateMonitor pocketState];
-[SBPocketStateMonitor initWithCMPocketStateManager:calloutQueue:];
```
