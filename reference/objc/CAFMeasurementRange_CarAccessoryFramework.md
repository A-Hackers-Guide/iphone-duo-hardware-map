# `CAFMeasurementRange`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFRange`
- 1 instance variables, 4 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSUnit" _unit;
```

## Properties

```
@property (T@"NSMeasurement",R,N) minimumValue;
@property (T@"NSMeasurement",R,N) maximumValue;
@property (T@"NSMeasurement",R,N) stepValue;
@property (T@"NSUnit",R,N,V_unit) unit;
```

## Class methods

```
+[CAFMeasurementRange step];
+[CAFMeasurementRange minimum];
+[CAFMeasurementRange maximum];
```

## Instance methods

```
-[CAFMeasurementRange unit];
-[CAFMeasurementRange minimumValue];
-[CAFMeasurementRange maximumValue];
-[CAFMeasurementRange stepValue];
-[CAFMeasurementRange valueIsInRange:];
-[CAFMeasurementRange valueRoundedToNearestStepValue:];
-[CAFMeasurementRange initWithMetaData:unit:];
-[CAFMeasurementRange limitedValueForValue:];
-[CAFMeasurementRange rangeDescription];
```
