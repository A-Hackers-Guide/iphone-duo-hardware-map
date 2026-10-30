# `WiFiUsageRealTimeCoexSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageSession`
- 27 instance variables, 27 properties, 75 instance methods, 0 class methods

## Instance variables

```
B _lastRequestDifferentSSID;
B _isSplitSSID;
B _hasCandidates;
B _hasDifferentIpv4DetailsAfterSSIDTransition;
B _hasDifferentIpv6DetailsAfterSSIDTransition;
B _isRtCoexOptimal;
i _lastRequestPreferredBand;
Q _rtCoexType;
@"NSString" _rtCoexSubType;
Q _lastRequestType;
Q _lastRequestPreferredChannel;
@"NSString" _lastRequestPreferredSSID;
@"NSString" _lastRequestPreferredBSS;
@"NSDate" _firstRtCoexOptimal;
@"NSDate" _lastRtCoexOptimalStatusChange;
d _rtCoexInOptimalDuration;
@"NSDate" _lastEnterPreferredChannel;
d _preferredChannelDuration;
@"NSDate" _lastEnterPreferredBand;
d _preferredBandDuration;
@"NSDate" _firstSSIDTransition;
@"NSDate" _firstIPUpdateAfterSSIDTransition;
@"NSDate" _firstManualJoin;
@"NSDate" _firstManualJoinAfterSSIDTransition;
Q _requestSteerToPreferredChannelCount;
Q _requestSteerCount;
Q _requestDisconnectCount;
```

## Properties

```
@property (TQ,V_rtCoexType) rtCoexType;
@property (T@"NSString",&,V_rtCoexSubType) rtCoexSubType;
@property (TQ,V_lastRequestType) lastRequestType;
@property (TQ,V_lastRequestPreferredChannel) lastRequestPreferredChannel;
@property (Ti,V_lastRequestPreferredBand) lastRequestPreferredBand;
@property (TB,V_lastRequestDifferentSSID) lastRequestDifferentSSID;
@property (T@"NSString",&,V_lastRequestPreferredSSID) lastRequestPreferredSSID;
@property (T@"NSString",&,V_lastRequestPreferredBSS) lastRequestPreferredBSS;
@property (TB,V_isSplitSSID) isSplitSSID;
@property (TB,V_hasCandidates) hasCandidates;
@property (TB,V_hasDifferentIpv4DetailsAfterSSIDTransition) hasDifferentIpv4DetailsAfterSSIDTransition;
@property (TB,V_hasDifferentIpv6DetailsAfterSSIDTransition) hasDifferentIpv6DetailsAfterSSIDTransition;
@property (TB,V_isRtCoexOptimal) isRtCoexOptimal;
@property (T@"NSDate",&,V_firstRtCoexOptimal) firstRtCoexOptimal;
@property (T@"NSDate",&,V_lastRtCoexOptimalStatusChange) lastRtCoexOptimalStatusChange;
@property (Td,V_rtCoexInOptimalDuration) rtCoexInOptimalDuration;
@property (T@"NSDate",&,V_lastEnterPreferredChannel) lastEnterPreferredChannel;
@property (Td,V_preferredChannelDuration) preferredChannelDuration;
@property (T@"NSDate",&,V_lastEnterPreferredBand) lastEnterPreferredBand;
@property (Td,V_preferredBandDuration) preferredBandDuration;
@property (T@"NSDate",&,V_firstSSIDTransition) firstSSIDTransition;
@property (T@"NSDate",&,V_firstIPUpdateAfterSSIDTransition) firstIPUpdateAfterSSIDTransition;
@property (T@"NSDate",&,V_firstManualJoin) firstManualJoin;
@property (T@"NSDate",&,V_firstManualJoinAfterSSIDTransition) firstManualJoinAfterSSIDTransition;
@property (TQ,V_requestSteerToPreferredChannelCount) requestSteerToPreferredChannelCount;
@property (TQ,V_requestSteerCount) requestSteerCount;
@property (TQ,V_requestDisconnectCount) requestDisconnectCount;
```

## Instance methods

```
-[WiFiUsageRealTimeCoexSession setHasCandidates:];
-[WiFiUsageRealTimeCoexSession setFirstManualJoin:];
-[WiFiUsageRealTimeCoexSession requestSteerCount];
-[WiFiUsageRealTimeCoexSession setIsRtCoexOptimal:];
-[WiFiUsageRealTimeCoexSession lastEnterPreferredChannel];
-[WiFiUsageRealTimeCoexSession preferredBandDuration];
-[WiFiUsageRealTimeCoexSession setRequestSteerToPreferredChannelCount:];
-[WiFiUsageRealTimeCoexSession processIPv4Changes:];
-[WiFiUsageRealTimeCoexSession rtCoexType];
-[WiFiUsageRealTimeCoexSession setLastRequestPreferredBand:];
-[WiFiUsageRealTimeCoexSession firstIPUpdateAfterSSIDTransition];
-[WiFiUsageRealTimeCoexSession lastEnterPreferredBand];
-[WiFiUsageRealTimeCoexSession requestSteerToPreferredChannelCount];
-[WiFiUsageRealTimeCoexSession hasDifferentIpv4DetailsAfterSSIDTransition];
-[WiFiUsageRealTimeCoexSession hasCandidates];
-[WiFiUsageRealTimeCoexSession isSplitSSID];
-[WiFiUsageRealTimeCoexSession metricName];
-[WiFiUsageRealTimeCoexSession updateAssociatedNetworkDetails:];
-[WiFiUsageRealTimeCoexSession firstManualJoin];
-[WiFiUsageRealTimeCoexSession lastRequestPreferredBand];
-[WiFiUsageRealTimeCoexSession requestDisconnectCount];
-[WiFiUsageRealTimeCoexSession lastRequestPreferredBSS];
-[WiFiUsageRealTimeCoexSession setFirstRtCoexOptimal:];
-[WiFiUsageRealTimeCoexSession setRealtimeCoexStarted:type:reasons:];
-[WiFiUsageRealTimeCoexSession isRtCoexOptimal];
-[WiFiUsageRealTimeCoexSession setPreferredChannelAndBandUsageWithReferenceDate:];
-[WiFiUsageRealTimeCoexSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:];
-[WiFiUsageRealTimeCoexSession firstManualJoinAfterSSIDTransition];
-[WiFiUsageRealTimeCoexSession eventDictionary:];
-[WiFiUsageRealTimeCoexSession summarizeSession];
-[WiFiUsageRealTimeCoexSession preferredChannelDuration];
-[WiFiUsageRealTimeCoexSession setLastRequestDifferentSSID:];
-[WiFiUsageRealTimeCoexSession setRtCoexSubType:];
-[WiFiUsageRealTimeCoexSession setLastRtCoexOptimalStatusChange:];
-[WiFiUsageRealTimeCoexSession setPreferredChannelDuration:];
-[WiFiUsageRealTimeCoexSession lastRequestPreferredSSID];
-[WiFiUsageRealTimeCoexSession initWithInterfaceName:andCapabilities:];
-[WiFiUsageRealTimeCoexSession updatePreferredChannelAndBandUsageWithReferenceDate:];
-[WiFiUsageRealTimeCoexSession setHasDifferentIpv6DetailsAfterSSIDTransition:];
-[WiFiUsageRealTimeCoexSession setLastRequestPreferredSSID:];
-[WiFiUsageRealTimeCoexSession lastRtCoexOptimalStatusChange];
-[WiFiUsageRealTimeCoexSession setLastRequestType:];
-[WiFiUsageRealTimeCoexSession lastRequestType];
-[WiFiUsageRealTimeCoexSession setLastRequestPreferredChannel:];
-[WiFiUsageRealTimeCoexSession setRequestSteerCount:];
-[WiFiUsageRealTimeCoexSession hasDifferentIpv6DetailsAfterSSIDTransition];
-[WiFiUsageRealTimeCoexSession eventDictionaryByBand:isFirst:];
-[WiFiUsageRealTimeCoexSession setLastEnterPreferredChannel:];
-[WiFiUsageRealTimeCoexSession isCurrentChannelPreferredChannel];
-[WiFiUsageRealTimeCoexSession setPreferredBandDuration:];
-[WiFiUsageRealTimeCoexSession sessionDidStart];
-[WiFiUsageRealTimeCoexSession setRtCoexInOptimalDuration:];
-[WiFiUsageRealTimeCoexSession joinStateDidChange:withReason:lastDisconnectReason:lastJoinFailure:andNetworkDetails:];
-[WiFiUsageRealTimeCoexSession lastRequestDifferentSSID];
-[WiFiUsageRealTimeCoexSession rtCoexSubType];
-[WiFiUsageRealTimeCoexSession isCurrentBandPreferredBand];
-[WiFiUsageRealTimeCoexSession processIPv6Changes:];
-[WiFiUsageRealTimeCoexSession setHasDifferentIpv4DetailsAfterSSIDTransition:];
-[WiFiUsageRealTimeCoexSession rtCoexInOptimalDuration];
-[WiFiUsageRealTimeCoexSession setIsSplitSSID:];
-[WiFiUsageRealTimeCoexSession copyWithZone:];
-[WiFiUsageRealTimeCoexSession setRequestDisconnectCount:];
-[WiFiUsageRealTimeCoexSession infraIsPartOfSplitSSID];
-[WiFiUsageRealTimeCoexSession setSteeringRequest:preferredChannel:preferredBand:preferredSSID:targetSSIDDiffersFromCurrent:preferredBSS:ssidIsSplit:transitionCandidates:];
-[WiFiUsageRealTimeCoexSession setFirstManualJoinAfterSSIDTransition:];
-[WiFiUsageRealTimeCoexSession setLastRequestPreferredBSS:];
-[WiFiUsageRealTimeCoexSession setRealTimeCoexStatus:type:];
-[WiFiUsageRealTimeCoexSession setFirstSSIDTransition:];
-[WiFiUsageRealTimeCoexSession setFirstIPUpdateAfterSSIDTransition:];
-[WiFiUsageRealTimeCoexSession updateRtCoexInOptimalDuration:];
-[WiFiUsageRealTimeCoexSession setRtCoexType:];
-[WiFiUsageRealTimeCoexSession lastRequestPreferredChannel];
-[WiFiUsageRealTimeCoexSession setLastEnterPreferredBand:];
-[WiFiUsageRealTimeCoexSession firstRtCoexOptimal];
-[WiFiUsageRealTimeCoexSession firstSSIDTransition];
```
