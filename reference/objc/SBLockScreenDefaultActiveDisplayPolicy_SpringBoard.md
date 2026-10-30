# `SBLockScreenDefaultActiveDisplayPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLockScreenActiveDisplayPolicyProviding`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
@"NSPointerArray" _queue_lockScreenManagers;
@"NSHashTable" _queue_observers;
@"SBLockScreenManager" _queue_overrideActiveLockScreenManager;
```

## Properties

```
@property (T@"SBLockScreenManager",W,N,V_queue_overrideActiveLockScreenManager) overrideActiveLockScreenManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockScreenDefaultActiveDisplayPolicy setOverrideActiveLockScreenManager:];
-[SBLockScreenDefaultActiveDisplayPolicy removeObserver:];
-[SBLockScreenDefaultActiveDisplayPolicy init];
-[SBLockScreenDefaultActiveDisplayPolicy addObserver:];
-[SBLockScreenDefaultActiveDisplayPolicy activeDisplayLockScreenManager];
-[SBLockScreenDefaultActiveDisplayPolicy removeLockScreenManager:];
-[SBLockScreenDefaultActiveDisplayPolicy addLockScreenManager:];
-[SBLockScreenDefaultActiveDisplayPolicy overrideActiveLockScreenManager];
-[SBLockScreenDefaultActiveDisplayPolicy _queue_activeLockScreenManager];
-[SBLockScreenDefaultActiveDisplayPolicy _queue_notifyObserversActiveDisplayChangedWithCurrentLockScreenManager:previousLockScreenManager:];
```
