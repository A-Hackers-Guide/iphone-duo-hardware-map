# `CMWaterTemperature`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _date;
@"NSMeasurement" _temperature;
@"NSMeasurement" _temperatureUncertainty;
```

## Properties

```
@property (T@"NSDate",R,N,V_date) date;
@property (T@"NSMeasurement",R,N,V_temperature) temperature;
@property (T@"NSMeasurement",R,N,V_temperatureUncertainty) temperatureUncertainty;
```

## Class methods

```
+[CMWaterTemperature supportsSecureCoding];
```

## Instance methods

```
-[CMWaterTemperature dealloc];
-[CMWaterTemperature date];
-[CMWaterTemperature encodeWithCoder:];
-[CMWaterTemperature description];
-[CMWaterTemperature initWithCoder:];
-[CMWaterTemperature copyWithZone:];
-[CMWaterTemperature temperature];
-[CMWaterTemperature initWithTemperature:andTemperatureUncertainty:andDate:];
-[CMWaterTemperature temperatureUncertainty];
```
