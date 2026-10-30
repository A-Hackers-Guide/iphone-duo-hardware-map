# `PKTextInputDebugSharpenerLogViewController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`
- 6 instance variables, 10 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSURL" _sharpenerLogURL;
@"UITableView" __mainTableView;
@"UILabel" __tableHeaderLabel;
@"PKTextInputDebugLogEntryRerun" __currentEntryRerun;
@"NSMutableDictionary" __rerunResultsBySection;
@"PKTextInputDebugSharpenerLog" _sharpenerLog;
```

## Properties

```
@property (T@"UITableView",&,N,V__mainTableView) _mainTableView;
@property (T@"UILabel",&,N,V__tableHeaderLabel) _tableHeaderLabel;
@property (T@"PKTextInputDebugLogEntryRerun",&,N,V__currentEntryRerun) _currentEntryRerun;
@property (T@"NSMutableDictionary",R,N,V__rerunResultsBySection) _rerunResultsBySection;
@property (T@"PKTextInputDebugSharpenerLog",R,N,V_sharpenerLog) sharpenerLog;
@property (T@"NSURL",R,N,V_sharpenerLogURL) sharpenerLogURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKTextInputDebugSharpenerLogViewController canLoadFromFileAtURL:];
```

## Instance methods

```
-[PKTextInputDebugSharpenerLogViewController tableView:numberOfRowsInSection:];
-[PKTextInputDebugSharpenerLogViewController numberOfSectionsInTableView:];
-[PKTextInputDebugSharpenerLogViewController tableView:cellForRowAtIndexPath:];
-[PKTextInputDebugSharpenerLogViewController tableView:titleForHeaderInSection:];
-[PKTextInputDebugSharpenerLogViewController viewDidLoad];
-[PKTextInputDebugSharpenerLogViewController viewDidLayoutSubviews];
-[PKTextInputDebugSharpenerLogViewController _canShowWhileLocked];
-[PKTextInputDebugSharpenerLogViewController _handleDoneButton:];
-[PKTextInputDebugSharpenerLogViewController _mainTableView];
-[PKTextInputDebugSharpenerLogViewController _handleActionButton:];
-[PKTextInputDebugSharpenerLogViewController sharpenerLogURL];
-[PKTextInputDebugSharpenerLogViewController _configureCell:asDrawingDisplayForEntry:];
-[PKTextInputDebugSharpenerLogViewController _configureCell:withTitle:details:];
-[PKTextInputDebugSharpenerLogViewController _currentEntryRerun];
-[PKTextInputDebugSharpenerLogViewController _handleRerunButton:];
-[PKTextInputDebugSharpenerLogViewController _rerunRecognitionForEntryAtIndex:];
-[PKTextInputDebugSharpenerLogViewController _rerunResultsBySection];
-[PKTextInputDebugSharpenerLogViewController _tableHeaderLabel];
-[PKTextInputDebugSharpenerLogViewController _tableHeaderText];
-[PKTextInputDebugSharpenerLogViewController initWithSharpenerLog:];
-[PKTextInputDebugSharpenerLogViewController initWithSharpenerLogURL:error:];
-[PKTextInputDebugSharpenerLogViewController set_currentEntryRerun:];
-[PKTextInputDebugSharpenerLogViewController set_mainTableView:];
-[PKTextInputDebugSharpenerLogViewController set_tableHeaderLabel:];
-[PKTextInputDebugSharpenerLogViewController sharpenerLog];
```
