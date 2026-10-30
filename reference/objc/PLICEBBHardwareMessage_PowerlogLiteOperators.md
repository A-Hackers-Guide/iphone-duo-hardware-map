# `PLICEBBHardwareMessage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 37 instance methods, 2 class methods

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
+[PLICEBBHardwareMessage entryEventBackwardDefinitionBBIceEventMetrics];
+[PLICEBBHardwareMessage entryEventBackwardDefinitionBBIcePeriodicMetrics];
```

## Instance methods

```
-[PLICEBBHardwareMessage init];
-[PLICEBBHardwareMessage data];
-[PLICEBBHardwareMessage setData:];
-[PLICEBBHardwareMessage metricData];
-[PLICEBBHardwareMessage setMetricData:];
-[PLICEBBHardwareMessage metricId];
-[PLICEBBHardwareMessage triggerId];
-[PLICEBBHardwareMessage pbc];
-[PLICEBBHardwareMessage protocolHist2ForClass:forEntry:];
-[PLICEBBHardwareMessage setBbMonotonic:];
-[PLICEBBHardwareMessage decodeEventPayload:forMetricId:];
-[PLICEBBHardwareMessage setBbtimestamp:];
-[PLICEBBHardwareMessage setMetricIdArr:];
-[PLICEBBHardwareMessage setPbc:];
-[PLICEBBHardwareMessage addToListMetric:payload:];
-[PLICEBBHardwareMessage bbMonotonic];
-[PLICEBBHardwareMessage bbtimestamp];
-[PLICEBBHardwareMessage componentCarrierForClass:forEntry:];
-[PLICEBBHardwareMessage cpcStatsForClass:forEntry:];
-[PLICEBBHardwareMessage decodePayload:forMetricId:];
-[PLICEBBHardwareMessage duplexModeForClass:forEntry:];
-[PLICEBBHardwareMessage initEntryWithBBTS:triggerId:seqnum:payload:logAgent:];
-[PLICEBBHardwareMessage logAgent];
-[PLICEBBHardwareMessage logBBIceAperiodicMetrics];
-[PLICEBBHardwareMessage logBBIcePeriodicMetrics];
-[PLICEBBHardwareMessage metricDataArr];
-[PLICEBBHardwareMessage metricIdArr];
-[PLICEBBHardwareMessage pdcchStateStatsFor:forEntry:];
-[PLICEBBHardwareMessage protocolHistForClass:forEntry:];
-[PLICEBBHardwareMessage protocolPerStateForClass:forEntry:];
-[PLICEBBHardwareMessage rrcModeHistForClass:forEntry:];
-[PLICEBBHardwareMessage setLogAgent:];
-[PLICEBBHardwareMessage setMetricDataArr:];
-[PLICEBBHardwareMessage setMetricId:];
-[PLICEBBHardwareMessage setTriggerCnt:];
-[PLICEBBHardwareMessage setTriggerId:];
-[PLICEBBHardwareMessage triggerCnt];
```
