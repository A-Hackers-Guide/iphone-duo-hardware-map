# `AVPlayerPlaybackCoordinator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlaybackCoordinator`
- 21 instance variables, 4 properties, 96 instance methods, 0 class methods

## Instance variables

```
@"AVPlayer" _weakPlayer;
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
@"NSObject<OS_dispatch_queue>" _figPlaybackCoordinatorConfigQueue;
@"NSObject<OS_dispatch_queue>" _localParticipantUUIDConfigQueue;
^{OpaqueFigPlaybackCoordinator=} _figPlaybackCoordinator;
@"NSMutableArray" _suspensionReasons;
@"NSMutableArray" _assumedActiveSuspensions;
@"NSMutableArray" _otherParticipants;
@"AVPlayerPlaybackCoordinatorStorage" _storage;
@"NSMutableArray" _currentSuspensions;
@"AVPlayerPlaybackCoordinator" _weakPrimaryPlaybackCoordinator;
@"AVPlayerPlaybackCoordinator" _interstitialPlaybackCoordinator;
B _isInExpanseMediaPlayback;
@"NSMutableDictionary" _pendingFigPlaybackCoordinatorProperties;
{?="value"q"timescale"i"flags"I"epoch"q} _networkToHostTimeOffset;
@"NSMapTable" _playerItemToItemIdentifierMap;
I _defaultItemIdentifierCounter;
B _shouldOverrideGroupState;
@ _suspensionsChangedNotificationToken;
@ _participantsChangedNotificationToken;
@ _didIssueCommandToPlaybackObjectNotificationToken;
```

## Properties

```
@property (T@"NSString",R) localParticipantUUIDString;
@property (TB,R,G_hasFigPlaybackCoordinator) hasFigPlaybackCoordinator;
@property (T@"AVPlayer",R,W,N) player;
@property (T@"<AVPlayerPlaybackCoordinatorDelegate>",W) delegate;
```

## Instance methods

```
-[AVPlayerPlaybackCoordinator networkToHostTimeOffset];
-[AVPlayerPlaybackCoordinator participantLimitForWaitingOutSuspensionsWithReason:];
-[AVPlayerPlaybackCoordinator setInterstitialPlaybackCoordinator:];
-[AVPlayerPlaybackCoordinator player];
-[AVPlayerPlaybackCoordinator _postNotificationWithName:userInfo:];
-[AVPlayerPlaybackCoordinator _updateParticipantStateDictionaryWithParticipantState:];
-[AVPlayerPlaybackCoordinator coordinateUsingCoordinationMedium:error:];
-[AVPlayerPlaybackCoordinator _copyFigPlaybackCoordinator];
-[AVPlayerPlaybackCoordinator shouldOverrideGroupState];
-[AVPlayerPlaybackCoordinator _updateSuspensionReasons:];
-[AVPlayerPlaybackCoordinator handleRemovalOfParticipant:];
-[AVPlayerPlaybackCoordinator setWeakReferenceToPrimaryPlaybackCoordinator:];
-[AVPlayerPlaybackCoordinator _updateWaitingPoliciesOnFigPlaybackCoordinator:];
-[AVPlayerPlaybackCoordinator _updateWaitingPoliciesArray:withPolicies:];
-[AVPlayerPlaybackCoordinator setFigPlaybackCoordinator:];
-[AVPlayerPlaybackCoordinator setPauseSnapsToMediaTimeOfOriginator:];
-[AVPlayerPlaybackCoordinator _pendingFigPlaybackCoordinatorPropertyForKey:];
-[AVPlayerPlaybackCoordinator dealloc];
-[AVPlayerPlaybackCoordinator mediumLoggingIdentifier];
-[AVPlayerPlaybackCoordinator _resetGroupTimelineExpectationsForIdentifier:];
-[AVPlayerPlaybackCoordinator _setNetworkToHostTimeOffset];
-[AVPlayerPlaybackCoordinator participantForIdentifier:];
-[AVPlayerPlaybackCoordinator _updateLocalParticipantUUIDOnFigPlaybackCoordinator:];
-[AVPlayerPlaybackCoordinator _updateParticipantStateOnFigPlaybackCoordinatorForItemWithIdentifier:];
-[AVPlayerPlaybackCoordinator _replaceAllParticipantStateDictionariesOnFigPlaybackCoordinator:];
-[AVPlayerPlaybackCoordinator _setWeakReferenceToPlayerItem:withItemIdentifier:];
-[AVPlayerPlaybackCoordinator _hasRemovedSuspensionReason:currentReasons:newReasons:];
-[AVPlayerPlaybackCoordinator _pendingFigPlaybackCoordinatorProperties];
-[AVPlayerPlaybackCoordinator initWithPlayer:];
-[AVPlayerPlaybackCoordinator _updateCoordinationMediumDelegateOnFigPlaybackCoordinator];
-[AVPlayerPlaybackCoordinator handleReplacementParticipantStateDictionaries:];
-[AVPlayerPlaybackCoordinator _endSuspensionWithReason:];
-[AVPlayerPlaybackCoordinator _updateParticipantLimitOnFigPlaybackCoordinatorWithReason:];
-[AVPlayerPlaybackCoordinator otherParticipants];
-[AVPlayerPlaybackCoordinator isDefunct];
-[AVPlayerPlaybackCoordinator _hasFigPlaybackCoordinator];
-[AVPlayerPlaybackCoordinator _convertToMediaTimeForTime:withNetworkTime:rate:];
-[AVPlayerPlaybackCoordinator _updateTransportControlStateDictionaryOnFigPlaybackCoordinatorForItemIdentifier:];
-[AVPlayerPlaybackCoordinator _endSuspension:proposingNewTime:];
-[AVPlayerPlaybackCoordinator _endSuspension:];
-[AVPlayerPlaybackCoordinator _storageWrite:];
-[AVPlayerPlaybackCoordinator _updateSuspensionsForNewSuspensionReasons:];
-[AVPlayerPlaybackCoordinator _disconnectFromCoordinationMedium];
-[AVPlayerPlaybackCoordinator setDelegate:];
-[AVPlayerPlaybackCoordinator _removeSuspension:];
-[AVPlayerPlaybackCoordinator _updateTransportControlStateDictionaryWithTransportControlState:];
-[AVPlayerPlaybackCoordinator coordinationMediumDelegate];
-[AVPlayerPlaybackCoordinator interstitialTimeRangesForPlayerItem:];
-[AVPlayerPlaybackCoordinator _synchronizeWorkOnPlayerQueue:];
-[AVPlayerPlaybackCoordinator _addFigPlaybackCoordinatorListeners:];
-[AVPlayerPlaybackCoordinator suspensionReasonsThatTriggerWaiting];
-[AVPlayerPlaybackCoordinator assumedActiveSuspensions];
-[AVPlayerPlaybackCoordinator setCoordinationMediumDelegate:];
-[AVPlayerPlaybackCoordinator _connectToCoordinationMedium:];
-[AVPlayerPlaybackCoordinator expectedItemTimeAtHostTime:];
-[AVPlayerPlaybackCoordinator coordinationOffsetForPlayerItem:];
-[AVPlayerPlaybackCoordinator _figPlaybackCoordinatorConfigQueue];
-[AVPlayerPlaybackCoordinator itemIdentifierForPlayerItem:];
-[AVPlayerPlaybackCoordinator _setInterstitialActive:];
-[AVPlayerPlaybackCoordinator primaryPlaybackCoordinatorForInterstitial];
-[AVPlayerPlaybackCoordinator _ensureIntegratedTimelineIsEstablished];
-[AVPlayerPlaybackCoordinator _setIsInExpanseMediaPlaybackOnAVAudioSession];
-[AVPlayerPlaybackCoordinator suspensionReasons];
-[AVPlayerPlaybackCoordinator delegate];
-[AVPlayerPlaybackCoordinator avfParticipantsForFigParticipantsUUIDs:];
-[AVPlayerPlaybackCoordinator _removeUnusedTransportControlStates];
-[AVPlayerPlaybackCoordinator pauseSnapsToMediaTimeOfOriginator];
-[AVPlayerPlaybackCoordinator description];
-[AVPlayerPlaybackCoordinator handleNewTransportControlStateDictionary:];
-[AVPlayerPlaybackCoordinator trackedTransportControlStateDictionaries];
-[AVPlayerPlaybackCoordinator _updateSuspensionReasonsThatTriggerWaitingOFigPlaybackCoordinator];
-[AVPlayerPlaybackCoordinator _synchronizeFigPlayerEvents];
-[AVPlayerPlaybackCoordinator setSuspensionReasonsThatTriggerWaiting:];
-[AVPlayerPlaybackCoordinator localParticipantUUIDString];
-[AVPlayerPlaybackCoordinator setDefaultItemIdentifierCounter:postingNotification:];
-[AVPlayerPlaybackCoordinator currentLamportTimestampForIdentifier];
-[AVPlayerPlaybackCoordinator isConnectedToLocalPlaybackCoordinationMedium];
-[AVPlayerPlaybackCoordinator _setStorage:];
-[AVPlayerPlaybackCoordinator setParticipantLimit:forWaitingOutSuspensionsWithReason:];
-[AVPlayerPlaybackCoordinator playbackCoordinationMedium];
-[AVPlayerPlaybackCoordinator handleNewParticipantStateDictionary:];
-[AVPlayerPlaybackCoordinator _reactToNewDelegate];
-[AVPlayerPlaybackCoordinator beginSuspensionForReason:];
-[AVPlayerPlaybackCoordinator _setIsLocallyCoordinated:];
-[AVPlayerPlaybackCoordinator _updatePauseSnapsToMediaTimeOfOriginatorOnFigPlaybackCoordinator];
-[AVPlayerPlaybackCoordinator interstitialPlaybackCoordinator];
-[AVPlayerPlaybackCoordinator _applyIntegratedTimelineSeek:];
-[AVPlayerPlaybackCoordinator _setPendingFigPlaybackCoordinatorProperty:forKey:];
-[AVPlayerPlaybackCoordinator _currentWaitingPoliciesArray];
-[AVPlayerPlaybackCoordinator defaultItemIdentifierCounter];
-[AVPlayerPlaybackCoordinator currentSuspensions];
-[AVPlayerPlaybackCoordinator identifierForPlayerItem:];
-[AVPlayerPlaybackCoordinator _storageRead:];
-[AVPlayerPlaybackCoordinator _updateOtherParticipantsUsingFigParticipantUUIDs:];
-[AVPlayerPlaybackCoordinator _applyAdjustedIntegratedSeekTimeFromTime:withNetworkTime:rate:];
-[AVPlayerPlaybackCoordinator setMediumLoggingIdentifier:];
```
