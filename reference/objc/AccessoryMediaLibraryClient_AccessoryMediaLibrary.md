# `AccessoryMediaLibraryClient`

- Image: [`/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`](../userland/System__Library__PrivateFrameworks__AccessoryMediaLibrary.framework__AccessoryMediaLibrary.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCMediaLibraryFeatureClientProtocol`, `AccessoryMediaLibraryClientAPI`
- 10 instance variables, 16 properties, 51 instance methods, 0 class methods

## Instance variables

```
B _isServiceReady;
i _featureUserCount;
@"<AccessoryMediaLibraryClientDelegate>" _delegate;
@"NSXPCConnection" _serviceConnection;
@"<ACCMediaLibraryFeatureServiceProtocol>" _remoteObject;
@"NSXPCListenerEndpoint" _mockListenerEndpoint;
@"NSObject<OS_dispatch_queue>" _clientQueue;
@"NSMutableSet" _mutableAttachedAccessoryUIDs;
@"NSArray" _lastAvailableLibraries;
@"NSMutableSet" _pendingResetLibraryUIDs;
```

## Properties

```
@property (T@"NSXPCConnection",&,V_serviceConnection) serviceConnection;
@property (T@"<ACCMediaLibraryFeatureServiceProtocol>",&,V_remoteObject) remoteObject;
@property (T@"NSXPCListenerEndpoint",&,V_mockListenerEndpoint) mockListenerEndpoint;
@property (Ti,V_featureUserCount) featureUserCount;
@property (TB,V_isServiceReady) isServiceReady;
@property (T@"NSObject<OS_dispatch_queue>",&,V_clientQueue) clientQueue;
@property (T@"NSMutableSet",&,V_mutableAttachedAccessoryUIDs) mutableAttachedAccessoryUIDs;
@property (T@"NSArray",&,V_lastAvailableLibraries) lastAvailableLibraries;
@property (T@"NSMutableSet",&,V_pendingResetLibraryUIDs) pendingResetLibraryUIDs;
@property (T@"<AccessoryMediaLibraryClientDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) isConnected;
@property (T@"NSSet",R) attachedAccessoryUIDs;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AccessoryMediaLibraryClient setClientQueue:];
-[AccessoryMediaLibraryClient clientQueue];
-[AccessoryMediaLibraryClient setServiceConnection:];
-[AccessoryMediaLibraryClient isConnected];
-[AccessoryMediaLibraryClient serviceConnection];
-[AccessoryMediaLibraryClient init];
-[AccessoryMediaLibraryClient setRemoteObject:];
-[AccessoryMediaLibraryClient dealloc];
-[AccessoryMediaLibraryClient remoteObject];
-[AccessoryMediaLibraryClient disconnect];
-[AccessoryMediaLibraryClient setDelegate:];
-[AccessoryMediaLibraryClient delegate];
-[AccessoryMediaLibraryClient connectToService];
-[AccessoryMediaLibraryClient accessoryDetached:];
-[AccessoryMediaLibraryClient _connectToServiceOnQueue];
-[AccessoryMediaLibraryClient _disconnectOnQueue];
-[AccessoryMediaLibraryClient decrementUserCount];
-[AccessoryMediaLibraryClient featureUserCount];
-[AccessoryMediaLibraryClient incrementUserCount];
-[AccessoryMediaLibraryClient mockListenerEndpoint];
-[AccessoryMediaLibraryClient setFeatureUserCount:];
-[AccessoryMediaLibraryClient setMockListenerEndpoint:];
-[AccessoryMediaLibraryClient playAllSongs:library:startItem:];
-[AccessoryMediaLibraryClient stopMediaLibraryUpdate:library:];
-[AccessoryMediaLibraryClient _performWithRemoteObject:];
-[AccessoryMediaLibraryClient accessoryAttached:windowPerLibrary:];
-[AccessoryMediaLibraryClient accessoryUpdate:windowPerLibrary:];
-[AccessoryMediaLibraryClient attachedAccessoryUIDs];
-[AccessoryMediaLibraryClient availableLibrariesDidChange:];
-[AccessoryMediaLibraryClient checkPendingResetForLibrary:];
-[AccessoryMediaLibraryClient confirmPlaylistContentUpdate:library:lastRevision:];
-[AccessoryMediaLibraryClient confirmUpdate:library:lastRevision:updateCount:];
-[AccessoryMediaLibraryClient isServiceReady];
-[AccessoryMediaLibraryClient lastAvailableLibraries];
-[AccessoryMediaLibraryClient libraryResetUpdate:accessory:];
-[AccessoryMediaLibraryClient libraryStateDidChange:stateType:enabled:];
-[AccessoryMediaLibraryClient libraryUpdate:revision:content:accessory:];
-[AccessoryMediaLibraryClient libraryUpdate:updates:accessory:];
-[AccessoryMediaLibraryClient mutableAttachedAccessoryUIDs];
-[AccessoryMediaLibraryClient pendingResetLibraryUIDs];
-[AccessoryMediaLibraryClient playCollection:library:collection:type:startIndex:];
-[AccessoryMediaLibraryClient playCollection:library:collection:type:startItem:];
-[AccessoryMediaLibraryClient playCurrentSelection:library:];
-[AccessoryMediaLibraryClient playItems:library:itemList:startIndex:];
-[AccessoryMediaLibraryClient requestLibraryInfoUpdate:];
-[AccessoryMediaLibraryClient setIsServiceReady:];
-[AccessoryMediaLibraryClient setLastAvailableLibraries:];
-[AccessoryMediaLibraryClient setMutableAttachedAccessoryUIDs:];
-[AccessoryMediaLibraryClient setPendingResetLibraryUIDs:];
-[AccessoryMediaLibraryClient startMediaLibraryUpdate:library:lastRevision:requestedInfo:];
-[AccessoryMediaLibraryClient stopAllMediaLibraryUpdate:];
```
