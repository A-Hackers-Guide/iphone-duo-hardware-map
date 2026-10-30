# `WFBlacklistEngine`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 7 properties, 47 instance methods, 2 class methods

## Instance variables

```
Q _profile;
@"NSMutableArray" _blacklist;
B _enabled;
@"<WFBlacklistDelegate>" _blacklistDelegate;
@"NSMutableArray" _ssidThresholds;
@"NSMutableArray" _bssidThresholds;
d _wowBlacklistExpiry;
d _autojoinBlacklistExpiry;
d _bssBlacklistExpiry;
```

## Properties

```
@property (T@"<WFBlacklistDelegate>",N,V_blacklistDelegate) blacklistDelegate;
@property (TB,V_enabled) enabled;
@property (T@"NSMutableArray",&,V_ssidThresholds) ssidThresholds;
@property (T@"NSMutableArray",&,V_bssidThresholds) bssidThresholds;
@property (Td,V_wowBlacklistExpiry) wowBlacklistExpiry;
@property (Td,V_autojoinBlacklistExpiry) autojoinBlacklistExpiry;
@property (Td,V_bssBlacklistExpiry) bssBlacklistExpiry;
```

## Class methods

```
+[WFBlacklistEngine stringRepresentationWithReason:];
+[WFBlacklistEngine stringRepresentationWithState:];
```

## Instance methods

```
-[WFBlacklistEngine enabled];
-[WFBlacklistEngine dealloc];
-[WFBlacklistEngine setEnabled:];
-[WFBlacklistEngine _printBlacklist];
-[WFBlacklistEngine bssidThresholds];
-[WFBlacklistEngine _evaluateTriggersForBlacklisting:reason:reasonData:bssid:ssid:state:];
-[WFBlacklistEngine _evaluateTriggersForUnblacklisting:unblacklistReason:ssid:];
-[WFBlacklistEngine _findBlacklistNode:];
-[WFBlacklistEngine _ignoreTriggersForDeviceProfile:node:];
-[WFBlacklistEngine _meetsThresholds:count:perSsid:bssid:ssid:];
-[WFBlacklistEngine _setBlacklistedState:state:reason:reasonData:];
-[WFBlacklistEngine autojoinBlacklistExpiry];
-[WFBlacklistEngine blacklistDelegate];
-[WFBlacklistEngine bssBlacklistExpiry];
-[WFBlacklistEngine changeBlacklistingThresholds:value:perSsid:];
-[WFBlacklistEngine clearTriggerForNetworkWithUnblacklistReason:reason:];
-[WFBlacklistEngine configureBlacklistedStateExpiryIntervalInSec:state:];
-[WFBlacklistEngine denyListThreshold:perSSID:];
-[WFBlacklistEngine getBlacklist];
-[WFBlacklistEngine getBlacklistedNetworkCount];
-[WFBlacklistEngine getNodeFromBlacklist:];
-[WFBlacklistEngine getRssiWhenNetworkWasBlacklisted:];
-[WFBlacklistEngine initWithBlacklistDelegate:profile:];
-[WFBlacklistEngine isNetworkBlacklistedForAutoJoinDueToTrigDisc:rssi:timestamp:];
-[WFBlacklistEngine isNetworkInBlacklistedState:state:];
-[WFBlacklistEngine networkPruned:];
-[WFBlacklistEngine networkRemovedForSsid:];
-[WFBlacklistEngine removeBlacklistedStateForNetworkWithReason:state:reason:];
-[WFBlacklistEngine removeBlacklistedStateWithUnblacklistType:];
-[WFBlacklistEngine removeBlacklistedStates];
-[WFBlacklistEngine removeExpiredBlacklistedState:];
-[WFBlacklistEngine retrieveBlacklistedNetworkSsids:];
-[WFBlacklistEngine retrieveBlacklistedStateHistoryForNetwork:state:timestamps:reasonData:];
-[WFBlacklistEngine retrieveNetworksInBlacklistedState:];
-[WFBlacklistEngine retrieveNetworksInBlacklistedStateHistory:];
-[WFBlacklistEngine retrieveReasonsForNetworkInBlacklistedState:state:timestamps:reasonData:];
-[WFBlacklistEngine setAutojoinBlacklistExpiry:];
-[WFBlacklistEngine setBlacklistDelegate:];
-[WFBlacklistEngine setBssBlacklistExpiry:];
-[WFBlacklistEngine setBssidThresholds:];
-[WFBlacklistEngine setDefaultBlacklistThresholds];
-[WFBlacklistEngine setSsidThresholds:];
-[WFBlacklistEngine setTriggerForNetworkWithReason:reason:reasonData:bssid:];
-[WFBlacklistEngine setTriggerForNetworkWithReasonAndState:reason:reasonData:bssid:state:];
-[WFBlacklistEngine setWowBlacklistExpiry:];
-[WFBlacklistEngine ssidThresholds];
-[WFBlacklistEngine wowBlacklistExpiry];
```
