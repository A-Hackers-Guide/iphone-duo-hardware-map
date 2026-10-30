# `WFNetworkListing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 10 properties, 40 instance methods, 0 class methods

## Properties

```
@property (TB,N) showOtherNetwork;
@property (Tf) currentNetworkScaledRSSI;
@property (T@"<WFNetworkListRecord>",&) currentNetwork;
@property (Tq) currentNetworkState;
@property (TB,?,N) networkListVisible;
@property (TQ,?) currentNetworkSignalBars;
@property (Tq,?,N) deviceCapability;
@property (T@"NSString",?,C,N) currentNetworkSubtitle;
@property (TB,?,N) disabled;
@property (TB,?,N) userAutoJoinEnabled;
```

## Instance methods

```
-[WFNetworkListing setCurrentNetwork:];
-[WFNetworkListing currentNetwork];
-[WFNetworkListing setNetworks:];
-[WFNetworkListing currentNetworkState];
-[WFNetworkListing powerStateDidChange:];
-[WFNetworkListing refresh];
-[WFNetworkListing showOtherNetwork];
-[WFNetworkListing currentNetworkScaledRSSI];
-[WFNetworkListing setCurrentNetworkState:];
-[WFNetworkListing setShowOtherNetwork:];
-[WFNetworkListing setListDelegate:];
-[WFNetworkListing setCurrentNetworkScaledRSSI:];
-[WFNetworkListing deviceCapability];
-[WFNetworkListing setScanning:];
-[WFNetworkListing disabled];
-[WFNetworkListing setAskToJoinMode:];
-[WFNetworkListing setAutoInstantHotspotJoinOption:];
-[WFNetworkListing setCurrentNetworkSignalBars:];
-[WFNetworkListing currentNetworkSignalBars];
-[WFNetworkListing setDeviceCapability:];
-[WFNetworkListing setDisabled:];
-[WFNetworkListing currentNetworkSubtitle];
-[WFNetworkListing managedAppleIDStateChange:];
-[WFNetworkListing networkListDelegateDidPresentAccessoryViewController:];
-[WFNetworkListing networkListDelegateWillPresentAccessoryViewController:];
-[WFNetworkListing networkListVisible];
-[WFNetworkListing powerModificationStateDidChange:];
-[WFNetworkListing powerStateDidChangeToggle:];
-[WFNetworkListing reloadCellsForNetworkNames:];
-[WFNetworkListing scrollToAirportCell:];
-[WFNetworkListing setCurrentNetwork:previousNetwork:reason:];
-[WFNetworkListing setCurrentNetworkSubtitle:];
-[WFNetworkListing setNetworkListVisible:];
-[WFNetworkListing setUserAutoJoinEnabled:];
-[WFNetworkListing shouldPromptWhenCarPlaySessionIsActive];
-[WFNetworkListing shouldPromptWhenPersonalHotspotIsEnabled];
-[WFNetworkListing supportsHealthRecommendations];
-[WFNetworkListing supportsWiFiPasswordSharing];
-[WFNetworkListing updateViewsForNetworks:];
-[WFNetworkListing userAutoJoinEnabled];
```
