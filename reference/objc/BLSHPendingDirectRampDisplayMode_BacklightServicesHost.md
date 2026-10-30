# `BLSHPendingDirectRampDisplayMode`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHPendingTwoPhaseUpdateDisplayMode`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _readyToStart;
q _rampBeginDisplayMode;
d _duration;
```

## Properties

```
@property (Tq,R,V_rampBeginDisplayMode) rampBeginDisplayMode;
@property (TB,GisReadyToStart,V_readyToStart) readyToStart;
@property (Td,V_duration) duration;
```

## Instance methods

```
-[BLSHPendingDirectRampDisplayMode isDirectRamp];
-[BLSHPendingDirectRampDisplayMode rampOperation];
-[BLSHPendingDirectRampDisplayMode isReadyToStart];
-[BLSHPendingDirectRampDisplayMode updateOperation];
-[BLSHPendingDirectRampDisplayMode initWithRampBeginDisplayMode:targetDisplayMode:];
-[BLSHPendingDirectRampDisplayMode rampBeginDisplayMode];
-[BLSHPendingDirectRampDisplayMode setReadyToStart:];
-[BLSHPendingDirectRampDisplayMode duration];
-[BLSHPendingDirectRampDisplayMode description];
-[BLSHPendingDirectRampDisplayMode setDuration:];
```
