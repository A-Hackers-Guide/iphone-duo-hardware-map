# `WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 18 instance variables, 34 properties, 79 instance methods, 0 class methods

## Instance variables

```
i _ac;
I _dpsNotifications;
I _durSinceLastEnqueue;
I _durSinceLastEnqueueAtLastCheck;
I _durSinceLastFailedComp;
I _durSinceLastSuccessfulComp;
I _expiredComp;
I _failedComp;
I _failedCompletionsAtLastCheck;
I _noAckComp;
I _otherErrComp;
I _qeuedPackets;
I _sinceLastEnqueueHowManyFailed;
I _sinceLastEnqueueHowManySuccess;
I _sinceLastSuccessHowManyFailed;
I _success;
I _successfulCompletionsAtLastCheck;
{?="ac"b1"dpsNotifications"b1"durSinceLastEnqueue"b1"durSinceLastEnqueueAtLastCheck"b1"durSinceLastFailedComp"b1"durSinceLastSuccessfulComp"b1"expiredComp"b1"failedComp"b1"failedCompletionsAtLastCheck"b1"noAckComp"b1"otherErrComp"b1"qeuedPackets"b1"sinceLastEnqueueHowManyFailed"b1"sinceLastEnqueueHowManySuccess"b1"sinceLastSuccessHowManyFailed"b1"success"b1"successfulCompletionsAtLastCheck"b1} _has;
```

## Properties

```
@property (TB,N) hasAc;
@property (Ti,N,V_ac) ac;
@property (TB,N) hasSuccess;
@property (TI,N,V_success) success;
@property (TB,N) hasDurSinceLastSuccessfulComp;
@property (TI,N,V_durSinceLastSuccessfulComp) durSinceLastSuccessfulComp;
@property (TB,N) hasFailedComp;
@property (TI,N,V_failedComp) failedComp;
@property (TB,N) hasDurSinceLastFailedComp;
@property (TI,N,V_durSinceLastFailedComp) durSinceLastFailedComp;
@property (TB,N) hasExpiredComp;
@property (TI,N,V_expiredComp) expiredComp;
@property (TB,N) hasNoAckComp;
@property (TI,N,V_noAckComp) noAckComp;
@property (TB,N) hasOtherErrComp;
@property (TI,N,V_otherErrComp) otherErrComp;
@property (TB,N) hasDurSinceLastEnqueue;
@property (TI,N,V_durSinceLastEnqueue) durSinceLastEnqueue;
@property (TB,N) hasQeuedPackets;
@property (TI,N,V_qeuedPackets) qeuedPackets;
@property (TB,N) hasSinceLastEnqueueHowManyFailed;
@property (TI,N,V_sinceLastEnqueueHowManyFailed) sinceLastEnqueueHowManyFailed;
@property (TB,N) hasSinceLastEnqueueHowManySuccess;
@property (TI,N,V_sinceLastEnqueueHowManySuccess) sinceLastEnqueueHowManySuccess;
@property (TB,N) hasSinceLastSuccessHowManyFailed;
@property (TI,N,V_sinceLastSuccessHowManyFailed) sinceLastSuccessHowManyFailed;
@property (TB,N) hasDurSinceLastEnqueueAtLastCheck;
@property (TI,N,V_durSinceLastEnqueueAtLastCheck) durSinceLastEnqueueAtLastCheck;
@property (TB,N) hasSuccessfulCompletionsAtLastCheck;
@property (TI,N,V_successfulCompletionsAtLastCheck) successfulCompletionsAtLastCheck;
@property (TB,N) hasFailedCompletionsAtLastCheck;
@property (TI,N,V_failedCompletionsAtLastCheck) failedCompletionsAtLastCheck;
@property (TB,N) hasDpsNotifications;
@property (TI,N,V_dpsNotifications) dpsNotifications;
```

## Instance methods

```
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasSuccess];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions writeTo:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions success];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions mergeFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasSuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hash];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions copyTo:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions description];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions readFrom:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions copyWithZone:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions isEqual:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions dictionaryRepresentation];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions ac];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setAc:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions StringAsAc:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasFailedCompletionsAtLastCheck];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasOtherErrComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasQeuedPackets];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setExpiredComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions acAsString:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions dpsNotifications];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions durSinceLastEnqueue];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions durSinceLastEnqueueAtLastCheck];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions durSinceLastFailedComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions durSinceLastSuccessfulComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions expiredComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions failedComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions failedCompletionsAtLastCheck];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasAc];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasDpsNotifications];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasDurSinceLastEnqueue];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasDurSinceLastEnqueueAtLastCheck];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasDurSinceLastFailedComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasDurSinceLastSuccessfulComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasExpiredComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasFailedComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasNoAckComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasSinceLastEnqueueHowManyFailed];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasSinceLastEnqueueHowManySuccess];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasSinceLastSuccessHowManyFailed];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions hasSuccessfulCompletionsAtLastCheck];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions noAckComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions otherErrComp];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions qeuedPackets];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setDpsNotifications:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setDurSinceLastEnqueue:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setDurSinceLastEnqueueAtLastCheck:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setDurSinceLastFailedComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setDurSinceLastSuccessfulComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setFailedComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setFailedCompletionsAtLastCheck:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasAc:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasDpsNotifications:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasDurSinceLastEnqueue:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasDurSinceLastEnqueueAtLastCheck:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasDurSinceLastFailedComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasDurSinceLastSuccessfulComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasExpiredComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasFailedComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasFailedCompletionsAtLastCheck:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasNoAckComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasOtherErrComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasQeuedPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasSinceLastEnqueueHowManyFailed:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasSinceLastEnqueueHowManySuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasSinceLastSuccessHowManyFailed:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setHasSuccessfulCompletionsAtLastCheck:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setNoAckComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setOtherErrComp:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setQeuedPackets:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setSinceLastEnqueueHowManyFailed:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setSinceLastEnqueueHowManySuccess:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setSinceLastSuccessHowManyFailed:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions setSuccessfulCompletionsAtLastCheck:];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions sinceLastEnqueueHowManyFailed];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions sinceLastEnqueueHowManySuccess];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions sinceLastSuccessHowManyFailed];
-[WiFiAnalyticsAWDWiFiNWActivityPerACTxCompletions successfulCompletionsAtLastCheck];
```
