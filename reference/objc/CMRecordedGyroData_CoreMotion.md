# `CMRecordedGyroData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMGyroData`
- 5 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
d _startDateValue;
{?="x"d"y"d"z"d} _rotationRate;
d _timestampValue;
f _temperatureValue;
Q _identifier;
```

## Properties

```
@property (TQ,R,V_identifier) identifier;
@property (T@"NSDate",R) startDate;
@property (Td,R) startTime;
@property (Tf,R) temperature;
```

## Class methods

```
+[CMRecordedGyroData supportsSecureCoding];
```

## Instance methods

```
-[CMRecordedGyroData startDate];
-[CMRecordedGyroData identifier];
-[CMRecordedGyroData startTime];
-[CMRecordedGyroData dealloc];
-[CMRecordedGyroData timestamp];
-[CMRecordedGyroData encodeWithCoder:];
-[CMRecordedGyroData description];
-[CMRecordedGyroData initWithCoder:];
-[CMRecordedGyroData temperature];
-[CMRecordedGyroData rotationRate];
-[CMRecordedGyroData initWithData:timestamp:walltime:identifier:];
-[CMRecordedGyroData resetWithData:timestamp:walltime:identifier:];
```
