# `WFNetworkListDataSource`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _currentNetwork;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _currentNetworkRowConfig;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _listMode;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _knownNetworks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _phNetworks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _publicNetworks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _infraNetworks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _adhocNetworks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _unConfiguredNetworks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _managedPreferredNetworks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _editablePreferredNetworks;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _isScanning;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _unconfiguredNetworksSectionTitle;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 networksToBeDeleted;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 networkTapHandler;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 infoButtonTapHandler;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 associationHandler;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pendingDeletingNetworksChangedCallback;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 otherNetworkTapHandler;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 unconfiguredNetworksSectionTitleDelegate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 scanResults;
```

## Instance methods

```
-[WFNetworkListDataSource setScanning:];
-[WFNetworkListDataSource init];
-[WFNetworkListDataSource updateCurrentNetwork:];
-[WFNetworkListDataSource updateManagedPreferredNetworks:];
-[WFNetworkListDataSource setAssociationHandler:];
-[WFNetworkListDataSource setInfoButtonHandler:];
-[WFNetworkListDataSource setOtherNetworkTapHandler:];
-[WFNetworkListDataSource setPendingDeletingNetworksChangedCallback:];
-[WFNetworkListDataSource setUnconfiguredNetworksSectionTitleDelegate:];
-[WFNetworkListDataSource startEditingPreferredNetworks];
-[WFNetworkListDataSource switchToScanList];
-[WFNetworkListDataSource updateCurrentNetworkConfig:];
-[WFNetworkListDataSource updateEditablePreferredNetworks:];
-[WFNetworkListDataSource updateScanResults:];
```
