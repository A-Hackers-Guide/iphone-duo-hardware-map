# `CBColorPolicyFilter`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBFilter`
- 23 instance variables, 6 properties, 28 instance methods, 0 class methods

## Instance variables

```
[20f] _mitigationThrE;
[20f] _mitigationThrL;
Q _mitigationThrSize;
[20f] _ceMitigationThrE;
[20f] _ceMitigationThrL;
i _ceMitigationThrSize;
^[47f] _mitigatedStrengthLUT;
@"CBCEModule" _ceModule;
B _ceEnabled;
f _ceConfidenceThreshold;
i _ceModelID;
@"CBStack" _alsStack;
Q _stackLength;
Q _stackCurrentCount;
Q _consecutiveNonMitgatedCount;
B _mitigationUsedYet;
@"NSNumber" _serviceID;
B _isColorMitigationTriggered;
B _colorAdaptationActive;
B _useAngleDrivenMitigation;
f _filteredStrength;
f _currentAngleDegrees;
@"<CBALSEventProtocol>" _filteredALS;
```

## Properties

```
@property (TB,V_isColorMitigationTriggered) isColorMitigationTriggered;
@property (Tf,V_filteredStrength) filteredStrength;
@property (TB,N,V_colorAdaptationActive) colorAdaptationActive;
@property (T@"<CBALSEventProtocol>",R,N,V_filteredALS) filteredALS;
@property (TB,V_useAngleDrivenMitigation) useAngleDrivenMitigation;
@property (Tf,N,V_currentAngleDegrees) currentAngleDegrees;
```

## Instance methods

```
-[CBColorPolicyFilter copyPropertyForKey:];
-[CBColorPolicyFilter setProperty:forKey:];
-[CBColorPolicyFilter dealloc];
-[CBColorPolicyFilter filterEvent:];
-[CBColorPolicyFilter handleALSEvent:];
-[CBColorPolicyFilter resetFilter];
-[CBColorPolicyFilter initWithID:];
-[CBColorPolicyFilter resetMitigationBoundaryOverride];
-[CBColorPolicyFilter initializeMitigationsForDevice:];
-[CBColorPolicyFilter biLinearInterpBetweenIndices:forPoint1:andPoint2:strengthLUT:luxCount:luxArray:nitsArray:];
-[CBColorPolicyFilter colorAdaptationActive];
-[CBColorPolicyFilter computeBaselineStrengthForLux:andNits:];
-[CBColorPolicyFilter computeBaselineStrengthForLux:andNits:andAngle:];
-[CBColorPolicyFilter currentAngleDegrees];
-[CBColorPolicyFilter filteredALS];
-[CBColorPolicyFilter filteredStrength];
-[CBColorPolicyFilter initWithID:serviceID:];
-[CBColorPolicyFilter isColorMitigationTriggered];
-[CBColorPolicyFilter sampleIsFromCERegion:];
-[CBColorPolicyFilter sampleIsFromMitigatedRegion:];
-[CBColorPolicyFilter setColorAdaptationActive:];
-[CBColorPolicyFilter setCurrentAngleDegrees:];
-[CBColorPolicyFilter setFilteredStrength:];
-[CBColorPolicyFilter setIsColorMitigationTriggered:];
-[CBColorPolicyFilter setModuleObject:];
-[CBColorPolicyFilter setUseAngleDrivenMitigation:];
-[CBColorPolicyFilter shouldMitigateForSample:withLuxThr:NitsThr:andSize:];
-[CBColorPolicyFilter useAngleDrivenMitigation];
```
