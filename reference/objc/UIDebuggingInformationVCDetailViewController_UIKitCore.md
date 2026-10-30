# `UIDebuggingInformationVCDetailViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`
- 3 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UITableView" _tableView;
@"NSArray" _data;
@"UIViewController" _inspectedVC;
```

## Properties

```
@property (T@"UIViewController",W,N,V_inspectedVC) inspectedVC;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDebuggingInformationVCDetailViewController tableView:numberOfRowsInSection:];
-[UIDebuggingInformationVCDetailViewController numberOfSectionsInTableView:];
-[UIDebuggingInformationVCDetailViewController tableView:cellForRowAtIndexPath:];
-[UIDebuggingInformationVCDetailViewController tableView:titleForHeaderInSection:];
-[UIDebuggingInformationVCDetailViewController viewDidLoad];
-[UIDebuggingInformationVCDetailViewController initWithNibName:bundle:];
-[UIDebuggingInformationVCDetailViewController viewWillAppear:];
-[UIDebuggingInformationVCDetailViewController tableView:didSelectRowAtIndexPath:];
-[UIDebuggingInformationVCDetailViewController setInspectedVC:];
-[UIDebuggingInformationVCDetailViewController _updateDataAndReload:];
-[UIDebuggingInformationVCDetailViewController inspectVC:];
-[UIDebuggingInformationVCDetailViewController inspectedVC];
```
