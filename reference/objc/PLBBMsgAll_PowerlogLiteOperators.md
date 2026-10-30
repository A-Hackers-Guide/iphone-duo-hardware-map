# `PLBBMsgAll`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBBMsgRoot`
- 10 instance variables, 10 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSNumber" _seqNum;
@"NSDate" _bbDate;
@"NSString" _payload;
@"NSString" _error;
@"NSMutableDictionary" _info;
@"NSNumber" _iseqNum;
@"NSDate" _ibbDate;
@"NSString" _ieventCode;
@"NSString" _ipayload;
@"NSString" _ierror;
```

## Properties

```
@property (T@"NSNumber",&,V_iseqNum) iseqNum;
@property (T@"NSDate",&,V_ibbDate) ibbDate;
@property (T@"NSString",&,V_ieventCode) ieventCode;
@property (T@"NSString",&,V_ipayload) ipayload;
@property (T@"NSString",&,V_ierror) ierror;
@property (T@"NSNumber",&,V_seqNum) seqNum;
@property (T@"NSDate",&,V_bbDate) bbDate;
@property (T@"NSString",&,V_payload) payload;
@property (T@"NSString",&,V_error) error;
@property (T@"NSMutableDictionary",&,V_info) info;
```

## Class methods

```
+[PLBBMsgAll entryEventNoneBBMsgAll];
```

## Instance methods

```
-[PLBBMsgAll setError:];
-[PLBBMsgAll info];
-[PLBBMsgAll setInfo:];
-[PLBBMsgAll payload];
-[PLBBMsgAll error];
-[PLBBMsgAll setPayload:];
-[PLBBMsgAll sendAndLogPLEntry:withName:withType:];
-[PLBBMsgAll seqNum];
-[PLBBMsgAll refreshBBMsgAll];
-[PLBBMsgAll ibbDate];
-[PLBBMsgAll iseqNum];
-[PLBBMsgAll bbDate];
-[PLBBMsgAll ierror];
-[PLBBMsgAll ieventCode];
-[PLBBMsgAll ipayload];
-[PLBBMsgAll logEventNoneBBMsgAll];
-[PLBBMsgAll setBbDate:];
-[PLBBMsgAll setISeqNum:];
-[PLBBMsgAll setIbbDate:];
-[PLBBMsgAll setIerror:];
-[PLBBMsgAll setIeventCode:];
-[PLBBMsgAll setIpayload:];
-[PLBBMsgAll setIseqNum:];
-[PLBBMsgAll setSeqNum:];
```
