# `WFPickerViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`, `WFNetworkListing`
- 10 instance variables, 19 properties, 36 instance methods, 0 class methods

## Instance variables

```
B showOtherNetwork;
B _dismissed;
B _showCurrentNetworkTop;
f _currentNetworkScaledRSSI;
@"<WFNetworkListRecord>" _currentNetwork;
q _currentNetworkState;
q _deviceCapability;
@"UITableView" _tableView;
@"NSArray" _sortedNetworks;
@"<WFNetworkListDelegate>" _listDelegate;
```

## Properties

```
@property (T@"UITableView",W,N,V_tableView) tableView;
@property (T@"NSArray",&,N,V_sortedNetworks) sortedNetworks;
@property (T@"<WFNetworkListDelegate>",W,V_listDelegate) listDelegate;
@property (TB,N,V_showCurrentNetworkTop) showCurrentNetworkTop;
@property (TB,N,V_dismissed) dismissed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,VshowOtherNetwork) showOtherNetwork;
@property (Tf,V_currentNetworkScaledRSSI) currentNetworkScaledRSSI;
@property (T@"<WFNetworkListRecord>",&,V_currentNetwork) currentNetwork;
@property (Tq,V_currentNetworkState) currentNetworkState;
@property (TB,?,N) networkListVisible;
@property (TQ,?) currentNetworkSignalBars;
@property (Tq,?,N,V_deviceCapability) deviceCapability;
@property (T@"NSString",?,C,N) currentNetworkSubtitle;
@property (TB,?,N) disabled;
@property (TB,?,N) userAutoJoinEnabled;
```

## Instance methods

```
-[WFPickerViewController deviceCapability];
-[WFPickerViewController setCurrentNetwork:];
-[WFPickerViewController tableView];
-[WFPickerViewController currentNetwork];
-[WFPickerViewController tableView:numberOfRowsInSection:];
-[WFPickerViewController numberOfSectionsInTableView:];
-[WFPickerViewController tableView:cellForRowAtIndexPath:];
-[WFPickerViewController setNetworks:];
-[WFPickerViewController dismissed];
-[WFPickerViewController currentNetworkState];
-[WFPickerViewController init];
-[WFPickerViewController powerStateDidChange:];
-[WFPickerViewController refresh];
-[WFPickerViewController showOtherNetwork];
-[WFPickerViewController viewDidLoad];
-[WFPickerViewController currentNetworkScaledRSSI];
-[WFPickerViewController viewWillAppear:];
-[WFPickerViewController listDelegate];
-[WFPickerViewController setTableView:];
-[WFPickerViewController loadView];
-[WFPickerViewController didReceiveMemoryWarning];
-[WFPickerViewController tableView:didSelectRowAtIndexPath:];
-[WFPickerViewController setCurrentNetworkState:];
-[WFPickerViewController viewDidDisappear:];
-[WFPickerViewController setDeviceCapability:];
-[WFPickerViewController setShowOtherNetwork:];
-[WFPickerViewController setDismissed:];
-[WFPickerViewController setListDelegate:];
-[WFPickerViewController setCurrentNetworkScaledRSSI:];
-[WFPickerViewController shouldPromptWhenCarPlaySessionIsActive];
-[WFPickerViewController shouldPromptWhenPersonalHotspotIsEnabled];
-[WFPickerViewController _cellForNetworkRecord:tableView:indexPath:];
-[WFPickerViewController setShowCurrentNetworkTop:];
-[WFPickerViewController setSortedNetworks:];
-[WFPickerViewController showCurrentNetworkTop];
-[WFPickerViewController sortedNetworks];
```
