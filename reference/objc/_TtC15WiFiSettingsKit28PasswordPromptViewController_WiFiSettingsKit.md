# `_TtC15WiFiSettingsKit28PasswordPromptViewController`

- Image: [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](../userland/System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `OBTableWelcomeController`
- Protocols: `UITextFieldDelegate`, `UITableViewDelegate`, `UITableViewDataSource`
- 14 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
WiFiSettingsKit.PasswordPromptContext context;
WiFiSettingsKit.AssociationCredentials credentials;
Swift.Bool chinaDevice;
WiFiSettingsKit.PasswordSharer ? sharer;
Swift.Bool joining;
_$sSS originalTitle;
_$sSS originalDetailText;
WiFiSettingsKit.LabeledTextFieldCell ? usernameCell;
WiFiSettingsKit.LabeledTextFieldCell ? passwordCell;
_$sSo15UITableViewCellCSg identityCell;
_$sSo15UITableViewCellCSg modePickerCell;
WiFiSettingsKit.WiFiField ? focusedField;
_$syycSg onCancel;
WiFiSettingsKit.AssociationCredentials _$scSg -> onJoin;
```

## Instance methods

```
-[_TtC15WiFiSettingsKit28PasswordPromptViewController tableView:titleForFooterInSection:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController tableView:numberOfRowsInSection:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController numberOfSectionsInTableView:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController tableView:cellForRowAtIndexPath:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController initWithTitle:detailText:symbolName:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController cancelTapped];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController viewWillDisappear:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController initWithTitle:detailText:icon:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController dealloc];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController textFieldShouldEndEditing:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController textFieldDidBeginEditing:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController viewDidLoad];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController textFieldShouldReturn:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController viewDidAppear:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController textField:shouldChangeCharactersInRange:replacementString:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController tableView:didSelectRowAtIndexPath:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController initWithTitle:detailText:icon:adoptTableViewScrollView:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController initWithTitle:detailText:symbolName:adoptTableViewScrollView:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController handleSceneDidActivate:];
-[_TtC15WiFiSettingsKit28PasswordPromptViewController joinTapped];
```
