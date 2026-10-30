# `SBIdleTimerProxy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBIdleTimerBase`
- Protocols: `SBIdleTimerObserving`
- 1 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"<SBIdleTimer>" _sourceTimer;
```

## Properties

```
@property (T@"<SBIdleTimer>",&,N,V_sourceTimer) sourceTimer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBIdleTimerProxy disabledIdleTimerProxy];
```

## Instance methods

```
-[SBIdleTimerProxy isActivated];
-[SBIdleTimerProxy setActivated:];
-[SBIdleTimerProxy sourceTimer];
-[SBIdleTimerProxy idleTimerDidRefresh:];
-[SBIdleTimerProxy _logExpirationTimeout:];
-[SBIdleTimerProxy reset];
-[SBIdleTimerProxy isDisabled];
-[SBIdleTimerProxy idleTimerDidExpire:];
-[SBIdleTimerProxy idleTimerDidResetForUserAttention:];
-[SBIdleTimerProxy idleTimerDidWarn:];
-[SBIdleTimerProxy setSourceTimer:];
-[SBIdleTimerProxy initWithIdleTimerSource:];
```
