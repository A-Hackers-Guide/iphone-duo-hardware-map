# `WiFiUsageRoamingSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WiFiUsageSession`
- 31 instance variables, 31 properties, 83 instance methods, 0 class methods

## Instance variables

```
B _hasFwRoamDurations;
B _hasAirInfo;
B _hasAttemptedRoamToRSNO;
B _hasAttemptedRoamToMRSNO;
B _hasFailedRoamToRSNO;
B _hasFailedRoamToMRSNO;
@"NSDate" _lastRoamStartTime;
@"NSDate" _lastSuccessfulRoamTime;
Q _bandsInDeployment;
Q _numChannelsScanned;
Q _roamScanDurationInMs;
Q _numVeryLowRssiAttempts;
Q _numRoamsToLowerRSSI;
Q _numRoamsWithWiFiPrimary;
Q _numRoamsNoARP;
Q _fwRoamDurationInMs;
Q _fwRoamScanDurationInMs;
Q _numRoamsWithAirRecommendedChannel;
Q _numRoamsWithAirGuessr;
@"NSDate" _inWiFi1BarEntryTime;
@"NSDate" _inWiFi2BarEntryTime;
@"NSDate" _inWiFi3BarEntryTime;
@"NSDate" _inWiFiPrimaryEntryTime;
d _inWiFi1BarDuration;
d _inWiFi2BarDuration;
d _inWiFi3BarDuration;
d _inWiFiPrimaryDuration;
@"NSMutableDictionary" _roamProfileCounts;
Q _sessionEndReason;
@"NSMutableDictionary" _failedRoamReasonCounts;
@"NSMutableArray" _originRSSIValues;
```

## Properties

```
@property (T@"NSDate",&,N,V_lastRoamStartTime) lastRoamStartTime;
@property (T@"NSDate",&,N,V_lastSuccessfulRoamTime) lastSuccessfulRoamTime;
@property (TQ,N,V_bandsInDeployment) bandsInDeployment;
@property (TQ,N,V_numChannelsScanned) numChannelsScanned;
@property (TQ,N,V_roamScanDurationInMs) roamScanDurationInMs;
@property (TQ,N,V_numVeryLowRssiAttempts) numVeryLowRssiAttempts;
@property (TQ,N,V_numRoamsToLowerRSSI) numRoamsToLowerRSSI;
@property (TQ,N,V_numRoamsWithWiFiPrimary) numRoamsWithWiFiPrimary;
@property (TQ,N,V_numRoamsNoARP) numRoamsNoARP;
@property (TQ,N,V_fwRoamDurationInMs) fwRoamDurationInMs;
@property (TQ,N,V_fwRoamScanDurationInMs) fwRoamScanDurationInMs;
@property (TQ,N,V_numRoamsWithAirRecommendedChannel) numRoamsWithAirRecommendedChannel;
@property (TQ,N,V_numRoamsWithAirGuessr) numRoamsWithAirGuessr;
@property (TB,N,V_hasFwRoamDurations) hasFwRoamDurations;
@property (TB,N,V_hasAirInfo) hasAirInfo;
@property (TB,N,V_hasAttemptedRoamToRSNO) hasAttemptedRoamToRSNO;
@property (TB,N,V_hasAttemptedRoamToMRSNO) hasAttemptedRoamToMRSNO;
@property (TB,N,V_hasFailedRoamToRSNO) hasFailedRoamToRSNO;
@property (TB,N,V_hasFailedRoamToMRSNO) hasFailedRoamToMRSNO;
@property (T@"NSDate",&,N,V_inWiFi1BarEntryTime) inWiFi1BarEntryTime;
@property (T@"NSDate",&,N,V_inWiFi2BarEntryTime) inWiFi2BarEntryTime;
@property (T@"NSDate",&,N,V_inWiFi3BarEntryTime) inWiFi3BarEntryTime;
@property (T@"NSDate",&,N,V_inWiFiPrimaryEntryTime) inWiFiPrimaryEntryTime;
@property (Td,N,V_inWiFi1BarDuration) inWiFi1BarDuration;
@property (Td,N,V_inWiFi2BarDuration) inWiFi2BarDuration;
@property (Td,N,V_inWiFi3BarDuration) inWiFi3BarDuration;
@property (Td,N,V_inWiFiPrimaryDuration) inWiFiPrimaryDuration;
@property (T@"NSMutableDictionary",&,N,V_roamProfileCounts) roamProfileCounts;
@property (TQ,N,V_sessionEndReason) sessionEndReason;
@property (T@"NSMutableDictionary",&,N,V_failedRoamReasonCounts) failedRoamReasonCounts;
@property (T@"NSMutableArray",&,N,V_originRSSIValues) originRSSIValues;
```

## Instance methods

```
-[WiFiUsageRoamingSession sessionDidEnd];
-[WiFiUsageRoamingSession setInWiFi3BarDuration:];
-[WiFiUsageRoamingSession numRoamsWithAirRecommendedChannel];
-[WiFiUsageRoamingSession setNumVeryLowRssiAttempts:];
-[WiFiUsageRoamingSession bandsInDeployment];
-[WiFiUsageRoamingSession fwRoamScanDurationInMs];
-[WiFiUsageRoamingSession setHasAttemptedRoamToMRSNO:];
-[WiFiUsageRoamingSession setHasFailedRoamToMRSNO:];
-[WiFiUsageRoamingSession inWiFi2BarEntryTime];
-[WiFiUsageRoamingSession setNumRoamsNoARP:];
-[WiFiUsageRoamingSession linkQualityDidChange:];
-[WiFiUsageRoamingSession setRoamScanDurationInMs:];
-[WiFiUsageRoamingSession setHasAttemptedRoamToRSNO:];
-[WiFiUsageRoamingSession lastRoamStartTime];
-[WiFiUsageRoamingSession inWiFiPrimaryEntryTime];
-[WiFiUsageRoamingSession interfaceRankingDidChange:];
-[WiFiUsageRoamingSession metricName];
-[WiFiUsageRoamingSession inWiFiPrimaryDuration];
-[WiFiUsageRoamingSession setFwRoamDurationInMs:];
-[WiFiUsageRoamingSession failedRoamReasonCounts];
-[WiFiUsageRoamingSession setHasFwRoamDurations:];
-[WiFiUsageRoamingSession setLastSuccessfulRoamTime:];
-[WiFiUsageRoamingSession numRoamsWithAirGuessr];
-[WiFiUsageRoamingSession originRSSIValues];
-[WiFiUsageRoamingSession getMostCommonMotionStatus];
-[WiFiUsageRoamingSession numVeryLowRssiAttempts];
-[WiFiUsageRoamingSession setOriginRSSIValues:];
-[WiFiUsageRoamingSession hasFwRoamDurations];
-[WiFiUsageRoamingSession fwRoamDurationInMs];
-[WiFiUsageRoamingSession hasFailedRoamToMRSNO];
-[WiFiUsageRoamingSession setInWiFiPrimaryDuration:];
-[WiFiUsageRoamingSession sessionEndReason];
-[WiFiUsageRoamingSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:];
-[WiFiUsageRoamingSession eventDictionary:];
-[WiFiUsageRoamingSession summarizeSession];
-[WiFiUsageRoamingSession setInWiFi1BarDuration:];
-[WiFiUsageRoamingSession calculatePercentage:denominator:];
-[WiFiUsageRoamingSession setInWiFi2BarEntryTime:];
-[WiFiUsageRoamingSession inWiFi3BarEntryTime];
-[WiFiUsageRoamingSession getMostCommonRoamProfile];
-[WiFiUsageRoamingSession initWithInterfaceName:andCapabilities:];
-[WiFiUsageRoamingSession setSessionEndReason:];
-[WiFiUsageRoamingSession setFailedRoamReasonCounts:];
-[WiFiUsageRoamingSession hasFailedRoamToRSNO];
-[WiFiUsageRoamingSession hasAttemptedRoamToRSNO];
-[WiFiUsageRoamingSession systemWakeStateDidChange:wokenByWiFi:];
-[WiFiUsageRoamingSession setRoamProfileCounts:];
-[WiFiUsageRoamingSession roamScanDurationInMs];
-[WiFiUsageRoamingSession setNumChannelsScanned:];
-[WiFiUsageRoamingSession hasAttemptedRoamToMRSNO];
-[WiFiUsageRoamingSession sessionDidStart];
-[WiFiUsageRoamingSession numRoamsToLowerRSSI];
-[WiFiUsageRoamingSession setNumRoamsWithWiFiPrimary:];
-[WiFiUsageRoamingSession inWiFi3BarDuration];
-[WiFiUsageRoamingSession setHasFailedRoamToRSNO:];
-[WiFiUsageRoamingSession roamingStateDidChange:reason:andStatus:andLatency:andRoamData:andPingPongStats:];
-[WiFiUsageRoamingSession numChannelsScanned];
-[WiFiUsageRoamingSession numRoamsWithWiFiPrimary];
-[WiFiUsageRoamingSession setNumRoamsToLowerRSSI:];
-[WiFiUsageRoamingSession setInWiFi2BarDuration:];
-[WiFiUsageRoamingSession getMostCommonFailedRoamReason];
-[WiFiUsageRoamingSession hasAirInfo];
-[WiFiUsageRoamingSession populateBandsInDeployment];
-[WiFiUsageRoamingSession setLastRoamStartTime:];
-[WiFiUsageRoamingSession setBandsInDeployment:];
-[WiFiUsageRoamingSession copyWithZone:];
-[WiFiUsageRoamingSession inWiFi1BarEntryTime];
-[WiFiUsageRoamingSession setFwRoamScanDurationInMs:];
-[WiFiUsageRoamingSession setInWiFiPrimaryEntryTime:];
-[WiFiUsageRoamingSession roamProfileCounts];
-[WiFiUsageRoamingSession inWiFi1BarDuration];
-[WiFiUsageRoamingSession faultEventDetected:event:];
-[WiFiUsageRoamingSession setNumRoamsWithAirGuessr:];
-[WiFiUsageRoamingSession setInWiFi1BarEntryTime:];
-[WiFiUsageRoamingSession setHasAirInfo:];
-[WiFiUsageRoamingSession getUsedRoamProfilesBitmask];
-[WiFiUsageRoamingSession setNumRoamsWithAirRecommendedChannel:];
-[WiFiUsageRoamingSession getMostCommonRoamReason];
-[WiFiUsageRoamingSession inWiFi2BarDuration];
-[WiFiUsageRoamingSession computeOriginRSSIP50];
-[WiFiUsageRoamingSession lastSuccessfulRoamTime];
-[WiFiUsageRoamingSession numRoamsNoARP];
-[WiFiUsageRoamingSession setInWiFi3BarEntryTime:];
```
