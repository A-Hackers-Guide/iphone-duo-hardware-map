# `CMHistoricalMobilitySamples`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampling`, `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 5 instance variables, 9 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _walkingBoutMobility;
@"NSArray" _strideCalEntries;
@"NSArray" _predictedDistanceBoutsMobilityCalibration;
@"NSArray" _predictedDistanceBouts;
@"NSArray" _gaitMetrics;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",&,V_walkingBoutMobility) walkingBoutMobility;
@property (T@"NSArray",&,V_strideCalEntries) strideCalEntries;
@property (T@"NSArray",&,V_predictedDistanceBoutsMobilityCalibration) predictedDistanceBoutsMobilityCalibration;
@property (T@"NSArray",&,V_predictedDistanceBouts) predictedDistanceBouts;
@property (T@"NSArray",&,V_gaitMetrics) gaitMetrics;
```

## Class methods

```
+[CMHistoricalMobilitySamples supportsSecureCoding];
```

## Instance methods

```
-[CMHistoricalMobilitySamples init];
-[CMHistoricalMobilitySamples dealloc];
-[CMHistoricalMobilitySamples encodeWithCoder:];
-[CMHistoricalMobilitySamples description];
-[CMHistoricalMobilitySamples initWithCoder:];
-[CMHistoricalMobilitySamples copyWithZone:];
-[CMHistoricalMobilitySamples isEqual:];
-[CMHistoricalMobilitySamples setGaitMetrics:];
-[CMHistoricalMobilitySamples binarySampleRepresentation];
-[CMHistoricalMobilitySamples gaitMetrics];
-[CMHistoricalMobilitySamples initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMHistoricalMobilitySamples predictedDistanceBouts];
-[CMHistoricalMobilitySamples predictedDistanceBoutsMobilityCalibration];
-[CMHistoricalMobilitySamples setPredictedDistanceBouts:];
-[CMHistoricalMobilitySamples setPredictedDistanceBoutsMobilityCalibration:];
-[CMHistoricalMobilitySamples setStrideCalEntries:];
-[CMHistoricalMobilitySamples setWalkingBoutMobility:];
-[CMHistoricalMobilitySamples sr_dictionaryRepresentation];
-[CMHistoricalMobilitySamples strideCalEntries];
-[CMHistoricalMobilitySamples walkingBoutMobility];
```
