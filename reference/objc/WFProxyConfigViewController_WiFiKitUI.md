# `WFProxyConfigViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFInsetTableViewController`
- 10 instance variables, 10 properties, 34 instance methods, 0 class methods

## Instance variables

```
@? _saveHandler;
@"WFNetworkSettingsConfig" _originalConfig;
@"WFNetworkSettingsConfig" _modifiedConfig;
@"UISwitch" _authSwitch;
@"WFTextFieldCell" _serverCell;
@"WFTextFieldCell" _portCell;
@"WFTextFieldCell" _userCell;
@"WFTextFieldCell" _passwordCell;
@"WFTextFieldCell" _urlCell;
@"WFAppearanceProxy" _appearanceProxy;
```

## Properties

```
@property (T@"WFNetworkSettingsConfig",&,N,V_originalConfig) originalConfig;
@property (T@"WFNetworkSettingsConfig",&,N,V_modifiedConfig) modifiedConfig;
@property (T@"UISwitch",&,N,V_authSwitch) authSwitch;
@property (T@"WFTextFieldCell",&,N,V_serverCell) serverCell;
@property (T@"WFTextFieldCell",&,N,V_portCell) portCell;
@property (T@"WFTextFieldCell",&,N,V_userCell) userCell;
@property (T@"WFTextFieldCell",&,N,V_passwordCell) passwordCell;
@property (T@"WFTextFieldCell",&,N,V_urlCell) urlCell;
@property (T@"WFAppearanceProxy",&,N,V_appearanceProxy) appearanceProxy;
@property (T@?,C,N,V_saveHandler) saveHandler;
```

## Instance methods

```
-[WFProxyConfigViewController tableView:titleForFooterInSection:];
-[WFProxyConfigViewController tableView:numberOfRowsInSection:];
-[WFProxyConfigViewController numberOfSectionsInTableView:];
-[WFProxyConfigViewController tableView:cellForRowAtIndexPath:];
-[WFProxyConfigViewController initWithConfig:];
-[WFProxyConfigViewController save:];
-[WFProxyConfigViewController viewDidLoad];
-[WFProxyConfigViewController appearanceProxy];
-[WFProxyConfigViewController _canShowWhileLocked];
-[WFProxyConfigViewController tableView:didSelectRowAtIndexPath:];
-[WFProxyConfigViewController setSaveHandler:];
-[WFProxyConfigViewController saveHandler];
-[WFProxyConfigViewController _updateSaveEnabled];
-[WFProxyConfigViewController passwordCell];
-[WFProxyConfigViewController setPasswordCell:];
-[WFProxyConfigViewController setAppearanceProxy:];
-[WFProxyConfigViewController urlCell];
-[WFProxyConfigViewController initWithConfig:appearanceProxy:];
-[WFProxyConfigViewController _changeProxyAuthentication:];
-[WFProxyConfigViewController _configCellLeadingInset];
-[WFProxyConfigViewController _setFirstResponderAfterCell:];
-[WFProxyConfigViewController authSwitch];
-[WFProxyConfigViewController modifiedConfig];
-[WFProxyConfigViewController originalConfig];
-[WFProxyConfigViewController portCell];
-[WFProxyConfigViewController serverCell];
-[WFProxyConfigViewController setAuthSwitch:];
-[WFProxyConfigViewController setModifiedConfig:];
-[WFProxyConfigViewController setOriginalConfig:];
-[WFProxyConfigViewController setPortCell:];
-[WFProxyConfigViewController setServerCell:];
-[WFProxyConfigViewController setUrlCell:];
-[WFProxyConfigViewController setUserCell:];
-[WFProxyConfigViewController userCell];
```
