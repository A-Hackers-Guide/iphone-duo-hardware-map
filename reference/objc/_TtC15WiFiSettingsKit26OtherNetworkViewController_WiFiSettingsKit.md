# `_TtC15WiFiSettingsKit26OtherNetworkViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](../userland/System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBTableWelcomeController`
- Protocols: `UITextFieldDelegate`, `UITableViewDelegate`, `UITableViewDataSource`
- 19 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
WiFiSettingsKit.AssociationCredentials credentials;
Swift.Bool chinaDevice;
Swift.Bool wapiEnabled;
WiFiSettingsKit.AssociationModel ? associationModel;
WiFiSettingsKit.WiFiAssociator associator;
Swift.Bool joining;
_$sSS originalTitle;
_$sSS originalDetailText;
Swift.Bool isScanListEnterpriseWAPINetwork;
WiFiSettingsKit.LabeledTextFieldCell ? nameCell;
WiFiSettingsKit.LabeledTextFieldCell ? usernameCell;
WiFiSettingsKit.LabeledTextFieldCell ? passwordCell;
_$sSo15UITableViewCellCSg securityCell;
_$sSo15UITableViewCellCSg identityCell;
_$sSo15UITableViewCellCSg modeCell;
WiFiSettingsKit.WiFiField ? focusedField;
WiFiSettingsKit.WiFiField ? lastFocusedField;
_$syycSg onCancel;
WiFiSettingsKit.AssociationCredentials _$scSg -> onJoin;
```

## Instance methods

```
-[_TtC15WiFiSettingsKit26OtherNetworkViewController tableView:numberOfRowsInSection:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController numberOfSectionsInTableView:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController tableView:cellForRowAtIndexPath:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController initWithTitle:detailText:symbolName:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController cancelTapped];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController viewWillDisappear:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController initWithTitle:detailText:icon:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController textFieldDidBeginEditing:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController viewDidLoad];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController textFieldShouldReturn:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController viewDidAppear:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController tableView:didSelectRowAtIndexPath:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController initWithTitle:detailText:icon:adoptTableViewScrollView:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController initWithTitle:detailText:symbolName:adoptTableViewScrollView:];
-[_TtC15WiFiSettingsKit26OtherNetworkViewController joinTapped];
```
