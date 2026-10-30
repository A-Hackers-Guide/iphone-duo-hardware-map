# `WiFiUsagePowerAnalytics`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 21 properties, 79 instance methods, 0 class methods

## Instance variables

```
B _mloConnection;
B _lpEmlsrSupported;
B _instantHotspotActive;
B _nonInstantHotspotActive;
B _nanHotspotActive;
B _lastHotspotStateValue;
i _cachedPhyMode;
@"NSString" _interfaceName;
@"NSDictionary" _baselinePowerStats;
@"NSDate" _lastCollectionTime;
@"NSDate" _lastSubmissionTime;
@"WiFiUsageInterfaceStats" _baselineIfStats;
^{_Apple80211=} _apple80211Ref;
@"NSMutableDictionary" _rateLimitTracker;
@"NSMutableArray" _recentCollectionTimes;
@"NSObject<OS_dispatch_queue>" _internalQueue;
Q _numHotspotClientsEmlsr;
Q _numHotspotClientsNonEmlsr;
d _lastAssociatedDurationSec;
@"NSDate" _hotspotStartTime;
q _lastHotspotType;
```

## Properties

```
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T^{_Apple80211=},N,V_apple80211Ref) apple80211Ref;
@property (T@"NSMutableDictionary",&,N,V_rateLimitTracker) rateLimitTracker;
@property (T@"NSMutableArray",&,N,V_recentCollectionTimes) recentCollectionTimes;
@property (T@"NSDictionary",&,N,V_baselinePowerStats) baselinePowerStats;
@property (T@"NSDate",&,N,V_lastCollectionTime) lastCollectionTime;
@property (T@"NSDate",&,N,V_lastSubmissionTime) lastSubmissionTime;
@property (T@"WiFiUsageInterfaceStats",&,N,V_baselineIfStats) baselineIfStats;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_internalQueue) internalQueue;
@property (TB,N,V_mloConnection) mloConnection;
@property (TB,N,V_lpEmlsrSupported) lpEmlsrSupported;
@property (TQ,N,V_numHotspotClientsEmlsr) numHotspotClientsEmlsr;
@property (TQ,N,V_numHotspotClientsNonEmlsr) numHotspotClientsNonEmlsr;
@property (Ti,N,V_cachedPhyMode) cachedPhyMode;
@property (Td,N,V_lastAssociatedDurationSec) lastAssociatedDurationSec;
@property (T@"NSDate",&,N,V_hotspotStartTime) hotspotStartTime;
@property (TB,N,V_instantHotspotActive) instantHotspotActive;
@property (TB,N,V_nonInstantHotspotActive) nonInstantHotspotActive;
@property (TB,N,V_nanHotspotActive) nanHotspotActive;
@property (TB,N,V_lastHotspotStateValue) lastHotspotStateValue;
@property (Tq,N,V_lastHotspotType) lastHotspotType;
```

## Instance methods

```
-[WiFiUsagePowerAnalytics stringFromValue:];
-[WiFiUsagePowerAnalytics currentBssInformationFromMonitor:];
-[WiFiUsagePowerAnalytics setRecentCollectionTimes:];
-[WiFiUsagePowerAnalytics setCachedPhyMode:];
-[WiFiUsagePowerAnalytics instantHotspotActive];
-[WiFiUsagePowerAnalytics internalCleanupOldCollectionTimes];
-[WiFiUsagePowerAnalytics extractMloLinkInfo:];
-[WiFiUsagePowerAnalytics setNumHotspotClientsNonEmlsr:];
-[WiFiUsagePowerAnalytics cleanupOldCollectionTimes];
-[WiFiUsagePowerAnalytics mloConnection];
-[WiFiUsagePowerAnalytics deriveWiFiTechFromBss:];
-[WiFiUsagePowerAnalytics addInterfaceStatistics:toAnalyticsEvent:];
-[WiFiUsagePowerAnalytics internalOnHotspotStateChanged:requester:associatedDurationSec:];
-[WiFiUsagePowerAnalytics setHotspotStartTime:];
-[WiFiUsagePowerAnalytics setInterfaceName:];
-[WiFiUsagePowerAnalytics dealloc];
-[WiFiUsagePowerAnalytics updateRateLimitTracker:];
-[WiFiUsagePowerAnalytics baselinePowerStats];
-[WiFiUsagePowerAnalytics internalUpdateRateLimitTracker:];
-[WiFiUsagePowerAnalytics detectCounterReset:fromBaseline:];
-[WiFiUsagePowerAnalytics internalShouldCollectAnalytics:];
-[WiFiUsagePowerAnalytics setLpEmlsrSupported:];
-[WiFiUsagePowerAnalytics rateLimitTracker];
-[WiFiUsagePowerAnalytics interfaceName];
-[WiFiUsagePowerAnalytics cachedPhyMode];
-[WiFiUsagePowerAnalytics setLastSubmissionTime:];
-[WiFiUsagePowerAnalytics submitPowerAnalyticsWithDeltas:ifStatsDeltas:dimension:deltaTime:currentValue:associatedDurationSec:];
-[WiFiUsagePowerAnalytics lpEmlsrSupported];
-[WiFiUsagePowerAnalytics collectCurrentNetworkInfo];
-[WiFiUsagePowerAnalytics setBaselineIfStats:];
-[WiFiUsagePowerAnalytics numHotspotClientsEmlsr];
-[WiFiUsagePowerAnalytics setLastAssociatedDurationSec:];
-[WiFiUsagePowerAnalytics setInstantHotspotActive:];
-[WiFiUsagePowerAnalytics setLastHotspotStateValue:];
-[WiFiUsagePowerAnalytics createInstantCounterMapping];
-[WiFiUsagePowerAnalytics lastHotspotStateValue];
-[WiFiUsagePowerAnalytics collectPowerDebugInfo];
-[WiFiUsagePowerAnalytics setNonInstantHotspotActive:];
-[WiFiUsagePowerAnalytics computeDeltaForKey:current:baseline:];
-[WiFiUsagePowerAnalytics hotspotStartTime];
-[WiFiUsagePowerAnalytics addEMLSRToggleCounts:toAnalyticsEvent:];
-[WiFiUsagePowerAnalytics shouldCollectAnalytics:];
-[WiFiUsagePowerAnalytics internalResetBaseline];
-[WiFiUsagePowerAnalytics initWithInterfaceName:];
-[WiFiUsagePowerAnalytics classifyHotspotTypeForRequester:hotspotType:hotspotStateProperty:dimensionName:];
-[WiFiUsagePowerAnalytics lastHotspotType];
-[WiFiUsagePowerAnalytics setLastCollectionTime:];
-[WiFiUsagePowerAnalytics cachePhyMode:];
-[WiFiUsagePowerAnalytics setLastHotspotType:];
-[WiFiUsagePowerAnalytics setApple80211Ref:];
-[WiFiUsagePowerAnalytics nanHotspotActive];
-[WiFiUsagePowerAnalytics lastCollectionTime];
-[WiFiUsagePowerAnalytics bandStringFromFrequencyBand:];
-[WiFiUsagePowerAnalytics isCumulativeCounterKey:];
-[WiFiUsagePowerAnalytics isSessionBasedDimension:];
-[WiFiUsagePowerAnalytics setInternalQueue:];
-[WiFiUsagePowerAnalytics lastAssociatedDurationSec];
-[WiFiUsagePowerAnalytics lastSubmissionTime];
-[WiFiUsagePowerAnalytics internalOnSystemStateChanged:currentValue:associatedDurationSec:];
-[WiFiUsagePowerAnalytics applyInstantCounterMappings:toAnalyticsEvent:withMapping:];
-[WiFiUsagePowerAnalytics baselineIfStats];
-[WiFiUsagePowerAnalytics computeDeltaStats:fromBaseline:];
-[WiFiUsagePowerAnalytics onHotspotStateChanged:requester:associatedDurationSec:];
-[WiFiUsagePowerAnalytics setRateLimitTracker:];
-[WiFiUsagePowerAnalytics setMloConnection:];
-[WiFiUsagePowerAnalytics currentSystemDimensionStatesForTrigger:];
-[WiFiUsagePowerAnalytics setNumHotspotClientsEmlsr:];
-[WiFiUsagePowerAnalytics computeIfStatsDeltas:fromBaseline:deltaTime:];
-[WiFiUsagePowerAnalytics onSystemStateChanged:currentValue:associatedDurationSec:];
-[WiFiUsagePowerAnalytics apple80211Ref];
-[WiFiUsagePowerAnalytics numHotspotClientsNonEmlsr];
-[WiFiUsagePowerAnalytics nonInstantHotspotActive];
-[WiFiUsagePowerAnalytics setBaselinePowerStats:];
-[WiFiUsagePowerAnalytics addMappedInstantCounters:fromDeltas:];
-[WiFiUsagePowerAnalytics internalQueue];
-[WiFiUsagePowerAnalytics recentCollectionTimes];
-[WiFiUsagePowerAnalytics setNanHotspotActive:];
-[WiFiUsagePowerAnalytics updateHotspotSessionAndGetDuration:currentValue:];
-[WiFiUsagePowerAnalytics resetBaseline];
```
