# `_UIFeedbackEngine`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 9 properties, 68 instance methods, 7 class methods

## Instance variables

```
@"NSMutableDictionary" _completionBlocks;
@"NSTimer" _suspensionTimer;
B _suspended;
@"NSTimer" _springBoardTimer;
B _enabled;
q _prewarmCount;
q _state;
Q _numberOfClients;
@"NSMapTable" _playerDequeueBlocks;
Q _backgroundTaskIdentifier;
q _suspensionState;
```

## Properties

```
@property (Tq,N,V_prewarmCount) prewarmCount;
@property (TB,N,GisEnabled,S_setEnabled:,V_enabled) enabled;
@property (Tq,N,G_state,S_setState:,V_state) state;
@property (TQ,R,N,V_numberOfClients) numberOfClients;
@property (T@"NSMapTable",&,N,G_playerDequeueBlocks,S_setPlayerDequeueBlocks:,V_playerDequeueBlocks) playerDequeueBlocks;
@property (TQ,N,G_backgroundTaskIdentifier,S_setBackgroundTaskIdentifier:,V_backgroundTaskIdentifier) backgroundTaskIdentifier;
@property (Tq,R,N,G_suspensionState,V_suspensionState) suspensionState;
@property (Td,R,N) currentTime;
@property (T@"NSString",R,N) _stats_key;
```

## Class methods

```
+[_UIFeedbackEngine _internalQueue];
+[_UIFeedbackEngine sharedEngine];
+[_UIFeedbackEngine _supportsPlayingIndividualFeedback:];
+[_UIFeedbackEngine _supportsAbortingDeactivation];
+[_UIFeedbackEngine _supportsPlayingFeedback:];
+[_UIFeedbackEngine _supportsPlayingFeedbackPatternsDirectly];
+[_UIFeedbackEngine engineForFeedback:];
```

## Instance methods

```
-[_UIFeedbackEngine _applicationDidBecomeActive:];
-[_UIFeedbackEngine _state];
-[_UIFeedbackEngine _stats_key];
-[_UIFeedbackEngine _deactivate];
-[_UIFeedbackEngine _setState:];
-[_UIFeedbackEngine _setEnabled:];
-[_UIFeedbackEngine init];
-[_UIFeedbackEngine _internal_startWarmingFeedbacks:];
-[_UIFeedbackEngine currentTime];
-[_UIFeedbackEngine numberOfClients];
-[_UIFeedbackEngine _internal_cooldownUnderlyingPlayerIfPossibleWithCompletion:];
-[_UIFeedbackEngine isEnabled];
-[_UIFeedbackEngine _internal_updateSuspension];
-[_UIFeedbackEngine _internal_activateUnderlyingPlayerWithCompletion:];
-[_UIFeedbackEngine _internal_prewarmUnderlyingPlayerWithCompletion:];
-[_UIFeedbackEngine _applicationWillResignActive:];
-[_UIFeedbackEngine _applicationWillSuspend:];
-[_UIFeedbackEngine _internal_dequeueReusableFeedbackPlayerWithCompletionBlock:];
-[_UIFeedbackEngine description];
-[_UIFeedbackEngine _internal_stopWarmingFeedbacks:];
-[_UIFeedbackEngine _internal_teardownUnderlyingPlayerIfPossibleWithCompletion:];
-[_UIFeedbackEngine _internal_performAtState:block:];
-[_UIFeedbackEngine _activate:andPerformWhenRunning:];
-[_UIFeedbackEngine _activationCountStatistics];
-[_UIFeedbackEngine _activationDurationStatistics];
-[_UIFeedbackEngine _applicationDidResume:];
-[_UIFeedbackEngine _backgroundTaskIdentifier];
-[_UIFeedbackEngine _cooldown];
-[_UIFeedbackEngine _dequeueReusableFeedbackPlayerWithCompletionBlock:];
-[_UIFeedbackEngine _hostDidEnterBackground:];
-[_UIFeedbackEngine _hostWillEnterForeground:];
-[_UIFeedbackEngine _internal_activate:andPerformWhenRunning:];
-[_UIFeedbackEngine _internal_activateEngine];
-[_UIFeedbackEngine _internal_cooldown];
-[_UIFeedbackEngine _internal_cooldownEngineIfPossible];
-[_UIFeedbackEngine _internal_deactivate];
-[_UIFeedbackEngine _internal_deactivateEngineIfPossible];
-[_UIFeedbackEngine _internal_isSuspended];
-[_UIFeedbackEngine _internal_playFeedbackData:atTime:feedback:effectiveFeedbackType:existingPlayer:withCompletionBlock:];
-[_UIFeedbackEngine _internal_prewarm:andPerformWhenPrewarmed:];
-[_UIFeedbackEngine _internal_prewarmEngine];
-[_UIFeedbackEngine _internal_serviceBlocksForState:withSuccess:];
-[_UIFeedbackEngine _internal_setSuspended:];
-[_UIFeedbackEngine _internal_setupBackgroundTask];
-[_UIFeedbackEngine _internal_teardownBackgroundTask];
-[_UIFeedbackEngine _internal_willCancelFeedback:];
-[_UIFeedbackEngine _internal_willPlayFeedback:atTime:];
-[_UIFeedbackEngine _outOfChannelsCountStatistics];
-[_UIFeedbackEngine _playFeedback:atTime:withCompletionBlock:];
-[_UIFeedbackEngine _playerDequeueBlocks];
-[_UIFeedbackEngine _prewarm:andPerformWhenPrewarmed:];
-[_UIFeedbackEngine _prewarmCountStatistics];
-[_UIFeedbackEngine _prewarmDurationStatistics];
-[_UIFeedbackEngine _remoteViewControllerWillDisconnect:];
-[_UIFeedbackEngine _sb_stuckInNonInactiveState];
-[_UIFeedbackEngine _setBackgroundTaskIdentifier:];
-[_UIFeedbackEngine _setPlayerDequeueBlocks:];
-[_UIFeedbackEngine _setSuspended:];
-[_UIFeedbackEngine _startWarmingFeedbacks:];
-[_UIFeedbackEngine _statsSuffix];
-[_UIFeedbackEngine _stats_outOfChannels];
-[_UIFeedbackEngine _stats_stateDidChangeFrom:to:];
-[_UIFeedbackEngine _stopWarmingFeedbacks:];
-[_UIFeedbackEngine _suspendEngineNow];
-[_UIFeedbackEngine _suspensionState];
-[_UIFeedbackEngine prewarmCount];
-[_UIFeedbackEngine runWhenReady:];
-[_UIFeedbackEngine setPrewarmCount:];
```
