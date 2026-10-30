# `PLSinopeBBHardwareMessage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"NSNumber" _metricId;
@"NSString" _metricData;
@"NSNumber" _triggerId;
@"NSData" _data;
@"PBCodable" _pbc;
@"NSMutableArray" _metricIdArr;
@"NSMutableArray" _metricDataArr;
@"NSNumber" _triggerCnt;
@"NSNumber" _bbtimestamp;
@"NSDate" _timestampLogged;
@"NSDate" _bbMonotonic;
@"PLAgent" _logAgent;
```

## Properties

```
@property (T@"NSNumber",&,V_metricId) metricId;
@property (T@"NSString",&,V_metricData) metricData;
@property (T@"NSNumber",&,V_triggerId) triggerId;
@property (T@"NSData",&,V_data) data;
@property (T@"PBCodable",&,V_pbc) pbc;
@property (T@"NSMutableArray",&,V_metricIdArr) metricIdArr;
@property (T@"NSMutableArray",&,V_metricDataArr) metricDataArr;
@property (T@"NSNumber",&,V_triggerCnt) triggerCnt;
@property (T@"NSNumber",&,V_bbtimestamp) bbtimestamp;
@property (T@"NSDate",&,V_timestampLogged) timestampLogged;
@property (T@"NSDate",&,V_bbMonotonic) bbMonotonic;
@property (T@"PLAgent",&,V_logAgent) logAgent;
```

## Instance methods

```
-[PLSinopeBBHardwareMessage init];
-[PLSinopeBBHardwareMessage data];
-[PLSinopeBBHardwareMessage setData:];
-[PLSinopeBBHardwareMessage metricData];
-[PLSinopeBBHardwareMessage setMetricData:];
-[PLSinopeBBHardwareMessage metricId];
-[PLSinopeBBHardwareMessage triggerId];
-[PLSinopeBBHardwareMessage pbc];
-[PLSinopeBBHardwareMessage setBbMonotonic:];
-[PLSinopeBBHardwareMessage nrCaConfigActForClass:forEntry:];
-[PLSinopeBBHardwareMessage protocolStateForClass:forEntry:];
-[PLSinopeBBHardwareMessage setBbtimestamp:];
-[PLSinopeBBHardwareMessage setMetricIdArr:];
-[PLSinopeBBHardwareMessage setPbc:];
-[PLSinopeBBHardwareMessage timestampLogged];
-[PLSinopeBBHardwareMessage addToListMetric:payload:];
-[PLSinopeBBHardwareMessage bbMonotonic];
-[PLSinopeBBHardwareMessage bbtimestamp];
-[PLSinopeBBHardwareMessage decodePayload:forMetricId:];
-[PLSinopeBBHardwareMessage dlTbsHistForClass:forEntry:];
-[PLSinopeBBHardwareMessage gsmRabModeHistForClass:forEntry:];
-[PLSinopeBBHardwareMessage initEntryWithBBTS:triggerId:seqnum:payload:logAgent:];
-[PLSinopeBBHardwareMessage logAgent];
-[PLSinopeBBHardwareMessage logBBSinopeAperiodicMetrics];
-[PLSinopeBBHardwareMessage logBBSinopePeriodicMetrics];
-[PLSinopeBBHardwareMessage lteCaConfigActStatsForClass:forEntry:];
-[PLSinopeBBHardwareMessage lteComponentCarrierInfoForClass:forEntry:];
-[PLSinopeBBHardwareMessage lteNrRxDivForClass:forEntry:];
-[PLSinopeBBHardwareMessage lteNrRxTxActForClass:forEntry:];
-[PLSinopeBBHardwareMessage lteNrTxPowerForClass:forEntry:];
-[PLSinopeBBHardwareMessage metricDataArr];
-[PLSinopeBBHardwareMessage metricIdArr];
-[PLSinopeBBHardwareMessage nrCCInfoForClass:forEntry:];
-[PLSinopeBBHardwareMessage plmnSearchHistForClass:forEntry:];
-[PLSinopeBBHardwareMessage powerEstimatorForClass:forEntry:];
-[PLSinopeBBHardwareMessage protocolStackHistForClass:forEntry:];
-[PLSinopeBBHardwareMessage setLogAgent:];
-[PLSinopeBBHardwareMessage setMetricDataArr:];
-[PLSinopeBBHardwareMessage setMetricId:];
-[PLSinopeBBHardwareMessage setTimestampLogged:];
-[PLSinopeBBHardwareMessage setTriggerCnt:];
-[PLSinopeBBHardwareMessage setTriggerId:];
-[PLSinopeBBHardwareMessage sleepStatesForClass:forEntry:];
-[PLSinopeBBHardwareMessage triggerCnt];
```
