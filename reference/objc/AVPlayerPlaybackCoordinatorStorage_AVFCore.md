# `AVPlayerPlaybackCoordinatorStorage`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" rwQueue;
@"NSMutableDictionary" controlStates;
@"NSMutableDictionary" participantStates;
@"NSMutableDictionary" participantLimitPerSuspensionReason;
@"NSMutableArray" suspensionReasonsThatTriggerWaiting;
B pauseSnapsToMediaTimeOfOriginator;
@"NSMutableArray" waitingPoliciesArray;
@"NSUUID" localParticipantUUID;
@"<AVPlayerPlaybackCoordinatorDelegate>" delegate;
@"<AVPlaybackCoordinationMediumDelegate>" coordinationMediumDelegate;
@"NSString" mediumLoggingIdentifier;
@"AVPlaybackCoordinationMedium" playbackCoordinationMedium;
@"NSMutableDictionary" currentLamportTimestampForIdentifier;
```

## Instance methods

```
-[AVPlayerPlaybackCoordinatorStorage init];
-[AVPlayerPlaybackCoordinatorStorage dealloc];
```
