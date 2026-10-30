# `CBDisplayALSSamplingPolicy`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
I _panelPlacement;
B _rearActive;
B _displayOn;
B _aodMode;
f _rearSensorInterval;
f _angleThreshold;
f _angleHysteresis;
```

## Properties

```
@property (TB,N,V_displayOn) displayOn;
@property (TB,N,V_aodMode) aodMode;
@property (Tf,R,N,V_rearSensorInterval) rearSensorInterval;
@property (Tf,N,V_angleThreshold) angleThreshold;
@property (Tf,N,V_angleHysteresis) angleHysteresis;
@property (TB,R,N,V_rearActive) rearActive;
```

## Instance methods

```
-[CBDisplayALSSamplingPolicy setDisplayOn:];
-[CBDisplayALSSamplingPolicy displayOn];
-[CBDisplayALSSamplingPolicy angleHysteresis];
-[CBDisplayALSSamplingPolicy aodMode];
-[CBDisplayALSSamplingPolicy adjustedInterval:forSensorPlacement:sensorOrientation:];
-[CBDisplayALSSamplingPolicy angleThreshold];
-[CBDisplayALSSamplingPolicy initWithPanelPlacement:];
-[CBDisplayALSSamplingPolicy isDesignatedAODSensor:orientation:];
-[CBDisplayALSSamplingPolicy rearActive];
-[CBDisplayALSSamplingPolicy rearSensorInterval];
-[CBDisplayALSSamplingPolicy setAngleHysteresis:];
-[CBDisplayALSSamplingPolicy setAngleThreshold:];
-[CBDisplayALSSamplingPolicy setAodMode:];
-[CBDisplayALSSamplingPolicy updateAngle:];
```
