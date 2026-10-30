# `WFDNSConfigViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- 11 instance variables, 11 properties, 44 instance methods, 0 class methods

## Instance variables

```
B _shouldShowPrivacyRelayHeader;
@? _saveHandler;
q _originalDNSConfig;
q _dnsConfig;
@"NSArray" _originalServers;
@"NSMutableArray" _servers;
@"NSArray" _originalDomains;
@"NSMutableArray" _domains;
@"UIBarButtonItem" _saveButton;
@"WFAppearanceProxy" _appearanceProxy;
q _deviceCapability;
```

## Properties

```
@property (Tq,N,V_originalDNSConfig) originalDNSConfig;
@property (Tq,N,V_dnsConfig) dnsConfig;
@property (T@"NSArray",&,N,V_originalServers) originalServers;
@property (T@"NSMutableArray",&,N,V_servers) servers;
@property (T@"NSArray",&,N,V_originalDomains) originalDomains;
@property (T@"NSMutableArray",&,N,V_domains) domains;
@property (T@"UIBarButtonItem",&,N,V_saveButton) saveButton;
@property (T@"WFAppearanceProxy",&,N,V_appearanceProxy) appearanceProxy;
@property (TB,N,V_shouldShowPrivacyRelayHeader) shouldShowPrivacyRelayHeader;
@property (Tq,N,V_deviceCapability) deviceCapability;
@property (T@?,C,N,V_saveHandler) saveHandler;
```

## Instance methods

```
-[WFDNSConfigViewController deviceCapability];
-[WFDNSConfigViewController tableView:titleForFooterInSection:];
-[WFDNSConfigViewController tableView:numberOfRowsInSection:];
-[WFDNSConfigViewController tableView:shouldIndentWhileEditingRowAtIndexPath:];
-[WFDNSConfigViewController numberOfSectionsInTableView:];
-[WFDNSConfigViewController domains];
-[WFDNSConfigViewController tableView:editingStyleForRowAtIndexPath:];
-[WFDNSConfigViewController tableView:commitEditingStyle:forRowAtIndexPath:];
-[WFDNSConfigViewController tableView:cellForRowAtIndexPath:];
-[WFDNSConfigViewController initWithConfig:];
-[WFDNSConfigViewController save:];
-[WFDNSConfigViewController tableView:titleForHeaderInSection:];
-[WFDNSConfigViewController viewDidLoad];
-[WFDNSConfigViewController appearanceProxy];
-[WFDNSConfigViewController _canShowWhileLocked];
-[WFDNSConfigViewController tableView:didSelectRowAtIndexPath:];
-[WFDNSConfigViewController setDeviceCapability:];
-[WFDNSConfigViewController setDomains:];
-[WFDNSConfigViewController saveButton];
-[WFDNSConfigViewController setSaveButton:];
-[WFDNSConfigViewController servers];
-[WFDNSConfigViewController setSaveHandler:];
-[WFDNSConfigViewController saveHandler];
-[WFDNSConfigViewController _updateSaveEnabled];
-[WFDNSConfigViewController setServers:];
-[WFDNSConfigViewController dnsConfig];
-[WFDNSConfigViewController setAppearanceProxy:];
-[WFDNSConfigViewController setDnsConfig:];
-[WFDNSConfigViewController originalServers];
-[WFDNSConfigViewController initWithConfig:appearanceProxy:];
-[WFDNSConfigViewController originalDomains];
-[WFDNSConfigViewController _addDomainAtIndexPath:];
-[WFDNSConfigViewController _addServerAtIndexPath:];
-[WFDNSConfigViewController _configCellLeadingInset];
-[WFDNSConfigViewController _configCellTrailingInset];
-[WFDNSConfigViewController _isChinaDevice];
-[WFDNSConfigViewController originalDNSConfig];
-[WFDNSConfigViewController sectionForSectionNumber:];
-[WFDNSConfigViewController sectionNumberForSection:];
-[WFDNSConfigViewController setOriginalDNSConfig:];
-[WFDNSConfigViewController setOriginalDomains:];
-[WFDNSConfigViewController setOriginalServers:];
-[WFDNSConfigViewController setShouldShowPrivacyRelayHeader:];
-[WFDNSConfigViewController shouldShowPrivacyRelayHeader];
```
