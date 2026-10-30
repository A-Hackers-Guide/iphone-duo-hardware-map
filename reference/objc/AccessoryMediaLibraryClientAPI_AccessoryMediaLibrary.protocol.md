# `AccessoryMediaLibraryClientAPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](../userland/System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 20 instance methods, 0 class methods

## Properties

```
@property (T@"<AccessoryMediaLibraryClientDelegate>",W,N) delegate;
@property (Ti,R) featureUserCount;
```

## Instance methods

```
-[AccessoryMediaLibraryClientAPI setDelegate:];
-[AccessoryMediaLibraryClientAPI delegate];
-[AccessoryMediaLibraryClientAPI accessoryDetached:];
-[AccessoryMediaLibraryClientAPI decrementUserCount];
-[AccessoryMediaLibraryClientAPI featureUserCount];
-[AccessoryMediaLibraryClientAPI incrementUserCount];
-[AccessoryMediaLibraryClientAPI playAllSongs:library:startItem:];
-[AccessoryMediaLibraryClientAPI stopMediaLibraryUpdate:library:];
-[AccessoryMediaLibraryClientAPI accessoryAttached:windowPerLibrary:];
-[AccessoryMediaLibraryClientAPI accessoryUpdate:windowPerLibrary:];
-[AccessoryMediaLibraryClientAPI checkPendingResetForLibrary:];
-[AccessoryMediaLibraryClientAPI confirmPlaylistContentUpdate:library:lastRevision:];
-[AccessoryMediaLibraryClientAPI confirmUpdate:library:lastRevision:updateCount:];
-[AccessoryMediaLibraryClientAPI playCollection:library:collection:type:startIndex:];
-[AccessoryMediaLibraryClientAPI playCollection:library:collection:type:startItem:];
-[AccessoryMediaLibraryClientAPI playCurrentSelection:library:];
-[AccessoryMediaLibraryClientAPI playItems:library:itemList:startIndex:];
-[AccessoryMediaLibraryClientAPI requestLibraryInfoUpdate:];
-[AccessoryMediaLibraryClientAPI startMediaLibraryUpdate:library:lastRevision:requestedInfo:];
-[AccessoryMediaLibraryClientAPI stopAllMediaLibraryUpdate:];
```
