# `SBStatusBarStateProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBStatusBarStateAggregatorPosting`, `UIStatusBarStateProvider`
- 11 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _stateObservers;
{?="itemIsEnabled"[46B]"timeString"[64c]"shortTimeString"[64c]"dateString"[256c]"gsmSignalStrengthRaw"i"secondaryGsmSignalStrengthRaw"i"gsmSignalStrengthBars"i"secondaryGsmSignalStrengthBars"i"serviceString"[100c]"secondaryServiceString"[100c]"serviceCrossfadeString"[100c]"secondaryServiceCrossfadeString"[100c]"serviceImages"[2[100c]]"operatorDirectory"[1024c]"serviceContentType"I"secondaryServiceContentType"I"cellLowDataModeActive"b1"secondaryCellLowDataModeActive"b1"wifiSignalStrengthRaw"i"wifiSignalStrengthBars"i"wifiLowDataModeActive"b1"dataNetworkType"I"secondaryDataNetworkType"I"batteryCapacity"i"batteryState"I"batteryDetailString"[150c]"bluetoothBatteryCapacity"i"thermalColor"i"thermalSunlightMode"b1"slowActivity"b1"syncActivity"b1"activityDisplayId"[256c]"bluetoothConnected"b1"displayRawGSMSignal"b1"displayRawWifiSignal"b1"locationIconType"b2"voiceControlIconType"b2"quietModeInactive"b1"tetheringConnectionCount"I"batterySaverModeActive"b1"deviceIsRTL"b1"lock"b1"breadcrumbTitle"[256c]"breadcrumbSecondaryTitle"[256c]"personName"[100c]"electronicTollCollectionAvailable"b1"radarAvailable"b1"announceNotificationsAvailable"b1"wifiLinkWarning"b1"wifiSearching"b1"backgroundActivityDisplayStartDate"d"shouldShowEmergencyOnlyStatus"b1"emergencyOnly"b1"secondaryCellularConfigured"b1"primaryServiceBadgeString"[100c]"secondaryServiceBadgeString"[100c]"quietModeImage"[256c]"quietModeName"[256c]"serviceSuffixString"[100c]"secondaryServiceSuffixString"[100c]"numberSharingState"b2"secondaryNumberSharingState"b2"localNetworkType"I"localNetworkName"[100c]} _aggregatorData;
i _aggregatorActions;
{?="itemIsEnabled"[46B]"timeString"[64c]"shortTimeString"[64c]"dateString"[256c]"gsmSignalStrengthRaw"i"secondaryGsmSignalStrengthRaw"i"gsmSignalStrengthBars"i"secondaryGsmSignalStrengthBars"i"serviceString"[100c]"secondaryServiceString"[100c]"serviceCrossfadeString"[100c]"secondaryServiceCrossfadeString"[100c]"serviceImages"[2[100c]]"operatorDirectory"[1024c]"serviceContentType"I"secondaryServiceContentType"I"cellLowDataModeActive"b1"secondaryCellLowDataModeActive"b1"wifiSignalStrengthRaw"i"wifiSignalStrengthBars"i"wifiLowDataModeActive"b1"dataNetworkType"I"secondaryDataNetworkType"I"batteryCapacity"i"batteryState"I"batteryDetailString"[150c]"bluetoothBatteryCapacity"i"thermalColor"i"thermalSunlightMode"b1"slowActivity"b1"syncActivity"b1"activityDisplayId"[256c]"bluetoothConnected"b1"displayRawGSMSignal"b1"displayRawWifiSignal"b1"locationIconType"b2"voiceControlIconType"b2"quietModeInactive"b1"tetheringConnectionCount"I"batterySaverModeActive"b1"deviceIsRTL"b1"lock"b1"breadcrumbTitle"[256c]"breadcrumbSecondaryTitle"[256c]"personName"[100c]"electronicTollCollectionAvailable"b1"radarAvailable"b1"announceNotificationsAvailable"b1"wifiLinkWarning"b1"wifiSearching"b1"backgroundActivityDisplayStartDate"d"shouldShowEmergencyOnlyStatus"b1"emergencyOnly"b1"secondaryCellularConfigured"b1"primaryServiceBadgeString"[100c]"secondaryServiceBadgeString"[100c]"quietModeImage"[256c]"quietModeName"[256c]"serviceSuffixString"[100c]"secondaryServiceSuffixString"[100c]"numberSharingState"b2"secondaryNumberSharingState"b2"localNetworkType"I"localNetworkName"[100c]} _lastPost;
Q _coalescentBlockDepth;
[46B] _itemNeedsPost;
B _anyItemNeedsPost;
B _nonItemDataNeedsPost;
B _posting;
@"NSMutableArray" _stylesWithDetailUpdates;
@"SBStatusBarStateAggregator" _stateAggregator;
```

## Properties

```
@property (T@"SBStatusBarStateAggregator",W,N,V_stateAggregator) stateAggregator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBStatusBarStateProvider dealloc];
-[SBStatusBarStateProvider updateStatusBarItem:];
-[SBStatusBarStateProvider beginCoalescentBlock];
-[SBStatusBarStateProvider endCoalescentBlock];
-[SBStatusBarStateProvider addStatusBarStateObserver:];
-[SBStatusBarStateProvider getStatusBarData:];
-[SBStatusBarStateProvider removeStatusBarStateObserver:];
-[SBStatusBarStateProvider stateAggregator];
-[SBStatusBarStateProvider _composePostActionsFromAggregatorActions:];
-[SBStatusBarStateProvider _composePostDataFromAggregatorData:];
-[SBStatusBarStateProvider _didFinishPost];
-[SBStatusBarStateProvider _shouldPostForUpdatesToNonItemData:];
-[SBStatusBarStateProvider _shouldPostForVisitedItem:withUpdates:toAggregatorData:lastPost:];
-[SBStatusBarStateProvider initWithStateAggregator:];
-[SBStatusBarStateProvider setStateAggregator:];
-[SBStatusBarStateProvider statusBarStateAggregator:didUpdateNonItemData:];
-[SBStatusBarStateProvider statusBarStateAggregator:didVisitItem:withUpdates:toData:];
-[SBStatusBarStateProvider statusBarStateAggregatorDidFinishPost:withData:actions:];
-[SBStatusBarStateProvider statusBarStateAggregatorDidStartPost:];
```
