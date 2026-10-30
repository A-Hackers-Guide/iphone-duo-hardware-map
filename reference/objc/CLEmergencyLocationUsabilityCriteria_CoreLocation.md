# `CLEmergencyLocationUsabilityCriteria`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _vuncCheckRequiredForUsability;
B _altitudeStitchingEnabled;
I _minUsableIntegrity;
d _maxUsableAge;
d _maxUsableHunc;
```

## Properties

```
@property (TB,N,V_vuncCheckRequiredForUsability) vuncCheckRequiredForUsability;
@property (TB,N,V_altitudeStitchingEnabled) altitudeStitchingEnabled;
@property (Td,N,V_maxUsableAge) maxUsableAge;
@property (Td,N,V_maxUsableHunc) maxUsableHunc;
@property (TI,N,V_minUsableIntegrity) minUsableIntegrity;
```

## Instance methods

```
-[CLEmergencyLocationUsabilityCriteria init];
-[CLEmergencyLocationUsabilityCriteria altitudeStitchingEnabled];
-[CLEmergencyLocationUsabilityCriteria maxUsableAge];
-[CLEmergencyLocationUsabilityCriteria maxUsableHunc];
-[CLEmergencyLocationUsabilityCriteria minUsableIntegrity];
-[CLEmergencyLocationUsabilityCriteria printUsabilityCriteria:];
-[CLEmergencyLocationUsabilityCriteria setAltitudeStitchingEnabled:];
-[CLEmergencyLocationUsabilityCriteria setMaxUsableAge:];
-[CLEmergencyLocationUsabilityCriteria setMaxUsableHunc:];
-[CLEmergencyLocationUsabilityCriteria setMinUsableIntegrity:];
-[CLEmergencyLocationUsabilityCriteria setVuncCheckRequiredForUsability:];
-[CLEmergencyLocationUsabilityCriteria vuncCheckRequiredForUsability];
```
