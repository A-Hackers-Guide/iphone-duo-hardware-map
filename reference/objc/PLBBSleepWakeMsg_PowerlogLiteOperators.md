# `PLBBSleepWakeMsg`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBBMsgRoot`
- 31 instance variables, 31 properties, 65 instance methods, 2 class methods

## Instance variables

```
@"NSString" _swReason;
@"NSString" _bbWakeChannel;
@"NSString" _bbWakeType;
@"NSString" _bbWakeSubType;
@"NSData" _bbWakeDataBin;
@"NSDictionary" _bbWakeDataParsed;
@"NSString" _qmiSvcType;
@"NSString" _qmiClntId;
@"NSString" _qmiMsgId;
@"NSString" _qmiMsgType;
@"NSString" _qmiLen;
@"NSString" _ariGroupId;
@"NSString" _ariMsgId;
@"NSString" _ariMsgName;
@"NSString" _ariLen;
@"NSString" _ariSeqNum;
@"NSString" _swAtCmd;
@"NSString" _swRawData;
@"NSNumber" _swSvcId;
@"NSString" _swClientId;
@"NSString" _swMsgId;
@"NSString" _swMsgType;
@"NSString" _swCmdName;
@"NSString" _swCmdFullName;
@"NSDictionary" _swIpData;
@"NSString" _swRadioClass;
@"NSString" _swCTData;
@"NSString" _swChan;
@"NSString" _swCmd;
@"NSMutableDictionary" _commonInfo;
@"NSMutableDictionary" _kvPairs;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_commonInfo) commonInfo;
@property (T@"NSMutableDictionary",&,N,V_kvPairs) kvPairs;
@property (T@"NSString",&,V_swReason) swReason;
@property (T@"NSString",&,V_bbWakeChannel) bbWakeChannel;
@property (T@"NSString",&,V_bbWakeType) bbWakeType;
@property (T@"NSString",&,V_bbWakeSubType) bbWakeSubType;
@property (T@"NSData",&,V_bbWakeDataBin) bbWakeDataBin;
@property (T@"NSDictionary",&,V_bbWakeDataParsed) bbWakeDataParsed;
@property (T@"NSString",&,V_qmiSvcType) qmiSvcType;
@property (T@"NSString",&,V_qmiClntId) qmiClntId;
@property (T@"NSString",&,V_qmiMsgId) qmiMsgId;
@property (T@"NSString",&,V_qmiMsgType) qmiMsgType;
@property (T@"NSString",&,V_qmiLen) qmiLen;
@property (T@"NSString",&,V_ariGroupId) ariGroupId;
@property (T@"NSString",&,V_ariMsgId) ariMsgId;
@property (T@"NSString",&,V_ariMsgName) ariMsgName;
@property (T@"NSString",&,V_ariLen) ariLen;
@property (T@"NSString",&,V_ariSeqNum) ariSeqNum;
@property (T@"NSString",&,V_swAtCmd) swAtCmd;
@property (T@"NSString",&,V_swRawData) swRawData;
@property (T@"NSNumber",&,V_swSvcId) swSvcId;
@property (T@"NSString",&,V_swClientId) swClientId;
@property (T@"NSString",&,V_swMsgId) swMsgId;
@property (T@"NSString",&,V_swMsgType) swMsgType;
@property (T@"NSString",&,V_swCmdName) swCmdName;
@property (T@"NSString",&,V_swCmdFullName) swCmdFullName;
@property (T@"NSDictionary",&,V_swIpData) swIpData;
@property (T@"NSString",&,V_swRadioClass) swRadioClass;
@property (T@"NSString",&,V_swCTData) swCTData;
@property (T@"NSString",&,V_swChan) swChan;
@property (T@"NSString",&,V_swCmd) swCmd;
```

## Class methods

```
+[PLBBSleepWakeMsg entryEventPointDefinitionSleepWakeActivityIceABM];
+[PLBBSleepWakeMsg entryEventPointDefinitionSleepWakeActivityMavABM];
```

## Instance methods

```
-[PLBBSleepWakeMsg sendAndLogPLEntry:withName:withType:];
-[PLBBSleepWakeMsg kvPairs];
-[PLBBSleepWakeMsg swAtCmd];
-[PLBBSleepWakeMsg swSvcId];
-[PLBBSleepWakeMsg swMsgId];
-[PLBBSleepWakeMsg ariGroupId];
-[PLBBSleepWakeMsg ariLen];
-[PLBBSleepWakeMsg ariMsgId];
-[PLBBSleepWakeMsg ariMsgName];
-[PLBBSleepWakeMsg ariSeqNum];
-[PLBBSleepWakeMsg bbWakeChannel];
-[PLBBSleepWakeMsg bbWakeDataBin];
-[PLBBSleepWakeMsg bbWakeDataParsed];
-[PLBBSleepWakeMsg bbWakeSubType];
-[PLBBSleepWakeMsg bbWakeType];
-[PLBBSleepWakeMsg commonInfo];
-[PLBBSleepWakeMsg logEventPointSleepWakeABM];
-[PLBBSleepWakeMsg qmiClntId];
-[PLBBSleepWakeMsg qmiLen];
-[PLBBSleepWakeMsg qmiMsgId];
-[PLBBSleepWakeMsg qmiMsgType];
-[PLBBSleepWakeMsg qmiSvcType];
-[PLBBSleepWakeMsg refreshSleepWakeActivity];
-[PLBBSleepWakeMsg setAriGroupId:];
-[PLBBSleepWakeMsg setAriLen:];
-[PLBBSleepWakeMsg setAriMsgId:];
-[PLBBSleepWakeMsg setAriMsgName:];
-[PLBBSleepWakeMsg setAriSeqNum:];
-[PLBBSleepWakeMsg setBbWakeChannel:];
-[PLBBSleepWakeMsg setBbWakeDataBin:];
-[PLBBSleepWakeMsg setBbWakeDataParsed:];
-[PLBBSleepWakeMsg setBbWakeSubType:];
-[PLBBSleepWakeMsg setBbWakeType:];
-[PLBBSleepWakeMsg setCommonInfo:];
-[PLBBSleepWakeMsg setKvPairs:];
-[PLBBSleepWakeMsg setQmiClntId:];
-[PLBBSleepWakeMsg setQmiLen:];
-[PLBBSleepWakeMsg setQmiMsgId:];
-[PLBBSleepWakeMsg setQmiMsgType:];
-[PLBBSleepWakeMsg setQmiSvcType:];
-[PLBBSleepWakeMsg setSwAtCmd:];
-[PLBBSleepWakeMsg setSwCTData:];
-[PLBBSleepWakeMsg setSwChan:];
-[PLBBSleepWakeMsg setSwClientId:];
-[PLBBSleepWakeMsg setSwCmd:];
-[PLBBSleepWakeMsg setSwCmdFullName:];
-[PLBBSleepWakeMsg setSwCmdName:];
-[PLBBSleepWakeMsg setSwIpData:];
-[PLBBSleepWakeMsg setSwMsgId:];
-[PLBBSleepWakeMsg setSwMsgType:];
-[PLBBSleepWakeMsg setSwRadioClass:];
-[PLBBSleepWakeMsg setSwRawData:];
-[PLBBSleepWakeMsg setSwReason:];
-[PLBBSleepWakeMsg setSwSvcId:];
-[PLBBSleepWakeMsg swCTData];
-[PLBBSleepWakeMsg swChan];
-[PLBBSleepWakeMsg swClientId];
-[PLBBSleepWakeMsg swCmd];
-[PLBBSleepWakeMsg swCmdFullName];
-[PLBBSleepWakeMsg swCmdName];
-[PLBBSleepWakeMsg swIpData];
-[PLBBSleepWakeMsg swMsgType];
-[PLBBSleepWakeMsg swRadioClass];
-[PLBBSleepWakeMsg swRawData];
-[PLBBSleepWakeMsg swReason];
```
