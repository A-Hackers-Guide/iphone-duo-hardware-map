# `CABTMIDICentralViewController`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewController`
- Protocols: `UITableViewDelegate`, `UITableViewDataSource`, `BTLEConnectionTable`
- 12 instance variables, 4 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" peripheralList;
@"AMSBTLEConnectionManager" connectionManager;
@"UIActivityIndicatorView" indicator;
B didCleanup;
B didRegisterObserver;
B inEditingMode;
@"NSTimer" connectionTimer;
@"UIBarButtonItem" previousLeftItem;
@"UIBarButtonItem" previousRightItem;
@"UIBarButtonItem" editButton;
@"UIBarButtonItem" cancelButton;
@"UIBarButtonItem" forgetButton;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CABTMIDICentralViewController tableView:shouldHighlightRowAtIndexPath:];
-[CABTMIDICentralViewController cleanup];
-[CABTMIDICentralViewController tableView:titleForFooterInSection:];
-[CABTMIDICentralViewController tableView:numberOfRowsInSection:];
-[CABTMIDICentralViewController numberOfSectionsInTableView:];
-[CABTMIDICentralViewController tableView:editingStyleForRowAtIndexPath:];
-[CABTMIDICentralViewController tableView:commitEditingStyle:forRowAtIndexPath:];
-[CABTMIDICentralViewController tableView:cellForRowAtIndexPath:];
-[CABTMIDICentralViewController observeValueForKeyPath:ofObject:change:context:];
-[CABTMIDICentralViewController dealloc];
-[CABTMIDICentralViewController tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:];
-[CABTMIDICentralViewController tableView:titleForHeaderInSection:];
-[CABTMIDICentralViewController viewDidLoad];
-[CABTMIDICentralViewController setEditing:animated:];
-[CABTMIDICentralViewController initWithNibName:bundle:];
-[CABTMIDICentralViewController viewWillAppear:];
-[CABTMIDICentralViewController title];
-[CABTMIDICentralViewController loadView];
-[CABTMIDICentralViewController didReceiveMemoryWarning];
-[CABTMIDICentralViewController tableView:didSelectRowAtIndexPath:];
-[CABTMIDICentralViewController viewDidDisappear:];
-[CABTMIDICentralViewController tableView:estimatedHeightForRowAtIndexPath:];
-[CABTMIDICentralViewController tableView:canEditRowAtIndexPath:];
-[CABTMIDICentralViewController cancelAction:];
-[CABTMIDICentralViewController editAction:];
-[CABTMIDICentralViewController peripheralCount];
-[CABTMIDICentralViewController centralTimerFired:];
-[CABTMIDICentralViewController forgetAction:];
-[CABTMIDICentralViewController peripheralAtIndex:];
-[CABTMIDICentralViewController setUIEnabled:];
-[CABTMIDICentralViewController updateButtonsToMatchTableState];
-[CABTMIDICentralViewController updatePeripheralTable];
```
