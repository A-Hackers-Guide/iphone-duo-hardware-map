# `SBIdleTimerService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ITIdleTimerStateServiceDelegate`, `SBIdleTimerIdleEventHandler`
- 12 instance variables, 6 properties, 23 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accessLock;
@"NSObject<OS_dispatch_queue>" _serviceCalloutQueue;
@"NSMutableDictionary" _lock_clientRequestConfigurations;
@"NSMutableSet" _lock_mediaPlaybackDisableReasons;
@"NSMutableArray" _access_idleExpirationHandlers;
@"NSMutableArray" _access_idleWarnHandlers;
@"NSMutableArray" _access_idleUserAttentionResetHandlers;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"ITIdleTimerStateService" _idleTimerStateService;
@"SBScreenLongevityController" _screenLongevityController;
@"<SBIdleTimerServiceDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBIdleTimerServiceDelegate>",W,N,V_delegate) delegate;
@property (T@"SBIdleTimerAggregatedClientConfiguration",R,N) aggregatedClientConfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerService _addStateCaptureHandlers];
-[SBIdleTimerService _stateCaptureDescription];
-[SBIdleTimerService dealloc];
-[SBIdleTimerService setDelegate:];
-[SBIdleTimerService delegate];
-[SBIdleTimerService aggregatedClientConfiguration];
-[SBIdleTimerService handleIdleTimerDidExpire];
-[SBIdleTimerService handleIdleTimerDidWarn];
-[SBIdleTimerService handleIdleTimerUserAttentionDidReset];
-[SBIdleTimerService _addMediaPlaybackDisableReason:];
-[SBIdleTimerService _removeConfiguration:fromArray:];
-[SBIdleTimerService _addClientRequestConfiguration:forReason:];
-[SBIdleTimerService _addConfiguration:toSortedArray:];
-[SBIdleTimerService _clientRequestConfigurations];
-[SBIdleTimerService _isMediaPlaybackClient:];
-[SBIdleTimerService _mediaPlaybackDisableReasons];
-[SBIdleTimerService _removeClientRequestConfigurationForReason:];
-[SBIdleTimerService _removeMediaPlaybackDisableReason:];
-[SBIdleTimerService acquireIdleTimerAssertionOnBehalfOfSceneWithPID:fromProcess:withConfiguration:forReason:];
-[SBIdleTimerService acquireIdleTimerAssertionWithConfiguration:fromClient:forReason:];
-[SBIdleTimerService initWithScreenLongevityController:];
-[SBIdleTimerService isDisabledByMediaPlayback];
-[SBIdleTimerService registerServices];
```
