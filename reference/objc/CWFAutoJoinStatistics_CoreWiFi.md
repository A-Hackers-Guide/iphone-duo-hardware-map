# `CWFAutoJoinStatistics`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 48 instance variables, 63 properties, 116 instance methods, 1 class methods

## Instance variables

```
Q _startTimestampUptime;
Q _startTimestampMonotonic;
@"NSMutableDictionary" _autoJoinTriggerCounts;
Q _autoJoinAlreadyAssociatedCount;
Q _autoJoinDidFindCandidateCount;
Q _autoJoinDidJoinCount;
Q _autoJoinDidJoinWithDisplayOnCount;
Q _autoJoinRetryDidFindCandidateCount;
Q _autoJoinRetryDidJoinCount;
Q _autoJoinAbortedCount;
Q _autoJoinAbortedRetryCount;
Q _scanChannelCount;
Q _scanChannelCount2GHz;
Q _scanChannelCount5GHz;
Q _scanChannelCount6GHz;
Q _preAssocScanChannelCount;
Q _preAssocScanChannelCount2GHz;
Q _preAssocScanChannelCount5GHz;
Q _preAssocScanChannelCount6GHz;
Q _followup6GHzScanChannelCount;
Q _GASQueryCount;
Q _timeWiFiOff;
Q _timeAssoc;
Q _timeUnassocAutoJoinDisabled;
Q _timeUnassocAutoJoinIdle;
Q _timeUnassocNoNetworks;
Q _timeUnassocNoCandidates;
Q _timeUnassocJoinFailed;
Q _timeUnassocSkippedDisabledCandidate;
Q _timeUnassocSkippedDisallowedCandidate;
Q _timeUnassocSkippedLowRSSICandidate;
Q _timeUnassocSkippedPartiallyMatchedCandidate;
Q _timeUnassocSkippedUnclassifiedCandidate;
Q _userJoinedPartiallyMatchedCandidateCount;
Q _userJoinedLowRSSICandidateCount;
Q _userJoinedDisabledCandidateCount;
Q _userJoinedDisallowedCandidateCount;
Q _userJoined6GHzOnlyCandidateCount;
Q _userJoinedDeferredCandidateCount;
Q _userJoinedStandalone6GHzCandidateCount;
Q _userJoinedLessPreferredCandidateCount;
Q _userJoinedFailedJoinCandidateCount;
Q _userJoinedUnclassifiedCandidateCount;
Q _autoHotspotCount;
Q _autoHotspotDidFindCandidateCount;
Q _autoHotspotDidJoinCount;
Q _autoHotspotAbortedCount;
@"NSArray" _knownNetworks;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSMutableDictionary",&,N,V_autoJoinTriggerCounts) autoJoinTriggerCounts;
@property (TQ,N,V_startTimestampUptime) startTimestampUptime;
@property (TQ,N,V_startTimestampMonotonic) startTimestampMonotonic;
@property (TQ,R,D) autoJoinCount;
@property (TQ,R,D) autoJoinRetryCount;
@property (TQ,N,V_autoJoinAlreadyAssociatedCount) autoJoinAlreadyAssociatedCount;
@property (TQ,N,V_autoJoinDidFindCandidateCount) autoJoinDidFindCandidateCount;
@property (TQ,N,V_autoJoinDidJoinCount) autoJoinDidJoinCount;
@property (TQ,N,V_autoJoinDidJoinWithDisplayOnCount) autoJoinDidJoinWithDisplayOnCount;
@property (TQ,N,V_autoJoinRetryDidFindCandidateCount) autoJoinRetryDidFindCandidateCount;
@property (TQ,N,V_autoJoinRetryDidJoinCount) autoJoinRetryDidJoinCount;
@property (TQ,N,V_autoJoinAbortedCount) autoJoinAbortedCount;
@property (TQ,N,V_autoJoinAbortedRetryCount) autoJoinAbortedRetryCount;
@property (TQ,R,D) combinedScanChannelCount;
@property (TQ,R,D) combinedScanChannelCount2GHz;
@property (TQ,R,D) combinedScanChannelCount5GHz;
@property (TQ,R,D) combinedScanChannelCount6GHz;
@property (TQ,N,V_scanChannelCount) scanChannelCount;
@property (TQ,N,V_scanChannelCount2GHz) scanChannelCount2GHz;
@property (TQ,N,V_scanChannelCount5GHz) scanChannelCount5GHz;
@property (TQ,N,V_scanChannelCount6GHz) scanChannelCount6GHz;
@property (TQ,N,V_preAssocScanChannelCount) preAssocScanChannelCount;
@property (TQ,N,V_preAssocScanChannelCount2GHz) preAssocScanChannelCount2GHz;
@property (TQ,N,V_preAssocScanChannelCount5GHz) preAssocScanChannelCount5GHz;
@property (TQ,N,V_preAssocScanChannelCount6GHz) preAssocScanChannelCount6GHz;
@property (TQ,N,V_followup6GHzScanChannelCount) followup6GHzScanChannelCount;
@property (TQ,N,V_GASQueryCount) GASQueryCount;
@property (TQ,N,V_timeWiFiOff) timeWiFiOff;
@property (TQ,N,V_timeAssoc) timeAssoc;
@property (TQ,N,V_timeUnassocAutoJoinDisabled) timeUnassocAutoJoinDisabled;
@property (TQ,N,V_timeUnassocAutoJoinIdle) timeUnassocAutoJoinIdle;
@property (TQ,N,V_timeUnassocNoNetworks) timeUnassocNoNetworks;
@property (TQ,N,V_timeUnassocNoCandidates) timeUnassocNoCandidates;
@property (TQ,N,V_timeUnassocJoinFailed) timeUnassocJoinFailed;
@property (TQ,R,D) timeUnassocSkippedCandidate;
@property (TQ,N,V_timeUnassocSkippedDisabledCandidate) timeUnassocSkippedDisabledCandidate;
@property (TQ,N,V_timeUnassocSkippedDisallowedCandidate) timeUnassocSkippedDisallowedCandidate;
@property (TQ,N,V_timeUnassocSkippedLowRSSICandidate) timeUnassocSkippedLowRSSICandidate;
@property (TQ,N,V_timeUnassocSkippedPartiallyMatchedCandidate) timeUnassocSkippedPartiallyMatchedCandidate;
@property (TQ,N,V_timeUnassocSkippedUnclassifiedCandidate) timeUnassocSkippedUnclassifiedCandidate;
@property (TQ,N,V_userJoinedPartiallyMatchedCandidateCount) userJoinedPartiallyMatchedCandidateCount;
@property (TQ,N,V_userJoinedLowRSSICandidateCount) userJoinedLowRSSICandidateCount;
@property (TQ,N,V_userJoinedDisabledCandidateCount) userJoinedDisabledCandidateCount;
@property (TQ,N,V_userJoinedDisallowedCandidateCount) userJoinedDisallowedCandidateCount;
@property (TQ,N,V_userJoined6GHzOnlyCandidateCount) userJoined6GHzOnlyCandidateCount;
@property (TQ,N,V_userJoinedDeferredCandidateCount) userJoinedDeferredCandidateCount;
@property (TQ,N,V_userJoinedStandalone6GHzCandidateCount) userJoinedStandalone6GHzCandidateCount;
@property (TQ,N,V_userJoinedLessPreferredCandidateCount) userJoinedLessPreferredCandidateCount;
@property (TQ,N,V_userJoinedFailedJoinCandidateCount) userJoinedFailedJoinCandidateCount;
@property (TQ,N,V_userJoinedUnclassifiedCandidateCount) userJoinedUnclassifiedCandidateCount;
@property (TQ,R,D) userJoinedCandidateCount;
@property (TQ,N,V_autoHotspotCount) autoHotspotCount;
@property (TQ,N,V_autoHotspotDidFindCandidateCount) autoHotspotDidFindCandidateCount;
@property (TQ,N,V_autoHotspotDidJoinCount) autoHotspotDidJoinCount;
@property (TQ,N,V_autoHotspotAbortedCount) autoHotspotAbortedCount;
@property (T@"NSDictionary",R,C,D,N) debugInfo;
@property (T@"NSArray",C,N,V_knownNetworks) knownNetworks;
@property (T@"NSString",R) coreAnalyticsEventName;
@property (T@"NSDictionary",R) coreAnalyticsEventPayload;
```

## Class methods

```
+[CWFAutoJoinStatistics supportsSecureCoding];
```

## Instance methods

```
-[CWFAutoJoinStatistics combinedScanChannelCount6GHz];
-[CWFAutoJoinStatistics setFollowup6GHzScanChannelCount:];
-[CWFAutoJoinStatistics knownNetworks];
-[CWFAutoJoinStatistics scanChannelCount6GHz];
-[CWFAutoJoinStatistics userJoinedLessPreferredCandidateCount];
-[CWFAutoJoinStatistics JSONCompatibleKeyValueMap];
-[CWFAutoJoinStatistics preAssocScanChannelCount2GHz];
-[CWFAutoJoinStatistics setScanChannelCount6GHz:];
-[CWFAutoJoinStatistics setScanChannelCount5GHz:];
-[CWFAutoJoinStatistics scanChannelCount];
-[CWFAutoJoinStatistics setUserJoinedDeferredCandidateCount:];
-[CWFAutoJoinStatistics coreAnalyticsEventPayload];
-[CWFAutoJoinStatistics init];
-[CWFAutoJoinStatistics timeUnassocAutoJoinIdle];
-[CWFAutoJoinStatistics debugInfo];
-[CWFAutoJoinStatistics setStartTimestampUptime:];
-[CWFAutoJoinStatistics timeUnassocNoNetworks];
-[CWFAutoJoinStatistics scanChannelCount2GHz];
-[CWFAutoJoinStatistics userJoined6GHzOnlyCandidateCount];
-[CWFAutoJoinStatistics setUserJoinedFailedJoinCandidateCount:];
-[CWFAutoJoinStatistics userJoinedStandalone6GHzCandidateCount];
-[CWFAutoJoinStatistics timeWiFiOff];
-[CWFAutoJoinStatistics setUserJoinedStandalone6GHzCandidateCount:];
-[CWFAutoJoinStatistics autoJoinRetryDidFindCandidateCount];
-[CWFAutoJoinStatistics setPreAssocScanChannelCount2GHz:];
-[CWFAutoJoinStatistics setAutoJoinRetryDidJoinCount:];
-[CWFAutoJoinStatistics coreAnalyticsEventName];
-[CWFAutoJoinStatistics autoHotspotCount];
-[CWFAutoJoinStatistics userJoinedCandidateCount];
-[CWFAutoJoinStatistics startTimestampMonotonic];
-[CWFAutoJoinStatistics setTimeUnassocAutoJoinIdle:];
-[CWFAutoJoinStatistics scanChannelCount5GHz];
-[CWFAutoJoinStatistics setGASQueryCount:];
-[CWFAutoJoinStatistics setTimeUnassocJoinFailed:];
-[CWFAutoJoinStatistics followup6GHzScanChannelCount];
-[CWFAutoJoinStatistics isEqualToAutoJoinStatistics:];
-[CWFAutoJoinStatistics autoJoinDidFindCandidateCount];
-[CWFAutoJoinStatistics setPreAssocScanChannelCount6GHz:];
-[CWFAutoJoinStatistics setTimeWiFiOff:];
-[CWFAutoJoinStatistics setPreAssocScanChannelCount:];
-[CWFAutoJoinStatistics setAutoHotspotAbortedCount:];
-[CWFAutoJoinStatistics timeUnassocSkippedPartiallyMatchedCandidate];
-[CWFAutoJoinStatistics setAutoJoinDidJoinCount:];
-[CWFAutoJoinStatistics userJoinedLowRSSICandidateCount];
-[CWFAutoJoinStatistics autoHotspotDidFindCandidateCount];
-[CWFAutoJoinStatistics autoHotspotAbortedCount];
-[CWFAutoJoinStatistics autoJoinRetryDidJoinCount];
-[CWFAutoJoinStatistics setScanChannelCount:];
-[CWFAutoJoinStatistics timeUnassocSkippedCandidate];
-[CWFAutoJoinStatistics timeUnassocNoCandidates];
-[CWFAutoJoinStatistics autoJoinRetryCount];
-[CWFAutoJoinStatistics setUserJoinedLessPreferredCandidateCount:];
-[CWFAutoJoinStatistics userJoinedDisallowedCandidateCount];
-[CWFAutoJoinStatistics autoJoinAbortedCount];
-[CWFAutoJoinStatistics userJoinedDeferredCandidateCount];
-[CWFAutoJoinStatistics autoJoinAbortedRetryCount];
-[CWFAutoJoinStatistics autoJoinAlreadyAssociatedCount];
-[CWFAutoJoinStatistics timeUnassocSkippedDisallowedCandidate];
-[CWFAutoJoinStatistics timeUnassocAutoJoinDisabled];
-[CWFAutoJoinStatistics setAutoJoinAbortedRetryCount:];
-[CWFAutoJoinStatistics setPreAssocScanChannelCount5GHz:];
-[CWFAutoJoinStatistics userJoinedUnclassifiedCandidateCount];
-[CWFAutoJoinStatistics setTimeUnassocSkippedDisabledCandidate:];
-[CWFAutoJoinStatistics setAutoJoinTriggerCounts:];
-[CWFAutoJoinStatistics combinedScanChannelCount];
-[CWFAutoJoinStatistics setUserJoinedUnclassifiedCandidateCount:];
-[CWFAutoJoinStatistics setTimeUnassocAutoJoinDisabled:];
-[CWFAutoJoinStatistics setTimeUnassocSkippedLowRSSICandidate:];
-[CWFAutoJoinStatistics GASQueryCount];
-[CWFAutoJoinStatistics encodeWithCoder:];
-[CWFAutoJoinStatistics combinedScanChannelCount5GHz];
-[CWFAutoJoinStatistics setAutoHotspotDidFindCandidateCount:];
-[CWFAutoJoinStatistics autoJoinTriggerCounts];
-[CWFAutoJoinStatistics setUserJoinedPartiallyMatchedCandidateCount:];
-[CWFAutoJoinStatistics setKnownNetworks:];
-[CWFAutoJoinStatistics setTimeUnassocSkippedPartiallyMatchedCandidate:];
-[CWFAutoJoinStatistics userJoinedPartiallyMatchedCandidateCount];
-[CWFAutoJoinStatistics setAutoJoinRetryDidFindCandidateCount:];
-[CWFAutoJoinStatistics preAssocScanChannelCount5GHz];
-[CWFAutoJoinStatistics setAutoHotspotCount:];
-[CWFAutoJoinStatistics hash];
-[CWFAutoJoinStatistics autoHotspotDidJoinCount];
-[CWFAutoJoinStatistics timeUnassocSkippedUnclassifiedCandidate];
-[CWFAutoJoinStatistics description];
-[CWFAutoJoinStatistics combinedScanChannelCount2GHz];
-[CWFAutoJoinStatistics initWithCoder:];
-[CWFAutoJoinStatistics preAssocScanChannelCount6GHz];
-[CWFAutoJoinStatistics setAutoJoinDidFindCandidateCount:];
-[CWFAutoJoinStatistics setUserJoinedLowRSSICandidateCount:];
-[CWFAutoJoinStatistics setUserJoinedDisallowedCandidateCount:];
-[CWFAutoJoinStatistics timeUnassocSkippedLowRSSICandidate];
-[CWFAutoJoinStatistics setScanChannelCount2GHz:];
-[CWFAutoJoinStatistics setTimeUnassocSkippedDisallowedCandidate:];
-[CWFAutoJoinStatistics setStartTimestampMonotonic:];
-[CWFAutoJoinStatistics copyWithZone:];
-[CWFAutoJoinStatistics userJoinedFailedJoinCandidateCount];
-[CWFAutoJoinStatistics setAutoJoinAbortedCount:];
-[CWFAutoJoinStatistics setUserJoinedDisabledCandidateCount:];
-[CWFAutoJoinStatistics setTimeUnassocNoCandidates:];
-[CWFAutoJoinStatistics isEqual:];
-[CWFAutoJoinStatistics timeUnassocSkippedDisabledCandidate];
-[CWFAutoJoinStatistics preAssocScanChannelCount];
-[CWFAutoJoinStatistics setUserJoined6GHzOnlyCandidateCount:];
-[CWFAutoJoinStatistics autoJoinCount];
-[CWFAutoJoinStatistics timeAssoc];
-[CWFAutoJoinStatistics autoJoinDidJoinWithDisplayOnCount];
-[CWFAutoJoinStatistics setAutoJoinDidJoinWithDisplayOnCount:];
-[CWFAutoJoinStatistics startTimestampUptime];
-[CWFAutoJoinStatistics setTimeUnassocSkippedUnclassifiedCandidate:];
-[CWFAutoJoinStatistics autoJoinDidJoinCount];
-[CWFAutoJoinStatistics setAutoJoinAlreadyAssociatedCount:];
-[CWFAutoJoinStatistics userJoinedDisabledCandidateCount];
-[CWFAutoJoinStatistics setTimeUnassocNoNetworks:];
-[CWFAutoJoinStatistics setAutoHotspotDidJoinCount:];
-[CWFAutoJoinStatistics timeUnassocJoinFailed];
-[CWFAutoJoinStatistics setTimeAssoc:];
```
