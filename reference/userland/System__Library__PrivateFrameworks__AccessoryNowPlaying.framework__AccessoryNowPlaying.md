# `/System/Library/PrivateFrameworks/AccessoryNowPlaying.framework/AccessoryNowPlaying`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 1 classes, 3 protocols, 75 methods, 17 properties

### Class pages

Every class and protocol, with its methods: [`ACCNowPlayingFeatureClientProtocol`](../objc/ACCNowPlayingFeatureClientProtocol_AccessoryNowPlaying.protocol.md), [`ACCNowPlayingFeatureServiceProtocol`](../objc/ACCNowPlayingFeatureServiceProtocol_AccessoryNowPlaying.protocol.md), [`AccessoryNowPlayingClient`](../objc/AccessoryNowPlayingClient_AccessoryNowPlaying.md), [`NSObject`](../objc/NSObject_AccessoryNowPlaying.protocol.md)

### Classes

`AccessoryNowPlayingClient`

### Protocols

`ACCNowPlayingFeatureClientProtocol`, `ACCNowPlayingFeatureServiceProtocol`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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

## Strings (101)

```
NonLibrary
Available
v12@?0i8
com.apple.accessories.signposts
MediaItemAttributes
AlbumTitle
AlbumTrackNum
AlbumDiscNum
Composer
IsLiked
RepeatMode
AlbumDiscCount
General
-[AccessoryNowPlayingClient _connectToServiceOnQueue]
Status
iTunesRadioStationIdentifier
PlaybackDurationMS
Artist
QueueListAvailable
Count
PersistentID
List
PlaybackQueueIndex
PlaybackQueueList
null
_SetupAvailabilityChangedHandlerForServiceEntry
Transport
Genre
ShuffleMode
MediaItemArtwork
AlbumTrackCount
QueueCount
QueueChapterIndex
RequestID
StartIndex
Connection
com.apple.accessories.now-playing-client
IsBanSupported
IsMusicApp
ElapsedTime
v8@?0
v12@?0B8
QueueIndex
AppName
Title
ElapsedTimeMS
AlbumArtist
com.apple.accessories.frameworks
com.apple.accessories.now-playing-feature
v16@?0@\"NSError\"8
PlaybackAttributes
IsBanned
ArtworkID
iTunesRadioStationMediaPlaylistPersistentID
Endpoint
ChapterCount
iTunesRadioStation
SetElapsedTimeAvailable
<Undefined>
IsLikeSupported
MediaLibraryUID
%
PlaybackSpeed
accessoryServer_isServerAvailableForServiceEntry
iTunesRadioAd
AppBundleID
Received playbackQueueListInfoResponse from service: %@ requestID: %@ info: %@
Unregister AvailabilityChangedHandler (%d, %s)
Created %d log object(s)!
NowPlaying XPC service connection invalidated!
Created log object %s: %s
Failed to create os_log_t object %s: %s!
%s:%d
NowPlaying XPC service error: %@
%s did not register for notification (%d, %s), token (%d)
#Artwork Received mediaItemArtwork update from service: %lu bytes
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
%s (%d)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
NowPlaying XPC service interrupted (service crash). Will reconnect after delay...
Added subscriber for key: %@... New count: %lu
Set playback elapsed time result: %d
Register AvailabilityChangedHandler (%d, %s)
%s (%d, %s)
Resync subscriber list result: %d
No more NowPlaying users, disconnecting from service...
Received mediaItemAttributes update from service: %@
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
Removed subscriber for key: %@... New count: %lu
Update subscriber list result: %d
No service connection, ignore cancel for accessoryUID %@, requestID %@
Received playbackQueueListChanged from service
%s cannot get server state (%d, %s)
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Getting remote object for NowPlaying service...
Resyncing subscriber list after service restart...
Set playback queue index result: %d
No service connection, sending playback queue list not available...
Received playbackAttributes update from service: %@
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
```
