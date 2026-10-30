# `CAFMeasurementCharacteristic`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFNumberCharacteristic`
- 1 instance variables, 4 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"CAFMeasurementRange" _range;
```

## Properties

```
@property (T@"NSNumber",&,N) numberValue;
@property (T@"NSMeasurement",C,N) measurementValue;
@property (T@"CAFMeasurementRange",R,N,V_range) range;
@property (T@"NSUnit",R,N) unit;
```

## Class methods

```
+[CAFMeasurementCharacteristic _sharedStringFromMeasurement:];
+[CAFMeasurementCharacteristic primaryCharacteristicFormat];
+[CAFMeasurementCharacteristic secondaryCharacteristicFormats];
```

## Instance methods

```
-[CAFMeasurementCharacteristic unit];
-[CAFMeasurementCharacteristic range];
-[CAFMeasurementCharacteristic formattedValue];
-[CAFMeasurementCharacteristic numberValue];
-[CAFMeasurementCharacteristic setNumberValue:];
-[CAFMeasurementCharacteristic _setNumberValue:];
-[CAFMeasurementCharacteristic measurementValue];
-[CAFMeasurementCharacteristic setMeasurementValue:];
```
