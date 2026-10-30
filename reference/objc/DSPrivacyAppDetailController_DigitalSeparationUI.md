# `DSPrivacyAppDetailController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- 4 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"DSApp" _app;
@"NSMutableArray" _selectedPermissions;
@"<DSPrivacyPermissionsDelegate>" _delegate;
@"NSArray" _sortedPermissions;
```

## Properties

```
@property (T@"NSArray",&,N,V_sortedPermissions) sortedPermissions;
@property (T@"DSApp",&,N,V_app) app;
@property (T@"NSMutableArray",&,N,V_selectedPermissions) selectedPermissions;
@property (T@"<DSPrivacyPermissionsDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[DSPrivacyAppDetailController tableView:numberOfRowsInSection:];
-[DSPrivacyAppDetailController tableView:cellForRowAtIndexPath:];
-[DSPrivacyAppDetailController viewDidLoad];
-[DSPrivacyAppDetailController setDelegate:];
-[DSPrivacyAppDetailController tableView:didSelectRowAtIndexPath:];
-[DSPrivacyAppDetailController delegate];
-[DSPrivacyAppDetailController app];
-[DSPrivacyAppDetailController tableView:didDeselectRowAtIndexPath:];
-[DSPrivacyAppDetailController setApp:];
-[DSPrivacyAppDetailController _updateButton];
-[DSPrivacyAppDetailController back];
-[DSPrivacyAppDetailController initWithTitle:detailText:symbolName:adoptTableViewScrollView:shouldShowSearchBar:];
-[DSPrivacyAppDetailController initWithTitle:detailText:symbolName:app:];
-[DSPrivacyAppDetailController returnFromDetailAndDeleteApp];
-[DSPrivacyAppDetailController returnFromDetailAndRevokeSelectedPermissions];
-[DSPrivacyAppDetailController selectedPermissions];
-[DSPrivacyAppDetailController setSelectedPermissions:];
-[DSPrivacyAppDetailController setSortedPermissions:];
-[DSPrivacyAppDetailController sortedPermissions];
```
