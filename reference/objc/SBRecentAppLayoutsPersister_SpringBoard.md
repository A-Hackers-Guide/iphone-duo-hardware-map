# `SBRecentAppLayoutsPersister`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _ioQueue;
@"NSURL" _persistenceURL;
@"NSTimer" _persistTimer;
B _initializedNewStoreOnDisk;
@"<SBDisplayItemLayoutAttributesProviding>" _layoutAttributesProvider;
@"NSArray" _recents;
```

## Properties

```
@property (T@"NSArray",&,N,V_recents) recents;
@property (TB,R,N) initializedNewStoreOnDisk;
```

## Instance methods

```
-[SBRecentAppLayoutsPersister recents];
-[SBRecentAppLayoutsPersister setRecents:];
-[SBRecentAppLayoutsPersister _enqueueDiskWrite];
-[SBRecentAppLayoutsPersister _loadRecents];
-[SBRecentAppLayoutsPersister _persistTimerExpired:];
-[SBRecentAppLayoutsPersister _queue_writeCompressedProtobufRepresentationToDisk:];
-[SBRecentAppLayoutsPersister _scheduledPersistTimer];
-[SBRecentAppLayoutsPersister initWithPersistenceURL:layoutAttributesProvider:];
-[SBRecentAppLayoutsPersister initializedNewStoreOnDisk];
-[SBRecentAppLayoutsPersister syncToDiskSoonIfDirty];
-[SBRecentAppLayoutsPersister syncToDiskSynchronously];
```
