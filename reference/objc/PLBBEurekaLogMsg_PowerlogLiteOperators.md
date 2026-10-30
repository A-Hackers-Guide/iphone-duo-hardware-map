# `PLBBEurekaLogMsg`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBasebandMessage`
- 9 instance variables, 9 properties, 25 instance methods, 0 class methods

## Instance variables

```
C _inited;
@"NSDate" _bbDate;
^d _bbTimeCal;
@"NSNumber" _bbSeqNum;
@"NSMutableString" _sdEvent;
@"NSMutableString" _sdAct;
@"NSMutableString" _sdState;
@"NSMutableDictionary" _commonInfo;
@"NSMutableDictionary" _kvPairs;
```

## Properties

```
@property (TC,N,V_inited) inited;
@property (T@"NSMutableString",&,N,V_sdEvent) sdEvent;
@property (T@"NSMutableString",&,N,V_sdAct) sdAct;
@property (T@"NSMutableString",&,N,V_sdState) sdState;
@property (T@"NSMutableDictionary",&,N,V_commonInfo) commonInfo;
@property (T@"NSMutableDictionary",&,N,V_kvPairs) kvPairs;
@property (T@"NSDate",&,V_bbDate) bbDate;
@property (T^d,V_bbTimeCal) bbTimeCal;
@property (T@"NSNumber",&,V_bbSeqNum) bbSeqNum;
```

## Instance methods

```
-[PLBBEurekaLogMsg setError:];
-[PLBBEurekaLogMsg init];
-[PLBBEurekaLogMsg setPayload:];
-[PLBBEurekaLogMsg sendAndLogPLEntry:withName:withType:];
-[PLBBEurekaLogMsg setEventCode:];
-[PLBBEurekaLogMsg kvPairs];
-[PLBBEurekaLogMsg sdState];
-[PLBBEurekaLogMsg sdEvent];
-[PLBBEurekaLogMsg addPairWithKey:andWithVal:];
-[PLBBEurekaLogMsg bbDate];
-[PLBBEurekaLogMsg bbSeqNum];
-[PLBBEurekaLogMsg bbTimeCal];
-[PLBBEurekaLogMsg commonInfo];
-[PLBBEurekaLogMsg inited];
-[PLBBEurekaLogMsg sdAct];
-[PLBBEurekaLogMsg setBbDate:];
-[PLBBEurekaLogMsg setBbSeqNum:];
-[PLBBEurekaLogMsg setBbTimeCal:];
-[PLBBEurekaLogMsg setCommonInfo:];
-[PLBBEurekaLogMsg setHeaderWithSeqNum:andDate:andTimeCal:];
-[PLBBEurekaLogMsg setInited:];
-[PLBBEurekaLogMsg setKvPairs:];
-[PLBBEurekaLogMsg setSdAct:];
-[PLBBEurekaLogMsg setSdEvent:];
-[PLBBEurekaLogMsg setSdState:];
```
