# `WiFiUsageLinkSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageSession`
- 29 instance variables, 3 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _linkUp;
@"NSDate" _lastLinkTest;
@"NSDate" _lastFaultIndicationTime;
B _didBecomePrimary;
@"NSString" _ssid;
@"NSString" _bssid;
Q _numLinkTestFailures;
B _didHandleFaultEvent;
B _foundSuccessfulLinkTest;
Q _numLinkRecoverySkips;
Q _periodicLinkTestInterval;
@"NSDate" _lastFaultEventHandled;
@"NSString" _lastFaultEventHandledReason;
Q _lastFaultEventHandledOptions;
i _lastFaultEventHandledTrafficClass;
i _band;
@"NSMutableDictionary" _linkTestResult;
Q _joinSeqNo;
@"NSMutableArray" _deferredFailureSessions;
Q _lastSubmittedSessionSeqNo;
B _joinAttemptedBeforeLinkDown;
Q _faultCountOnBss;
B _hasRSNOIE;
@"NSNumber" _hasMultipleRSNOIE;
@"NSNumber" _didRSNOFallback;
q _usedAKMType;
@"WiFiSoftError" _joinFailSoftError;
@"WiFiSoftError" _homeKitEAPFailSoftError;
@"WiFiSoftError" _faultEventSoftError;
```

## Properties

```
@property (T@"WiFiSoftError",&,N,V_joinFailSoftError) joinFailSoftError;
@property (T@"WiFiSoftError",&,N,V_homeKitEAPFailSoftError) homeKitEAPFailSoftError;
@property (T@"WiFiSoftError",&,N,V_faultEventSoftError) faultEventSoftError;
```

## Instance methods

```
-[WiFiUsageLinkSession handleFaultEventWithReason:];
-[WiFiUsageLinkSession processIPv4Changes:];
-[WiFiUsageLinkSession linkQualityDidChange:];
-[WiFiUsageLinkSession retryLinkTestInOneMinute];
-[WiFiUsageLinkSession interfaceRankingDidChange:];
-[WiFiUsageLinkSession metricName];
-[WiFiUsageLinkSession canSubmitToCA];
-[WiFiUsageLinkSession _fetchAuthTypeForInterface:];
-[WiFiUsageLinkSession updateLinkRecoveryDisabled:];
-[WiFiUsageLinkSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:];
-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:];
-[WiFiUsageLinkSession eventDictionary:];
-[WiFiUsageLinkSession initWithInterfaceName:andCapabilities:];
-[WiFiUsageLinkSession setHomeKitEAPFailSoftError:];
-[WiFiUsageLinkSession systemWakeStateDidChange:wokenByWiFi:];
-[WiFiUsageLinkSession useSavedJoinStats];
-[WiFiUsageLinkSession displayStateDidChange:];
-[WiFiUsageLinkSession rangingCompleted];
-[WiFiUsageLinkSession getLazyNSNumberPreference:exists:];
-[WiFiUsageLinkSession sessionDidStart];
-[WiFiUsageLinkSession setJoinFailSoftError:];
-[WiFiUsageLinkSession joinStateDidChange:withReason:lastDisconnectReason:lastJoinFailure:andNetworkDetails:];
-[WiFiUsageLinkSession updateLinkTestInterval:];
-[WiFiUsageLinkSession setFaultEventSoftError:];
-[WiFiUsageLinkSession processIPv6Changes:];
-[WiFiUsageLinkSession applicationStateDidChange:withAttributes:];
-[WiFiUsageLinkSession copyWithZone:];
-[WiFiUsageLinkSession processDHCPChanges:];
-[WiFiUsageLinkSession faultEventSoftError];
-[WiFiUsageLinkSession joinFailSoftError];
-[WiFiUsageLinkSession faultEventDetected:event:];
-[WiFiUsageLinkSession processDriverAvailability:available:version:flags:eventID:reason:subReason:minorReason:reasonString:];
-[WiFiUsageLinkSession addDictionary:withKeysPrefix:toFlatDictionary:];
-[WiFiUsageLinkSession homeKitEAPFailSoftError];
-[WiFiUsageLinkSession lockStateDidChange:];
```
