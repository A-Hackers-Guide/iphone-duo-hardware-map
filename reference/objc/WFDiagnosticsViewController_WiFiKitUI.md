# `WFDiagnosticsViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- 5 instance variables, 5 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _saving;
B _showNANUI;
@? _saveHandler;
@"NSString" _comment;
@"NSOrderedSet" _sections;
```

## Properties

```
@property (T@"NSString",C,N,V_comment) comment;
@property (T@"NSOrderedSet",&,N,V_sections) sections;
@property (TB,N,V_showNANUI) showNANUI;
@property (T@?,C,N,V_saveHandler) saveHandler;
@property (TB,N,V_saving) saving;
```

## Instance methods

```
-[WFDiagnosticsViewController tableView:titleForFooterInSection:];
-[WFDiagnosticsViewController tableView:numberOfRowsInSection:];
-[WFDiagnosticsViewController numberOfSectionsInTableView:];
-[WFDiagnosticsViewController tableView:cellForRowAtIndexPath:];
-[WFDiagnosticsViewController sections];
-[WFDiagnosticsViewController viewDidLoad];
-[WFDiagnosticsViewController comment];
-[WFDiagnosticsViewController tableView:didSelectRowAtIndexPath:];
-[WFDiagnosticsViewController setSections:];
-[WFDiagnosticsViewController setComment:];
-[WFDiagnosticsViewController saving];
-[WFDiagnosticsViewController setSaving:];
-[WFDiagnosticsViewController setSaveHandler:];
-[WFDiagnosticsViewController saveHandler];
-[WFDiagnosticsViewController _defaultSections];
-[WFDiagnosticsViewController initWithNANUI:];
-[WFDiagnosticsViewController setShowNANUI:];
-[WFDiagnosticsViewController showNANUI];
```
