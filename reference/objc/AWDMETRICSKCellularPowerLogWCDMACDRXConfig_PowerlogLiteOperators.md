# `AWDMETRICSKCellularPowerLogWCDMACDRXConfig`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 10 instance variables, 18 properties, 44 instance methods, 0 class methods

## Instance variables

```
Q _timestamp;
I _drxCycleLength;
I _numSubs;
@"NSData" _plmn;
I _subsId;
I _ueDrxCycleInactivityThreshold;
I _ueGrantMonitoringInactivityThreshold;
B _isDataPreferred;
B _ueDrxGrantMonitoring;
{?="timestamp"b1"drxCycleLength"b1"numSubs"b1"subsId"b1"ueDrxCycleInactivityThreshold"b1"ueGrantMonitoringInactivityThreshold"b1"isDataPreferred"b1"ueDrxGrantMonitoring"b1} _has;
```

## Properties

```
@property (TB,N) hasTimestamp;
@property (TQ,N,V_timestamp) timestamp;
@property (TB,N) hasDrxCycleLength;
@property (TI,N,V_drxCycleLength) drxCycleLength;
@property (TB,N) hasUeDrxCycleInactivityThreshold;
@property (TI,N,V_ueDrxCycleInactivityThreshold) ueDrxCycleInactivityThreshold;
@property (TB,N) hasUeGrantMonitoringInactivityThreshold;
@property (TI,N,V_ueGrantMonitoringInactivityThreshold) ueGrantMonitoringInactivityThreshold;
@property (TB,N) hasUeDrxGrantMonitoring;
@property (TB,N,V_ueDrxGrantMonitoring) ueDrxGrantMonitoring;
@property (TB,N) hasSubsId;
@property (TI,N,V_subsId) subsId;
@property (TB,R,N) hasPlmn;
@property (T@"NSData",&,N,V_plmn) plmn;
@property (TB,N) hasNumSubs;
@property (TI,N,V_numSubs) numSubs;
@property (TB,N) hasIsDataPreferred;
@property (TB,N,V_isDataPreferred) isDataPreferred;
```

## Instance methods

```
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasTimestamp];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setHasTimestamp:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setTimestamp:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig writeTo:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig mergeFrom:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig timestamp];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setPlmn:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hash];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig copyTo:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig description];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig readFrom:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig copyWithZone:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig isEqual:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig plmn];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig dictionaryRepresentation];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasPlmn];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig isDataPreferred];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig numSubs];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig drxCycleLength];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasDrxCycleLength];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasIsDataPreferred];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasNumSubs];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasSubsId];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasUeDrxCycleInactivityThreshold];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasUeDrxGrantMonitoring];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig hasUeGrantMonitoringInactivityThreshold];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setDrxCycleLength:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setHasDrxCycleLength:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setHasIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setHasNumSubs:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setHasSubsId:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setHasUeDrxCycleInactivityThreshold:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setHasUeDrxGrantMonitoring:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setHasUeGrantMonitoringInactivityThreshold:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setIsDataPreferred:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setNumSubs:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setSubsId:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setUeDrxCycleInactivityThreshold:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setUeDrxGrantMonitoring:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig setUeGrantMonitoringInactivityThreshold:];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig subsId];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig ueDrxCycleInactivityThreshold];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig ueDrxGrantMonitoring];
-[AWDMETRICSKCellularPowerLogWCDMACDRXConfig ueGrantMonitoringInactivityThreshold];
```
