# `CMFitnessMachineData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 18 instance variables, 18 properties, 44 instance methods, 2 class methods

## Instance variables

```
d fTimestamp;
i _externalFitnessType;
d _elapsedTime;
d _totalEnergy;
d _totalDistance;
d _totalElevationAscended;
q _totalStrideCount;
q _totalStrokeCount;
q _totalFloorsClimbed;
d _instantaneousSpeed;
d _instantaneousCadence;
d _instantaneousPower;
d _inclination;
d _resistanceLevel;
d _mets;
@"NSString" _manufacturer;
@"NSString" _model;
@"NSString" _deviceIdentifier;
```

## Properties

```
@property (Ti,N,V_externalFitnessType) externalFitnessType;
@property (T@"NSString",N,V_deviceIdentifier) deviceIdentifier;
@property (T@"NSDate",R,N) timestamp;
@property (Td,N,V_elapsedTime) elapsedTime;
@property (Td,N,V_totalEnergy) totalEnergy;
@property (Td,N,V_totalDistance) totalDistance;
@property (Td,N,V_totalElevationAscended) totalElevationAscended;
@property (Tq,N,V_totalStrideCount) totalStrideCount;
@property (Tq,N,V_totalStrokeCount) totalStrokeCount;
@property (Tq,N,V_totalFloorsClimbed) totalFloorsClimbed;
@property (Td,N,V_instantaneousSpeed) instantaneousSpeed;
@property (Td,N,V_instantaneousCadence) instantaneousCadence;
@property (Td,N,V_instantaneousPower) instantaneousPower;
@property (Td,N,V_inclination) inclination;
@property (Td,N,V_resistanceLevel) resistanceLevel;
@property (Td,N,V_mets) mets;
@property (T@"NSString",C,N,V_manufacturer) manufacturer;
@property (T@"NSString",C,N,V_model) model;
```

## Class methods

```
+[CMFitnessMachineData supportsSecureCoding];
+[CMFitnessMachineData isAvailable];
```

## Instance methods

```
-[CMFitnessMachineData setElapsedTime:];
-[CMFitnessMachineData model];
-[CMFitnessMachineData elapsedTime];
-[CMFitnessMachineData setModel:];
-[CMFitnessMachineData setDeviceIdentifier:];
-[CMFitnessMachineData dealloc];
-[CMFitnessMachineData timestamp];
-[CMFitnessMachineData manufacturer];
-[CMFitnessMachineData totalDistance];
-[CMFitnessMachineData deviceIdentifier];
-[CMFitnessMachineData initWithTimestamp:];
-[CMFitnessMachineData encodeWithCoder:];
-[CMFitnessMachineData description];
-[CMFitnessMachineData initWithCoder:];
-[CMFitnessMachineData setTotalDistance:];
-[CMFitnessMachineData copyWithZone:];
-[CMFitnessMachineData setManufacturer:];
-[CMFitnessMachineData setInclination:];
-[CMFitnessMachineData setTotalEnergy:];
-[CMFitnessMachineData resistanceLevel];
-[CMFitnessMachineData convertToCLFitnessMachineData:deviceId:];
-[CMFitnessMachineData externalFitnessType];
-[CMFitnessMachineData inclination];
-[CMFitnessMachineData initWithExernalBikeSensorData:speed:cadence:power:model:deviceIdentifier:manufacturer:externalFitnessType:];
-[CMFitnessMachineData initializeVariables];
-[CMFitnessMachineData instantaneousCadence];
-[CMFitnessMachineData instantaneousPower];
-[CMFitnessMachineData instantaneousSpeed];
-[CMFitnessMachineData mets];
-[CMFitnessMachineData setExternalFitnessType:];
-[CMFitnessMachineData setInstantaneousCadence:];
-[CMFitnessMachineData setInstantaneousPower:];
-[CMFitnessMachineData setInstantaneousSpeed:];
-[CMFitnessMachineData setMets:];
-[CMFitnessMachineData setResistanceLevel:];
-[CMFitnessMachineData setTotalElevationAscended:];
-[CMFitnessMachineData setTotalFloorsClimbed:];
-[CMFitnessMachineData setTotalStrideCount:];
-[CMFitnessMachineData setTotalStrokeCount:];
-[CMFitnessMachineData totalElevationAscended];
-[CMFitnessMachineData totalEnergy];
-[CMFitnessMachineData totalFloorsClimbed];
-[CMFitnessMachineData totalStrideCount];
-[CMFitnessMachineData totalStrokeCount];
```
