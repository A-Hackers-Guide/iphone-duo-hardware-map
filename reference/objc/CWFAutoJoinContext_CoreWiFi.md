# `CWFAutoJoinContext`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 38 instance variables, 38 properties, 80 instance methods, 0 class methods

## Instance variables

```
B _BSSChannelsOnly;
B _passiveScan;
B _cacheOnly;
B _useCacheBeforeScan;
B _useCacheForPreviouslyScannedChannels;
B _includeAdjacent5GHzChannel;
B _includeOnlyRemaining5GHzChannels;
B _allowStandalone6GHz;
B _include6GHzChannels;
B _alwaysIncludeRemainingNon2GHzChannels;
B _allowDeferredCandidates;
B _allowRecentlyJoinedDeferrableCandidates;
B _didForceAllRemainingChannels;
B _skipRemainingNon2GHzChannelsUnlessKnownNetworkFound;
B _preferUserConfiguredNetworks;
B _allowSSIDBasedMatchingForPasspointNetworks;
B _skipMorePreferredNetworkDiscovery;
B _skip6GHzFollowupScan;
B _skip6GHzSameSSIDFollowupScan;
B _prioritize6GHzChannel;
@"CWFAutoJoinParameters" _autoJoinParameters;
@"NSOrderedSet" _knownNetworks;
@"NSArray" _recentChannelList;
@"NSArray" _remainingChannelList;
@"NSArray" _SSIDList;
@"NSArray" _ANQPElementIDList;
Q _maxScanChannelCount;
Q _maxBSSChannelCount;
Q _maxBSSChannelAge;
Q _maxScanSSIDCount;
Q _maxHiddenKnownNetworkSSIDAge;
Q _maxScanCacheAge;
Q _maxANQPCacheAge;
Q _maxScanCycles;
q _minRSSI;
Q _dwellTime;
d _minBSSLocationAccuracy;
d _maxBSSLocationDistance;
```

## Properties

```
@property (T@"CWFAutoJoinParameters",C,N,V_autoJoinParameters) autoJoinParameters;
@property (T@"NSOrderedSet",C,N,V_knownNetworks) knownNetworks;
@property (T@"NSArray",C,N,V_recentChannelList) recentChannelList;
@property (T@"NSArray",C,N,V_remainingChannelList) remainingChannelList;
@property (T@"NSArray",C,N,V_SSIDList) SSIDList;
@property (T@"NSArray",C,N,V_ANQPElementIDList) ANQPElementIDList;
@property (TQ,N,V_maxScanChannelCount) maxScanChannelCount;
@property (TB,N,V_BSSChannelsOnly) BSSChannelsOnly;
@property (TQ,N,V_maxBSSChannelCount) maxBSSChannelCount;
@property (TQ,N,V_maxBSSChannelAge) maxBSSChannelAge;
@property (TQ,N,V_maxScanSSIDCount) maxScanSSIDCount;
@property (TQ,N,V_maxHiddenKnownNetworkSSIDAge) maxHiddenKnownNetworkSSIDAge;
@property (TQ,N,V_maxScanCacheAge) maxScanCacheAge;
@property (TQ,N,V_maxANQPCacheAge) maxANQPCacheAge;
@property (TQ,N,V_maxScanCycles) maxScanCycles;
@property (Tq,N,V_minRSSI) minRSSI;
@property (TQ,N,V_dwellTime) dwellTime;
@property (TB,N,V_passiveScan) passiveScan;
@property (TB,N,V_cacheOnly) cacheOnly;
@property (TB,N,V_useCacheBeforeScan) useCacheBeforeScan;
@property (TB,N,V_useCacheForPreviouslyScannedChannels) useCacheForPreviouslyScannedChannels;
@property (Td,N,V_minBSSLocationAccuracy) minBSSLocationAccuracy;
@property (Td,N,V_maxBSSLocationDistance) maxBSSLocationDistance;
@property (TB,N,V_includeAdjacent5GHzChannel) includeAdjacent5GHzChannel;
@property (TB,N,V_includeOnlyRemaining5GHzChannels) includeOnlyRemaining5GHzChannels;
@property (TB,N,V_allowStandalone6GHz) allowStandalone6GHz;
@property (TB,N,V_include6GHzChannels) include6GHzChannels;
@property (TB,N,V_alwaysIncludeRemainingNon2GHzChannels) alwaysIncludeRemainingNon2GHzChannels;
@property (TB,N,V_allowDeferredCandidates) allowDeferredCandidates;
@property (TB,N,V_allowRecentlyJoinedDeferrableCandidates) allowRecentlyJoinedDeferrableCandidates;
@property (TB,N,V_didForceAllRemainingChannels) didForceAllRemainingChannels;
@property (TB,N,V_skipRemainingNon2GHzChannelsUnlessKnownNetworkFound) skipRemainingNon2GHzChannelsUnlessKnownNetworkFound;
@property (TB,N,V_preferUserConfiguredNetworks) preferUserConfiguredNetworks;
@property (TB,N,V_allowSSIDBasedMatchingForPasspointNetworks) allowSSIDBasedMatchingForPasspointNetworks;
@property (TB,N,V_skipMorePreferredNetworkDiscovery) skipMorePreferredNetworkDiscovery;
@property (TB,N,V_skip6GHzFollowupScan) skip6GHzFollowupScan;
@property (TB,N,V_skip6GHzSameSSIDFollowupScan) skip6GHzSameSSIDFollowupScan;
@property (TB,N,V_prioritize6GHzChannel) prioritize6GHzChannel;
```

## Instance methods

```
-[CWFAutoJoinContext cacheOnly];
-[CWFAutoJoinContext setIncludeAdjacent5GHzChannel:];
-[CWFAutoJoinContext alwaysIncludeRemainingNon2GHzChannels];
-[CWFAutoJoinContext setMaxBSSChannelAge:];
-[CWFAutoJoinContext useCacheBeforeScan];
-[CWFAutoJoinContext isEqualToAutoJoinContext:];
-[CWFAutoJoinContext maxBSSChannelAge];
-[CWFAutoJoinContext setAutoJoinParameters:];
-[CWFAutoJoinContext SSIDList];
-[CWFAutoJoinContext setIncludeOnlyRemaining5GHzChannels:];
-[CWFAutoJoinContext maxBSSChannelCount];
-[CWFAutoJoinContext knownNetworks];
-[CWFAutoJoinContext maxHiddenKnownNetworkSSIDAge];
-[CWFAutoJoinContext dwellTime];
-[CWFAutoJoinContext passiveScan];
-[CWFAutoJoinContext maxScanCycles];
-[CWFAutoJoinContext setAlwaysIncludeRemainingNon2GHzChannels:];
-[CWFAutoJoinContext setMaxBSSChannelCount:];
-[CWFAutoJoinContext setAllowSSIDBasedMatchingForPasspointNetworks:];
-[CWFAutoJoinContext includeOnlyRemaining5GHzChannels];
-[CWFAutoJoinContext setDidForceAllRemainingChannels:];
-[CWFAutoJoinContext BSSChannelsOnly];
-[CWFAutoJoinContext setPassiveScan:];
-[CWFAutoJoinContext setDwellTime:];
-[CWFAutoJoinContext includeAdjacent5GHzChannel];
-[CWFAutoJoinContext maxScanCacheAge];
-[CWFAutoJoinContext ANQPElementIDList];
-[CWFAutoJoinContext setBSSChannelsOnly:];
-[CWFAutoJoinContext setUseCacheForPreviouslyScannedChannels:];
-[CWFAutoJoinContext setAllowDeferredCandidates:];
-[CWFAutoJoinContext setMaxHiddenKnownNetworkSSIDAge:];
-[CWFAutoJoinContext setMaxScanChannelCount:];
-[CWFAutoJoinContext allowStandalone6GHz];
-[CWFAutoJoinContext allowRecentlyJoinedDeferrableCandidates];
-[CWFAutoJoinContext setANQPElementIDList:];
-[CWFAutoJoinContext setSkip6GHzFollowupScan:];
-[CWFAutoJoinContext allowDeferredCandidates];
-[CWFAutoJoinContext setRemainingChannelList:];
-[CWFAutoJoinContext allowSSIDBasedMatchingForPasspointNetworks];
-[CWFAutoJoinContext setAllowStandalone6GHz:];
-[CWFAutoJoinContext maxBSSLocationDistance];
-[CWFAutoJoinContext didForceAllRemainingChannels];
-[CWFAutoJoinContext setCacheOnly:];
-[CWFAutoJoinContext setPreferUserConfiguredNetworks:];
-[CWFAutoJoinContext maxANQPCacheAge];
-[CWFAutoJoinContext skip6GHzFollowupScan];
-[CWFAutoJoinContext setMinBSSLocationAccuracy:];
-[CWFAutoJoinContext maxScanChannelCount];
-[CWFAutoJoinContext setUseCacheBeforeScan:];
-[CWFAutoJoinContext setInclude6GHzChannels:];
-[CWFAutoJoinContext include6GHzChannels];
-[CWFAutoJoinContext useCacheForPreviouslyScannedChannels];
-[CWFAutoJoinContext minBSSLocationAccuracy];
-[CWFAutoJoinContext setMaxScanSSIDCount:];
-[CWFAutoJoinContext skip6GHzSameSSIDFollowupScan];
-[CWFAutoJoinContext autoJoinParameters];
-[CWFAutoJoinContext setKnownNetworks:];
-[CWFAutoJoinContext setMaxANQPCacheAge:];
-[CWFAutoJoinContext hash];
-[CWFAutoJoinContext setMinRSSI:];
-[CWFAutoJoinContext setSkipRemainingNon2GHzChannelsUnlessKnownNetworkFound:];
-[CWFAutoJoinContext setRecentChannelList:];
-[CWFAutoJoinContext setSkip6GHzSameSSIDFollowupScan:];
-[CWFAutoJoinContext remainingChannelList];
-[CWFAutoJoinContext setSSIDList:];
-[CWFAutoJoinContext setAllowRecentlyJoinedDeferrableCandidates:];
-[CWFAutoJoinContext minRSSI];
-[CWFAutoJoinContext setMaxBSSLocationDistance:];
-[CWFAutoJoinContext recentChannelList];
-[CWFAutoJoinContext copyWithZone:];
-[CWFAutoJoinContext setMaxScanCycles:];
-[CWFAutoJoinContext isEqual:];
-[CWFAutoJoinContext prioritize6GHzChannel];
-[CWFAutoJoinContext setSkipMorePreferredNetworkDiscovery:];
-[CWFAutoJoinContext setPrioritize6GHzChannel:];
-[CWFAutoJoinContext setMaxScanCacheAge:];
-[CWFAutoJoinContext maxScanSSIDCount];
-[CWFAutoJoinContext skipMorePreferredNetworkDiscovery];
-[CWFAutoJoinContext preferUserConfiguredNetworks];
-[CWFAutoJoinContext skipRemainingNon2GHzChannelsUnlessKnownNetworkFound];
```
