# `DSSharingPermissionsController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `DSSharingPermissionsDetailDelegate`, `DSController`
- 10 instance variables, 14 properties, 58 instance methods, 1 class methods

## Instance variables

```
Ai _fetchState;
@"<DSNavigationDelegate>" _delegate;
@"DSSourceRepository" _repo;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"DSSharingPermissions" _permissions;
@"NSMutableSet" _selectedPeople;
@"NSMutableSet" _selectedTypes;
Q _fetchCompletedTime;
@"NSError" _cachedFetchError;
@"NSMutableDictionary" _personIconCache;
```

## Properties

```
@property (T@"DSSourceRepository",&,N,V_repo) repo;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"DSSharingPermissions",&,N,V_permissions) permissions;
@property (T@"NSMutableSet",&,N,V_selectedPeople) selectedPeople;
@property (T@"NSMutableSet",&,N,V_selectedTypes) selectedTypes;
@property (TQ,V_fetchCompletedTime) fetchCompletedTime;
@property (T@"NSError",&,N,V_cachedFetchError) cachedFetchError;
@property (T@"NSMutableDictionary",&,N,V_personIconCache) personIconCache;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (T@"DSTableView",&,D,N) tableView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSSharingPermissionsController initialize];
```

## Instance methods

```
-[DSSharingPermissionsController setWorkQueue:];
-[DSSharingPermissionsController tableView:numberOfRowsInSection:];
-[DSSharingPermissionsController tableView:cellForRowAtIndexPath:];
-[DSSharingPermissionsController didEnterBackground];
-[DSSharingPermissionsController setPermissions:];
-[DSSharingPermissionsController init];
-[DSSharingPermissionsController workQueue];
-[DSSharingPermissionsController viewDidLoad];
-[DSSharingPermissionsController permissions];
-[DSSharingPermissionsController tableView:willDisplayCell:forRowAtIndexPath:];
-[DSSharingPermissionsController _updateTitle];
-[DSSharingPermissionsController viewWillAppear:];
-[DSSharingPermissionsController setDelegate:];
-[DSSharingPermissionsController viewDidAppear:];
-[DSSharingPermissionsController tableView:didSelectRowAtIndexPath:];
-[DSSharingPermissionsController delegate];
-[DSSharingPermissionsController unregisterForNotifications];
-[DSSharingPermissionsController viewDidDisappear:];
-[DSSharingPermissionsController searchBar:selectedScopeButtonIndexDidChange:];
-[DSSharingPermissionsController registerForNotifications];
-[DSSharingPermissionsController tableView:viewForHeaderInSection:];
-[DSSharingPermissionsController updateSearchResultsForSearchController:];
-[DSSharingPermissionsController tableView:didDeselectRowAtIndexPath:];
-[DSSharingPermissionsController selectedTypes];
-[DSSharingPermissionsController setSelectedTypes:];
-[DSSharingPermissionsController _updateButton];
-[DSSharingPermissionsController cachedFetchError];
-[DSSharingPermissionsController fetchCompletedTime];
-[DSSharingPermissionsController repo];
-[DSSharingPermissionsController setCachedFetchError:];
-[DSSharingPermissionsController setFetchCompletedTime:];
-[DSSharingPermissionsController setRepo:];
-[DSSharingPermissionsController isFindMyASource];
-[DSSharingPermissionsController personIconCache];
-[DSSharingPermissionsController _fetchCompletedWithError:];
-[DSSharingPermissionsController _pushNextPane];
-[DSSharingPermissionsController addUnsharedPerson:];
-[DSSharingPermissionsController addUnsharedSource:resources:];
-[DSSharingPermissionsController fetchSharingPermissions];
-[DSSharingPermissionsController filterContentForSearchText:category:];
-[DSSharingPermissionsController personForIndexPath:];
-[DSSharingPermissionsController postAnalytics];
-[DSSharingPermissionsController presentFetchErrorMessage:];
-[DSSharingPermissionsController reloadTableViewData];
-[DSSharingPermissionsController requestNewFetchImmediately:];
-[DSSharingPermissionsController reviewSelectedSharing];
-[DSSharingPermissionsController reviewSelectedSharingFlowCompleted];
-[DSSharingPermissionsController selectedPeople];
-[DSSharingPermissionsController setFetchNeeded];
-[DSSharingPermissionsController setPersonIconCache:];
-[DSSharingPermissionsController setSelectedPeople:];
-[DSSharingPermissionsController setUrgentFetchNeeded];
-[DSSharingPermissionsController sharingStoppedForPerson:sourceNames:];
-[DSSharingPermissionsController sharingStoppedForType:people:];
-[DSSharingPermissionsController sharingTypeForIndexPath:];
-[DSSharingPermissionsController stopAllSharing];
-[DSSharingPermissionsController stopSharingFailedWithError:];
-[DSSharingPermissionsController tableIconForPerson:];
```
