# `CMRecordedRotationRateData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMRotationRateData`
- 3 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
d _startDateValue;
{?="x"d"y"d"z"d} _rotationRate;
d _timestampValue;
```

## Properties

```
@property (T@"NSDate",R) startDate;
```

## Class methods

```
+[CMRecordedRotationRateData supportsSecureCoding];
```

## Instance methods

```
-[CMRecordedRotationRateData startDate];
-[CMRecordedRotationRateData dealloc];
-[CMRecordedRotationRateData timestamp];
-[CMRecordedRotationRateData encodeWithCoder:];
-[CMRecordedRotationRateData description];
-[CMRecordedRotationRateData initWithCoder:];
-[CMRecordedRotationRateData rotationRate];
-[CMRecordedRotationRateData initWithData:timestamp:walltime:];
```
