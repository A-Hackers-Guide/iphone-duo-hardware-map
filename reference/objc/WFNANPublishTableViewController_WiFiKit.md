# `WFNANPublishTableViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- 12 instance variables, 12 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _isServiceSpecificInfoHex;
@"NSOrderedSet" _sections;
@"WFNANTableViewContext" _context;
@"WFNetworkSettingsCellFactory" _cellFactory;
@"WFNANPublishTableViewDataSource" _dataSource;
@"NSString" _serviceName;
q _serviceType;
@"NSString" _instanceName;
@"NSString" _serviceSpecificInfo;
@"NSString" _portNumber;
q _protocolType;
@"NSString" _passphrase;
```

## Properties

```
@property (T@"NSOrderedSet",&,N,V_sections) sections;
@property (T@"WFNANTableViewContext",&,N,V_context) context;
@property (T@"WFNetworkSettingsCellFactory",&,N,V_cellFactory) cellFactory;
@property (T@"WFNANPublishTableViewDataSource",&,N,V_dataSource) dataSource;
@property (T@"NSString",&,N,V_serviceName) serviceName;
@property (Tq,N,V_serviceType) serviceType;
@property (T@"NSString",&,N,V_instanceName) instanceName;
@property (T@"NSString",&,N,V_serviceSpecificInfo) serviceSpecificInfo;
@property (TB,N,V_isServiceSpecificInfoHex) isServiceSpecificInfoHex;
@property (T@"NSString",N,V_portNumber) portNumber;
@property (Tq,N,V_protocolType) protocolType;
@property (T@"NSString",N,V_passphrase) passphrase;
```

## Instance methods

```
-[WFNANPublishTableViewController setPortNumber:];
-[WFNANPublishTableViewController initWithContext:];
-[WFNANPublishTableViewController portNumber];
-[WFNANPublishTableViewController sections];
-[WFNANPublishTableViewController serviceSpecificInfo];
-[WFNANPublishTableViewController setServiceSpecificInfo:];
-[WFNANPublishTableViewController viewDidLoad];
-[WFNANPublishTableViewController setDataSource:];
-[WFNANPublishTableViewController serviceName];
-[WFNANPublishTableViewController setContext:];
-[WFNANPublishTableViewController dataSource];
-[WFNANPublishTableViewController setServiceName:];
-[WFNANPublishTableViewController tableView:didSelectRowAtIndexPath:];
-[WFNANPublishTableViewController setSections:];
-[WFNANPublishTableViewController viewDidDisappear:];
-[WFNANPublishTableViewController setServiceType:];
-[WFNANPublishTableViewController context];
-[WFNANPublishTableViewController dismissKeyboard];
-[WFNANPublishTableViewController serviceType];
-[WFNANPublishTableViewController instanceName];
-[WFNANPublishTableViewController protocolType];
-[WFNANPublishTableViewController setProtocolType:];
-[WFNANPublishTableViewController setInstanceName:];
-[WFNANPublishTableViewController _identifierForSection:];
-[WFNANPublishTableViewController passphrase];
-[WFNANPublishTableViewController setPassphrase:];
-[WFNANPublishTableViewController _configureDataSource];
-[WFNANPublishTableViewController setCellFactory:];
-[WFNANPublishTableViewController _defaultSections];
-[WFNANPublishTableViewController _handleAddPublisher];
-[WFNANPublishTableViewController _handleDataSessionsChangedNotification:];
-[WFNANPublishTableViewController _handlePublishersChangedNotification:];
-[WFNANPublishTableViewController cellFactory];
-[WFNANPublishTableViewController clearInputFields];
-[WFNANPublishTableViewController createTextFieldCellWithTableView:indexPath:text:placeholder:keyboardType:textChangedHandler:];
-[WFNANPublishTableViewController isServiceSpecificInfoHex];
-[WFNANPublishTableViewController serviceSpecificInfoFromString];
-[WFNANPublishTableViewController setIsServiceSpecificInfoHex:];
```
