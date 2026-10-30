# `DSDevicesAppRecentSessionsController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`
- 5 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" _deviceIdentifier;
@"<DSDevicesAppSessionManagerProtocol>" _sessionStore;
@"NSArray" _sortedYears;
@"NSDictionary" _sessionsByYear;
@"UITableView" _tableView;
```

## Properties

```
@property (T@"NSString",C,N,V_deviceIdentifier) deviceIdentifier;
@property (T@"<DSDevicesAppSessionManagerProtocol>",&,N,V_sessionStore) sessionStore;
@property (T@"NSArray",&,N,V_sortedYears) sortedYears;
@property (T@"NSDictionary",&,N,V_sessionsByYear) sessionsByYear;
@property (T@"UITableView",&,N,V_tableView) tableView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSDevicesAppRecentSessionsController tableView];
-[DSDevicesAppRecentSessionsController tableView:numberOfRowsInSection:];
-[DSDevicesAppRecentSessionsController numberOfSectionsInTableView:];
-[DSDevicesAppRecentSessionsController tableView:cellForRowAtIndexPath:];
-[DSDevicesAppRecentSessionsController setDeviceIdentifier:];
-[DSDevicesAppRecentSessionsController close];
-[DSDevicesAppRecentSessionsController tableView:titleForHeaderInSection:];
-[DSDevicesAppRecentSessionsController viewDidLoad];
-[DSDevicesAppRecentSessionsController setTableView:];
-[DSDevicesAppRecentSessionsController deviceIdentifier];
-[DSDevicesAppRecentSessionsController setSessionStore:];
-[DSDevicesAppRecentSessionsController sessionStore];
-[DSDevicesAppRecentSessionsController setSortedYears:];
-[DSDevicesAppRecentSessionsController _buildSectionsFromSessions:];
-[DSDevicesAppRecentSessionsController initWithDeviceIdentifier:sessionStore:];
-[DSDevicesAppRecentSessionsController sessionEventAtIndexPath:];
-[DSDevicesAppRecentSessionsController sessionsByYear];
-[DSDevicesAppRecentSessionsController setSessionsByYear:];
-[DSDevicesAppRecentSessionsController sortedYears];
```
