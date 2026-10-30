# `AABRear`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"<CBRearALSModuleProtocol>" _rearALSModule;
f _frontALSThreshold;
f _rearALSThreshold;
f _luxRatioThreshold;
@"CBDisplayContext" _context;
B _sensorIsSampling;
B _aodDisabled;
B _propertyDisabled;
B _factorDisabled;
B _otherALSDisabled;
B _grimaldiLuxInUse;
f _nitsRatioThreshold;
f _frontLux;
```

## Properties

```
@property (TB,N,GisPropertyDisabled,V_propertyDisabled) propertyDisabled;
@property (TB,N,GisAODDisabled,V_aodDisabled) aodDisabled;
@property (TB,N,GisFactorDisabled,V_factorDisabled) factorDisabled;
@property (TB,N,GisOtherALSDisabled,V_otherALSDisabled) otherALSDisabled;
@property (Tf,N,GgetFrontLux,V_frontLux) frontLux;
@property (TB,R,N,GisFrontLuxSatisfied) frontLuxSatisfied;
@property (TB,GisGrimaldiLuxInUse,V_grimaldiLuxInUse) grimaldiLuxInUse;
@property (TB,R,N,V_sensorIsSampling) sensorIsSampling;
@property (Tf,R,N,V_nitsRatioThreshold) nitsRatio;
```

## Instance methods

```
-[AABRear stop];
-[AABRear dealloc];
-[AABRear stopSampling];
-[AABRear initWithDisplayContext:];
-[AABRear checkSensorEnablementConditions];
-[AABRear setAodDisabled:];
-[AABRear copyParam:];
-[AABRear getFrontLux];
-[AABRear isAODDisabled];
-[AABRear isFactorDisabled];
-[AABRear isFrontLuxSatisfied];
-[AABRear isGrimaldiLuxInUse];
-[AABRear isOtherALSDisabled];
-[AABRear isPropertyDisabled];
-[AABRear nitsRatio];
-[AABRear sensorIsSampling];
-[AABRear setFactorDisabled:];
-[AABRear setFrontLux:];
-[AABRear setGrimaldiLuxInUse:];
-[AABRear setOtherALSDisabled:];
-[AABRear setPropertyDisabled:];
-[AABRear shouldUseRLux:rLux:inUse:];
```
