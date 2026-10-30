# `SBIdleTimerSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _disableIdleTimer;
B _overrideIdleTimer;
d _unlockedIdleTimerCap;
d _durationInterval;
d _warnInterval;
d _samplingStartBeforeFirstTimeout;
```

## Properties

```
@property (TB,N,V_disableIdleTimer) disableIdleTimer;
@property (Td,N,V_unlockedIdleTimerCap) unlockedIdleTimerCap;
@property (TB,N,V_overrideIdleTimer) overrideIdleTimer;
@property (Td,N,V_durationInterval) durationInterval;
@property (Td,N,V_warnInterval) warnInterval;
@property (Td,N,V_samplingStartBeforeFirstTimeout) samplingStartBeforeFirstTimeout;
```

## Class methods

```
+[SBIdleTimerSettings settingsControllerModule];
```

## Instance methods

```
-[SBIdleTimerSettings samplingStartBeforeFirstTimeout];
-[SBIdleTimerSettings setWarnInterval:];
-[SBIdleTimerSettings setSamplingStartBeforeFirstTimeout:];
-[SBIdleTimerSettings warnInterval];
-[SBIdleTimerSettings setDefaultValues];
-[SBIdleTimerSettings durationInterval];
-[SBIdleTimerSettings setDurationInterval:];
-[SBIdleTimerSettings disableIdleTimer];
-[SBIdleTimerSettings overrideIdleTimer];
-[SBIdleTimerSettings setDisableIdleTimer:];
-[SBIdleTimerSettings setOverrideIdleTimer:];
-[SBIdleTimerSettings setUnlockedIdleTimerCap:];
-[SBIdleTimerSettings unlockedIdleTimerCap];
```
