# `WFNANDiscoveryResultsTableViewDataSource`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewDiffableDataSource`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSOrderedSet" _sections;
@"WFNANTableViewContext" _context;
@"WiFiAwareSubscriber" _subscriber;
```

## Properties

```
@property (T@"NSOrderedSet",&,N,V_sections) sections;
@property (T@"WFNANTableViewContext",&,N,V_context) context;
@property (T@"WiFiAwareSubscriber",&,N,V_subscriber) subscriber;
```

## Instance methods

```
-[WFNANDiscoveryResultsTableViewDataSource subscriber];
-[WFNANDiscoveryResultsTableViewDataSource tableView:commitEditingStyle:forRowAtIndexPath:];
-[WFNANDiscoveryResultsTableViewDataSource sections];
-[WFNANDiscoveryResultsTableViewDataSource tableView:titleForHeaderInSection:];
-[WFNANDiscoveryResultsTableViewDataSource setContext:];
-[WFNANDiscoveryResultsTableViewDataSource setSections:];
-[WFNANDiscoveryResultsTableViewDataSource setSubscriber:];
-[WFNANDiscoveryResultsTableViewDataSource context];
-[WFNANDiscoveryResultsTableViewDataSource tableView:canEditRowAtIndexPath:];
-[WFNANDiscoveryResultsTableViewDataSource initWithTableView:context:subscriber:sections:cellProvider:];
```
