# `SBMedusa1oSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 8 instance variables, 8 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _debugRotationCenter;
B _debugColorRotationRegions;
B _clipRotationRegions;
B _fencesRotation;
d _zoomOutRotationFactor;
d _rotationSlowdownFactor;
Q _millisecondsBetweenResizeSteps;
d _gapSwipeBuffer;
```

## Properties

```
@property (TB,N,V_debugRotationCenter) debugRotationCenter;
@property (TB,N,V_debugColorRotationRegions) debugColorRotationRegions;
@property (TB,N,V_clipRotationRegions) clipRotationRegions;
@property (Td,N,V_zoomOutRotationFactor) zoomOutRotationFactor;
@property (Td,N,V_rotationSlowdownFactor) rotationSlowdownFactor;
@property (TB,N,V_fencesRotation) fencesRotation;
@property (TQ,N,V_millisecondsBetweenResizeSteps) millisecondsBetweenResizeSteps;
@property (Td,N,V_gapSwipeBuffer) gapSwipeBuffer;
```

## Class methods

```
+[SBMedusa1oSettings settingsControllerModule];
```

## Instance methods

```
-[SBMedusa1oSettings setDefaultValues];
-[SBMedusa1oSettings clipRotationRegions];
-[SBMedusa1oSettings debugColorRotationRegions];
-[SBMedusa1oSettings debugRotationCenter];
-[SBMedusa1oSettings fencesRotation];
-[SBMedusa1oSettings gapSwipeBuffer];
-[SBMedusa1oSettings millisecondsBetweenResizeSteps];
-[SBMedusa1oSettings rotationSlowdownFactor];
-[SBMedusa1oSettings setClipRotationRegions:];
-[SBMedusa1oSettings setDebugColorRotationRegions:];
-[SBMedusa1oSettings setDebugRotationCenter:];
-[SBMedusa1oSettings setFencesRotation:];
-[SBMedusa1oSettings setGapSwipeBuffer:];
-[SBMedusa1oSettings setMillisecondsBetweenResizeSteps:];
-[SBMedusa1oSettings setRotationSlowdownFactor:];
-[SBMedusa1oSettings setZoomOutRotationFactor:];
-[SBMedusa1oSettings zoomOutRotationFactor];
```
