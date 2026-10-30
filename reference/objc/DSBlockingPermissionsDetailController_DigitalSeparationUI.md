# `DSBlockingPermissionsDetailController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `DSController`
- 9 instance variables, 13 properties, 50 instance methods, 0 class methods

## Instance variables

```
@"<DSNavigationDelegate>" _delegate;
@"<DSBlockingPermissionsDetailDelegate>" _permissionsDelegate;
@"DSXPCSharingPerson" _person;
@"NSArray" _remainingSharingPeople;
@"DSXPCSharingPermissions" _permissions;
@"NSArray" _sortedSourceNames;
@"NSArray" _unblockedEmailAddresses;
@"NSMutableSet" _unsharedSources;
@"NSError" _cachedFetchError;
```

## Properties

```
@property (T@"DSXPCSharingPerson",&,N,V_person) person;
@property (T@"NSArray",&,N,V_remainingSharingPeople) remainingSharingPeople;
@property (T@"DSXPCSharingPermissions",&,N,V_permissions) permissions;
@property (T@"NSArray",&,N,V_sortedSourceNames) sortedSourceNames;
@property (T@"NSArray",&,N,V_unblockedEmailAddresses) unblockedEmailAddresses;
@property (T@"NSMutableSet",&,N,V_unsharedSources) unsharedSources;
@property (T@"NSError",&,N,V_cachedFetchError) cachedFetchError;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (T@"<DSBlockingPermissionsDetailDelegate>",W,N,V_permissionsDelegate) permissionsDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSBlockingPermissionsDetailController setPerson:];
-[DSBlockingPermissionsDetailController tableView:numberOfRowsInSection:];
-[DSBlockingPermissionsDetailController numberOfSectionsInTableView:];
-[DSBlockingPermissionsDetailController tableView:cellForRowAtIndexPath:];
-[DSBlockingPermissionsDetailController next];
-[DSBlockingPermissionsDetailController setPermissions:];
-[DSBlockingPermissionsDetailController viewDidLoad];
-[DSBlockingPermissionsDetailController permissions];
-[DSBlockingPermissionsDetailController tableView:willDisplayCell:forRowAtIndexPath:];
-[DSBlockingPermissionsDetailController viewWillAppear:];
-[DSBlockingPermissionsDetailController setDelegate:];
-[DSBlockingPermissionsDetailController viewDidAppear:];
-[DSBlockingPermissionsDetailController person];
-[DSBlockingPermissionsDetailController tableView:didSelectRowAtIndexPath:];
-[DSBlockingPermissionsDetailController delegate];
-[DSBlockingPermissionsDetailController viewDidDisappear:];
-[DSBlockingPermissionsDetailController tableView:didDeselectRowAtIndexPath:];
-[DSBlockingPermissionsDetailController tableView:willDeselectRowAtIndexPath:];
-[DSBlockingPermissionsDetailController _presentAlertForError:];
-[DSBlockingPermissionsDetailController cachedFetchError];
-[DSBlockingPermissionsDetailController setCachedFetchError:];
-[DSBlockingPermissionsDetailController sortedSourceNames];
-[DSBlockingPermissionsDetailController selectedSources];
-[DSBlockingPermissionsDetailController unsharedSources];
-[DSBlockingPermissionsDetailController cellForUnsavedEmailAtIndexPath:];
-[DSBlockingPermissionsDetailController numberOfSources];
-[DSBlockingPermissionsDetailController _setUpLinkButton];
-[DSBlockingPermissionsDetailController _stopFindMyPushNextPane];
-[DSBlockingPermissionsDetailController alertControllerWithTitle:message:actionButtonText:actionHandler:];
-[DSBlockingPermissionsDetailController alertMessageForSelectedEmails:selectedSources:];
-[DSBlockingPermissionsDetailController confirmationAlertControllerForSelectedEmails:selectedSources:stopSharingCompletion:];
-[DSBlockingPermissionsDetailController initWithPeople:permissions:];
-[DSBlockingPermissionsDetailController numberOfUnsavedEmails];
-[DSBlockingPermissionsDetailController permissionsDelegate];
-[DSBlockingPermissionsDetailController postExitAnalytics];
-[DSBlockingPermissionsDetailController presentFetchError:];
-[DSBlockingPermissionsDetailController reloadTableViewData];
-[DSBlockingPermissionsDetailController remainingSharingPeople];
-[DSBlockingPermissionsDetailController selectedEmails];
-[DSBlockingPermissionsDetailController setPermissionsDelegate:];
-[DSBlockingPermissionsDetailController setRemainingSharingPeople:];
-[DSBlockingPermissionsDetailController setSortedSourceNames:];
-[DSBlockingPermissionsDetailController setUnblockedEmailAddresses:];
-[DSBlockingPermissionsDetailController setUnsharedSources:];
-[DSBlockingPermissionsDetailController sharingCellForRowAtIndexPath:];
-[DSBlockingPermissionsDetailController sharingStoppedForSourceNames:error:];
-[DSBlockingPermissionsDetailController sourceNameForIndexPath:];
-[DSBlockingPermissionsDetailController unblockedEmailAddresses];
-[DSBlockingPermissionsDetailController unsavedEmailForIndexPath:];
-[DSBlockingPermissionsDetailController userPressedBoldButton];
```
