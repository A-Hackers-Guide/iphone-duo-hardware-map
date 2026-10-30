# `PLMAVBBHardwareMessage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 31 instance methods, 2 class methods

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
@property (T@"NSDate",&,V_bbMonotonic) bbMonotonic;
@property (T@"PLAgent",&,V_logAgent) logAgent;
```

## Class methods

```
+[PLMAVBBHardwareMessage entryEventBackwardDefinitionBBMavEventMetrics];
+[PLMAVBBHardwareMessage entryEventBackwardDefinitionBBMavPeriodicMetrics];
```

## Instance methods

```
-[PLMAVBBHardwareMessage init];
-[PLMAVBBHardwareMessage data];
-[PLMAVBBHardwareMessage setData:];
-[PLMAVBBHardwareMessage metricData];
-[PLMAVBBHardwareMessage setMetricData:];
-[PLMAVBBHardwareMessage metricId];
-[PLMAVBBHardwareMessage triggerId];
-[PLMAVBBHardwareMessage pbc];
-[PLMAVBBHardwareMessage setBbMonotonic:];
-[PLMAVBBHardwareMessage setBbtimestamp:];
-[PLMAVBBHardwareMessage setMetricIdArr:];
-[PLMAVBBHardwareMessage setPbc:];
-[PLMAVBBHardwareMessage addToListMetric:payload:];
-[PLMAVBBHardwareMessage bbMonotonic];
-[PLMAVBBHardwareMessage bbtimestamp];
-[PLMAVBBHardwareMessage decodePayload:forMetricId:];
-[PLMAVBBHardwareMessage initEntryWithBBTS:triggerId:seqnum:payload:logAgent:];
-[PLMAVBBHardwareMessage logAgent];
-[PLMAVBBHardwareMessage logBBMavAperiodicMetrics];
-[PLMAVBBHardwareMessage logBBMavPeriodicMetrics];
-[PLMAVBBHardwareMessage lteComponentCarrierForClass:forEntry:];
-[PLMAVBBHardwareMessage metricDataArr];
-[PLMAVBBHardwareMessage metricIdArr];
-[PLMAVBBHardwareMessage nrComponentCarrierForClass:forEntry:];
-[PLMAVBBHardwareMessage protocolHistForClass:forEntry:];
-[PLMAVBBHardwareMessage setLogAgent:];
-[PLMAVBBHardwareMessage setMetricDataArr:];
-[PLMAVBBHardwareMessage setMetricId:];
-[PLMAVBBHardwareMessage setTriggerCnt:];
-[PLMAVBBHardwareMessage setTriggerId:];
-[PLMAVBBHardwareMessage triggerCnt];
```
