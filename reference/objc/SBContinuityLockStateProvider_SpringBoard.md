# `SBContinuityLockStateProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLockStateProviding`
- 0 instance variables, 4 properties, 5 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBContinuityLockStateProvider unlockWithRequest:completion:];
-[SBContinuityLockStateProvider isUIUnlocking];
-[SBContinuityLockStateProvider removeLockStateObserver:];
-[SBContinuityLockStateProvider isUILocked];
-[SBContinuityLockStateProvider addLockStateObserver:];
```
