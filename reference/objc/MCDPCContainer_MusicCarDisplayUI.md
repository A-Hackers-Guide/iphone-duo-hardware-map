# `MCDPCContainer`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 13 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSIndexPath" _indexPath;
@"MCDPCItem" _rootItem;
@"MCDPCModel" _model;
B _showPlaybackProgress;
{?="didInvalidateRootItem"b1"didInvalidateIndicies"b1"willChangeCount"b1"didChangeCount"b1} __supportedDelegateCalls;
q _cachedCount;
@"<MCDPCContainerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _serialAccessContainerQueue;
@"NSMutableDictionary" _cachedIndiciesByIdentifier;
@"NSMutableDictionary" _cachedItemsByIndicies;
```

## Properties

```
@property (Tq,N,V_cachedCount) cachedCount;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_serialAccessContainerQueue) serialAccessContainerQueue;
@property (T@"NSMutableDictionary",&,N,V_cachedIndiciesByIdentifier) cachedIndiciesByIdentifier;
@property (T@"NSMutableDictionary",&,N,V_cachedItemsByIndicies) cachedItemsByIndicies;
@property (T@"MCDPCItem",R,W,N,V_rootItem) rootItem;
@property (T@"NSIndexPath",R,N,V_indexPath) indexPath;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSString",R,N) appTitle;
@property (T@"NSString",R,N) title;
@property (T@"MCDPCModel",R,W,N,V_model) model;
@property (TB,R,N,V_showPlaybackProgress) showPlaybackProgress;
@property (Tq,R,N) showCurrentlyPlayingIndex;
@property (T@"<MCDPCContainerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[MCDPCContainer model];
-[MCDPCContainer indexPath];
-[MCDPCContainer setCount:];
-[MCDPCContainer identifier];
-[MCDPCContainer dealloc];
-[MCDPCContainer invalidate];
-[MCDPCContainer setDelegate:];
-[MCDPCContainer title];
-[MCDPCContainer cachedCount];
-[MCDPCContainer refreshWithCompletion:];
-[MCDPCContainer delegate];
-[MCDPCContainer description];
-[MCDPCContainer setCachedCount:];
-[MCDPCContainer rootItem];
-[MCDPCContainer appTitle];
-[MCDPCContainer beginLoadingItemWithCompletion:];
-[MCDPCContainer _contentItemsUpdated:];
-[MCDPCContainer _initWithModel:rootItem:indexPath:];
-[MCDPCContainer _nowPlayingIdentifiersDidChange:];
-[MCDPCContainer beginLoadingItem:completion:];
-[MCDPCContainer cachedIndexByIdentifier:];
-[MCDPCContainer cachedIndiciesByIdentifier];
-[MCDPCContainer cachedItemForIdentifier:];
-[MCDPCContainer cachedItemForIndex:];
-[MCDPCContainer cachedItemsByIndicies];
-[MCDPCContainer containerAtIndex:];
-[MCDPCContainer containerForItem:];
-[MCDPCContainer fetchContentWithCompletion:];
-[MCDPCContainer getChildrenInRange:completion:];
-[MCDPCContainer getCountOfChildrenWithCompletion:];
-[MCDPCContainer getNowPlayingIdentifiersWithCompletion:];
-[MCDPCContainer getPlaybackProgressSupportForChildrenWithCompletion:];
-[MCDPCContainer isValidForRefreshedParent:];
-[MCDPCContainer serialAccessContainerQueue];
-[MCDPCContainer setCachedIndiciesByIdentifier:];
-[MCDPCContainer setCachedItemsByIndicies:];
-[MCDPCContainer setSerialAccessContainerQueue:];
-[MCDPCContainer setShowPlaybackProgress:];
-[MCDPCContainer showCurrentlyPlayingIndex];
-[MCDPCContainer showPlaybackProgress];
-[MCDPCContainer updateRootItemWithCompletion:];
```
