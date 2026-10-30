# `WFDiagnosticsTableViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- 11 instance variables, 11 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _networkQualitySpinning;
B _useInsetGroupedTableView;
@"<WFDiagnosticsProviderContext>" _context;
@"<WFDetailsProviderContext>" _detailsContext;
@"NSOrderedSet" _sections;
@"WFNetworkSettingsCellFactory" _cellFactory;
@"WFHyperlinkFooterView" _linkFooterView;
@"WFAppearanceProxy" _appearanceProxy;
@"WFHyperlinkFooterView" _networkQualityFooterView;
@"NSDate" _networkQualityFooterDate;
@"UITableViewCell" _networkQualityCell;
```

## Properties

```
@property (T@"<WFDiagnosticsProviderContext>",&,N,V_context) context;
@property (T@"<WFDetailsProviderContext>",&,N,V_detailsContext) detailsContext;
@property (T@"NSOrderedSet",&,N,V_sections) sections;
@property (T@"WFNetworkSettingsCellFactory",&,N,V_cellFactory) cellFactory;
@property (T@"WFHyperlinkFooterView",&,N,V_linkFooterView) linkFooterView;
@property (T@"WFAppearanceProxy",&,N,V_appearanceProxy) appearanceProxy;
@property (T@"WFHyperlinkFooterView",&,N,V_networkQualityFooterView) networkQualityFooterView;
@property (T@"NSDate",&,N,V_networkQualityFooterDate) networkQualityFooterDate;
@property (T@"UITableViewCell",&,N,V_networkQualityCell) networkQualityCell;
@property (TB,N,V_networkQualitySpinning) networkQualitySpinning;
@property (TB,N,V_useInsetGroupedTableView) useInsetGroupedTableView;
```

## Instance methods

```
-[WFDiagnosticsTableViewController tableView:titleForFooterInSection:];
-[WFDiagnosticsTableViewController tableView:numberOfRowsInSection:];
-[WFDiagnosticsTableViewController numberOfSectionsInTableView:];
-[WFDiagnosticsTableViewController tableView:viewForFooterInSection:];
-[WFDiagnosticsTableViewController tableView:cellForRowAtIndexPath:];
-[WFDiagnosticsTableViewController sections];
-[WFDiagnosticsTableViewController tableView:titleForHeaderInSection:];
-[WFDiagnosticsTableViewController viewDidLoad];
-[WFDiagnosticsTableViewController appearanceProxy];
-[WFDiagnosticsTableViewController setContext:];
-[WFDiagnosticsTableViewController setSections:];
-[WFDiagnosticsTableViewController _refresh];
-[WFDiagnosticsTableViewController viewDidDisappear:];
-[WFDiagnosticsTableViewController context];
-[WFDiagnosticsTableViewController donePressed];
-[WFDiagnosticsTableViewController linkFooterView];
-[WFDiagnosticsTableViewController _updateNetworkQualityFooterText];
-[WFDiagnosticsTableViewController setCellFactory:];
-[WFDiagnosticsTableViewController _defaultSections];
-[WFDiagnosticsTableViewController _fillNetworkQualityCell:];
-[WFDiagnosticsTableViewController _networkQualityOpenURL];
-[WFDiagnosticsTableViewController _openNetworkQualityDetails:];
-[WFDiagnosticsTableViewController _reloadNetworkQualityCell];
-[WFDiagnosticsTableViewController _runNetworkQuality];
-[WFDiagnosticsTableViewController cellFactory];
-[WFDiagnosticsTableViewController detailsContext];
-[WFDiagnosticsTableViewController initWithDiagnosticsContext:detailsProviderContext:];
-[WFDiagnosticsTableViewController initWithDiagnosticsContext:detailsProviderContext:appearanceProxy:];
-[WFDiagnosticsTableViewController networkQualityCell];
-[WFDiagnosticsTableViewController networkQualityFooterDate];
-[WFDiagnosticsTableViewController networkQualityFooterView];
-[WFDiagnosticsTableViewController networkQualitySpinning];
-[WFDiagnosticsTableViewController setAppearanceProxy:];
-[WFDiagnosticsTableViewController setDetailsContext:];
-[WFDiagnosticsTableViewController setLinkFooterView:];
-[WFDiagnosticsTableViewController setNetworkQualityCell:];
-[WFDiagnosticsTableViewController setNetworkQualityFooterDate:];
-[WFDiagnosticsTableViewController setNetworkQualityFooterView:];
-[WFDiagnosticsTableViewController setNetworkQualitySpinning:];
-[WFDiagnosticsTableViewController setUseInsetGroupedTableView:];
-[WFDiagnosticsTableViewController useInsetGroupedTableView];
```
