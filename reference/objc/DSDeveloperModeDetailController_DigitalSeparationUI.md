# `DSDeveloperModeDetailController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- 6 instance variables, 6 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _hasRecentSessions;
@"<DSPairedComputerDelegate>" _delegate;
@"DSPairedComputer" _computer;
@"<DSDevicesAppSessionManagerProtocol>" _sessionStore;
@"NSMutableArray" _orderedCells;
@"UITableViewCell" _recentSessionsCell;
```

## Properties

```
@property (T@"DSPairedComputer",&,N,V_computer) computer;
@property (T@"<DSDevicesAppSessionManagerProtocol>",&,N,V_sessionStore) sessionStore;
@property (T@"NSMutableArray",&,N,V_orderedCells) orderedCells;
@property (T@"UITableViewCell",&,N,V_recentSessionsCell) recentSessionsCell;
@property (TB,N,V_hasRecentSessions) hasRecentSessions;
@property (T@"<DSPairedComputerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[DSDeveloperModeDetailController initialize];
```

## Instance methods

```
-[DSDeveloperModeDetailController tableView:titleForFooterInSection:];
-[DSDeveloperModeDetailController tableView:numberOfRowsInSection:];
-[DSDeveloperModeDetailController numberOfSectionsInTableView:];
-[DSDeveloperModeDetailController tableView:editingStyleForRowAtIndexPath:];
-[DSDeveloperModeDetailController tableView:cellForRowAtIndexPath:];
-[DSDeveloperModeDetailController viewDidLoad];
-[DSDeveloperModeDetailController setDelegate:];
-[DSDeveloperModeDetailController tableView:willSelectRowAtIndexPath:];
-[DSDeveloperModeDetailController setSessionStore:];
-[DSDeveloperModeDetailController tableView:didSelectRowAtIndexPath:];
-[DSDeveloperModeDetailController delegate];
-[DSDeveloperModeDetailController orderedCells];
-[DSDeveloperModeDetailController setOrderedCells:];
-[DSDeveloperModeDetailController sessionStore];
-[DSDeveloperModeDetailController cellWithText:secondaryText:];
-[DSDeveloperModeDetailController computer];
-[DSDeveloperModeDetailController hasRecentSessions];
-[DSDeveloperModeDetailController initWithPairedComputer:sessionStore:hasSessions:];
-[DSDeveloperModeDetailController presentUnpairAlert];
-[DSDeveloperModeDetailController recentSessionsCell];
-[DSDeveloperModeDetailController returnFromDetailAndRemoveComputer];
-[DSDeveloperModeDetailController setComputer:];
-[DSDeveloperModeDetailController setHasRecentSessions:];
-[DSDeveloperModeDetailController setRecentSessionsCell:];
-[DSDeveloperModeDetailController unpairCell];
```
