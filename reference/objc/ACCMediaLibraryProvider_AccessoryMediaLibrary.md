# `ACCMediaLibraryProvider`

- Image: [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](../userland/System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 51 instance methods, 0 class methods

## Instance variables

```
i _lastUpdateType;
@"<ACCMediaLibraryProviderDelegateProtocol>" _delegate;
@"NSXPCConnection" _serverConnection;
@"NSString" _providerUID;
@"NSObject<OS_dispatch_queue>" _delegateQ;
@"<ACCMediaLibraryXPCServerProtocol>" _remoteObject;
@"NSMutableDictionary" _accessories;
@"NSMutableDictionary" _libraries;
@"NSObject<OS_dispatch_queue>" _processingQueue;
@"NSXPCListenerEndpoint" _listenerEndpoint;
```

## Properties

```
@property (T@"<ACCMediaLibraryProviderDelegateProtocol>",W,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",&,V_delegateQ) delegateQ;
@property (T@"NSXPCConnection",&,V_serverConnection) serverConnection;
@property (T@"<ACCMediaLibraryXPCServerProtocol>",&,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,V_accessories) accessories;
@property (T@"NSMutableDictionary",&,V_libraries) libraries;
@property (Ti,V_lastUpdateType) lastUpdateType;
@property (T@"NSObject<OS_dispatch_queue>",&,V_processingQueue) processingQueue;
@property (T@"NSXPCListenerEndpoint",&,V_listenerEndpoint) listenerEndpoint;
@property (T@"NSString",&,V_providerUID) providerUID;
```

## Instance methods

```
-[ACCMediaLibraryProvider processingQueue];
-[ACCMediaLibraryProvider setProcessingQueue:];
-[ACCMediaLibraryProvider connectToServer];
-[ACCMediaLibraryProvider listenerEndpoint];
-[ACCMediaLibraryProvider setListenerEndpoint:];
-[ACCMediaLibraryProvider setRemoteObject:];
-[ACCMediaLibraryProvider serverConnection];
-[ACCMediaLibraryProvider dealloc];
-[ACCMediaLibraryProvider accessories];
-[ACCMediaLibraryProvider providerUID];
-[ACCMediaLibraryProvider remoteObject];
-[ACCMediaLibraryProvider setDelegate:];
-[ACCMediaLibraryProvider setLibraries:];
-[ACCMediaLibraryProvider setAccessories:];
-[ACCMediaLibraryProvider delegate];
-[ACCMediaLibraryProvider description];
-[ACCMediaLibraryProvider libraries];
-[ACCMediaLibraryProvider setServerConnection:];
-[ACCMediaLibraryProvider setProviderUID:];
-[ACCMediaLibraryProvider playAllSongs:library:startItem:];
-[ACCMediaLibraryProvider stopMediaLibraryUpdate:library:];
-[ACCMediaLibraryProvider _checkPlaylistContentToSend:accessory:];
-[ACCMediaLibraryProvider _notifyRemoteOfAvailableLibraries];
-[ACCMediaLibraryProvider accessoryMediaLibraryAllDetached];
-[ACCMediaLibraryProvider accessoryMediaLibraryAttached:windowPerLibrary:];
-[ACCMediaLibraryProvider accessoryMediaLibraryDetached:];
-[ACCMediaLibraryProvider accessoryMediaLibraryUpdate:windowPerLibrary:];
-[ACCMediaLibraryProvider confirmPlaylistContentUpdate:library:lastRevision:];
-[ACCMediaLibraryProvider confirmUpdate:library:lastRevision:updateCount:];
-[ACCMediaLibraryProvider delegateQ];
-[ACCMediaLibraryProvider flushUpdates:accessory:];
-[ACCMediaLibraryProvider initWithDelegate:queue:listenerEndpoint:];
-[ACCMediaLibraryProvider lastUpdateType];
-[ACCMediaLibraryProvider notify:stateChange:enabled:];
-[ACCMediaLibraryProvider notifyAvailableLibraries:];
-[ACCMediaLibraryProvider playCollection:library:collection:type:startIndex:];
-[ACCMediaLibraryProvider playCollection:library:collection:type:startItem:];
-[ACCMediaLibraryProvider playCurrentSelection:library:];
-[ACCMediaLibraryProvider playItems:library:itemList:startIndex:];
-[ACCMediaLibraryProvider resetUpdate:accessory:];
-[ACCMediaLibraryProvider setDelegateQ:];
-[ACCMediaLibraryProvider setLastUpdateType:];
-[ACCMediaLibraryProvider startMediaLibraryUpdate:library:lastRevision:mediaItemProperties:playlistProperties:playlistContentStyle:playlistContentProperties:reqOptions:];
-[ACCMediaLibraryProvider stopAllMediaLibraryUpdate:];
-[ACCMediaLibraryProvider update:revision:content:accessory:];
-[ACCMediaLibraryProvider update:revision:deleteItem:progress:accessory:];
-[ACCMediaLibraryProvider update:revision:deletePlaylist:progress:accessory:];
-[ACCMediaLibraryProvider update:revision:item:progress:accessory:];
-[ACCMediaLibraryProvider update:revision:persistentID:type:updateInfo:progress:accessory:];
-[ACCMediaLibraryProvider update:revision:playlist:progress:accessory:];
-[ACCMediaLibraryProvider update:revision:progress:accessory:];
```
