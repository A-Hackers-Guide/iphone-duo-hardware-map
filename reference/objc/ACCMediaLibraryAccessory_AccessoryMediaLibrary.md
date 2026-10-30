# `ACCMediaLibraryAccessory`

- Image: [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](../userland/System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 44 instance methods, 0 class methods

## Instance variables

```
I _windowPerLibrary;
@"NSString" _accessoryUID;
@"ACCMediaLibraryProvider" _provider;
@"NSMutableDictionary" _libraries;
@"NSMutableDictionary" _pendingUpdates;
@"NSMutableDictionary" _waitingConfirm;
@"NSMutableDictionary" _pendingPlaylistContentUpdates;
@"NSMutableDictionary" _confirmedRevisionList;
@"NSObject<OS_dispatch_queue>" _listQueue;
```

## Properties

```
@property (T@"NSMutableDictionary",R,V_libraries) libraries;
@property (T@"NSMutableDictionary",&,V_pendingUpdates) pendingUpdates;
@property (T@"NSMutableDictionary",&,V_waitingConfirm) waitingConfirm;
@property (T@"NSMutableDictionary",&,V_pendingPlaylistContentUpdates) pendingPlaylistContentUpdates;
@property (T@"NSMutableDictionary",&,V_confirmedRevisionList) confirmedRevisionList;
@property (T@"NSObject<OS_dispatch_queue>",R,V_listQueue) listQueue;
@property (T@"NSString",R,V_accessoryUID) accessoryUID;
@property (T@"ACCMediaLibraryProvider",R,W,V_provider) provider;
@property (TI,V_windowPerLibrary) windowPerLibrary;
```

## Instance methods

```
-[ACCMediaLibraryAccessory dealloc];
-[ACCMediaLibraryAccessory provider];
-[ACCMediaLibraryAccessory pendingUpdates];
-[ACCMediaLibraryAccessory description];
-[ACCMediaLibraryAccessory libraries];
-[ACCMediaLibraryAccessory setPendingUpdates:];
-[ACCMediaLibraryAccessory accessoryUID];
-[ACCMediaLibraryAccessory clearAllUpdates];
-[ACCMediaLibraryAccessory addLibraryInfo:];
-[ACCMediaLibraryAccessory _addConfirmedRevisionForLibrary:revision:];
-[ACCMediaLibraryAccessory _addConfirmedRevisionForLibrary:revisionsToAdd:];
-[ACCMediaLibraryAccessory _addToWaitlistForLibrary:item:];
-[ACCMediaLibraryAccessory _addToWaitlistForLibrary:list:];
-[ACCMediaLibraryAccessory _confirmedRevisionListForLibrary:createIfNotExist:];
-[ACCMediaLibraryAccessory _confirmedRevisionListRemoveLibraryIfEmpty:];
-[ACCMediaLibraryAccessory _pendingAndWaitingConfirmUpdatesCountForLibrary:];
-[ACCMediaLibraryAccessory _pendingPlaylistContentUpdatesCountForLibrary:];
-[ACCMediaLibraryAccessory _pendingPlaylistContentUpdatesForLibrary:createIfNotExist:];
-[ACCMediaLibraryAccessory _pendingPlaylistContentUpdatesRemoveLibraryIfEmpty:];
-[ACCMediaLibraryAccessory _pendingUpdatesAndWaitingConfirmFullForLibrary:];
-[ACCMediaLibraryAccessory _pendingUpdatesForLibrary:createIfNotExist:];
-[ACCMediaLibraryAccessory _pendingUpdatesRemoveLibraryIfEmpty:];
-[ACCMediaLibraryAccessory _waitingUpdatesForLibrary:createIfNotExist:];
-[ACCMediaLibraryAccessory _waitingUpdatesRemoveLibraryIfEmpty:];
-[ACCMediaLibraryAccessory addPlaylistContentUpdate:library:];
-[ACCMediaLibraryAccessory addUpdate:library:];
-[ACCMediaLibraryAccessory clearAllUpdatesForLibrary:];
-[ACCMediaLibraryAccessory confirmPlaylistContentUpdates:revision:];
-[ACCMediaLibraryAccessory confirmUpdates:revision:count:];
-[ACCMediaLibraryAccessory confirmedRevisionList];
-[ACCMediaLibraryAccessory copyPendingNonContentUpdatesToSendForLibrary:];
-[ACCMediaLibraryAccessory copyPendingPlaylistContentUpdatesToSendForLibrary:];
-[ACCMediaLibraryAccessory initWithUID:windowPerLibrary:provider:];
-[ACCMediaLibraryAccessory listQueue];
-[ACCMediaLibraryAccessory pendingAndWaitingConfirmUpdatesCountForLibrary:];
-[ACCMediaLibraryAccessory pendingPlaylistContentUpdates];
-[ACCMediaLibraryAccessory pendingPlaylistContentUpdatesCountForLibrary:];
-[ACCMediaLibraryAccessory pendingUpdatesAndWaitingConfirmFullForLibrary:];
-[ACCMediaLibraryAccessory setConfirmedRevisionList:];
-[ACCMediaLibraryAccessory setPendingPlaylistContentUpdates:];
-[ACCMediaLibraryAccessory setWaitingConfirm:];
-[ACCMediaLibraryAccessory setWindowPerLibrary:];
-[ACCMediaLibraryAccessory waitingConfirm];
-[ACCMediaLibraryAccessory windowPerLibrary];
```
