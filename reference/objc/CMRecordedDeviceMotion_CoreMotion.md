# `CMRecordedDeviceMotion`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMDeviceMotion`
- Protocols: `SRSampleExporting`
- 2 instance variables, 7 properties, 9 instance methods, 1 class methods

## Instance variables

```
d _startTime;
Q _identifier;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R) startTime;
@property (TQ,R,V_identifier) identifier;
@property (T@"NSDate",R) startDate;
```

## Class methods

```
+[CMRecordedDeviceMotion supportsSecureCoding];
```

## Instance methods

```
-[CMRecordedDeviceMotion startDate];
-[CMRecordedDeviceMotion identifier];
-[CMRecordedDeviceMotion startTime];
-[CMRecordedDeviceMotion dealloc];
-[CMRecordedDeviceMotion encodeWithCoder:];
-[CMRecordedDeviceMotion description];
-[CMRecordedDeviceMotion initWithCoder:];
-[CMRecordedDeviceMotion initWithDeviceMotion:sensorTimestamp:startTime:identifier:];
-[CMRecordedDeviceMotion sr_dictionaryRepresentation];
```
