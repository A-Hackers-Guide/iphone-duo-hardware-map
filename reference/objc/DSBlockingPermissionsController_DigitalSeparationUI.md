# `DSBlockingPermissionsController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `DSBlockingPermissionsDetailDelegate`, `DSController`
- 7 instance variables, 12 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _hasPreselected;
@"<DSNavigationDelegate>" _delegate;
@"DSXPCSharingPermissions" _permissions;
@"NSMutableOrderedSet" _blockedPeople;
@"NSMutableDictionary" _personIconCache;
@"NSError" _permissionsFetchError;
@"NSMutableArray" _unsharedSources;
```

## Properties

```
@property (T@"DSXPCSharingPermissions",&,N,V_permissions) permissions;
@property (T@"NSMutableOrderedSet",&,N,V_blockedPeople) blockedPeople;
@property (T@"NSMutableDictionary",&,N,V_personIconCache) personIconCache;
@property (T@"NSError",&,N,V_permissionsFetchError) permissionsFetchError;
@property (T@"NSMutableArray",&,N,V_unsharedSources) unsharedSources;
@property (TB,N,V_hasPreselected) hasPreselected;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (T@"DSTableView",&,D,N) tableView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSBlockingPermissionsController tableView:numberOfRowsInSection:];
-[DSBlockingPermissionsController tableView:cellForRowAtIndexPath:];
-[DSBlockingPermissionsController next];
-[DSBlockingPermissionsController setPermissions:];
-[DSBlockingPermissionsController permissions];
-[DSBlockingPermissionsController viewWillAppear:];
-[DSBlockingPermissionsController _selectAll];
-[DSBlockingPermissionsController setDelegate:];
-[DSBlockingPermissionsController viewDidAppear:];
-[DSBlockingPermissionsController tableView:didSelectRowAtIndexPath:];
-[DSBlockingPermissionsController delegate];
-[DSBlockingPermissionsController viewDidDisappear:];
-[DSBlockingPermissionsController tableView:didDeselectRowAtIndexPath:];
-[DSBlockingPermissionsController _updateButton];
-[DSBlockingPermissionsController isFindMyASource];
-[DSBlockingPermissionsController unsharedSources];
-[DSBlockingPermissionsController personIconCache];
-[DSBlockingPermissionsController _sharingStoppedForPerson:sourceNames:];
-[DSBlockingPermissionsController _sortSharingPeople];
-[DSBlockingPermissionsController blockedPeople];
-[DSBlockingPermissionsController blockedPersonForIndex:];
-[DSBlockingPermissionsController hasPreselected];
-[DSBlockingPermissionsController initWithPeople:permissions:];
-[DSBlockingPermissionsController permissionsFetchError];
-[DSBlockingPermissionsController postAnalytics];
-[DSBlockingPermissionsController presentFetchErrorMessage:];
-[DSBlockingPermissionsController reloadTableViewData];
-[DSBlockingPermissionsController reviewSelectedSharing];
-[DSBlockingPermissionsController reviewSelectedSharingFlowCompleted];
-[DSBlockingPermissionsController selectAndStopAllSharing];
-[DSBlockingPermissionsController setBlockedPeople:];
-[DSBlockingPermissionsController setHasPreselected:];
-[DSBlockingPermissionsController setPermissionsFetchError:];
-[DSBlockingPermissionsController setPersonIconCache:];
-[DSBlockingPermissionsController setUnsharedSources:];
-[DSBlockingPermissionsController sharingStoppedForPerson:sourceNames:];
-[DSBlockingPermissionsController tableIconForPerson:];
```
