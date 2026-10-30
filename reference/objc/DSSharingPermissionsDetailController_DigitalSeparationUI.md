# `DSSharingPermissionsDetailController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- 9 instance variables, 9 properties, 36 instance methods, 3 class methods

## Instance variables

```
B _hasDisplayNames;
@"DSSharingPerson" _sharingPerson;
@"NSArray" _remainingPeople;
@"DSSharingType" _sharingType;
@"NSArray" _remainingSharingTypes;
@"NSArray" _sortedSourceNames;
@"NSArray" _sortedPeople;
@"UIViewController" _startingViewController;
@"<DSSharingPermissionsDetailDelegate>" _delegate;
```

## Properties

```
@property (T@"DSSharingPerson",&,N,V_sharingPerson) sharingPerson;
@property (T@"NSArray",&,N,V_remainingPeople) remainingPeople;
@property (T@"DSSharingType",&,N,V_sharingType) sharingType;
@property (T@"NSArray",&,N,V_remainingSharingTypes) remainingSharingTypes;
@property (T@"NSArray",&,N,V_sortedSourceNames) sortedSourceNames;
@property (T@"NSArray",&,N,V_sortedPeople) sortedPeople;
@property (T@"UIViewController",&,N,V_startingViewController) startingViewController;
@property (T@"<DSSharingPermissionsDetailDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_hasDisplayNames) hasDisplayNames;
```

## Class methods

```
+[DSSharingPermissionsDetailController initialize];
+[DSSharingPermissionsDetailController detailControllerWithPeople:startingViewController:delegate:];
+[DSSharingPermissionsDetailController detailControllerWithSharingTypes:startingViewController:delegate:];
```

## Instance methods

```
-[DSSharingPermissionsDetailController tableView:numberOfRowsInSection:];
-[DSSharingPermissionsDetailController tableView:cellForRowAtIndexPath:];
-[DSSharingPermissionsDetailController next];
-[DSSharingPermissionsDetailController setSortedPeople:];
-[DSSharingPermissionsDetailController viewDidLoad];
-[DSSharingPermissionsDetailController tableView:willDisplayCell:forRowAtIndexPath:];
-[DSSharingPermissionsDetailController sortedPeople];
-[DSSharingPermissionsDetailController setDelegate:];
-[DSSharingPermissionsDetailController tableView:didSelectRowAtIndexPath:];
-[DSSharingPermissionsDetailController delegate];
-[DSSharingPermissionsDetailController tableView:didDeselectRowAtIndexPath:];
-[DSSharingPermissionsDetailController _updateButton];
-[DSSharingPermissionsDetailController setStartingViewController:];
-[DSSharingPermissionsDetailController startingViewController];
-[DSSharingPermissionsDetailController setSharingType:];
-[DSSharingPermissionsDetailController sharingType];
-[DSSharingPermissionsDetailController sortedSourceNames];
-[DSSharingPermissionsDetailController remainingPeople];
-[DSSharingPermissionsDetailController hasDisplayNames];
-[DSSharingPermissionsDetailController alertTextForSources:];
-[DSSharingPermissionsDetailController checkDisplayNames];
-[DSSharingPermissionsDetailController personForIndexPath:];
-[DSSharingPermissionsDetailController reloadTableViewData];
-[DSSharingPermissionsDetailController remainingSharingTypes];
-[DSSharingPermissionsDetailController setHasDisplayNames:];
-[DSSharingPermissionsDetailController setRemainingPeople:];
-[DSSharingPermissionsDetailController setRemainingSharingTypes:];
-[DSSharingPermissionsDetailController setSharingPerson:];
-[DSSharingPermissionsDetailController setSortedSourceNames:];
-[DSSharingPermissionsDetailController sharingPerson];
-[DSSharingPermissionsDetailController sharingStoppedForPerson:sourceNames:error:];
-[DSSharingPermissionsDetailController sharingStoppedForType:people:error:];
-[DSSharingPermissionsDetailController sourceNameForIndexPath:];
-[DSSharingPermissionsDetailController stopAllSharing];
-[DSSharingPermissionsDetailController stopSelectedSharing];
-[DSSharingPermissionsDetailController stopSharingSources:people:alertLabel:alertDetail:completion:];
```
