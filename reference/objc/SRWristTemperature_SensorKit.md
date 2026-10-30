# `SRWristTemperature`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSCopying`, `NSSecureCoding`
- 6 instance variables, 10 properties, 16 instance methods, 3 class methods

## Instance variables

```
@"NSDate" _timestamp;
@"NSMeasurement" _value;
Q _condition;
@"NSMeasurement" _errorEstimate;
@"NSMeasurement" _temperatureT1;
@"NSMeasurement" _temperatureT2;
```

## Properties

```
@property (T@"NSMeasurement",R,N,V_temperatureT1) temperatureT1;
@property (T@"NSMeasurement",R,N,V_temperatureT2) temperatureT2;
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (T@"NSMeasurement",R,N,V_value) value;
@property (TQ,R,N,V_condition) condition;
@property (T@"NSMeasurement",R,N,V_errorEstimate) errorEstimate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRWristTemperature supportsSecureCoding];
+[SRWristTemperature initialize];
+[SRWristTemperature new];
```

## Instance methods

```
-[SRWristTemperature condition];
-[SRWristTemperature init];
-[SRWristTemperature dealloc];
-[SRWristTemperature timestamp];
-[SRWristTemperature value];
-[SRWristTemperature encodeWithCoder:];
-[SRWristTemperature hash];
-[SRWristTemperature description];
-[SRWristTemperature initWithCoder:];
-[SRWristTemperature copyWithZone:];
-[SRWristTemperature isEqual:];
-[SRWristTemperature sr_dictionaryRepresentation];
-[SRWristTemperature errorEstimate];
-[SRWristTemperature initWithTimestamp:temperature:condition:errorEstimate:temperatureT1:temperatureT2:];
-[SRWristTemperature temperatureT1];
-[SRWristTemperature temperatureT2];
```
