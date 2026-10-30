# `AccessoryNowPlayingClient`

- Image: [`/System/Library/PrivateFrameworks/AccessoryNowPlaying.framework/AccessoryNowPlaying`](../userland/System__Library__PrivateFrameworks__AccessoryNowPlaying.framework__AccessoryNowPlaying.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCNowPlayingFeatureClientProtocol`
- 8 instance variables, 13 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _needsSubscriberListResync;
i _featureUserCount;
@"<AccessoryNowPlayingClientDelegate>" _delegate;
@"NSCountedSet" _subscribers;
@"NSXPCConnection" _serviceConnection;
@"<ACCNowPlayingFeatureServiceProtocol>" _remoteObject;
@"NSXPCListenerEndpoint" _mockListenerEndpoint;
@"NSObject<OS_dispatch_queue>" _clientQueue;
```

## Properties

```
@property (T@"NSXPCConnection",&,V_serviceConnection) serviceConnection;
@property (T@"<ACCNowPlayingFeatureServiceProtocol>",&,V_remoteObject) remoteObject;
@property (T@"NSXPCListenerEndpoint",&,V_mockListenerEndpoint) mockListenerEndpoint;
@property (Ti,V_featureUserCount) featureUserCount;
@property (T@"NSCountedSet",&,V_subscribers) subscribers;
@property (T@"NSObject<OS_dispatch_queue>",&,V_clientQueue) clientQueue;
@property (TB,V_needsSubscriberListResync) needsSubscriberListResync;
@property (T@"<AccessoryNowPlayingClientDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) isConnected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AccessoryNowPlayingClient setClientQueue:];
-[AccessoryNowPlayingClient clientQueue];
-[AccessoryNowPlayingClient setServiceConnection:];
-[AccessoryNowPlayingClient isConnected];
-[AccessoryNowPlayingClient serviceConnection];
-[AccessoryNowPlayingClient init];
-[AccessoryNowPlayingClient setRemoteObject:];
-[AccessoryNowPlayingClient dealloc];
-[AccessoryNowPlayingClient remoteObject];
-[AccessoryNowPlayingClient disconnect];
-[AccessoryNowPlayingClient setDelegate:];
-[AccessoryNowPlayingClient delegate];
-[AccessoryNowPlayingClient removeSubscriber:];
-[AccessoryNowPlayingClient addSubscriber:];
-[AccessoryNowPlayingClient setSubscribers:];
-[AccessoryNowPlayingClient subscribers];
-[AccessoryNowPlayingClient connectToService];
-[AccessoryNowPlayingClient requestCurrentMediaItemArtwork:];
-[AccessoryNowPlayingClient _connectToServiceOnQueue];
-[AccessoryNowPlayingClient _disconnectOnQueue];
-[AccessoryNowPlayingClient _updateSubscriberListOnQueue];
-[AccessoryNowPlayingClient cancelRequestPlaybackQueueListInfo:requestID:];
-[AccessoryNowPlayingClient decrementUserCount];
-[AccessoryNowPlayingClient featureUserCount];
-[AccessoryNowPlayingClient incrementUserCount];
-[AccessoryNowPlayingClient mediaItemArtworkHasChanged:withReply:];
-[AccessoryNowPlayingClient mediaItemAttributesHaveChanged:withReply:];
-[AccessoryNowPlayingClient mockListenerEndpoint];
-[AccessoryNowPlayingClient needsSubscriberListResync];
-[AccessoryNowPlayingClient playbackAttributesHaveChanged:withReply:];
-[AccessoryNowPlayingClient playbackQueueListChanged];
-[AccessoryNowPlayingClient playbackQueueListInfoResponse:requestID:info:];
-[AccessoryNowPlayingClient requestCurrentMediaItemAttributes:];
-[AccessoryNowPlayingClient requestCurrentPlaybackAttributes:];
-[AccessoryNowPlayingClient requestPlaybackQueueListInfo:requestID:startIndex:upToCount:infoMask:];
-[AccessoryNowPlayingClient setFeatureUserCount:];
-[AccessoryNowPlayingClient setMockListenerEndpoint:];
-[AccessoryNowPlayingClient setNeedsSubscriberListResync:];
-[AccessoryNowPlayingClient setPlaybackElapsedTime:];
-[AccessoryNowPlayingClient setPlaybackQueueIndex:];
-[AccessoryNowPlayingClient updateSubscriberList:];
```
