# `CMHighFrequencyHeartRateData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- Protocols: `SRSampling`, `SRSampleExporting`
- 1 instance variables, 7 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"CMHeartRateData" _heartRateData;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,R,N) heartRate;
@property (Tq,R,N) confidence;
@property (T@"NSDate",R,N) date;
```

## Class methods

```
+[CMHighFrequencyHeartRateData supportsSecureCoding];
```

## Instance methods

```
-[CMHighFrequencyHeartRateData dealloc];
-[CMHighFrequencyHeartRateData date];
-[CMHighFrequencyHeartRateData encodeWithCoder:];
-[CMHighFrequencyHeartRateData initWithCoder:];
-[CMHighFrequencyHeartRateData copyWithZone:];
-[CMHighFrequencyHeartRateData confidence];
-[CMHighFrequencyHeartRateData heartRate];
-[CMHighFrequencyHeartRateData binarySampleRepresentation];
-[CMHighFrequencyHeartRateData initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMHighFrequencyHeartRateData initWithHeartRateData:];
-[CMHighFrequencyHeartRateData sr_dictionaryRepresentation];
```
