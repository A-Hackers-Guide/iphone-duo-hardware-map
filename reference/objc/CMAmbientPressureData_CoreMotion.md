# `CMAmbientPressureData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- Protocols: `SRSampleDirectExporting`
- 2 instance variables, 2 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSMeasurement" _pressure;
@"NSMeasurement" _temperature;
```

## Properties

```
@property (T@"NSMeasurement",R,N,V_pressure) pressure;
@property (T@"NSMeasurement",R,N,V_temperature) temperature;
```

## Class methods

```
+[CMAmbientPressureData supportsSecureCoding];
```

## Instance methods

```
-[CMAmbientPressureData dealloc];
-[CMAmbientPressureData pressure];
-[CMAmbientPressureData encodeWithCoder:];
-[CMAmbientPressureData description];
-[CMAmbientPressureData initWithCoder:];
-[CMAmbientPressureData copyWithZone:];
-[CMAmbientPressureData temperature];
-[CMAmbientPressureData initWithPressure:andTimestamp:];
-[CMAmbientPressureData sr_prefersUTF8StringRepresentation];
-[CMAmbientPressureData sr_writeUTF8RepresentationToOutputStream:];
```
