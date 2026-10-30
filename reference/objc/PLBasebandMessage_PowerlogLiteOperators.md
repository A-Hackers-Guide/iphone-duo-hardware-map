# `PLBasebandMessage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 14 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"NSData" rawData;
I ticksInGoodState;
I ticksInGPSONState;
d timeCalibration;
@"NSDate" _apTimestamp;
@"PLBBMsg" _logger;
@"PLAgent" _agent;
@"NSNumber" _seqNum;
@"NSDate" _date;
d _timeCal;
@"NSString" _pload;
@"NSNumber" _msgType;
```

## Properties

```
@property (T@"NSData",R,&,N,VrawData) rawData;
@property (TI,R,N,VticksInGoodState) ticksInGoodState;
@property (TI,R,N,VticksInGPSONState) ticksInGPSONState;
@property (T@"NSDate",R,&,N) timestamp;
@property (T@"NSDate",R,&,N,V_apTimestamp) apTimestamp;
@property (T@"NSDate",R,&,N) calibratedTimestamp;
@property (Td,N,VtimeCalibration) timeCalibration;
@property (T@"PLBBMsg",&,V_logger) logger;
@property (T@"PLAgent",&,N,V_agent) agent;
@property (T@"NSNumber",&,N,V_seqNum) seqNum;
@property (T@"NSDate",&,N,V_date) date;
@property (Td,V_timeCal) timeCal;
@property (T@"NSString",&,V_pload) pload;
@property (T@"NSNumber",&,V_msgType) msgType;
```

## Class methods

```
+[PLBasebandMessage messageWithData:];
```

## Instance methods

```
-[PLBasebandMessage logger];
-[PLBasebandMessage setLogger:];
-[PLBasebandMessage setDate:];
-[PLBasebandMessage agent];
-[PLBasebandMessage dealloc];
-[PLBasebandMessage timestamp];
-[PLBasebandMessage date];
-[PLBasebandMessage setAgent:];
-[PLBasebandMessage rawData];
-[PLBasebandMessage initWithData:];
-[PLBasebandMessage seqNum];
-[PLBasebandMessage msgType];
-[PLBasebandMessage timeCalibration];
-[PLBasebandMessage timeCal];
-[PLBasebandMessage apTimestamp];
-[PLBasebandMessage calibratedTimestamp];
-[PLBasebandMessage isCalibratedDateGood];
-[PLBasebandMessage isTimestampValid:];
-[PLBasebandMessage logEntry:withBody:];
-[PLBasebandMessage logMsgAll];
-[PLBasebandMessage logWithLogger:];
-[PLBasebandMessage pload];
-[PLBasebandMessage setMsgType:];
-[PLBasebandMessage setPload:];
-[PLBasebandMessage setSeqNum:];
-[PLBasebandMessage setTimeCal:];
-[PLBasebandMessage setTimeCalibration:];
-[PLBasebandMessage ticksInGPSONState];
-[PLBasebandMessage ticksInGoodState];
```
