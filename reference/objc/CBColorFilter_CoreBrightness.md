# `CBColorFilter`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBFilter`
- Protocols: `CBHIDServiceProtocol`
- 9 instance variables, 10 properties, 38 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _services;
@"NSMutableArray" _validServices;
@"NSMutableDictionary" _arrivedEvents;
@"NSArray" _activeALSServices;
I _panelPlacement;
Q _sensorPolicy;
Q _mode;
@"CBColorSample" _sample;
@"<CBALSSelectionPolicyProtocol>" _selectionPolicy;
```

## Properties

```
@property (TQ,N,V_sensorPolicy) sensorPolicy;
@property (TQ,N,V_mode) mode;
@property (T@"CBColorSample",R,V_sample) sample;
@property (T@"<CBALSSelectionPolicyProtocol>",&,N,V_selectionPolicy) selectionPolicy;
@property (T@"NSArray",R,C,N,V_activeALSServices) activeALSServices;
@property (TB,R) allValidALSEventsArrived;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBColorFilter calculateCCTForChromaticity:];
+[CBColorFilter calculateCCTForTristimulus:];
+[CBColorFilter calculateTristimulusForChromaticity:andLux:];
```

## Instance methods

```
-[CBColorFilter handleEvent:];
-[CBColorFilter addHIDServiceClient:];
-[CBColorFilter humanReadableModeRepresentation:];
-[CBColorFilter removeHIDServiceClient:];
-[CBColorFilter sensorPolicy];
-[CBColorFilter setSensorPolicy:];
-[CBColorFilter newColorSampleLogWeightedForSamples:];
-[CBColorFilter ALSServiceConformsToPolicy:];
-[CBColorFilter init];
-[CBColorFilter activeALSServices];
-[CBColorFilter hasExtFrontSensor];
-[CBColorFilter dealloc];
-[CBColorFilter allValidALSEventsArrived];
-[CBColorFilter hasExtRearSensor];
-[CBColorFilter reportSampleUpdate];
-[CBColorFilter initWithIdentifier:panelPlacement:];
-[CBColorFilter resetEvents];
-[CBColorFilter selectedServices];
-[CBColorFilter acknowledgeEvent:];
-[CBColorFilter setMode:];
-[CBColorFilter filterEvent:];
-[CBColorFilter copyHumanReadablePolicyRepresentation:];
-[CBColorFilter isRearALS:];
-[CBColorFilter forceSampleUpdate];
-[CBColorFilter mode];
-[CBColorFilter newColorSampleLinearWeightedForServices:];
-[CBColorFilter newColorSampleConditionWeightedForServices:];
-[CBColorFilter updateValidServices];
-[CBColorFilter setSelectionPolicy:];
-[CBColorFilter evaluatedFilterMode];
-[CBColorFilter selectionPolicy];
-[CBColorFilter isFrontALS:];
-[CBColorFilter newColorSampleWinnerTakesAllForServices:];
-[CBColorFilter initWithIdentifier:];
-[CBColorFilter newColorSampleLogWeightedForServices:];
-[CBColorFilter updateSample];
-[CBColorFilter newColorSampleLinearWeightedForSamples:];
-[CBColorFilter sample];
```
