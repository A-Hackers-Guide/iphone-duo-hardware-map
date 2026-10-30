# `AVPlaybackCoordinationMedium`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVPlaybackCoordinationMediumDelegate`
- 11 instance variables, 5 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _participants;
@"NSMutableDictionary" _currentParticipantStates;
@"NSMutableDictionary" _currentTransportControlStates;
^{OpaqueFigVideoTargetConfigurationSynchronizer=} _videoTargetsSynchronizer;
C _hasMixedAssetTypes;
@"AVPlaybackCoordinationMediumParticipant" _initialStateOriginator;
I _lowestInUseDefaultItemIdentifier;
@"NSCondition" _condition;
@"NSString" _itemIdentifierConditionWaitsOn;
@"NSObject<OS_dispatch_queue>" _stateQueue;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Properties

```
@property (T@"NSArray",R,N) connectedPlaybackCoordinators;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVPlaybackCoordinationMedium init];
-[AVPlaybackCoordinationMedium dealloc];
-[AVPlaybackCoordinationMedium _removeUnusedTransportControlStates];
-[AVPlaybackCoordinationMedium _initialStateOriginator];
-[AVPlaybackCoordinationMedium _lockedSeeksEnabled];
-[AVPlaybackCoordinationMedium _lowestInUseDefaultItemIdentifier];
-[AVPlaybackCoordinationMedium _mediumParticipantForCoordinator:orIdentifier:];
-[AVPlaybackCoordinationMedium _participantStatesAsArray];
-[AVPlaybackCoordinationMedium _participants];
-[AVPlaybackCoordinationMedium _removeParticipant:];
-[AVPlaybackCoordinationMedium _removeParticipantStateForIdentifier:];
-[AVPlaybackCoordinationMedium _setInitialStateOriginator:];
-[AVPlaybackCoordinationMedium _transportControlStateForItemIdentifier:];
-[AVPlaybackCoordinationMedium _transportControlStatesAsArray];
-[AVPlaybackCoordinationMedium _updateLowestInUseDefaultItemIdentifier];
-[AVPlaybackCoordinationMedium _updateMixedAssetTypesStatus];
-[AVPlaybackCoordinationMedium _updateParticipantState:forIdentifier:];
-[AVPlaybackCoordinationMedium _updateParticipantsWithParticipant:];
-[AVPlaybackCoordinationMedium _updateTransportControlState:forIdentifier:];
-[AVPlaybackCoordinationMedium areAllCoordinatorsSuspendedForReason:];
-[AVPlaybackCoordinationMedium attachVideoDestinations:forSynchronizationWithParticipantUUID:];
-[AVPlaybackCoordinationMedium connectPlaybackCoordinator:];
-[AVPlaybackCoordinationMedium connectedPlaybackCoordinators];
-[AVPlaybackCoordinationMedium disconnectPlaybackCoordinatorWithIdentifier:];
-[AVPlaybackCoordinationMedium endSuspensionOnAllCoordinatorsWithReason:];
-[AVPlaybackCoordinationMedium localParticipantUUIDForPlaybackCoordinator:];
-[AVPlaybackCoordinationMedium playbackCoordinator:broadcastLocalParticipantStateDictionary:];
-[AVPlaybackCoordinationMedium playbackCoordinator:broadcastTransportControlStateDictionary:forItemWithIdentifier:];
-[AVPlaybackCoordinationMedium playbackCoordinator:reloadTransportControlStateForItemWithIdentifier:completionHandler:];
-[AVPlaybackCoordinationMedium startCoordinatingVideoTargetsForSynchronization];
```
