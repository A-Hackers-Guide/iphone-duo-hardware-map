# `CMPredictedDistanceBout`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 11 instance variables, 15 properties, 22 instance methods, 2 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
@"NSDate" fEndDate;
I fStepCount;
d fDistance;
d fActiveTime;
I fElevationAsc;
I fElevationDesc;
I fStepCountGPS;
d fDistanceGPS;
q fBoutType;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (T@"NSDate",R,N) endDate;
@property (TI,R,N) stepCount;
@property (Td,R,N) distance;
@property (Td,R,N) activeTime;
@property (TI,R,N) elevationAsc;
@property (TI,R,N) elevationDesc;
@property (TI,R,N) stepCountGPS;
@property (Td,R,N) distanceGPS;
@property (Tq,R,N) boutType;
```

## Class methods

```
+[CMPredictedDistanceBout supportsSecureCoding];
+[CMPredictedDistanceBout inputFromPreparedStatement:];
```

## Instance methods

```
-[CMPredictedDistanceBout startDate];
-[CMPredictedDistanceBout distance];
-[CMPredictedDistanceBout stepCount];
-[CMPredictedDistanceBout recordId];
-[CMPredictedDistanceBout dealloc];
-[CMPredictedDistanceBout endDate];
-[CMPredictedDistanceBout encodeWithCoder:];
-[CMPredictedDistanceBout description];
-[CMPredictedDistanceBout initWithCoder:];
-[CMPredictedDistanceBout copyWithZone:];
-[CMPredictedDistanceBout isEqual:];
-[CMPredictedDistanceBout initWithSample:];
-[CMPredictedDistanceBout activeTime];
-[CMPredictedDistanceBout binarySampleRepresentation];
-[CMPredictedDistanceBout boutType];
-[CMPredictedDistanceBout distanceGPS];
-[CMPredictedDistanceBout elevationAsc];
-[CMPredictedDistanceBout elevationDesc];
-[CMPredictedDistanceBout initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMPredictedDistanceBout initWithRecordId:startDate:endDate:stepCount:distance:activeTime:elevationAsc:elevationDesc:stepCountGPS:distanceGPS:boutType:];
-[CMPredictedDistanceBout sr_dictionaryRepresentation];
-[CMPredictedDistanceBout stepCountGPS];
```
