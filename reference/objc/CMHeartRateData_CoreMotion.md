# `CMHeartRateData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- Protocols: `SRSampling`
- 7 instance variables, 11 properties, 17 instance methods, 3 class methods

## Instance variables

```
B _error;
d _heartRate;
d _confidence;
@"NSDate" _startDate;
q _dataSource;
q _mode;
d _frequency;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N,V_heartRate) heartRate;
@property (Td,R,N,V_confidence) confidence;
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (TB,R,N,V_error) error;
@property (Tq,R,N,V_dataSource) dataSource;
@property (Tq,R,N,V_mode) mode;
@property (Td,N,V_frequency) frequency;
```

## Class methods

```
+[CMHeartRateData supportsSecureCoding];
+[CMHeartRateData dataSourceName:];
+[CMHeartRateData modeName:];
```

## Instance methods

```
-[CMHeartRateData startDate];
-[CMHeartRateData frequency];
-[CMHeartRateData dealloc];
-[CMHeartRateData error];
-[CMHeartRateData setFrequency:];
-[CMHeartRateData dataSource];
-[CMHeartRateData encodeWithCoder:];
-[CMHeartRateData mode];
-[CMHeartRateData description];
-[CMHeartRateData initWithCoder:];
-[CMHeartRateData copyWithZone:];
-[CMHeartRateData confidence];
-[CMHeartRateData heartRate];
-[CMHeartRateData initWithHighFrequencyHeartRate:];
-[CMHeartRateData binarySampleRepresentation];
-[CMHeartRateData initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMHeartRateData initWithHeartRate:confidence:timestamp:startDate:error:dataSource:mode:];
```
