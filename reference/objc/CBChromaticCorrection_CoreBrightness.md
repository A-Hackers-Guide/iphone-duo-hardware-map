# `CBChromaticCorrection`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBAODProtocol`
- 12 instance variables, 12 properties, 40 instance methods, 0 class methods

## Instance variables

```
B _autoBrightnessIsEnabled;
B _aodIsOn;
B _isEnabled;
@"<CBChromaticCorrectionPolicy>" _policy;
@"CBLuxRamp" _ramp;
f _trustedLux;
B _aodRampHandoffPending;
B _referenceModeActive;
B _isExternallyClocked;
f _nits;
@"<CBChromaticCorectionParamsProtocol>" _params;
^? _currentTime;
```

## Properties

```
@property (T@"<CBChromaticCorectionParamsProtocol>",R,V_params) params;
@property (Tf,V_nits) nits;
@property (TB) enabled;
@property (TB,N,V_referenceModeActive) referenceModeActive;
@property (TB,V_isExternallyClocked) isExternallyClocked;
@property (Tf) trustedLux;
@property (T^?,V_currentTime) currentTime;
@property (Tf,R) aodRampDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBChromaticCorrection setCurrentTime:];
-[CBChromaticCorrection nits];
-[CBChromaticCorrection copyPropertyForKey:];
-[CBChromaticCorrection setProperty:forKey:];
-[CBChromaticCorrection setNits:];
-[CBChromaticCorrection params];
-[CBChromaticCorrection enabled];
-[CBChromaticCorrection stop];
-[CBChromaticCorrection dealloc];
-[CBChromaticCorrection currentTime];
-[CBChromaticCorrection start];
-[CBChromaticCorrection updateRamp];
-[CBChromaticCorrection setLux:];
-[CBChromaticCorrection handleNotificationForKey:withProperty:];
-[CBChromaticCorrection currentStrength];
-[CBChromaticCorrection setEnabled:];
-[CBChromaticCorrection description];
-[CBChromaticCorrection handleAODStateUpdate:transitionTime:context:];
-[CBChromaticCorrection handleAutoBrightnessStateUpdate:];
-[CBChromaticCorrection lux];
-[CBChromaticCorrection copyPropertyForKey:withParameter:];
-[CBChromaticCorrection rampDuration];
-[CBChromaticCorrection aodRampDuration];
-[CBChromaticCorrection isInActiveRange];
-[CBChromaticCorrection handleLuxUpdate:];
-[CBChromaticCorrection handleRampResult:];
-[CBChromaticCorrection initWithBacklightParams:andPolicy:andRamp:];
-[CBChromaticCorrection isExternallyClocked];
-[CBChromaticCorrection luxAdjustedByInternalPolicies:];
-[CBChromaticCorrection nitsAreInActiveRange:];
-[CBChromaticCorrection rampIsRunning];
-[CBChromaticCorrection referenceModeActive];
-[CBChromaticCorrection setIsExternallyClocked:];
-[CBChromaticCorrection setReferenceModeActive:];
-[CBChromaticCorrection setTrustedLux:];
-[CBChromaticCorrection shouldRampForIncomingLux:];
-[CBChromaticCorrection shouldRampFromStartLux:toTargetLux:];
-[CBChromaticCorrection targetLux];
-[CBChromaticCorrection trustedLux];
-[CBChromaticCorrection updateRampWithProgress:];
```
