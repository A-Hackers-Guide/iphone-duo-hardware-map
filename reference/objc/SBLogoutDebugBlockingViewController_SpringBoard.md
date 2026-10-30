# `SBLogoutDebugBlockingViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`
- 3 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _debugBlockingTasks;
@"NSArray" _applicationKeys;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_debugBlockingTasks) debugBlockingTasks;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLogoutDebugBlockingViewController tableView:shouldHighlightRowAtIndexPath:];
-[SBLogoutDebugBlockingViewController tableView:canMoveRowAtIndexPath:];
-[SBLogoutDebugBlockingViewController tableView:numberOfRowsInSection:];
-[SBLogoutDebugBlockingViewController numberOfSectionsInTableView:];
-[SBLogoutDebugBlockingViewController tableView:cellForRowAtIndexPath:];
-[SBLogoutDebugBlockingViewController initWithApplicationController:];
-[SBLogoutDebugBlockingViewController tableView:titleForHeaderInSection:];
-[SBLogoutDebugBlockingViewController viewWillAppear:];
-[SBLogoutDebugBlockingViewController _canShowWhileLocked];
-[SBLogoutDebugBlockingViewController loadView];
-[SBLogoutDebugBlockingViewController _tableView];
-[SBLogoutDebugBlockingViewController tableView:canEditRowAtIndexPath:];
-[SBLogoutDebugBlockingViewController tableView:indentationLevelForRowAtIndexPath:];
-[SBLogoutDebugBlockingViewController _configureCell:withBlockingTask:];
-[SBLogoutDebugBlockingViewController debugBlockingTasks];
-[SBLogoutDebugBlockingViewController setDebugBlockingTasks:];
```
