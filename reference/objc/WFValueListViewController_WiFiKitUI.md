# `WFValueListViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- 10 instance variables, 10 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _switchOn;
B _hasSwitch;
@"NSString" _selectedTitle;
@? _completionHandler;
@? _footerHandler;
@"NSArray" _titles;
@"UISwitch" _configSwitch;
@"NSMutableArray" _sections;
@"NSString" _switchTitle;
@"WFValueListViewController" _sublist;
```

## Properties

```
@property (T@"NSArray",&,N,V_titles) titles;
@property (TB,N,V_hasSwitch) hasSwitch;
@property (T@"UISwitch",&,N,V_configSwitch) configSwitch;
@property (T@"NSMutableArray",&,N,V_sections) sections;
@property (T@"NSString",C,N,V_switchTitle) switchTitle;
@property (T@"WFValueListViewController",&,N,V_sublist) sublist;
@property (T@"NSString",&,N,V_selectedTitle) selectedTitle;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@?,C,N,V_footerHandler) footerHandler;
@property (TB,N,V_switchOn) switchOn;
```

## Instance methods

```
-[WFValueListViewController tableView:titleForFooterInSection:];
-[WFValueListViewController tableView:numberOfRowsInSection:];
-[WFValueListViewController numberOfSectionsInTableView:];
-[WFValueListViewController tableView:cellForRowAtIndexPath:];
-[WFValueListViewController setCompletionHandler:];
-[WFValueListViewController completionHandler];
-[WFValueListViewController sections];
-[WFValueListViewController viewWillDisappear:];
-[WFValueListViewController viewDidLoad];
-[WFValueListViewController tableView:willDisplayCell:forRowAtIndexPath:];
-[WFValueListViewController tableView:didSelectRowAtIndexPath:];
-[WFValueListViewController setSections:];
-[WFValueListViewController setTitles:];
-[WFValueListViewController titles];
-[WFValueListViewController setSwitchOn:];
-[WFValueListViewController setSwitchTitle:];
-[WFValueListViewController sublist];
-[WFValueListViewController cellForTitleAtIndexPath:];
-[WFValueListViewController configSwitch];
-[WFValueListViewController footerHandler];
-[WFValueListViewController hasSwitch];
-[WFValueListViewController initWithTitles:switchTitle:];
-[WFValueListViewController initWithTitles:switchTitle:sublist:];
-[WFValueListViewController initWithTitles:switchTitle:sublist:appearanceProxy:];
-[WFValueListViewController selectedTitle];
-[WFValueListViewController setConfigSwitch:];
-[WFValueListViewController setFooterHandler:];
-[WFValueListViewController setHasSwitch:];
-[WFValueListViewController setSelectedTitle:];
-[WFValueListViewController setSublist:];
-[WFValueListViewController switchOn];
-[WFValueListViewController switchTitle];
```
