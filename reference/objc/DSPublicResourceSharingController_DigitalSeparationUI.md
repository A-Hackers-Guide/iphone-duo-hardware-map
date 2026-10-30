# `DSPublicResourceSharingController`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`](../userland/System__Library__PrivateFrameworks__DigitalSeparationUI.framework__DigitalSeparationUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `DSTableWelcomeController`
- Protocols: `DSController`
- 4 instance variables, 8 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"<DSNavigationDelegate>" _delegate;
@"DSSharingPermissions" _permissions;
@"NSMutableSet" _selectedTypes;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"DSSharingPermissions",&,N,V_permissions) permissions;
@property (T@"NSMutableSet",&,N,V_selectedTypes) selectedTypes;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (T@"<DSNavigationDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DSPublicResourceSharingController initialize];
```

## Instance methods

```
-[DSPublicResourceSharingController setWorkQueue:];
-[DSPublicResourceSharingController tableView:numberOfRowsInSection:];
-[DSPublicResourceSharingController tableView:cellForRowAtIndexPath:];
-[DSPublicResourceSharingController setPermissions:];
-[DSPublicResourceSharingController init];
-[DSPublicResourceSharingController workQueue];
-[DSPublicResourceSharingController permissions];
-[DSPublicResourceSharingController tableView:willDisplayCell:forRowAtIndexPath:];
-[DSPublicResourceSharingController _updateTitle];
-[DSPublicResourceSharingController viewWillAppear:];
-[DSPublicResourceSharingController setDelegate:];
-[DSPublicResourceSharingController tableView:didSelectRowAtIndexPath:];
-[DSPublicResourceSharingController delegate];
-[DSPublicResourceSharingController shouldShow];
-[DSPublicResourceSharingController tableView:didDeselectRowAtIndexPath:];
-[DSPublicResourceSharingController selectedTypes];
-[DSPublicResourceSharingController setSelectedTypes:];
-[DSPublicResourceSharingController _updateButton];
-[DSPublicResourceSharingController _pushNextPane];
-[DSPublicResourceSharingController publicSharingTypeForIndexPath:];
-[DSPublicResourceSharingController reloadTableViewData];
-[DSPublicResourceSharingController stopAllSharing];
-[DSPublicResourceSharingController stopSelectedSharing];
-[DSPublicResourceSharingController stopSharingFailedWithError:];
-[DSPublicResourceSharingController stopSharingTypes:alertLabel:alertDetail:];
```
