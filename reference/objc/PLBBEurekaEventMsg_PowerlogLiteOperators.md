# `PLBBEurekaEventMsg`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBasebandMessage`
- 6 instance variables, 6 properties, 41 instance methods, 15 class methods

## Instance variables

```
C _inited;
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
```

## Class methods

```
+[PLBBEurekaEventMsg bbEuEvMsgEventNotProcessed];
+[PLBBEurekaEventMsg bbEuEvMsgNameBBEurekaMsgLite];
+[PLBBEurekaEventMsg bbEuEvMsgNameCMCDMAExit];
+[PLBBEurekaEventMsg bbEuEvMsgNameCMCallEventConn];
+[PLBBEurekaEventMsg bbEuEvMsgNameCMCallEventConnV2];
+[PLBBEurekaEventMsg bbEuEvMsgNameCMCallEventEnd];
+[PLBBEurekaEventMsg bbEuEvMsgNameCMCallEventEndV2];
+[PLBBEurekaEventMsg bbEuEvMsgNameCMCallEventIncom];
+[PLBBEurekaEventMsg bbEuEvMsgNameCMCallEventOrig];
+[PLBBEurekaEventMsg bbEuEvMsgNameCMCallEventOrigV2];
+[PLBBEurekaEventMsg bbEuEvMsgNameGSML1State];
+[PLBBEurekaEventMsg bbEuEvMsgNameLTERRCState];
+[PLBBEurekaEventMsg bbEuEvMsgNameSDEventActionCode];
+[PLBBEurekaEventMsg bbEuEvMsgNameWCDMARRCState];
+[PLBBEurekaEventMsg bbEuEvMsgUTRANRRCState];
```

## Instance methods

```
-[PLBBEurekaEventMsg setError:];
-[PLBBEurekaEventMsg init];
-[PLBBEurekaEventMsg setPayload:];
-[PLBBEurekaEventMsg setEventCode:];
-[PLBBEurekaEventMsg kvPairs];
-[PLBBEurekaEventMsg sdState];
-[PLBBEurekaEventMsg sdEvent];
-[PLBBEurekaEventMsg addPairWithKey:andWithVal:];
-[PLBBEurekaEventMsg appendToError:];
-[PLBBEurekaEventMsg commonInfo];
-[PLBBEurekaEventMsg inited];
-[PLBBEurekaEventMsg logEventCMCallEventConnWithId:andCallType:andSysMode:];
-[PLBBEurekaEventMsg logEventCMCallEventConnWithId:andCallType:andSysMode:andClientId:];
-[PLBBEurekaEventMsg logEventCMCallEventEndWithId:andNumCalls:];
-[PLBBEurekaEventMsg logEventCMCallEventEndWithId:andNumCalls:andClientId:];
-[PLBBEurekaEventMsg logEventCMCallEventOrigWithId:andCallType:andSrvType:];
-[PLBBEurekaEventMsg logEventCMCallEventOrigWithId:andCallType:andSrvType:andClientId:];
-[PLBBEurekaEventMsg logEventForwardBBEurekaEventMsgLite];
-[PLBBEurekaEventMsg logEventForwardGSML1StateWith:];
-[PLBBEurekaEventMsg logEventForwardLTERRCStateAs:];
-[PLBBEurekaEventMsg logEventForwardSDEventActionCode];
-[PLBBEurekaEventMsg logEventForwardUTRANRRCNextStateAs:andCurrStateAs:andRateAs:];
-[PLBBEurekaEventMsg logEventForwardWCDMARRCPrevStateAs:andCurrState:andRate:];
-[PLBBEurekaEventMsg logEventNoneEventNotProcessed];
-[PLBBEurekaEventMsg logEventPointCMExitCodeWithState:];
-[PLBBEurekaEventMsg refreshBBEurekaEventMsgLite];
-[PLBBEurekaEventMsg refreshEventNotProcessed];
-[PLBBEurekaEventMsg refreshLTERRCState];
-[PLBBEurekaEventMsg refreshSDEventActionCode];
-[PLBBEurekaEventMsg refreshUTRANRRCState];
-[PLBBEurekaEventMsg refreshWCDMARRCState];
-[PLBBEurekaEventMsg sdAct];
-[PLBBEurekaEventMsg sendAndLogPLEntry:];
-[PLBBEurekaEventMsg setCommonInfo:];
-[PLBBEurekaEventMsg setHeaderWithSeqNum:andDate:andTimeCal:];
-[PLBBEurekaEventMsg setInited:];
-[PLBBEurekaEventMsg setKvPairs:];
-[PLBBEurekaEventMsg setSDEventActionCodeWith:andSDAction:andSDState:];
-[PLBBEurekaEventMsg setSdAct:];
-[PLBBEurekaEventMsg setSdEvent:];
-[PLBBEurekaEventMsg setSdState:];
```
