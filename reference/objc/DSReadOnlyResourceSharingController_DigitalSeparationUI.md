# `DSReadOnlyResourceSharingController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `DSReadOnlyResourceSharingDetailDelegate`, `DSController`
- 5 instance variables, 9 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"<DSNavigationDelegate>" _delegate;
@"DSSharingPermissions" _permissions;
Q _scope;
@"NSMutableSet" _selectedPeople;
@"NSMutableSet" _selectedTypes;
```

## Properties

```
@property (T@"DSSharingPermissions",&,N,V_permissions) permissions;
@property (TQ,N,V_scope) scope;
@property (T@"NSMutableSet",&,N,V_selectedPeople) selectedPeople;
@property (T@"NSMutableSet",&,N,V_selectedTypes) selectedTypes;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSReadOnlyResourceSharingController tableView:numberOfRowsInSection:];
-[DSReadOnlyResourceSharingController tableView:cellForRowAtIndexPath:];
-[DSReadOnlyResourceSharingController scope];
-[DSReadOnlyResourceSharingController setPermissions:];
-[DSReadOnlyResourceSharingController init];
-[DSReadOnlyResourceSharingController viewDidLoad];
-[DSReadOnlyResourceSharingController permissions];
-[DSReadOnlyResourceSharingController tableView:willDisplayCell:forRowAtIndexPath:];
-[DSReadOnlyResourceSharingController viewWillAppear:];
-[DSReadOnlyResourceSharingController setDelegate:];
-[DSReadOnlyResourceSharingController tableView:didSelectRowAtIndexPath:];
-[DSReadOnlyResourceSharingController delegate];
-[DSReadOnlyResourceSharingController searchBar:selectedScopeButtonIndexDidChange:];
-[DSReadOnlyResourceSharingController setScope:];
-[DSReadOnlyResourceSharingController updateSearchResultsForSearchController:];
-[DSReadOnlyResourceSharingController shouldShow];
-[DSReadOnlyResourceSharingController tableView:didDeselectRowAtIndexPath:];
-[DSReadOnlyResourceSharingController selectedTypes];
-[DSReadOnlyResourceSharingController setSelectedTypes:];
-[DSReadOnlyResourceSharingController _updateButton];
-[DSReadOnlyResourceSharingController _pushDetailPaneForSharingTypes:];
-[DSReadOnlyResourceSharingController learnMorePressedForSharingType:];
-[DSReadOnlyResourceSharingController _pushDetailPaneForSharingPeople:];
-[DSReadOnlyResourceSharingController _reviewAllSharing];
-[DSReadOnlyResourceSharingController filterContentForSearchText:category:];
-[DSReadOnlyResourceSharingController reloadTableViewData];
-[DSReadOnlyResourceSharingController reviewReadOnlySharingCompleted];
-[DSReadOnlyResourceSharingController reviewSelectedSharing];
-[DSReadOnlyResourceSharingController selectedPeople];
-[DSReadOnlyResourceSharingController setSelectedPeople:];
```
