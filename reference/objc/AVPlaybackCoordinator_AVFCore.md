# `AVPlaybackCoordinator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 2 properties, 17 instance methods, 1 class methods

## Properties

```
@property (T@"NSArray",R,N) otherParticipants;
@property (T@"NSArray",R,N) suspensionReasons;
```

## Class methods

```
+[AVPlaybackCoordinator initialize];
```

## Instance methods

```
-[AVPlaybackCoordinator participantLimitForWaitingOutSuspensionsWithReason:];
-[AVPlaybackCoordinator init];
-[AVPlaybackCoordinator initInternal];
-[AVPlaybackCoordinator setPauseSnapsToMediaTimeOfOriginator:];
-[AVPlaybackCoordinator otherParticipants];
-[AVPlaybackCoordinator isDefunct];
-[AVPlaybackCoordinator _endSuspension:proposingNewTime:];
-[AVPlaybackCoordinator _endSuspension:];
-[AVPlaybackCoordinator _removeSuspension:];
-[AVPlaybackCoordinator suspensionReasonsThatTriggerWaiting];
-[AVPlaybackCoordinator expectedItemTimeAtHostTime:];
-[AVPlaybackCoordinator suspensionReasons];
-[AVPlaybackCoordinator pauseSnapsToMediaTimeOfOriginator];
-[AVPlaybackCoordinator setSuspensionReasonsThatTriggerWaiting:];
-[AVPlaybackCoordinator setParticipantLimit:forWaitingOutSuspensionsWithReason:];
-[AVPlaybackCoordinator beginSuspensionForReason:];
-[AVPlaybackCoordinator _currentWaitingPoliciesArray];
```
