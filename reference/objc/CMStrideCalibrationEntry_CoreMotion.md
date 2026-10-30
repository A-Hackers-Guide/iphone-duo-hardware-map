# `CMStrideCalibrationEntry`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 1 instance variables, 17 properties, 24 instance methods, 2 class methods

## Instance variables

```
{CLStrideCalEntry="recordId"i"startTime"d"pacebin"I"kvalue"d"kvalueTrack"d"score"d"endTime"d"distance"d"steps"i"session"i"speed"d"percentGrade"d"gpsSource"i"timestamp"d"runningFormStrideLength"d"runningFormStrideLengthMetrics"i} _strideCalStruct;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (Td,R,N) startTime;
@property (Td,R,N) endTime;
@property (Td,R,N) distance;
@property (Ti,R,N) steps;
@property (Td,R,N) speed;
@property (Td,R,N) percentGrade;
@property (Tq,R,N) gpsSource;
@property (Td,R,N) kvalue;
@property (Td,R,N) kvalueTrack;
@property (Ti,R,N) session;
@property (Td,R,N) meanRunningStrideLength;
@property (Tq,R,N) numberRunningStrideLengthSamples;
```

## Class methods

```
+[CMStrideCalibrationEntry supportsSecureCoding];
+[CMStrideCalibrationEntry inputFromPreparedStatement:];
```

## Instance methods

```
-[CMStrideCalibrationEntry distance];
-[CMStrideCalibrationEntry endTime];
-[CMStrideCalibrationEntry speed];
-[CMStrideCalibrationEntry startTime];
-[CMStrideCalibrationEntry recordId];
-[CMStrideCalibrationEntry score];
-[CMStrideCalibrationEntry steps];
-[CMStrideCalibrationEntry encodeWithCoder:];
-[CMStrideCalibrationEntry description];
-[CMStrideCalibrationEntry initWithCoder:];
-[CMStrideCalibrationEntry session];
-[CMStrideCalibrationEntry copyWithZone:];
-[CMStrideCalibrationEntry isEqual:];
-[CMStrideCalibrationEntry pacebin];
-[CMStrideCalibrationEntry binarySampleRepresentation];
-[CMStrideCalibrationEntry gpsSource];
-[CMStrideCalibrationEntry initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMStrideCalibrationEntry initWithCLStrideCalEntry:];
-[CMStrideCalibrationEntry kvalue];
-[CMStrideCalibrationEntry kvalueTrack];
-[CMStrideCalibrationEntry meanRunningStrideLength];
-[CMStrideCalibrationEntry numberRunningStrideLengthSamples];
-[CMStrideCalibrationEntry percentGrade];
-[CMStrideCalibrationEntry sr_dictionaryRepresentation];
```
