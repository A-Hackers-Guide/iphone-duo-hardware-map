# `UIStatusBarComposedData`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="itemIsEnabled"[46B]"timeString"[64c]"shortTimeString"[64c]"dateString"[256c]"gsmSignalStrengthRaw"i"secondaryGsmSignalStrengthRaw"i"gsmSignalStrengthBars"i"secondaryGsmSignalStrengthBars"i"serviceString"[100c]"secondaryServiceString"[100c]"serviceCrossfadeString"[100c]"secondaryServiceCrossfadeString"[100c]"serviceImages"[2[100c]]"operatorDirectory"[1024c]"serviceContentType"I"secondaryServiceContentType"I"cellLowDataModeActive"b1"secondaryCellLowDataModeActive"b1"wifiSignalStrengthRaw"i"wifiSignalStrengthBars"i"wifiLowDataModeActive"b1"dataNetworkType"I"secondaryDataNetworkType"I"batteryCapacity"i"batteryState"I"batteryDetailString"[150c]"bluetoothBatteryCapacity"i"thermalColor"i"thermalSunlightMode"b1"slowActivity"b1"syncActivity"b1"activityDisplayId"[256c]"bluetoothConnected"b1"displayRawGSMSignal"b1"displayRawWifiSignal"b1"locationIconType"b2"voiceControlIconType"b2"quietModeInactive"b1"tetheringConnectionCount"I"batterySaverModeActive"b1"deviceIsRTL"b1"lock"b1"breadcrumbTitle"[256c]"breadcrumbSecondaryTitle"[256c]"personName"[100c]"electronicTollCollectionAvailable"b1"radarAvailable"b1"announceNotificationsAvailable"b1"wifiLinkWarning"b1"wifiSearching"b1"backgroundActivityDisplayStartDate"d"shouldShowEmergencyOnlyStatus"b1"emergencyOnly"b1"secondaryCellularConfigured"b1"primaryServiceBadgeString"[100c]"secondaryServiceBadgeString"[100c]"quietModeImage"[256c]"quietModeName"[256c]"serviceSuffixString"[100c]"secondaryServiceSuffixString"[100c]"numberSharingState"b2"secondaryNumberSharingState"b2"localNetworkType"I"localNetworkName"[100c]} _rawData;
[52B] _itemEnabled;
@"NSString" _doubleHeightStatus;
@"UISystemNavigationAction" _systemNavigationItem;
```

## Properties

```
@property (T^{?=[46B][64c][64c][256c]iiii[100c][100c][100c][100c][2[100c]][1024c]IIb1b1iib1IIiI[150c]iib1b1b1[256c]b1b1b1b2b2b1Ib1b1b1[256c][256c][100c]b1b1b1b1b1db1b1b1[100c][100c][256c][256c][100c][100c]b2b2I[100c]},R,N) rawData;
@property (T@"NSString",C,N,V_doubleHeightStatus) doubleHeightStatus;
@property (T@"UISystemNavigationAction",&,N,V_systemNavigationItem) systemNavigationItem;
```

## Instance methods

```
-[UIStatusBarComposedData rawData];
-[UIStatusBarComposedData description];
-[UIStatusBarComposedData copyWithZone:];
-[UIStatusBarComposedData isEqual:];
-[UIStatusBarComposedData doubleHeightStatus];
-[UIStatusBarComposedData initWithRawData:];
-[UIStatusBarComposedData isItemEnabled:];
-[UIStatusBarComposedData setDoubleHeightStatus:];
-[UIStatusBarComposedData setItem:enabled:];
-[UIStatusBarComposedData setSystemNavigationItem:];
-[UIStatusBarComposedData systemNavigationItem];
```
