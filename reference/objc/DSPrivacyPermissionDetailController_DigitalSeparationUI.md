# `DSPrivacyPermissionDetailController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- 4 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"DSSensor" _permission;
@"NSMutableArray" _selectedApps;
@"<DSPrivacyPermissionsDelegate>" _delegate;
@"NSArray" _apps;
```

## Properties

```
@property (T@"NSArray",&,N,V_apps) apps;
@property (T@"DSSensor",&,N,V_permission) permission;
@property (T@"NSMutableArray",&,N,V_selectedApps) selectedApps;
@property (T@"<DSPrivacyPermissionsDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[DSPrivacyPermissionDetailController tableView:numberOfRowsInSection:];
-[DSPrivacyPermissionDetailController tableView:cellForRowAtIndexPath:];
-[DSPrivacyPermissionDetailController viewDidLoad];
-[DSPrivacyPermissionDetailController setPermission:];
-[DSPrivacyPermissionDetailController setDelegate:];
-[DSPrivacyPermissionDetailController tableView:didSelectRowAtIndexPath:];
-[DSPrivacyPermissionDetailController delegate];
-[DSPrivacyPermissionDetailController permission];
-[DSPrivacyPermissionDetailController apps];
-[DSPrivacyPermissionDetailController setApps:];
-[DSPrivacyPermissionDetailController tableView:didDeselectRowAtIndexPath:];
-[DSPrivacyPermissionDetailController _updateButton];
-[DSPrivacyPermissionDetailController back];
-[DSPrivacyPermissionDetailController initWithTitle:detailText:symbolName:adoptTableViewScrollView:shouldShowSearchBar:];
-[DSPrivacyPermissionDetailController initWithTitle:detailText:symbolName:permission:apps:];
-[DSPrivacyPermissionDetailController returnFromDetailAndResetPermissionForSelectedApps];
-[DSPrivacyPermissionDetailController returnFromDetailAndStopAllSharingForPermission];
-[DSPrivacyPermissionDetailController selectedApps];
-[DSPrivacyPermissionDetailController setSelectedApps:];
-[DSPrivacyPermissionDetailController stopAllPressed];
```
