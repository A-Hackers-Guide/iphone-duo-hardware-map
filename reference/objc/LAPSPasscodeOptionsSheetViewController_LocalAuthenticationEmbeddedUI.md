# `LAPSPasscodeOptionsSheetViewController`

- Image: [`/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`](../userland/System__Library__Frameworks__LocalAuthenticationEmbeddedUI.framework__LocalAuthenticationEmbeddedUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`, `LAPSPasscodeOptionsViewController`
- 6 instance variables, 5 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"LACUIPasscodeServiceOptionsViewConfiguration" _config;
q _style;
@"UITableView" _tableView;
@"NSOrderedSet" _allowedPasscodeTypes;
q _selectedPasscodeTypeIndex;
@"<LAPSPasscodeOptionsViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<LAPSPasscodeOptionsViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LAPSPasscodeOptionsSheetViewController tableView:heightForFooterInSection:];
-[LAPSPasscodeOptionsSheetViewController _setup];
-[LAPSPasscodeOptionsSheetViewController tableView:numberOfRowsInSection:];
-[LAPSPasscodeOptionsSheetViewController numberOfSectionsInTableView:];
-[LAPSPasscodeOptionsSheetViewController tableView:viewForFooterInSection:];
-[LAPSPasscodeOptionsSheetViewController tableView:cellForRowAtIndexPath:];
-[LAPSPasscodeOptionsSheetViewController viewWillDisappear:];
-[LAPSPasscodeOptionsSheetViewController supportedInterfaceOrientations];
-[LAPSPasscodeOptionsSheetViewController viewDidLoad];
-[LAPSPasscodeOptionsSheetViewController initWithConfiguration:];
-[LAPSPasscodeOptionsSheetViewController _canShowWhileLocked];
-[LAPSPasscodeOptionsSheetViewController setDelegate:];
-[LAPSPasscodeOptionsSheetViewController tableView:willSelectRowAtIndexPath:];
-[LAPSPasscodeOptionsSheetViewController tableView:didSelectRowAtIndexPath:];
-[LAPSPasscodeOptionsSheetViewController delegate];
-[LAPSPasscodeOptionsSheetViewController viewDidDisappear:];
-[LAPSPasscodeOptionsSheetViewController preferredContentSize];
-[LAPSPasscodeOptionsSheetViewController tableView:viewForHeaderInSection:];
-[LAPSPasscodeOptionsSheetViewController tableView:heightForHeaderInSection:];
-[LAPSPasscodeOptionsSheetViewController _heightForFooterInSection:];
-[LAPSPasscodeOptionsSheetViewController _heightForHeaderInSection:];
-[LAPSPasscodeOptionsSheetViewController initWithConfiguration:style:];
-[LAPSPasscodeOptionsSheetViewController tableView:didDeselectRowAtIndexPath:];
-[LAPSPasscodeOptionsSheetViewController tableView:estimatedHeightForFooterInSection:];
-[LAPSPasscodeOptionsSheetViewController tableView:estimatedHeightForHeaderInSection:];
-[LAPSPasscodeOptionsSheetViewController _cellIdentifierForIndexPath:];
-[LAPSPasscodeOptionsSheetViewController _close:];
-[LAPSPasscodeOptionsSheetViewController _tableViewStyle];
-[LAPSPasscodeOptionsSheetViewController _changePasscodeRecoveryStatus:];
-[LAPSPasscodeOptionsSheetViewController _changeSelectedPasscodeTypeIndex:];
-[LAPSPasscodeOptionsSheetViewController _tableCellTextColor];
-[LAPSPasscodeOptionsSheetViewController _tableRowShouldDismissOnSelection];
-[LAPSPasscodeOptionsSheetViewController _tableViewNeedsHeaderView];
```
