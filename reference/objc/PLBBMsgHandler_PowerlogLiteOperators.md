# `PLBBMsgHandler`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 19 instance methods, 1 class methods

## Instance variables

```
I _ticksInGoodState;
I _ticksInGPSONState;
@"NSData" _rawData;
@"PLAgent" _agent;
@"NSNumber" _seqNum;
@"NSDate" _date;
@"NSDate" _timestamp;
@"NSDate" _apTimestamp;
@"NSDate" _calibratedTimestamp;
d _timeCalibration;
```

## Properties

```
@property (T@"NSData",&,N,V_rawData) rawData;
@property (T@"PLAgent",&,N,V_agent) agent;
@property (T@"NSNumber",&,N,V_seqNum) seqNum;
@property (T@"NSDate",&,N,V_date) date;
@property (TI,R,N,V_ticksInGoodState) ticksInGoodState;
@property (TI,R,N,V_ticksInGPSONState) ticksInGPSONState;
@property (T@"NSDate",R,&,N,V_timestamp) timestamp;
@property (T@"NSDate",R,&,N,V_apTimestamp) apTimestamp;
@property (T@"NSDate",R,&,N,V_calibratedTimestamp) calibratedTimestamp;
@property (Td,N,V_timeCalibration) timeCalibration;
```

## Class methods

```
+[PLBBMsgHandler getMsgHandler];
```

## Instance methods

```
-[PLBBMsgHandler setDate:];
-[PLBBMsgHandler init];
-[PLBBMsgHandler agent];
-[PLBBMsgHandler timestamp];
-[PLBBMsgHandler date];
-[PLBBMsgHandler setAgent:];
-[PLBBMsgHandler rawData];
-[PLBBMsgHandler setRawData:];
-[PLBBMsgHandler seqNum];
-[PLBBMsgHandler decodeMsgHeader];
-[PLBBMsgHandler timeCalibration];
-[PLBBMsgHandler apTimestamp];
-[PLBBMsgHandler calibratedTimestamp];
-[PLBBMsgHandler handleMsg:forAgent:];
-[PLBBMsgHandler registerWithHandlerAs:forType:];
-[PLBBMsgHandler setSeqNum:];
-[PLBBMsgHandler setTimeCalibration:];
-[PLBBMsgHandler ticksInGPSONState];
-[PLBBMsgHandler ticksInGoodState];
```
