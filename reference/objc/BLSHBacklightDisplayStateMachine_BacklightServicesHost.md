# `BLSHBacklightDisplayStateMachine`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSDisplayStateDelegate`, `BLSHWatchdogDelegate`
- 23 instance variables, 11 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<BLSHWatchdogInvalidatable>" _watchdogTimer;
@"BLSHTTRWatchdog" _liveRenderingTTRWatchdog;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHBacklightOSInterfaceProviding>" _osInterface;
@"<BLSHOSDisplayInterfaceProviding>" _display;
i _lock_sequenceNumber;
{?="sequenceNumber"i"displayMode"q"previousDisplayMode"q"duration"d"startSeconds"d"phase"q} _lock_displayRampOperation;
q _lock_prewarmingDisplayMode;
q _lock_lastSteadyStateDisplayMode;
q _lock_completedCBDisplayMode;
{?="sequenceNumber"i"cbDisplayMode"q"previousCBDisplayMode"q"duration"d"fullDuration"d"startSeconds"d"effectiveStartSeconds"d"phase"q"shouldWait"B} _lock_cbDisplayModeTransitionOperation;
{?="sequenceNumber"i"cbFlipbookState"q"phase"q"startTimestamp"Q} _lock_cbFlipbookStateChangeOperation;
q _lock_completedCBFlipbookState;
{?="sequenceNumber"i"caDisplayState"q"phase"q"startTimestamp"Q} _lock_caDisplayStateChangeOperation;
q _lock_completedCADisplayState;
@"<BLSCADisplayPowerAssertion>" _lock_caDisplayPowerAssertion;
@"<BLSHSystemActivityAsserting>" _lock_liveRenderingSystemActivityAssertion;
Q _lock_prewarmingDisplayMode_startTimestamp;
B _lock_isPrewarmingDisplayMode;
B _lock_highLuminanceAlwaysOn;
Q _stateHandler;
@"NSString" _displayLoggingName;
@"<BLSHBacklightDisplayStateMachineDelegate>" _delegate;
```

## Properties

```
@property (T@"<BLSHBacklightDisplayStateMachineDelegate>",R,W,N,V_delegate) delegate;
@property (Tq,R,N) displayMode;
@property (Tq,R,N) lastSteadyStateDisplayMode;
@property (TB,R,N,GisTransitioningDisplayMode) transitioningDisplayMode;
@property (TB,N,GisHighLuminanceAlwaysOn) highLuminanceAlwaysOn;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,?,N,SsetCBTransitionsDelayForTesting:) cbTransitionsDelayForTesting;
@property (Td,?,N,SsetCATransitionsDelayForTesting:) caTransitionsDelayForTesting;
```

## Instance methods

```
-[BLSHBacklightDisplayStateMachine setHighLuminanceAlwaysOn:];
-[BLSHBacklightDisplayStateMachine identifier];
-[BLSHBacklightDisplayStateMachine dealloc];
-[BLSHBacklightDisplayStateMachine displayMode];
-[BLSHBacklightDisplayStateMachine isHighLuminanceAlwaysOn];
-[BLSHBacklightDisplayStateMachine abortContextForTimer:];
-[BLSHBacklightDisplayStateMachine delegate];
-[BLSHBacklightDisplayStateMachine description];
-[BLSHBacklightDisplayStateMachine osInterfaceProvider];
-[BLSHBacklightDisplayStateMachine display:didCompleteSwitchToCBFlipbookState:withError:];
-[BLSHBacklightDisplayStateMachine display:didCompleteTransitionToCADisplayState:currentState:transitionStatus:];
-[BLSHBacklightDisplayStateMachine display:didCompleteTransitionToCBDisplayMode:withError:];
-[BLSHBacklightDisplayStateMachine initForDisplay:delegate:platformProvider:osInterfaceProvider:];
-[BLSHBacklightDisplayStateMachine isTransitioningDisplayMode];
-[BLSHBacklightDisplayStateMachine lastSteadyStateDisplayMode];
-[BLSHBacklightDisplayStateMachine prewarmForDisplayMode:];
-[BLSHBacklightDisplayStateMachine resumeDisplayMode:];
-[BLSHBacklightDisplayStateMachine setDisplayMode:withRampDuration:];
```
