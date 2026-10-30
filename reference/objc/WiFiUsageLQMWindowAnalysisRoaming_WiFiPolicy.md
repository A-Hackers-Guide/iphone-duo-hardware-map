# `WiFiUsageLQMWindowAnalysisRoaming`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageLQMWindowAnalysis`
- 22 instance variables, 22 properties, 46 instance methods, 3 class methods

## Instance variables

```
B _isWNMScoreRoam;
B _isColocatedRoam;
B _firstRoamAfterRoamRecommLifted;
@"NSString" _roamingReason;
@"NSString" _roamingStatus;
q _latency;
@"NSString" _roamBssSupports;
q _roamConfigTriggerRssi;
q _originRssi;
q _targetRssi;
@"WiFiUsageSessionPingPongStats" _pingPongStats;
Q _roamSuppressionEnabledPerc;
d _roamSuppressionWaitForRoamStart;
d _roamSuppressionWaitForRoamEnd;
q _scanDuration;
Q _roamScannedChannelCount;
Q _roamFullBandScanCount;
Q _roamPartialBandScanCount;
Q _roamPktsPendingAqm;
Q _roamPktsPendingTxSubQ;
{?="valueByBand"[3q]"valid"[3B]} _roamConfigChannels;
{?="isAllowed"B"forceApply"B"deviceSupport"B"isEAP"B"environment"Q"networkOfInterestType"Q"LOIType"Q} _roamConfigCriteria;
```

## Properties

```
@property (T@"NSString",&,N,V_roamingReason) roamingReason;
@property (T@"NSString",&,N,V_roamingStatus) roamingStatus;
@property (Tq,N,V_latency) latency;
@property (TB,N,V_isWNMScoreRoam) isWNMScoreRoam;
@property (TB,N,V_isColocatedRoam) isColocatedRoam;
@property (T@"NSString",&,N,V_roamBssSupports) roamBssSupports;
@property (Tq,N,V_roamConfigTriggerRssi) roamConfigTriggerRssi;
@property (T{?=[3q][3B]},N,V_roamConfigChannels) roamConfigChannels;
@property (T{?=BBBBQQQ},N,V_roamConfigCriteria) roamConfigCriteria;
@property (Tq,N,V_originRssi) originRssi;
@property (Tq,N,V_targetRssi) targetRssi;
@property (T@"WiFiUsageSessionPingPongStats",&,N,V_pingPongStats) pingPongStats;
@property (TQ,N,V_roamSuppressionEnabledPerc) roamSuppressionEnabledPerc;
@property (TB,N,V_firstRoamAfterRoamRecommLifted) firstRoamAfterRoamRecommLifted;
@property (Td,N,V_roamSuppressionWaitForRoamStart) roamSuppressionWaitForRoamStart;
@property (Td,N,V_roamSuppressionWaitForRoamEnd) roamSuppressionWaitForRoamEnd;
@property (Tq,N,V_scanDuration) scanDuration;
@property (TQ,N,V_roamScannedChannelCount) roamScannedChannelCount;
@property (TQ,N,V_roamFullBandScanCount) roamFullBandScanCount;
@property (TQ,N,V_roamPartialBandScanCount) roamPartialBandScanCount;
@property (TQ,N,V_roamPktsPendingAqm) roamPktsPendingAqm;
@property (TQ,N,V_roamPktsPendingTxSubQ) roamPktsPendingTxSubQ;
```

## Class methods

```
+[WiFiUsageLQMWindowAnalysisRoaming bssSupportWithFlags:];
+[WiFiUsageLQMWindowAnalysisRoaming isColocatedRoam:];
+[WiFiUsageLQMWindowAnalysisRoaming isWNMRoam:];
```

## Instance methods

```
-[WiFiUsageLQMWindowAnalysisRoaming setLatency:];
-[WiFiUsageLQMWindowAnalysisRoaming latency];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamSuppressionEnabledPerc:];
-[WiFiUsageLQMWindowAnalysisRoaming addDimensionsTo:];
-[WiFiUsageLQMWindowAnalysisRoaming roamingStatus];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamPartialBandScanCount:];
-[WiFiUsageLQMWindowAnalysisRoaming roamingReason];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamingStatus:];
-[WiFiUsageLQMWindowAnalysisRoaming roamPartialBandScanCount];
-[WiFiUsageLQMWindowAnalysisRoaming setTargetRssi:];
-[WiFiUsageLQMWindowAnalysisRoaming roamPktsPendingAqm];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamPktsPendingTxSubQ:];
-[WiFiUsageLQMWindowAnalysisRoaming roamSuppressionEnabledPerc];
-[WiFiUsageLQMWindowAnalysisRoaming initWithRollingWindow:WithRoamingState:andReasonString:andStatus:asString:andLatency:andRoamData:andCurrentBSSSession:andContext:andPingPongStats:andTimestamp:onQueue:];
-[WiFiUsageLQMWindowAnalysisRoaming targetRssi];
-[WiFiUsageLQMWindowAnalysisRoaming isColocatedRoam];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamingReason:];
-[WiFiUsageLQMWindowAnalysisRoaming roamConfigChannels];
-[WiFiUsageLQMWindowAnalysisRoaming setIsWNMScoreRoam:];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamScannedChannelCount:];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamSuppressionWaitForRoamEnd:];
-[WiFiUsageLQMWindowAnalysisRoaming setFirstRoamAfterRoamRecommLifted:];
-[WiFiUsageLQMWindowAnalysisRoaming isWNMScoreRoam];
-[WiFiUsageLQMWindowAnalysisRoaming setScanDuration:];
-[WiFiUsageLQMWindowAnalysisRoaming setIsColocatedRoam:];
-[WiFiUsageLQMWindowAnalysisRoaming roamConfigTriggerRssi];
-[WiFiUsageLQMWindowAnalysisRoaming setOriginRssi:];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamConfigTriggerRssi:];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamBssSupports:];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamFullBandScanCount:];
-[WiFiUsageLQMWindowAnalysisRoaming scanDuration];
-[WiFiUsageLQMWindowAnalysisRoaming setPingPongStats:];
-[WiFiUsageLQMWindowAnalysisRoaming roamSuppressionWaitForRoamEnd];
-[WiFiUsageLQMWindowAnalysisRoaming pingPongStats];
-[WiFiUsageLQMWindowAnalysisRoaming originRssi];
-[WiFiUsageLQMWindowAnalysisRoaming roamConfigCriteria];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamPktsPendingAqm:];
-[WiFiUsageLQMWindowAnalysisRoaming roamScannedChannelCount];
-[WiFiUsageLQMWindowAnalysisRoaming firstRoamAfterRoamRecommLifted];
-[WiFiUsageLQMWindowAnalysisRoaming roamSuppressionWaitForRoamStart];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamConfigCriteria:];
-[WiFiUsageLQMWindowAnalysisRoaming roamBssSupports];
-[WiFiUsageLQMWindowAnalysisRoaming roamPktsPendingTxSubQ];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamConfigChannels:];
-[WiFiUsageLQMWindowAnalysisRoaming setRoamSuppressionWaitForRoamStart:];
-[WiFiUsageLQMWindowAnalysisRoaming roamFullBandScanCount];
```
