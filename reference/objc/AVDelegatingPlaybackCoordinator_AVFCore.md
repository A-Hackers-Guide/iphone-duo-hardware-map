# `AVDelegatingPlaybackCoordinator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlaybackCoordinator`
- 21 instance variables, 2 properties, 48 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigTimelineCoordinator=} _figTimelineCoordinator;
@"NSObject<OS_dispatch_queue>" _timelineControlQueue;
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
@"NSObject<OS_dispatch_queue>" _figTimelineCoordinatorConfigQueue;
@"NSObject<OS_dispatch_queue>" _currentItemIDConfigQueue;
@"<AVPlaybackCoordinatorPlaybackControlDelegate>" _delegate;
@ _suspensionsChangedNotificationToken;
@ _participantsChangedNotificationToken;
@ _didIssueCommandToPlaybackObjectNotificationToken;
@"NSMutableArray" _suspensionReasons;
@"NSMutableArray" _otherParticipants;
@"NSMutableDictionary" _controlStates;
@"NSMutableDictionary" _participantStates;
@"NSMutableDictionary" _participantLimitPerSuspensionReason;
@"NSMutableArray" _suspensionReasonsThatTriggerWaiting;
@"NSMutableArray" _waitingPoliciesArray;
B _pauseSnapsToMediaTimeOfOriginator;
@"NSString" _currentItemIdentifier;
@"<AVPlaybackCoordinationMediumDelegate>" _coordinationMediumDelegate;
B _isInExpanseMediaPlayback;
@"NSString" _mediumLoggingIdentifier;
```

## Properties

```
@property (T@"<AVPlaybackCoordinatorPlaybackControlDelegate>",R,W,N) playbackControlDelegate;
@property (T@"NSString",R,N) currentItemIdentifier;
```

## Instance methods

```
-[AVDelegatingPlaybackCoordinator participantLimitForWaitingOutSuspensionsWithReason:];
-[AVDelegatingPlaybackCoordinator _updateParticipantStateDictionaryWithParticipantState:];
-[AVDelegatingPlaybackCoordinator _updateSuspensionReasons:];
-[AVDelegatingPlaybackCoordinator handleRemovalOfParticipant:];
-[AVDelegatingPlaybackCoordinator _updateWaitingPoliciesArray:withPolicies:];
-[AVDelegatingPlaybackCoordinator setPauseSnapsToMediaTimeOfOriginator:];
-[AVDelegatingPlaybackCoordinator dealloc];
-[AVDelegatingPlaybackCoordinator mediumLoggingIdentifier];
-[AVDelegatingPlaybackCoordinator participantForIdentifier:];
-[AVDelegatingPlaybackCoordinator handleReplacementParticipantStateDictionaries:];
-[AVDelegatingPlaybackCoordinator otherParticipants];
-[AVDelegatingPlaybackCoordinator _endSuspension:proposingNewTime:];
-[AVDelegatingPlaybackCoordinator _endSuspension:];
-[AVDelegatingPlaybackCoordinator _updateTransportControlStateDictionaryWithTransportControlState:];
-[AVDelegatingPlaybackCoordinator coordinationMediumDelegate];
-[AVDelegatingPlaybackCoordinator suspensionReasonsThatTriggerWaiting];
-[AVDelegatingPlaybackCoordinator setCoordinationMediumDelegate:];
-[AVDelegatingPlaybackCoordinator expectedItemTimeAtHostTime:];
-[AVDelegatingPlaybackCoordinator _setIsInExpanseMediaPlaybackOnAVAudioSession];
-[AVDelegatingPlaybackCoordinator suspensionReasons];
-[AVDelegatingPlaybackCoordinator avfParticipantsForFigParticipantsUUIDs:];
-[AVDelegatingPlaybackCoordinator _removeUnusedTransportControlStates];
-[AVDelegatingPlaybackCoordinator pauseSnapsToMediaTimeOfOriginator];
-[AVDelegatingPlaybackCoordinator handleNewTransportControlStateDictionary:];
-[AVDelegatingPlaybackCoordinator trackedTransportControlStateDictionaries];
-[AVDelegatingPlaybackCoordinator setSuspensionReasonsThatTriggerWaiting:];
-[AVDelegatingPlaybackCoordinator setParticipantLimit:forWaitingOutSuspensionsWithReason:];
-[AVDelegatingPlaybackCoordinator handleNewParticipantStateDictionary:];
-[AVDelegatingPlaybackCoordinator beginSuspensionForReason:];
-[AVDelegatingPlaybackCoordinator _currentWaitingPoliciesArray];
-[AVDelegatingPlaybackCoordinator _updateOtherParticipantsUsingFigParticipantUUIDs:];
-[AVDelegatingPlaybackCoordinator setMediumLoggingIdentifier:];
-[AVDelegatingPlaybackCoordinator _participantStateForIdentifier:];
-[AVDelegatingPlaybackCoordinator _figTimelineCoordinatorConfigQueue];
-[AVDelegatingPlaybackCoordinator _prepareToInitiatePlayback];
-[AVDelegatingPlaybackCoordinator _removeParticipantStateWithIdentifier:];
-[AVDelegatingPlaybackCoordinator _replaceParticipantStates:];
-[AVDelegatingPlaybackCoordinator _setWaitingPolicies:];
-[AVDelegatingPlaybackCoordinator _transportControlStateForItemIdentifier:];
-[AVDelegatingPlaybackCoordinator applyFigPauseSnapsToMediaTimeOfOriginator];
-[AVDelegatingPlaybackCoordinator coordinateRateChangeToRate:options:];
-[AVDelegatingPlaybackCoordinator coordinateSeekToTime:options:];
-[AVDelegatingPlaybackCoordinator currentItemIdentifier];
-[AVDelegatingPlaybackCoordinator initWithPlaybackControlDelegate:];
-[AVDelegatingPlaybackCoordinator participantStates];
-[AVDelegatingPlaybackCoordinator playbackControlDelegate];
-[AVDelegatingPlaybackCoordinator reapplyCurrentItemStateToPlaybackControlDelegate];
-[AVDelegatingPlaybackCoordinator transitionToItemWithIdentifier:proposingInitialTimingBasedOnTimebase:];
```
