# `SBDoubleClickSleepWakeHardwareButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSleepWakeHardwareButtonInteraction`
- 2 instance variables, 2 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSSet" _proxLockAssertions;
@"SBProximitySensorCoordinator" _proximitySensorCoordinator;
```

## Properties

```
@property (T@"NSSet",C,N,V_proxLockAssertions) proxLockAssertions;
@property (T@"SBProximitySensorCoordinator",&,N,V_proximitySensorCoordinator) proximitySensorCoordinator;
```

## Instance methods

```
-[SBDoubleClickSleepWakeHardwareButtonInteraction consumeInitialPressDown];
-[SBDoubleClickSleepWakeHardwareButtonInteraction _suspendProx];
-[SBDoubleClickSleepWakeHardwareButtonInteraction consumeInitialPressUp];
-[SBDoubleClickSleepWakeHardwareButtonInteraction setProximitySensorCoordinator:];
-[SBDoubleClickSleepWakeHardwareButtonInteraction observeFinalPressUp];
-[SBDoubleClickSleepWakeHardwareButtonInteraction _resumeProxAfterMultiplePressIntervalForReason:];
-[SBDoubleClickSleepWakeHardwareButtonInteraction _resumeProxForReason:];
-[SBDoubleClickSleepWakeHardwareButtonInteraction _performSleep];
-[SBDoubleClickSleepWakeHardwareButtonInteraction _performWake];
-[SBDoubleClickSleepWakeHardwareButtonInteraction initWithProximitySensorCoordinator:];
-[SBDoubleClickSleepWakeHardwareButtonInteraction proxLockAssertions];
-[SBDoubleClickSleepWakeHardwareButtonInteraction _cancelPreviousResumeProxRequests];
-[SBDoubleClickSleepWakeHardwareButtonInteraction consumeSecondPressDown];
-[SBDoubleClickSleepWakeHardwareButtonInteraction observeSinglePressDidFail];
-[SBDoubleClickSleepWakeHardwareButtonInteraction setProxLockAssertions:];
-[SBDoubleClickSleepWakeHardwareButtonInteraction proximitySensorCoordinator];
```
