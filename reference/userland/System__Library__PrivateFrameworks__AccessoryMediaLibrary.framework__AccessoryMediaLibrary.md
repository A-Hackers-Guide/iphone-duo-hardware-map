# `/System/Library/PrivateFrameworks/AccessoryMediaLibrary.framework/AccessoryMediaLibrary`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 10 classes, 6 protocols, 389 methods, 103 properties

### Class pages

Every class and protocol, with its methods: [`ACCMediaLibraryAccessory`](../objc/ACCMediaLibraryAccessory_AccessoryMediaLibrary.md), [`ACCMediaLibraryFeatureClientProtocol`](../objc/ACCMediaLibraryFeatureClientProtocol_AccessoryMediaLibrary.protocol.md), [`ACCMediaLibraryFeatureServiceProtocol`](../objc/ACCMediaLibraryFeatureServiceProtocol_AccessoryMediaLibrary.protocol.md), [`ACCMediaLibraryInfo`](../objc/ACCMediaLibraryInfo_AccessoryMediaLibrary.md), [`ACCMediaLibraryProvider`](../objc/ACCMediaLibraryProvider_AccessoryMediaLibrary.md), [`ACCMediaLibraryUpdateItem`](../objc/ACCMediaLibraryUpdateItem_AccessoryMediaLibrary.md), [`ACCMediaLibraryUpdateLibraryInfo`](../objc/ACCMediaLibraryUpdateLibraryInfo_AccessoryMediaLibrary.md), [`ACCMediaLibraryUpdatePlaylist`](../objc/ACCMediaLibraryUpdatePlaylist_AccessoryMediaLibrary.md), [`ACCMediaLibraryUpdatePlaylistContent`](../objc/ACCMediaLibraryUpdatePlaylistContent_AccessoryMediaLibrary.md), [`ACCMediaLibraryUpdatePlaylistContentItem`](../objc/ACCMediaLibraryUpdatePlaylistContentItem_AccessoryMediaLibrary.md), [`ACCMediaLibraryXPCClientProtocol`](../objc/ACCMediaLibraryXPCClientProtocol_AccessoryMediaLibrary.protocol.md), [`ACCMediaLibraryXPCServerProtocol`](../objc/ACCMediaLibraryXPCServerProtocol_AccessoryMediaLibrary.protocol.md), [`AccessoryMediaLibraryClient`](../objc/AccessoryMediaLibraryClient_AccessoryMediaLibrary.md), [`AccessoryMediaLibraryClientAPI`](../objc/AccessoryMediaLibraryClientAPI_AccessoryMediaLibrary.protocol.md), [`NSObject`](../objc/NSObject_AccessoryMediaLibrary.protocol.md), [`_ACCMediaLibraryAccessoryPendingUpdateItem`](../objc/_ACCMediaLibraryAccessoryPendingUpdateItem_AccessoryMediaLibrary.md)

### Classes

`ACCMediaLibraryAccessory`, `ACCMediaLibraryInfo`, `ACCMediaLibraryProvider`, `ACCMediaLibraryUpdateItem`, `ACCMediaLibraryUpdateLibraryInfo`, `ACCMediaLibraryUpdatePlaylist`, `ACCMediaLibraryUpdatePlaylistContent`, `ACCMediaLibraryUpdatePlaylistContentItem`, `AccessoryMediaLibraryClient`, `_ACCMediaLibraryAccessoryPendingUpdateItem`

### Protocols

`ACCMediaLibraryFeatureClientProtocol`, `ACCMediaLibraryFeatureServiceProtocol`, `ACCMediaLibraryXPCClientProtocol`, `ACCMediaLibraryXPCServerProtocol`, `AccessoryMediaLibraryClientAPI`, `NSObject`

### Properties

```
@property (T@"<AccessoryMediaLibraryClientDelegate>",W,N) delegate;
@property (Ti,R) featureUserCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSMutableDictionary",R,V_libraries) libraries;
@property (T@"NSMutableDictionary",&,V_pendingUpdates) pendingUpdates;
@property (T@"NSMutableDictionary",&,V_waitingConfirm) waitingConfirm;
@property (T@"NSMutableDictionary",&,V_pendingPlaylistContentUpdates) pendingPlaylistContentUpdates;
@property (T@"NSMutableDictionary",&,V_confirmedRevisionList) confirmedRevisionList;
@property (T@"NSObject<OS_dispatch_queue>",R,V_listQueue) listQueue;
@property (T@"NSString",R,V_accessoryUID) accessoryUID;
@property (T@"ACCMediaLibraryProvider",R,W,V_provider) provider;
@property (TI,V_windowPerLibrary) windowPerLibrary;
@property (T@"NSString",R,V_libraryUID) libraryUID;
@property (T@"ACCMediaLibraryUpdateLibraryInfo",R,V_info) info;
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
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (T@"NSString",&,V_revision) revision;
@property (TQ,V_persistentID) persistentID;
@property (TQ,R,V_validMask) validMask;
@property (T@"NSString",&,V_title) title;
@property (Ti,V_type) type;
@property (Ti,V_rating) rating;
@property (TI,V_duration) duration;
@property (TQ,V_albumPersistentID) albumPersistentID;
@property (T@"NSString",&,V_albumTitle) albumTitle;
@property (TS,V_albumTrackNumber) albumTrackNumber;
@property (TS,V_albumTrackCount) albumTrackCount;
@property (TS,V_albumDiscNumber) albumDiscNumber;
@property (TS,V_albumDiscCount) albumDiscCount;
@property (TQ,V_artistPersistentID) artistPersistentID;
@property (T@"NSString",&,V_artist) artist;
@property (TQ,V_albumArtistPersistentID) albumArtistPersistentID;
@property (T@"NSString",&,V_albumArtist) albumArtist;
@property (TQ,V_genrePersistentID) genrePersistentID;
@property (T@"NSString",&,V_genre) genre;
@property (TQ,V_composerPersistentID) composerPersistentID;
@property (T@"NSString",&,V_composer) composer;
@property (TB,V_partOfCompilation) partOfCompilation;
@property (TB,V_local) local;
@property (TS,V_chapterCount) chapterCount;
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (T@"NSString",&,V_name) name;
@property (Ti,V_type) type;
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (T@"NSString",&,V_revision) revision;
@property (TQ,V_persistentID) persistentID;
@property (TQ,R,V_validMask) validMask;
@property (T@"NSString",&,V_name) name;
@property (TQ,V_parentPersistentID) parentPersistentID;
@property (TB,V_folder) folder;
@property (TB,V_geniusMix) geniusMix;
@property (TB,V_radioStation) radioStation;
@property (TB,V_smartPlaylist) smartPlaylist;
@property (TS,V_radioStationOrdering) radioStationOrdering;
@property (Ti,V_contentStyle) contentStyle;
@property (T@"ACCMediaLibraryUpdatePlaylistContent",&,V_content) content;
@property (T@"NSMutableArray",&,V_contentList) contentList;
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (T@"NSString",&,V_revision) revision;
@property (TQ,V_persistentID) persistentID;
@property (Ti,V_contentStyle) contentStyle;
@property (T@"NSString",&,V_mediaLibraryUID) mediaLibraryUID;
@property (TQ,V_playlistPersistentID) playlistPersistentID;
@property (TQ,R,V_validMask) validMask;
@property (TQ,V_persistentID) persistentID;
@property (T@"NSString",&,V_title) title;
@property (T@"NSString",&,V_albumTitle) albumTitle;
@property (T@"NSString",&,V_artist) artist;
@property (T@"NSString",&,V_albumArtist) albumArtist;
@property (T@"NSString",&,V_genre) genre;
@property (T@"NSString",&,V_composer) composer;
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
@property (T@"NSString",R,N,V_libraryUID) libraryUID;
@property (T@"NSString",R,N,V_revision) revision;
@property (Ti,R,N,V_type) type;
@property (T@,R,N,V_item) item;
```

## Strings (218)

```
MediaLibrary XPC remoteObject unavailable; dropping outbound call to feature service (confirm/update may be lost)
Received libraryUpdate from service: lib=%@ accessory=%@ count=%lu
confirmUpdates: %@, library %@, revision %@, drained %lu update(s), waitlist now %lu
Failed to create os_log_t object %s: %s!
accessoryAttached: %@ windowPerLibrary=%u
Call notifyRemoteOfAvailableLibraries, providerUID:%@
startMediaLibraryUpdate: accessory %@ (%@) does not exist! or delegate does not respond to selector %@
update:%@ revision=%@ progress=%u addDeleteChange=%d status=%ld, pendingUpdatesFull=%d (%lu/%d), Skip sending Update!
MediaLibrary XPC service interrupted (service crash). Will reconnect on next call...
accessoryDetached: sending accessoryLeft to service for %@
confirmPlaylistContentUpdates: %@, library %@, revision %@, pendingUpdatesCount=%lu
playCollection: %@, library %@, accessory=%@, Call delegate play:collection:type:firstItemIndex:, collection=%llu type=%u startIndex=%u
playAllSongs: accessory %@ (%@) does not exist! or delegate does not respond to selector %@
dealloc: delegate=%@ providerUID=%@
initWithDelegate: delegate=%@ providerUID=%@
confirmUpdate: accessory %@ (%@), delegate does not respond to selector %@
updatePlaylist:%@ revision=%@ progress=%u playlist=%@ accessory=%@
_checkPlaylistContentToSend:%@ itemRevision=%@ item=%@
MediaLibrary service ready: %d
availableLibrariesDidChange unchanged — coalescing
copyPendingPlaylistContentUpdatesToSendForLibrary: %@, library %@, check for revision %@
shouldStayConnected: %d
confirmPlaylistContentUpdate: accessory %@ (%@), delegate does not respond to selector %@
%s did not register for notification (%d, %s), token (%d)
Received libraryContentUpdate from service: lib=%@ accessory=%@ revision=%@
update:%@ revision=%@ persistentID=%llu updateType=%d progress=%u info=%@ accessory=%@ self.lastUpdateType=%d, UNKNOWN TYPE!!!
Unregister AvailabilityChangedHandler (%d, %s)
%s (%d)
accessoryAttached: remoteObject is nil! Cannot send accessoryArrived for %@
accessoryMediaLibraryDetached: accessory %@ (%@) delegate does not respond to selector %@
accessoryMediaLibraryAllDetached: accessory %@ delegate does not respond to selector %@
update:%@ revision=%@, No Pending Updates (%lu / %d), update not sent!!!
copyPendingPlaylistContentUpdatesToSendForLibrary: %@, library %@, revisionList=%@
confirmUpdates: %@, library %@, revision %@, updateCount %u, pendingUpdatesCount=%lu
confirmUpdates: %@, library %@, revision %@, updateCount %u, index=%lu waitlist.count=%lu playlistRevisionToAdd=%@
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Connecting to XPC server...
XPC connection interrupted: providerUID:%@, notify of detach
accessoryMediaLibraryDetached: accessory %@, accessory=%@, Call delegate accessoryLeft:
update:%@ addDeleteChange=%d flushUpdate
%s (%d, %s)
accessoryDetached: %@
update:%@ revision=%@ persistentID=%llu updateType=%d progress=%u info=%@ accessory=%@, status=%ld
updateDeleteItem:%@ revision=%@ progress=%u persistentID=%llu accessory=%@
resetUpdate:%@
Received libraryResetUpdate from service: lib=%@ accessory=%@
copyPendingPlaylistContentUpdatesToSendForLibrary: %@, library %@, found %@
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
accessoryMediaLibraryAttached: accessory %@, accessory=%@, Call delegate accessoryArrived:windowPerLibrary:, windowPerLibrary=%u
stopAllMediaLibraryUpdate: accessory %@ (%@) does not exist! or delegate does not respond to selector %@
update:%@ revision=%@ persistentID=%llu updateType=%d progress=%u info=%@ accessory=%@ self.lastUpdateType=%d
Received libraryStateDidChange from service: %@ type=%d enabled=%d
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
accessoryMediaLibraryAttached: accessory %@ (%@) already exists!
playItems: accessory %@ (%@) does not exist! or delegate does not respond to selector %@
Received availableLibrariesDidChange from service: %@
addUpdate: %@, library %@, updateDict=%@
XPC connection error!
accessoryMediaLibraryUpdate: accessory %@ (%@) delegate does not respond to selector %@
confirmUpdate: accessory %@ (%@) does not exist!
%@ setContentStyle %d->%d
confirmUpdate: relaying to feature service accessory=%@ library=%@ lastRevision=%@ updateCount=%u
Getting remote object...
accessoryMediaLibraryAttached: accessory %@ (%@) delegate does not respond to selector %@
accessoryMediaLibraryUpdate: accessory %@, accessory=%@, Call delegate accessoryUpdate:windowPerLibrary:, windowPerLibrary=%u
flushUpdates:%@ accessory=%@
%s cannot get server state (%d, %s)
Getting remote object for MediaLibrary service...
No more MediaLibrary users, disconnecting from service...
Created log object %s: %s
XPC connection interrupted!
playCurrentSelection: %@, library %@, accessory=%@, Call delegate playCurrentSelection:
update:%@, No Pending Updates (%lu / %d), update not sent!!!
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
addPlaylistContentUpdate: %@, library %@, updateDict=%@
confirmUpdates: %@, library %@, WARNING!!! either revision (%@) or item.revision (%@) were not numbers! using string compare
notifyRemoteOfAvailableLibraries: providerUID:%@
_validMask=%llxh dict=%@
accessoryAttached: sending accessoryArrived to service for %@
_notifyRemoteOfAvailableLibraries:%@ providerUID:%@
%@
startMediaLibraryUpdate: accessory %@, library %@, accessory=%@, Call delegate startUpdate:lastRevision:requestedInfo:, lastRevision=%@ infoDictionary=%@
update:%@ revision=%@ progress=%u status=%ld, pendingUpdatesFull=%d (%lu/%d), Send Update!
%s:%d serviceConnection=%p remoteObject=%p isServiceReady=%d
MediaLibrary XPC service error: %@
Created %d log object(s)!
playCollection: accessory %@ (%@) does not exist! or delegate does not respond to selector %@
updateItem:%@ revision=%@ progress=%u item=%@ accessory=%@
_checkPlaylistContentToSend:%@ no pending playlistContentUpdates
XPC connection invalidated!
accessoryMediaLibraryUpdate: accessory %@ (%@) does not exist!
startMediaLibraryUpdate: accessory %@, library %@, accessory=%@, fill in infoDictionary, mediaItemProperties=%llxh playlistProperties=%llxh playlistContentProperties=%llxh, lastRevision=%@
confirmUpdate: %@, library %@, lastRevision %@, updateCount %u, accessory=%@, removedList=(%lu)%@
playItems: %@, library %@, accessory=%@, Call delegate play:itemList:firstItemIndex:, itemList.count=%lu startIndex=%u
_checkPlaylistContentToSend:%@ accessory=%@
MediaLibrary initConnection error: %@
playAllSongs: %@, library %@, accessory=%@, Call delegate playAllSongs:firstItemPersistentID:, startIitem=%llu
confirmPlaylistContentUpdate: %@, library %@, lastRevision %@, accessory=%@, Call delegate confirmPlaylistContentUpdate:
clearAllUpdatesForLibrary: %@, libraryUID %@, pendingUpdates.count=%lu waitingConfirm.count=%lu pendingUpdates.count=%lu waitingConfirm.count=%lu
accessoryMediaLibraryAllDetached: accessory %@, Call delegate accessoryLeft:
foundDeletionOrAdd=%d providerUID:%@ self.libraries= %@ -> %@
updateProgress:%@ revision=%@ progress=%u accessory=%@
%@ contentStyle %d->%@
copyPendingPlaylistContentUpdatesToSendForLibrary: %@, library %@, pendlist=%@
confirmUpdate: %@, library %@, lastRevision %@, updateCount %u, accessory=%@, Call delegate confirmUpdate
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
addUpdate: %@, pendingUpdatesAndWaitingConfirmFullForLibrary:%@ (%d), unable to addUpdate! updateDict=%@
confirmUpdates: %@, library %@, wasPlaylistUpdates, _addConfirmedRevisionForLibrary playlistRevisionToAdd=%@
update:%@ revision=%@, full after addUpdate (%lu / %d)
Register AvailabilityChangedHandler (%d, %s)
stopMediaLibraryUpdate: accessory %@, accessory=%@, Call delegate stopUpdate:
update:%@ revision=%@, ALREADY FULL (%lu / %d), update not added!!!
updateDeletePlaylist:%@ revision=%@ progress=%u persistentID=%llu accessory=%@
updateContent:%@ revision=%@, full after addPlaylistContentUpdate (%lu / %d)
MediaLibrary XPC service connection invalidated!
accessoryMediaLibraryDetached: accessory %@ (%@) does not exist!
playCurrentSelection: accessory %@ (%@) does not exist! or delegate does not respond to selector %@
foundDeletionOrAdd, notifyRemoteOfAvailableLibraries: providerUID:%@
update:%@ revision=%@, not full (%lu / %d), addUpdate: dict=%@
updateContent:%@ revision=%@ content=%@ accessory=%@
incrementUserCount: %d -> %d
decrementUserCount: %d -> %d
confirmUpdates: %@, library %@, WARNING!!! no revision specified so using updateCount only!
clearAllUpdates: %@, pendingUpdates.count=%lu waitingConfirm.count=%lu pendingPlaylistContentUpdates.count=%lu confirmedRevisionList.count=%lu
confirmPlaylistContentUpdate: accessory %@ (%@) does not exist!
playCollection: %@, library %@, accessory=%@, Call delegate play:collection:type:firstItemPersistentID:, collection=%llu type=%u startItem=%llu
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
stopAllMediaLibraryUpdate: accessory %@, accessory=%@, Call delegate stopAllUpdate:
v12@?0B8
v16@?0@\"<ACCMediaLibraryFeatureServiceProtocol>\"8
<ACCMediaLibraryInfo>[%@ state=[%d %d] info=%@]
ACCMediaLibraryUpdateItemTitle
ACCMediaLibraryUpdateItemComposerPersistentID
ACCMediaLibraryUpdateItemComposer
Connection
Transport
ACCMediaLibraryUpdateItemAlbumDiscCount
ACCMediaLibraryFullUpdateKey
ACCMediaLibraryUpdatePlaylistIsGeniusMix
ACCMediaLibraryUpdateItemAlbumPersistentID
ACCMediaLibraryUpdateItemAlbumDiscNumber
'
!
com.apple.acc.mediaLibrary.provider
_SetupAvailabilityChangedHandlerForServiceEntry
ACCMediaLibraryUpdatePlaylistItemDictionary
ACCMediaLibraryUpdatePlaylistParentPersistentID
ACCMediaLibraryUpdateItemGenrePersistentID
ACCMediaLibraryUpdateItemGenre
<ACCMediaLibraryUpdatePlaylistContent>[%@:%llu revision=%@ style=%d count=%lu]
 smart
ACCMediaLibraryUpdatePlaylistContentStyle
ACCMediaLibraryUpdatePlaylistIsSmartPlaylist
com.apple.accessories.frameworks
General
com.apple.accessories.media-library-feature
ACCMediaLibraryUpdatePlayAllSongsCapable
ACCMediaLibraryUpdatePlaylistName
ACCMediaLibraryUpdateItemAlbumTrackNumber
<_ACCMediaLibraryAccessoryPendingUpdateItem>[libraryUID=%@ revision=%@ type=%u]
ACCMediaLibraryUpdateItemDictionary
<ACCMediaLibraryUpdatePlaylist>[%@:%llu revision=%@ valid=%llxh '%@' %@ %@ %@ %@ parentPersistentID=%llu]
ACCMediaLibraryUpdateItemType
ACCMediaLibraryUpdateProgressKey
ACCMediaLibraryUpdatePlaylistPersistentID
com.apple.accMediaLibraryAccessory.listQueue
ACCMediaLibraryUpdatePlaylistDictionary
ACCMediaLibraryUpdateItemIsLocal
ACCMediaLibraryPlaylistItemAlbumTitle
 geniusMix
<ACCMediaLibraryUpdatePlaylistContentItem>[%@:%llu itemPersistentID=%llu '%@' validMask=%llxh]
ACCMediaLibraryUpdateItemRating
ACCMediaLibraryPlaylistItemPersistentID
ACCMediaLibraryPlaylistItemAlbumArtist
<ACCMediaLibraryAccessory>[%@ provider=%@]
<ACCMediaLibraryProvider>[%@]
ACCMediaLibraryUpdateItemAlbumArtistPersistentID
 station
ACCMediaLibraryNameKey
ACCMediaLibraryUpdateRevisionKey
ACCMediaLibraryUpdateItemAlbumTrackCount
ACCMediaLibraryUpdatePlaylistItemList
v16@?0@\"NSError\"8
<ACCMediaLibraryUpdateItem>[%@:%llu valid=%llxh '%@' mediaType=%d local=%d]
ACCMediaLibraryUpdatePlaylistIsRadioStation
ACCMediaLibraryUpdateItemArtist
(
Endpoint
null
accessoryServer_isServerAvailableForServiceEntry
ACCMediaLibraryUpdatePlaylistIsFolder
ACCMediaLibraryUpdateItemPlaybackDurationInMilliseconds
ACCMediaLibraryUpdateItemArtistPersistentID
ACCMediaLibraryPlaylistItemTitle
ACCMediaLibraryPlaylistItemArtist
ACCMediaLibraryPlaylistItemGenre
v8@?0
v12@?0i8
 folder
ACCMediaLibraryPlaylistItemComposer
com.apple.accessories.media-library-client
-[AccessoryMediaLibraryClient _connectToServiceOnQueue]
<Undefined>
com.apple.accessories.signposts
%@\n    %@
<ACCMediaLibraryUpdateLibraryInfo>[%@ '%@' type=%d]
ACCMediaLibraryTypeKey
ACCMediaLibraryUpdateTypeKey
ACCMediaLibraryUpdateItemDeletePersistentID
ACCMediaLibraryUpdateHidingRemoteItems
ACCMediaLibraryUpdateItemAlbumTitle
ACCMediaLibraryUpdateItemIsPartOfCompilation
ACCMediaLibraryUIDKey
ACCMediaLibraryUpdatePlaylistDeletePersistentID
ACCMediaLibraryUpdatePlaylistRadioStationOrdering
ACCMediaLibraryUpdateItemPersistentID
ACCMediaLibraryUpdateItemAlbumArtist
ACCMediaLibraryUpdateItemChapterCount
```
