# `CWFScanParameters`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSPredicateVisitor`, `NSCopying`, `NSSecureCoding`
- 33 instance variables, 36 properties, 82 instance methods, 1 class methods

## Instance variables

```
B _mergeScanResults;
B _includeHiddenNetworks;
B _addScanDurationToMaxAge;
B _includeMatchingKnownNetworkProfiles;
B _exclude6GChannels;
B _includeBeaconCacheResults;
B _includeBackgroundScanCacheResults;
B _sortByAutoJoinPreference;
B _invalidPredicate;
i _BSSType;
i _PHYMode;
i _scanType;
@"NSArray" _channels;
@"NSString" _SSID;
Q _shortSSID;
@"NSArray" _SSIDList;
@"NSString" _BSSID;
Q _numberOfScans;
Q _restTime;
Q _dwellTime;
Q _acceptableCacheAge;
q _minimumRSSI;
Q _maximumAge;
Q _minimumTimestamp;
Q _scanFlags;
Q _excludeScanFlags;
@"NSSet" _includeProperties;
@"NSArray" _includeScanResults;
@"NSArray" _ANQPElementIDListForPasspointScanResults;
Q _acceptableANQPCacheAgeForPasspointScanResults;
Q _maximumANQPAgeForPasspointScanResults;
@"NSString" _matchNetworkNamePrefix;
@"NSPredicate" _filterPredicate;
```

## Properties

```
@property (TB,N,V_invalidPredicate) invalidPredicate;
@property (T@"NSArray",C,N,V_channels) channels;
@property (T@"NSString",C,N,V_SSID) SSID;
@property (TQ,N,V_shortSSID) shortSSID;
@property (T@"NSArray",C,N,V_SSIDList) SSIDList;
@property (T@"NSString",C,N,V_BSSID) BSSID;
@property (TQ,N,V_numberOfScans) numberOfScans;
@property (TQ,N,V_restTime) restTime;
@property (TQ,N,V_dwellTime) dwellTime;
@property (TQ,N,V_acceptableCacheAge) acceptableCacheAge;
@property (TQ,D,N) maximumCacheAge;
@property (TB,D,N) cacheOnly;
@property (Ti,N,V_BSSType) BSSType;
@property (Ti,N,V_PHYMode) PHYMode;
@property (Ti,N,V_scanType) scanType;
@property (Tq,N,V_minimumRSSI) minimumRSSI;
@property (TQ,N,V_maximumAge) maximumAge;
@property (TQ,N,V_minimumTimestamp) minimumTimestamp;
@property (TB,N,V_mergeScanResults) mergeScanResults;
@property (TB,N,V_includeHiddenNetworks) includeHiddenNetworks;
@property (TB,N,V_addScanDurationToMaxAge) addScanDurationToMaxAge;
@property (TQ,N,V_scanFlags) scanFlags;
@property (TQ,N,V_excludeScanFlags) excludeScanFlags;
@property (T@"NSSet",C,N,V_includeProperties) includeProperties;
@property (T@"NSArray",C,N,V_includeScanResults) includeScanResults;
@property (TB,N,V_includeMatchingKnownNetworkProfiles) includeMatchingKnownNetworkProfiles;
@property (T@"NSArray",C,N,V_ANQPElementIDListForPasspointScanResults) ANQPElementIDListForPasspointScanResults;
@property (TQ,D,N) maximumANQPCacheAgeForPasspointScanResults;
@property (TQ,N,V_acceptableANQPCacheAgeForPasspointScanResults) acceptableANQPCacheAgeForPasspointScanResults;
@property (TQ,N,V_maximumANQPAgeForPasspointScanResults) maximumANQPAgeForPasspointScanResults;
@property (TB,N,V_exclude6GChannels) exclude6GChannels;
@property (T@"NSString",C,N,V_matchNetworkNamePrefix) matchNetworkNamePrefix;
@property (T@"NSPredicate",C,N,V_filterPredicate) filterPredicate;
@property (TB,N,V_includeBeaconCacheResults) includeBeaconCacheResults;
@property (TB,N,V_includeBackgroundScanCacheResults) includeBackgroundScanCacheResults;
@property (TB,N,V_sortByAutoJoinPreference) sortByAutoJoinPreference;
```

## Class methods

```
+[CWFScanParameters supportsSecureCoding];
```

## Instance methods

```
-[CWFScanParameters cacheOnly];
-[CWFScanParameters visitPredicateOperator:];
-[CWFScanParameters channels];
-[CWFScanParameters PHYMode];
-[CWFScanParameters visitPredicateExpression:];
-[CWFScanParameters visitPredicate:];
-[CWFScanParameters SSIDList];
-[CWFScanParameters setScanFlags:];
-[CWFScanParameters setSSID:];
-[CWFScanParameters dwellTime];
-[CWFScanParameters BSSID];
-[CWFScanParameters filterPredicate];
-[CWFScanParameters SSID];
-[CWFScanParameters BSSType];
-[CWFScanParameters setInvalidPredicate:];
-[CWFScanParameters setShortSSID:];
-[CWFScanParameters setFilterPredicate:];
-[CWFScanParameters setDwellTime:];
-[CWFScanParameters setBSSID:];
-[CWFScanParameters setExcludeScanFlags:];
-[CWFScanParameters includeBackgroundScanCacheResults];
-[CWFScanParameters setIncludeMatchingKnownNetworkProfiles:];
-[CWFScanParameters setExclude6GChannels:];
-[CWFScanParameters setRestTime:];
-[CWFScanParameters setIncludeBeaconCacheResults:];
-[CWFScanParameters includeProperties];
-[CWFScanParameters excludeScanFlags];
-[CWFScanParameters includeBeaconCacheResults];
-[CWFScanParameters addScanDurationToMaxAge];
-[CWFScanParameters restTime];
-[CWFScanParameters setChannels:];
-[CWFScanParameters setAddScanDurationToMaxAge:];
-[CWFScanParameters acceptableCacheAge];
-[CWFScanParameters setMinimumRSSI:];
-[CWFScanParameters acceptableANQPCacheAgeForPasspointScanResults];
-[CWFScanParameters setSortByAutoJoinPreference:];
-[CWFScanParameters setIncludeScanResults:];
-[CWFScanParameters exclude6GChannels];
-[CWFScanParameters setIncludeHiddenNetworks:];
-[CWFScanParameters setCacheOnly:];
-[CWFScanParameters numberOfScans];
-[CWFScanParameters includeHiddenNetworks];
-[CWFScanParameters setMaximumANQPCacheAgeForPasspointScanResults:];
-[CWFScanParameters scanType];
-[CWFScanParameters minimumTimestamp];
-[CWFScanParameters mergeScanResults];
-[CWFScanParameters shortSSID];
-[CWFScanParameters ANQPElementIDListForPasspointScanResults];
-[CWFScanParameters invalidPredicate];
-[CWFScanParameters setMatchNetworkNamePrefix:];
-[CWFScanParameters maximumCacheAge];
-[CWFScanParameters includeMatchingKnownNetworkProfiles];
-[CWFScanParameters encodeWithCoder:];
-[CWFScanParameters setIncludeProperties:];
-[CWFScanParameters setMaximumANQPAgeForPasspointScanResults:];
-[CWFScanParameters maximumANQPCacheAgeForPasspointScanResults];
-[CWFScanParameters hash];
-[CWFScanParameters maximumANQPAgeForPasspointScanResults];
-[CWFScanParameters description];
-[CWFScanParameters matchNetworkNamePrefix];
-[CWFScanParameters setNumberOfScans:];
-[CWFScanParameters setScanType:];
-[CWFScanParameters initWithCoder:];
-[CWFScanParameters sortByAutoJoinPreference];
-[CWFScanParameters setIncludeBackgroundScanCacheResults:];
-[CWFScanParameters setMergeScanResults:];
-[CWFScanParameters setSSIDList:];
-[CWFScanParameters maximumAge];
-[CWFScanParameters setMaximumCacheAge:];
-[CWFScanParameters setAcceptableANQPCacheAgeForPasspointScanResults:];
-[CWFScanParameters setAcceptableCacheAge:];
-[CWFScanParameters setMaximumAge:];
-[CWFScanParameters copyWithZone:];
-[CWFScanParameters isEqualToScanParameters:];
-[CWFScanParameters isEqual:];
-[CWFScanParameters setBSSType:];
-[CWFScanParameters setANQPElementIDListForPasspointScanResults:];
-[CWFScanParameters minimumRSSI];
-[CWFScanParameters scanFlags];
-[CWFScanParameters setMinimumTimestamp:];
-[CWFScanParameters setPHYMode:];
-[CWFScanParameters includeScanResults];
```
