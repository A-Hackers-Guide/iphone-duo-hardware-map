# `CLReductiveFilterOptions`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
Q _beaconType;
d _transmitPower;
d _biasRateInMeasurement;
d _applyRangeEstimation;
```

## Properties

```
@property (Td,N,V_biasRateInMeasurement) biasRateInMeasurement;
@property (Td,N,V_applyRangeEstimation) applyRangeEstimation;
@property (TQ,R,N,V_beaconType) beaconType;
@property (Td,R,N,V_transmitPower) transmitPower;
```

## Instance methods

```
-[CLReductiveFilterOptions init];
-[CLReductiveFilterOptions applyRangeEstimation];
-[CLReductiveFilterOptions beaconType];
-[CLReductiveFilterOptions biasRateInMeasurement];
-[CLReductiveFilterOptions initWithBeaconType:];
-[CLReductiveFilterOptions initWithBeaconType:transmitPower:];
-[CLReductiveFilterOptions setApplyRangeEstimation:];
-[CLReductiveFilterOptions setBiasRateInMeasurement:];
-[CLReductiveFilterOptions transmitPower];
```
