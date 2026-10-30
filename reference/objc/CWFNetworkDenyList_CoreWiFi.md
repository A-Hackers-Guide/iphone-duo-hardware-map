# `CWFNetworkDenyList`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 10 properties, 55 instance methods, 0 class methods

## Instance variables

```
Q _profile;
@"NSMutableArray" _denyList;
B _enabled;
@? _batteryInfoHandler;
@? _isUserModeInteractiveHandler;
@? _denyListDidUpdateHandler;
@"NSArray" _SSIDThresholds;
@"NSArray" _BSSIDThresholds;
d _wowDenyListExpiry;
d _autoJoinkDenyListExpiry;
d _BSSDenyListExpiry;
d _partialConnectivityDenyListExpiry;
```

## Properties

```
@property (T@?,C,V_batteryInfoHandler) batteryInfoHandler;
@property (T@?,C,V_isUserModeInteractiveHandler) isUserModeInteractiveHandler;
@property (T@?,C,V_denyListDidUpdateHandler) denyListDidUpdateHandler;
@property (TB,V_enabled) enabled;
@property (T@"NSArray",&,V_SSIDThresholds) SSIDThresholds;
@property (T@"NSArray",&,V_BSSIDThresholds) BSSIDThresholds;
@property (Td,V_wowDenyListExpiry) wowDenyListExpiry;
@property (Td,V_autoJoinkDenyListExpiry) autoJoinkDenyListExpiry;
@property (Td,V_BSSDenyListExpiry) BSSDenyListExpiry;
@property (Td,V_partialConnectivityDenyListExpiry) partialConnectivityDenyListExpiry;
```

## Instance methods

```
-[CWFNetworkDenyList enabled];
-[CWFNetworkDenyList denyList];
-[CWFNetworkDenyList setEnabled:];
-[CWFNetworkDenyList BSSIDThresholds];
-[CWFNetworkDenyList BSSDenyListExpiry];
-[CWFNetworkDenyList RSSIWhenNetworkWasDenyListed:];
-[CWFNetworkDenyList SSIDThresholds];
-[CWFNetworkDenyList processDenyListedBSSForMetrics:];
-[CWFNetworkDenyList reasonsForNetworkInDenyListedState:state:timestamps:reasonData:];
-[CWFNetworkDenyList _evaluateTriggersForDenyListRemove:denyListRemoveReason:SSID:];
-[CWFNetworkDenyList _evaluateTriggersForDenyListing:reason:reasonData:BSSID:SSID:state:];
-[CWFNetworkDenyList _findNetworkDenyListItem:];
-[CWFNetworkDenyList _findNetworkDenyListItemsForSSID:];
-[CWFNetworkDenyList _ignoreTriggersForDeviceProfile:denyListItem:];
-[CWFNetworkDenyList _meetsThresholds:count:forSSIDThresholds:BSSID:SSID:];
-[CWFNetworkDenyList _printDenyList];
-[CWFNetworkDenyList _setDenyListState:state:reason:reasonData:];
-[CWFNetworkDenyList autoJoinkDenyListExpiry];
-[CWFNetworkDenyList batteryInfoHandler];
-[CWFNetworkDenyList denyListDidUpdateHandler];
-[CWFNetworkDenyList denyListItemForScanResult:];
-[CWFNetworkDenyList denyListThresholdForReason:forSSIDThresholds:];
-[CWFNetworkDenyList denyListedNetworkCount];
-[CWFNetworkDenyList denyListedNetworkSSIDs:];
-[CWFNetworkDenyList denyListedReasonHistoryForNetwork:state:timestamps:reasonData:];
-[CWFNetworkDenyList initWithDenyListDeviceProfile:];
-[CWFNetworkDenyList isNetworkDenyListedForAutoJoinDueToCrash:];
-[CWFNetworkDenyList isNetworkDenyListedForAutoJoinDueToTrigDisc:RSSI:timestamp:];
-[CWFNetworkDenyList isNetworkInDenyListedState:scanResult:];
-[CWFNetworkDenyList isNetworkTemporarilyDenyListedForAutoJoin:];
-[CWFNetworkDenyList isNetworkTemporarilyDenyListedForAutoJoinDueToPartialConnectivity:];
-[CWFNetworkDenyList isUserModeInteractiveHandler];
-[CWFNetworkDenyList networksInDenyListedState:];
-[CWFNetworkDenyList networksInDenyListedStateHistory:];
-[CWFNetworkDenyList partialConnectivityDenyListExpiry];
-[CWFNetworkDenyList removeAllDenyListEntriesWithNetworkName:];
-[CWFNetworkDenyList removeAllDenyListedItems];
-[CWFNetworkDenyList removeDenyListStateWithDenyListRemoveReason:];
-[CWFNetworkDenyList removeExpiredDenyListedState:];
-[CWFNetworkDenyList removeNetworkDenyListInfoForTrigger:forNetwork:];
-[CWFNetworkDenyList removeNetworkDenyListInfoWithReason:forScanResult:];
-[CWFNetworkDenyList setAutoJoinkDenyListExpiry:];
-[CWFNetworkDenyList setBSSDenyListExpiry:];
-[CWFNetworkDenyList setBSSIDThresholds:];
-[CWFNetworkDenyList setBatteryInfoHandler:];
-[CWFNetworkDenyList setDefaultDenyListThresholds];
-[CWFNetworkDenyList setDenyListDidUpdateHandler:];
-[CWFNetworkDenyList setDenyListedStateExpiryIntervalInSec:state:];
-[CWFNetworkDenyList setDenyListingThresholds:value:forSSIDThresholds:];
-[CWFNetworkDenyList setIsUserModeInteractiveHandler:];
-[CWFNetworkDenyList setNetworkDenyListInfo:forScanResult:];
-[CWFNetworkDenyList setPartialConnectivityDenyListExpiry:];
-[CWFNetworkDenyList setSSIDThresholds:];
-[CWFNetworkDenyList setWowDenyListExpiry:];
-[CWFNetworkDenyList wowDenyListExpiry];
```
