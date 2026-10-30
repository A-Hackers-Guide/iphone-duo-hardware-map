# `CMRecoveryHeartRate`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`, `NSCopying`
- 4 instance variables, 8 properties, 15 instance methods, 3 class methods

## Instance variables

```
Q fRecordId;
@"NSDate" fStartDate;
d fHeartRate;
d fHeartRateConfidence;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) recordId;
@property (T@"NSDate",R,N) startDate;
@property (Td,R,N) heartRate;
@property (Td,R,N) heartRateConfidence;
```

## Class methods

```
+[CMRecoveryHeartRate supportsSecureCoding];
+[CMRecoveryHeartRate HRRecoveryInputHRFromCMRecoveryHeartRate:];
+[CMRecoveryHeartRate inputFromPreparedStatement:];
```

## Instance methods

```
-[CMRecoveryHeartRate startDate];
-[CMRecoveryHeartRate recordId];
-[CMRecoveryHeartRate dealloc];
-[CMRecoveryHeartRate encodeWithCoder:];
-[CMRecoveryHeartRate description];
-[CMRecoveryHeartRate initWithCoder:];
-[CMRecoveryHeartRate copyWithZone:];
-[CMRecoveryHeartRate isEqual:];
-[CMRecoveryHeartRate heartRate];
-[CMRecoveryHeartRate initWithSample:];
-[CMRecoveryHeartRate binarySampleRepresentation];
-[CMRecoveryHeartRate heartRateConfidence];
-[CMRecoveryHeartRate initWithBinarySampleRepresentation:metadata:timestamp:];
-[CMRecoveryHeartRate initWithRecordId:startDate:heartRate:heartRateConfidence:];
-[CMRecoveryHeartRate sr_dictionaryRepresentation];
```
