# `BLSHBacklightStateMachineEventPerforming` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BLSHBacklightHostObservable_Private`
- 0 instance variables, 6 properties, 11 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisTransitioning) transitioning;
@property (TQ,R,N) backlightStateChangeTimestamp;
@property (T@"NSString",R,C,N) backlightStateDescription;
@property (T@"<BLSHBacklightHostObserving>",W,N) performerDelegate;
@property (TB,N) safeToUnblank;
@property (TB,N,GisAlwaysOnSuppressed) alwaysOnSuppressed;
```

## Instance methods

```
-[BLSHBacklightStateMachineEventPerforming prewarmEvent:];
-[BLSHBacklightStateMachineEventPerforming backlightStateChangeTimestamp];
-[BLSHBacklightStateMachineEventPerforming isTransitioning];
-[BLSHBacklightStateMachineEventPerforming backlightStateDescription];
-[BLSHBacklightStateMachineEventPerforming setSafeToUnblank:];
-[BLSHBacklightStateMachineEventPerforming performEvent:];
-[BLSHBacklightStateMachineEventPerforming performerDelegate];
-[BLSHBacklightStateMachineEventPerforming setAlwaysOnSuppressed:];
-[BLSHBacklightStateMachineEventPerforming isAlwaysOnSuppressed];
-[BLSHBacklightStateMachineEventPerforming safeToUnblank];
-[BLSHBacklightStateMachineEventPerforming setPerformerDelegate:];
```
