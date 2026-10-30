# `CBAODThresholdModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBHIDServiceProtocol`
- 20 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
f _minNits;
f _maxNits;
f _Pthreshold_dim;
f _Pthreshold_dim_lowLux;
f _Pthreshold_brighten;
f _Pthreshold_brighten_lowLux;
f _AP_Pthreshold_dim;
f _AP_Pthreshold_brighten;
B _brightenLuxThresholdOverriden;
B _dimLuxThresholdOverriden;
f _currentBrightness;
f _currentLux;
f _currentBrightnessLimit;
f _lastPushedBrightenLuxThreshold;
f _lastPushedDimLuxThreshold;
B _useDynamicThresholds;
@"NSMutableArray" _alsServiceClients;
f _brightenLuxThreshold;
f _dimLuxThreshold;
@"CBAODState" _AODState;
```

## Properties

```
@property (Tf,V_brightenLuxThreshold) brightenLuxThreshold;
@property (Tf,V_dimLuxThreshold) dimLuxThreshold;
@property (T@"CBAODState",R,V_AODState) AODState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBAODThresholdModule copyPropertyForKey:];
-[CBAODThresholdModule sendNotificationForKey:andValue:];
-[CBAODThresholdModule setProperty:forKey:];
-[CBAODThresholdModule handleEvent:];
-[CBAODThresholdModule addHIDServiceClient:];
-[CBAODThresholdModule AODState];
-[CBAODThresholdModule removeHIDServiceClient:];
-[CBAODThresholdModule dealloc];
-[CBAODThresholdModule checkBootArgsConfiguration];
-[CBAODThresholdModule dimLuxThreshold];
-[CBAODThresholdModule applyFixedLuxThresholdsForLux:dimTarget:brightenTarget:];
-[CBAODThresholdModule brightenLuxThreshold];
-[CBAODThresholdModule copyPdeltaThresholdsForLux:];
-[CBAODThresholdModule initWithQueue:displayID:andAODState:];
-[CBAODThresholdModule reevaluateALSThresholds];
-[CBAODThresholdModule resetPushedThresholds];
-[CBAODThresholdModule setBrightenLuxThreshold:];
-[CBAODThresholdModule setDimLuxThreshold:];
-[CBAODThresholdModule thresholdsCrossedForLux:];
-[CBAODThresholdModule updateALSThresholdsWithBrightness:brightnessLimit:lux:];
```
