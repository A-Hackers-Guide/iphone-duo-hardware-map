# `TUIDSLookupManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `IDSBatchIDQueryControllerDelegate`
- 19 instance variables, 23 properties, 65 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<TUIDSIDQueryController>" _queryController;
@"TULocked" _idsFaceTimeVideoStatuses;
@"TULocked" _idsFaceTimeAudioStatuses;
@"TULocked" _idsFaceTimeMultiwayStatuses;
@"TULocked" _idsVideoMessagingStatuses;
@"TULocked" _idsiMessageStatuses;
@"TULocked" _idsNameAndPhotoStatuses;
@"TULocked" _idsModernStatuses;
@"TULocked" _idsWebCapableStatuses;
@"TULocked" _idsAVLessSharePlayCapableStatuses;
@"TULocked" _lastForcedQueryTimestamps;
@"<TUIDSBatchIDQueryController>" _batchQuerySearchVideoController;
@"<TUIDSBatchIDQueryController>" _batchQuerySearchAudioController;
@"<TUIDSBatchIDQueryController>" _batchQuerySearchMultiwayController;
@"<TUIDSBatchIDQueryController>" _batchQuerySearchVideoMessagingController;
@"<TUIDSBatchIDQueryController>" _batchQuerySearchiMessageController;
@"<TUIDSBatchIDQueryController>" _batchQuerySearchShareNameAndPhotoController;
@? _batchQueryControllerCreationBlock;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"<TUIDSIDQueryController>",R,N,V_queryController) queryController;
@property (T@"TULocked",R,N,V_idsFaceTimeVideoStatuses) idsFaceTimeVideoStatuses;
@property (T@"TULocked",R,N,V_idsFaceTimeAudioStatuses) idsFaceTimeAudioStatuses;
@property (T@"TULocked",R,N,V_idsFaceTimeMultiwayStatuses) idsFaceTimeMultiwayStatuses;
@property (T@"TULocked",R,N,V_idsVideoMessagingStatuses) idsVideoMessagingStatuses;
@property (T@"TULocked",R,N,V_idsiMessageStatuses) idsiMessageStatuses;
@property (T@"TULocked",R,N,V_idsNameAndPhotoStatuses) idsNameAndPhotoStatuses;
@property (T@"TULocked",R,N,V_idsModernStatuses) idsModernStatuses;
@property (T@"TULocked",R,N,V_idsWebCapableStatuses) idsWebCapableStatuses;
@property (T@"TULocked",R,N,V_idsAVLessSharePlayCapableStatuses) idsAVLessSharePlayCapableStatuses;
@property (T@"TULocked",R,N,V_lastForcedQueryTimestamps) lastForcedQueryTimestamps;
@property (T@"<TUIDSBatchIDQueryController>",&,N,V_batchQuerySearchVideoController) batchQuerySearchVideoController;
@property (T@"<TUIDSBatchIDQueryController>",&,N,V_batchQuerySearchAudioController) batchQuerySearchAudioController;
@property (T@"<TUIDSBatchIDQueryController>",&,N,V_batchQuerySearchMultiwayController) batchQuerySearchMultiwayController;
@property (T@"<TUIDSBatchIDQueryController>",&,N,V_batchQuerySearchVideoMessagingController) batchQuerySearchVideoMessagingController;
@property (T@"<TUIDSBatchIDQueryController>",&,N,V_batchQuerySearchiMessageController) batchQuerySearchiMessageController;
@property (T@"<TUIDSBatchIDQueryController>",&,N,V_batchQuerySearchShareNameAndPhotoController) batchQuerySearchShareNameAndPhotoController;
@property (T@?,C,N,V_batchQueryControllerCreationBlock) batchQueryControllerCreationBlock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUIDSLookupManager sharedManager];
+[TUIDSLookupManager fzHandleIDStatusForDestination:usingCache:];
+[TUIDSLookupManager isAnyDestinationAvailableInDestinations:usingCache:];
```

## Instance methods

```
-[TUIDSLookupManager queryController];
-[TUIDSLookupManager batchQueryController:updatedDestinationsStatus:onService:error:];
-[TUIDSLookupManager init];
-[TUIDSLookupManager dealloc];
-[TUIDSLookupManager queue];
-[TUIDSLookupManager batchQuerySearchAudioController];
-[TUIDSLookupManager preferredFromID];
-[TUIDSLookupManager batchQuerySearchVideoController];
-[TUIDSLookupManager batchQueryControllerCreationBlock];
-[TUIDSLookupManager batchQuerySearchMultiwayController];
-[TUIDSLookupManager batchQuerySearchShareNameAndPhotoController];
-[TUIDSLookupManager batchQuerySearchVideoMessagingController];
-[TUIDSLookupManager batchQuerySearchiMessageController];
-[TUIDSLookupManager beginBatchQueryWithDestinations:];
-[TUIDSLookupManager beginBatchQueryWithDestinations:includeMessages:];
-[TUIDSLookupManager beginBatchQueryWithDestinations:services:];
-[TUIDSLookupManager beginCachedQueryWithDestinations:];
-[TUIDSLookupManager beginCachedQueryWithDestinations:includeMessages:];
-[TUIDSLookupManager beginCachedQueryWithDestinations:onService:];
-[TUIDSLookupManager beginCachedQueryWithDestinations:services:];
-[TUIDSLookupManager beginQueryWithDestination:onService:];
-[TUIDSLookupManager beginQueryWithDestinations:];
-[TUIDSLookupManager beginQueryWithDestinations:includeMessages:];
-[TUIDSLookupManager beginQueryWithDestinations:services:];
-[TUIDSLookupManager beginQueryWithRefreshForDestination:onService:];
-[TUIDSLookupManager cancelQueries];
-[TUIDSLookupManager faceTimeAudioAvailabilityForDestination:];
-[TUIDSLookupManager faceTimeMultiwayAvailabilityForDestination:];
-[TUIDSLookupManager faceTimeVideoAvailabilityForDestination:];
-[TUIDSLookupManager filteredDestinationForMultiway:completionBlock:];
-[TUIDSLookupManager handleIDSQueryResultWithDestinationStatus:onService:];
-[TUIDSLookupManager idsAVLessSharePlayCapableStatuses];
-[TUIDSLookupManager idsFaceTimeAudioStatuses];
-[TUIDSLookupManager idsFaceTimeMultiwayStatuses];
-[TUIDSLookupManager idsFaceTimeVideoStatuses];
-[TUIDSLookupManager idsModernStatuses];
-[TUIDSLookupManager idsNameAndPhotoStatuses];
-[TUIDSLookupManager idsVideoMessagingStatuses];
-[TUIDSLookupManager idsWebCapableStatuses];
-[TUIDSLookupManager idsiMessageStatuses];
-[TUIDSLookupManager initWithQueryController:batchQueryControllerCreationBlock:];
-[TUIDSLookupManager isAVLessSharePlayCapableForAnyDestinationInDestinations:];
-[TUIDSLookupManager isFaceTimeAudioAvailableForAnyDestinationInDestinations:];
-[TUIDSLookupManager isFaceTimeAudioAvailableForItem:];
-[TUIDSLookupManager isFaceTimeMultiwayAvailableForAnyDestinationInDestinations:];
-[TUIDSLookupManager isFaceTimeMultiwayAvailableForItem:];
-[TUIDSLookupManager isFaceTimeVideoAvailableForAnyDestinationInDestinations:];
-[TUIDSLookupManager isFaceTimeVideoAvailableForItem:];
-[TUIDSLookupManager isModernFaceTimeAvailableForDestination:];
-[TUIDSLookupManager isNameAndPhotoAvailableForDestination:];
-[TUIDSLookupManager isVideoMessagingAvailableForAnyDestinationInDestinations:];
-[TUIDSLookupManager isVideoMessagingAvailableForItem:];
-[TUIDSLookupManager isWebCapableFaceTimeAvailableForDestination:];
-[TUIDSLookupManager isiMessageAvailableForAnyDestinationInDestinations:];
-[TUIDSLookupManager lastForcedQueryTimestamps];
-[TUIDSLookupManager postStatusChangedNotification];
-[TUIDSLookupManager queryHasEndpointWithCapabilities:forMultiwayDestinations:completionBlock:];
-[TUIDSLookupManager queryHasWebOnlyEndpointsForDestinations:completionBlock:];
-[TUIDSLookupManager setBatchQueryControllerCreationBlock:];
-[TUIDSLookupManager setBatchQuerySearchAudioController:];
-[TUIDSLookupManager setBatchQuerySearchMultiwayController:];
-[TUIDSLookupManager setBatchQuerySearchShareNameAndPhotoController:];
-[TUIDSLookupManager setBatchQuerySearchVideoController:];
-[TUIDSLookupManager setBatchQuerySearchVideoMessagingController:];
-[TUIDSLookupManager setBatchQuerySearchiMessageController:];
```
