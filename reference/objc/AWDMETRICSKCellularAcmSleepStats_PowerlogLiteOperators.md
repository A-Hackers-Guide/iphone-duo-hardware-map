# `AWDMETRICSKCellularAcmSleepStats`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 6 instance variables, 9 properties, 31 instance methods, 1 class methods

## Instance variables

```
Q _timestamp;
@"NSMutableArray" _acms;
I _durationMs;
I _numSubs;
B _isDataPreferred;
{?="timestamp"b1"durationMs"b1"numSubs"b1"isDataPreferred"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDurationMs;
@property (TI,N,V_durationMs) durationMs;
@property (T@"NSMutableArray",&,N,V_acms) acms;
@property (TB,N) hasNumSubs;
@property (TI,N,V_numSubs) numSubs;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Class methods

```
+[AWDMETRICSKCellularAcmSleepStats acmType];
```

## Instance methods

```
-[AWDMETRICSKCellularAcmSleepStats hasTimestamp];
-[AWDMETRICSKCellularAcmSleepStats setHasTimestamp:];
-[AWDMETRICSKCellularAcmSleepStats setTimestamp:];
-[AWDMETRICSKCellularAcmSleepStats writeTo:];
-[AWDMETRICSKCellularAcmSleepStats mergeFrom:];
-[AWDMETRICSKCellularAcmSleepStats timestamp];
-[AWDMETRICSKCellularAcmSleepStats hash];
-[AWDMETRICSKCellularAcmSleepStats copyTo:];
-[AWDMETRICSKCellularAcmSleepStats description];
-[AWDMETRICSKCellularAcmSleepStats readFrom:];
-[AWDMETRICSKCellularAcmSleepStats copyWithZone:];
-[AWDMETRICSKCellularAcmSleepStats isEqual:];
-[AWDMETRICSKCellularAcmSleepStats dictionaryRepresentation];
-[AWDMETRICSKCellularAcmSleepStats durationMs];
-[AWDMETRICSKCellularAcmSleepStats hasDurationMs];
-[AWDMETRICSKCellularAcmSleepStats setDurationMs:];
-[AWDMETRICSKCellularAcmSleepStats setHasDurationMs:];
-[AWDMETRICSKCellularAcmSleepStats addAcm:];
-[AWDMETRICSKCellularAcmSleepStats isDataPreferred];
-[AWDMETRICSKCellularAcmSleepStats numSubs];
-[AWDMETRICSKCellularAcmSleepStats acmAtIndex:];
-[AWDMETRICSKCellularAcmSleepStats acms];
-[AWDMETRICSKCellularAcmSleepStats acmsCount];
-[AWDMETRICSKCellularAcmSleepStats clearAcms];
-[AWDMETRICSKCellularAcmSleepStats hasIsDataPreferred];
-[AWDMETRICSKCellularAcmSleepStats hasNumSubs];
-[AWDMETRICSKCellularAcmSleepStats setAcms:];
-[AWDMETRICSKCellularAcmSleepStats setHasIsDataPreferred:];
-[AWDMETRICSKCellularAcmSleepStats setHasNumSubs:];
-[AWDMETRICSKCellularAcmSleepStats setIsDataPreferred:];
-[AWDMETRICSKCellularAcmSleepStats setNumSubs:];
```
