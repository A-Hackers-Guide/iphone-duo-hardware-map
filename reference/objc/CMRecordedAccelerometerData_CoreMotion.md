# `CMRecordedAccelerometerData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMAccelerometerData`
- 4 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
d _startDateValue;
{?="x"d"y"d"z"d} _accelerationValue;
d _timestampValue;
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
+[CMRecordedAccelerometerData supportsSecureCoding];
```

## Instance methods

```
-[CMRecordedAccelerometerData startDate];
-[CMRecordedAccelerometerData identifier];
-[CMRecordedAccelerometerData startTime];
-[CMRecordedAccelerometerData dealloc];
-[CMRecordedAccelerometerData timestamp];
-[CMRecordedAccelerometerData acceleration];
-[CMRecordedAccelerometerData encodeWithCoder:];
-[CMRecordedAccelerometerData description];
-[CMRecordedAccelerometerData initWithCoder:];
-[CMRecordedAccelerometerData initWithData:timestamp:walltime:identifier:];
-[CMRecordedAccelerometerData resetWithData:timestamp:walltime:identifier:];
```
