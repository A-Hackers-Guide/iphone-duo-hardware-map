# `WFBuddyViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBTableWelcomeController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`, `WFNetworkListing`
- 23 instance variables, 31 properties, 75 instance methods, 0 class methods

## Instance variables

```
B showOtherNetwork;
B _showNetworkSettings;
B _networkListVisible;
B _showAdditionalSetupInfo;
B _supportsCellularActivation;
B _tableViewIsUpdating;
B _networkResultsChangedWhileUIUpdates;
B _tableReloadRequestQueued;
B _didDrawOnHeaderSymbol;
f _currentNetworkScaledRSSI;
@"<WFNetworkListRecord>" _currentNetwork;
q _currentNetworkState;
q _deviceCapability;
@"<WFBuddyViewControllerDelegate>" _buddyDelegate;
@"NSArray" _sortedNetworks;
@"<WFNetworkListDelegate>" _listDelegate;
@"NSString" _alternateSetupTitle;
@"NSString" _alternateSetupFooter;
@"UIView" _buddyIPadContainerView;
@"NSOrderedSet" _sections;
@"UISwitch" _enableWAPISwitch;
@"NSArray" _pendingNetworks;
@"UIImageView" _headerSymbolView;
```

## Properties

```
@property (T@"NSArray",&,N,V_sortedNetworks) sortedNetworks;
@property (T@"<WFNetworkListDelegate>",W,V_listDelegate) listDelegate;
@property (T@"NSString",C,N,V_alternateSetupTitle) alternateSetupTitle;
@property (T@"NSString",C,N,V_alternateSetupFooter) alternateSetupFooter;
@property (T@"UIView",&,N,V_buddyIPadContainerView) buddyIPadContainerView;
@property (T@"NSOrderedSet",&,V_sections) sections;
@property (T@"UISwitch",&,N,V_enableWAPISwitch) enableWAPISwitch;
@property (TB,V_tableViewIsUpdating) tableViewIsUpdating;
@property (TB,N,V_networkResultsChangedWhileUIUpdates) networkResultsChangedWhileUIUpdates;
@property (TB,N,V_tableReloadRequestQueued) tableReloadRequestQueued;
@property (T@"NSArray",&,N,V_pendingNetworks) pendingNetworks;
@property (T@"UIImageView",W,N,V_headerSymbolView) headerSymbolView;
@property (TB,N,V_didDrawOnHeaderSymbol) didDrawOnHeaderSymbol;
@property (TB,N,V_showNetworkSettings) showNetworkSettings;
@property (TB,N,V_networkListVisible) networkListVisible;
@property (TB,N,V_showAdditionalSetupInfo) showAdditionalSetupInfo;
@property (TB,N,V_supportsCellularActivation) supportsCellularActivation;
@property (T@"<WFBuddyViewControllerDelegate>",W,N,V_buddyDelegate) buddyDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,VshowOtherNetwork) showOtherNetwork;
@property (Tf,V_currentNetworkScaledRSSI) currentNetworkScaledRSSI;
@property (T@"<WFNetworkListRecord>",&,V_currentNetwork) currentNetwork;
@property (Tq,V_currentNetworkState) currentNetworkState;
@property (TQ,?) currentNetworkSignalBars;
@property (Tq,?,N,V_deviceCapability) deviceCapability;
@property (T@"NSString",?,C,N) currentNetworkSubtitle;
@property (TB,?,N) disabled;
@property (TB,?,N) userAutoJoinEnabled;
```

## Instance methods

```
-[WFBuddyViewController deviceCapability];
-[WFBuddyViewController setCurrentNetwork:];
-[WFBuddyViewController tableView:titleForFooterInSection:];
-[WFBuddyViewController tableView:heightForFooterInSection:];
-[WFBuddyViewController currentNetwork];
-[WFBuddyViewController tableView:numberOfRowsInSection:];
-[WFBuddyViewController tableView:accessoryButtonTappedForRowWithIndexPath:];
-[WFBuddyViewController numberOfSectionsInTableView:];
-[WFBuddyViewController tableView:cellForRowAtIndexPath:];
-[WFBuddyViewController setNetworks:];
-[WFBuddyViewController currentNetworkState];
-[WFBuddyViewController sections];
-[WFBuddyViewController init];
-[WFBuddyViewController powerStateDidChange:];
-[WFBuddyViewController refresh];
-[WFBuddyViewController showOtherNetwork];
-[WFBuddyViewController viewDidLoad];
-[WFBuddyViewController currentNetworkScaledRSSI];
-[WFBuddyViewController viewWillAppear:];
-[WFBuddyViewController tableView:heightForRowAtIndexPath:];
-[WFBuddyViewController listDelegate];
-[WFBuddyViewController _canShowWhileLocked];
-[WFBuddyViewController viewDidAppear:];
-[WFBuddyViewController tableView:didSelectRowAtIndexPath:];
-[WFBuddyViewController setSections:];
-[WFBuddyViewController setCurrentNetworkState:];
-[WFBuddyViewController viewDidDisappear:];
-[WFBuddyViewController tableView:willDisplayFooterView:forSection:];
-[WFBuddyViewController setDeviceCapability:];
-[WFBuddyViewController setShowOtherNetwork:];
-[WFBuddyViewController setListDelegate:];
-[WFBuddyViewController tableView:heightForHeaderInSection:];
-[WFBuddyViewController setCurrentNetworkScaledRSSI:];
-[WFBuddyViewController networkListDelegateWillPresentAccessoryViewController:];
-[WFBuddyViewController networkListVisible];
-[WFBuddyViewController setNetworkListVisible:];
-[WFBuddyViewController _nameOfSection:];
-[WFBuddyViewController _notifyBuddyWiFiPickerIsVisble:];
-[WFBuddyViewController pendingNetworks];
-[WFBuddyViewController _cellForNetworkRecord:tableView:indexPath:];
-[WFBuddyViewController _chooseOtherNetworkTapped:];
-[WFBuddyViewController _debugSectionStringFromSections:];
-[WFBuddyViewController _enableWAPISwitchChanged:];
-[WFBuddyViewController _refreshSections];
-[WFBuddyViewController _setUpHeaderSymbolView];
-[WFBuddyViewController _updateCellsWithNewData:oldData:inSection:];
-[WFBuddyViewController alternateSetupFooter];
-[WFBuddyViewController alternateSetupTitle];
-[WFBuddyViewController buddyDelegate];
-[WFBuddyViewController buddyIPadContainerView];
-[WFBuddyViewController didDrawOnHeaderSymbol];
-[WFBuddyViewController enableWAPISwitch];
-[WFBuddyViewController headerSymbolView];
-[WFBuddyViewController networkResultsChangedWhileUIUpdates];
-[WFBuddyViewController setAlternateSetupFooter:];
-[WFBuddyViewController setAlternateSetupTitle:];
-[WFBuddyViewController setBuddyDelegate:];
-[WFBuddyViewController setBuddyIPadContainerView:];
-[WFBuddyViewController setDidDrawOnHeaderSymbol:];
-[WFBuddyViewController setEnableWAPISwitch:];
-[WFBuddyViewController setHeaderSymbolView:];
-[WFBuddyViewController setNetworkResultsChangedWhileUIUpdates:];
-[WFBuddyViewController setPendingNetworks:];
-[WFBuddyViewController setShowAdditionalSetupInfo:];
-[WFBuddyViewController setShowNetworkSettings:];
-[WFBuddyViewController setSortedNetworks:];
-[WFBuddyViewController setSupportsCellularActivation:];
-[WFBuddyViewController setTableReloadRequestQueued:];
-[WFBuddyViewController setTableViewIsUpdating:];
-[WFBuddyViewController showAdditionalSetupInfo];
-[WFBuddyViewController showNetworkSettings];
-[WFBuddyViewController sortedNetworks];
-[WFBuddyViewController supportsCellularActivation];
-[WFBuddyViewController tableReloadRequestQueued];
-[WFBuddyViewController tableViewIsUpdating];
```
