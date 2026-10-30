# `SBIdleTimerBehavior`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFIdleTimerBehaviorProviding`, `BSDescriptionProviding`, `BSDescriptionStreamable`
- 5 instance variables, 9 properties, 14 instance methods, 6 class methods

## Instance variables

```
q _idleWarnMode;
q _idleTimerMode;
q _idleTimerDuration;
d _customIdleWarningTimeout;
d _customIdleExpirationTimeout;
```

## Properties

```
@property (Tq,R,N,V_idleTimerDuration) idleTimerDuration;
@property (Tq,R,N,V_idleTimerMode) idleTimerMode;
@property (Tq,R,N,V_idleWarnMode) idleWarnMode;
@property (Td,?,R,N,V_customIdleExpirationTimeout) customIdleExpirationTimeout;
@property (Td,?,R,N,V_customIdleWarningTimeout) customIdleWarningTimeout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBIdleTimerBehavior defaultBehavior];
+[SBIdleTimerBehavior autoLockBehavior];
+[SBIdleTimerBehavior behaviorForBehaviorProvider:];
+[SBIdleTimerBehavior behaviorWithDuration:mode:warnMode:];
+[SBIdleTimerBehavior disabledBehavior];
+[SBIdleTimerBehavior lockScreenBehavior];
```

## Instance methods

```
-[SBIdleTimerBehavior succinctDescriptionBuilder];
-[SBIdleTimerBehavior appendDescriptionToFormatter:];
-[SBIdleTimerBehavior customIdleWarningTimeout];
-[SBIdleTimerBehavior idleTimerDuration];
-[SBIdleTimerBehavior descriptionWithMultilinePrefix:];
-[SBIdleTimerBehavior succinctDescription];
-[SBIdleTimerBehavior customIdleExpirationTimeout];
-[SBIdleTimerBehavior _initWithBehaviorProvider:];
-[SBIdleTimerBehavior description];
-[SBIdleTimerBehavior idleTimerMode];
-[SBIdleTimerBehavior _initWithDuration:mode:warnMode:];
-[SBIdleTimerBehavior idleWarnMode];
-[SBIdleTimerBehavior _appendInnerDescriptionToFormatter:];
-[SBIdleTimerBehavior descriptionBuilderWithMultilinePrefix:];
```
