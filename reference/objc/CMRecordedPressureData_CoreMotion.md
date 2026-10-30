# `CMRecordedPressureData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMAmbientPressureData`
- Protocols: `SRSampleDirectExporting`
- 7 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
d _startDateValue;
f _pressureValue;
d _timestampValue;
f _temperatureValue;
@"NSMeasurement" _pressureMeasurement;
@"NSMeasurement" _temperatureMeasurement;
Q _identifier;
```

## Properties

```
@property (Td,R) startTime;
@property (TQ,R,V_identifier) identifier;
@property (T@"NSDate",R) startDate;
```

## Class methods

```
+[CMRecordedPressureData supportsSecureCoding];
```

## Instance methods

```
-[CMRecordedPressureData startDate];
-[CMRecordedPressureData identifier];
-[CMRecordedPressureData startTime];
-[CMRecordedPressureData dealloc];
-[CMRecordedPressureData timestamp];
-[CMRecordedPressureData pressure];
-[CMRecordedPressureData encodeWithCoder:];
-[CMRecordedPressureData description];
-[CMRecordedPressureData initWithCoder:];
-[CMRecordedPressureData temperature];
-[CMRecordedPressureData initWithData:timestamp:walltime:identifier:];
-[CMRecordedPressureData resetWithData:timestamp:walltime:identifier:];
-[CMRecordedPressureData sr_prefersUTF8StringRepresentation];
-[CMRecordedPressureData sr_writeUTF8RepresentationToOutputStream:];
```
