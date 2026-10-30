# `BKSTouchStream`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _displayUUID;
I _contextID;
C _identifier;
B _shouldSendAmbiguityRecommendations;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_waitingOnServerHandshake;
@"BSServiceInitiatingConnection" _connection;
@"NSNumber" _lock_pendingEventDispatchMode;
@"NSNumber" _lock_pendingAmbiguityRecommendation;
@"NSNumber" _lock_pendingLastTouchTimestamp;
@"BSAtomicSignal" _invalidSignal;
```

## Instance methods

```
-[BKSTouchStream invalidate];
-[BKSTouchStream initWithContextID:displayUUID:identifier:policy:];
-[BKSTouchStream setEventDispatchMode:ambiguityRecommendation:lastTouchTimestamp:];
-[BKSTouchStream setEventDispatchMode:lastTouchTimestamp:];
-[BKSTouchStream _lock_flushInitialStateToServer];
-[BKSTouchStream _configureServerConnectionWithFactory:];
-[BKSTouchStream initWithContextID:displayUUID:identifier:policy:connectionFactory:];
```
