# `WFIPConfigViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- 10 instance variables, 10 properties, 34 instance methods, 0 class methods

## Instance variables

```
@? _saveHandler;
@"WFNetworkSettingsConfig" _originalConfig;
@"WFNetworkSettingsConfig" _modifiedConfig;
q _type;
@"WFTextFieldCell" _ipAddressCell;
@"WFTextFieldCell" _subnetMaskCell;
@"WFTextFieldCell" _routerCell;
@"WFTextFieldCell" _prefixCell;
@"WFTextFieldCell" _clientIDCell;
@"WFAppearanceProxy" _appearanceProxy;
```

## Properties

```
@property (T@"WFNetworkSettingsConfig",&,N,V_originalConfig) originalConfig;
@property (T@"WFNetworkSettingsConfig",&,N,V_modifiedConfig) modifiedConfig;
@property (Tq,N,V_type) type;
@property (T@"WFTextFieldCell",&,N,V_ipAddressCell) ipAddressCell;
@property (T@"WFTextFieldCell",&,N,V_subnetMaskCell) subnetMaskCell;
@property (T@"WFTextFieldCell",&,N,V_routerCell) routerCell;
@property (T@"WFTextFieldCell",&,N,V_prefixCell) prefixCell;
@property (T@"WFTextFieldCell",&,N,V_clientIDCell) clientIDCell;
@property (T@"WFAppearanceProxy",&,N,V_appearanceProxy) appearanceProxy;
@property (T@?,C,N,V_saveHandler) saveHandler;
```

## Instance methods

```
-[WFIPConfigViewController tableView:numberOfRowsInSection:];
-[WFIPConfigViewController numberOfSectionsInTableView:];
-[WFIPConfigViewController tableView:cellForRowAtIndexPath:];
-[WFIPConfigViewController save:];
-[WFIPConfigViewController tableView:titleForHeaderInSection:];
-[WFIPConfigViewController viewDidLoad];
-[WFIPConfigViewController appearanceProxy];
-[WFIPConfigViewController _canShowWhileLocked];
-[WFIPConfigViewController setType:];
-[WFIPConfigViewController type];
-[WFIPConfigViewController didReceiveMemoryWarning];
-[WFIPConfigViewController tableView:didSelectRowAtIndexPath:];
-[WFIPConfigViewController setSaveHandler:];
-[WFIPConfigViewController saveHandler];
-[WFIPConfigViewController _updateSaveEnabled];
-[WFIPConfigViewController setAppearanceProxy:];
-[WFIPConfigViewController _configCellLeadingInset];
-[WFIPConfigViewController _setFirstResponderAfterCell:];
-[WFIPConfigViewController clientIDCell];
-[WFIPConfigViewController initWithConfig:ipType:];
-[WFIPConfigViewController initWithConfig:ipType:appearanceProxy:];
-[WFIPConfigViewController ipAddressCell];
-[WFIPConfigViewController modifiedConfig];
-[WFIPConfigViewController originalConfig];
-[WFIPConfigViewController prefixCell];
-[WFIPConfigViewController routerCell];
-[WFIPConfigViewController setClientIDCell:];
-[WFIPConfigViewController setIpAddressCell:];
-[WFIPConfigViewController setModifiedConfig:];
-[WFIPConfigViewController setOriginalConfig:];
-[WFIPConfigViewController setPrefixCell:];
-[WFIPConfigViewController setRouterCell:];
-[WFIPConfigViewController setSubnetMaskCell:];
-[WFIPConfigViewController subnetMaskCell];
```
