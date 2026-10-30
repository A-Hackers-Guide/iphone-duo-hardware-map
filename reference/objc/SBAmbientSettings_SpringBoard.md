# `SBAmbientSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 5 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _enableSuppression;
q _idleTimerDuration;
q _idleTimerWarnMode;
q _suppressedIdleTimerDuration;
q _suppressedIdleTimerWarnMode;
```

## Properties

```
@property (Tq,N,V_idleTimerDuration) idleTimerDuration;
@property (Tq,N,V_idleTimerWarnMode) idleTimerWarnMode;
@property (TB,N,V_enableSuppression) enableSuppression;
@property (Tq,N,V_suppressedIdleTimerDuration) suppressedIdleTimerDuration;
@property (Tq,N,V_suppressedIdleTimerWarnMode) suppressedIdleTimerWarnMode;
```

## Class methods

```
+[SBAmbientSettings settingsControllerModule];
```

## Instance methods

```
-[SBAmbientSettings idleTimerDuration];
-[SBAmbientSettings setDefaultValues];
-[SBAmbientSettings setIdleTimerDuration:];
-[SBAmbientSettings setSuppressedIdleTimerWarnMode:];
-[SBAmbientSettings setSuppressedIdleTimerDuration:];
-[SBAmbientSettings enableSuppression];
-[SBAmbientSettings idleTimerWarnMode];
-[SBAmbientSettings setEnableSuppression:];
-[SBAmbientSettings setIdleTimerWarnMode:];
-[SBAmbientSettings suppressedIdleTimerDuration];
-[SBAmbientSettings suppressedIdleTimerWarnMode];
```
