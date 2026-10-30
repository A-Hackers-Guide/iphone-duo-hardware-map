# `WFNANDiscoveryResultsTableViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- Protocols: `WiFiAwareDataSessionDelegate`
- 5 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSOrderedSet" _sections;
@"WFNANTableViewContext" _context;
@"WiFiAwareSubscriber" _subscriber;
@"NSString" _passphrase;
@"WFNANDiscoveryResultsTableViewDataSource" _dataSource;
```

## Properties

```
@property (T@"NSOrderedSet",&,N,V_sections) sections;
@property (T@"WFNANTableViewContext",&,N,V_context) context;
@property (T@"WiFiAwareSubscriber",&,N,V_subscriber) subscriber;
@property (T@"NSString",&,N,V_passphrase) passphrase;
@property (T@"WFNANDiscoveryResultsTableViewDataSource",&,N,V_dataSource) dataSource;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFNANDiscoveryResultsTableViewController subscriber];
-[WFNANDiscoveryResultsTableViewController sections];
-[WFNANDiscoveryResultsTableViewController viewDidLoad];
-[WFNANDiscoveryResultsTableViewController setDataSource:];
-[WFNANDiscoveryResultsTableViewController setContext:];
-[WFNANDiscoveryResultsTableViewController dataSource];
-[WFNANDiscoveryResultsTableViewController tableView:didSelectRowAtIndexPath:];
-[WFNANDiscoveryResultsTableViewController setSections:];
-[WFNANDiscoveryResultsTableViewController viewDidDisappear:];
-[WFNANDiscoveryResultsTableViewController setSubscriber:];
-[WFNANDiscoveryResultsTableViewController context];
-[WFNANDiscoveryResultsTableViewController dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:];
-[WFNANDiscoveryResultsTableViewController dataSession:failedToStartWithError:];
-[WFNANDiscoveryResultsTableViewController dataSession:terminatedWithReason:];
-[WFNANDiscoveryResultsTableViewController dataSessionRequestStarted:];
-[WFNANDiscoveryResultsTableViewController _identifierForSection:];
-[WFNANDiscoveryResultsTableViewController passphrase];
-[WFNANDiscoveryResultsTableViewController setPassphrase:];
-[WFNANDiscoveryResultsTableViewController _configureDataSource];
-[WFNANDiscoveryResultsTableViewController _defaultSections];
-[WFNANDiscoveryResultsTableViewController _handleDataSessionsChangedNotification:];
-[WFNANDiscoveryResultsTableViewController _handleDiscoveryResultsChangedNotification:];
-[WFNANDiscoveryResultsTableViewController initWithContext:forSubscriber:];
-[WFNANDiscoveryResultsTableViewController passphraseTextFieldDidChange:];
```
