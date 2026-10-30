# `DSPrivacyPermissionsController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `DSPrivacyPermissionsDelegate`, `DSController`
- 10 instance variables, 15 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _isFiltered;
@"<DSNavigationDelegate>" _delegate;
@"DSAppSharing" _appSharing;
@"NSArray" _apps;
@"NSArray" _filteredApps;
@"NSMutableSet" _selectedApps;
Q _scope;
@"NSArray" _sensors;
@"NSMutableSet" _selectedSensors;
@"NSArray" _filteredSensors;
```

## Properties

```
@property (T@"DSAppSharing",&,N,V_appSharing) appSharing;
@property (T@"NSArray",&,N,V_apps) apps;
@property (T@"NSArray",&,N,V_filteredApps) filteredApps;
@property (TB,N,V_isFiltered) isFiltered;
@property (T@"NSMutableSet",&,N,V_selectedApps) selectedApps;
@property (TQ,N,V_scope) scope;
@property (T@"NSArray",&,N,V_sensors) sensors;
@property (T@"NSMutableSet",&,N,V_selectedSensors) selectedSensors;
@property (T@"NSArray",&,N,V_filteredSensors) filteredSensors;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (T@"DSTableView",&,D,N) tableView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSPrivacyPermissionsController tableView:numberOfRowsInSection:];
-[DSPrivacyPermissionsController tableView:accessoryButtonTappedForRowWithIndexPath:];
-[DSPrivacyPermissionsController tableView:cellForRowAtIndexPath:];
-[DSPrivacyPermissionsController setIsFiltered:];
-[DSPrivacyPermissionsController scope];
-[DSPrivacyPermissionsController init];
-[DSPrivacyPermissionsController viewDidLoad];
-[DSPrivacyPermissionsController _updateTitle];
-[DSPrivacyPermissionsController reloadData];
-[DSPrivacyPermissionsController viewWillAppear:];
-[DSPrivacyPermissionsController setDelegate:];
-[DSPrivacyPermissionsController tableView:didSelectRowAtIndexPath:];
-[DSPrivacyPermissionsController delegate];
-[DSPrivacyPermissionsController isFiltered];
-[DSPrivacyPermissionsController apps];
-[DSPrivacyPermissionsController setApps:];
-[DSPrivacyPermissionsController searchBar:selectedScopeButtonIndexDidChange:];
-[DSPrivacyPermissionsController setScope:];
-[DSPrivacyPermissionsController tableView:viewForHeaderInSection:];
-[DSPrivacyPermissionsController updateSearchResultsForSearchController:];
-[DSPrivacyPermissionsController tableView:didDeselectRowAtIndexPath:];
-[DSPrivacyPermissionsController _updateButton];
-[DSPrivacyPermissionsController sensors];
-[DSPrivacyPermissionsController setSensors:];
-[DSPrivacyPermissionsController filteredSensors];
-[DSPrivacyPermissionsController handleResetErrors:pushNextPane:];
-[DSPrivacyPermissionsController addUnsharedPermissions:andApps:];
-[DSPrivacyPermissionsController selectedSensors];
-[DSPrivacyPermissionsController _pushNextPane];
-[DSPrivacyPermissionsController appSharing];
-[DSPrivacyPermissionsController collectPermissionsByType];
-[DSPrivacyPermissionsController filterContentForSearchText:category:];
-[DSPrivacyPermissionsController filteredApps];
-[DSPrivacyPermissionsController resetAllPermissions];
-[DSPrivacyPermissionsController resetSelectedPermissions];
-[DSPrivacyPermissionsController returnFromDetailAndDeleteApp:];
-[DSPrivacyPermissionsController returnFromDetailAndResetPermissionForSelectedApps:permission:];
-[DSPrivacyPermissionsController returnFromDetailAndResetSelectedPermissions:forApp:];
-[DSPrivacyPermissionsController returnFromDetailAndStopAllSharingForPermission:];
-[DSPrivacyPermissionsController selectedApps];
-[DSPrivacyPermissionsController setAppSharing:];
-[DSPrivacyPermissionsController setFilteredApps:];
-[DSPrivacyPermissionsController setFilteredSensors:];
-[DSPrivacyPermissionsController setSelectedApps:];
-[DSPrivacyPermissionsController setSelectedSensors:];
```
