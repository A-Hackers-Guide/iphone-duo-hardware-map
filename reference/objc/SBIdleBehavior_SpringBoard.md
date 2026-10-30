# `SBIdleBehavior`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFIdleTimerBehaviorProviding`
- 2 instance variables, 11 properties, 6 instance methods, 0 class methods

## Instance variables

```
q _duration;
q _warnMode;
```

## Properties

```
@property (Tq,R,N,V_duration) duration;
@property (Tq,R,N,V_warnMode) warnMode;
@property (Tq,R,N) idleTimerDuration;
@property (Tq,R,N) idleTimerMode;
@property (Tq,R,N) idleWarnMode;
@property (Td,?,R,N) customIdleExpirationTimeout;
@property (Td,?,R,N) customIdleWarningTimeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleBehavior idleTimerDuration];
-[SBIdleBehavior duration];
-[SBIdleBehavior idleTimerMode];
-[SBIdleBehavior idleWarnMode];
-[SBIdleBehavior initWithDuration:warnMode:];
-[SBIdleBehavior warnMode];
```
