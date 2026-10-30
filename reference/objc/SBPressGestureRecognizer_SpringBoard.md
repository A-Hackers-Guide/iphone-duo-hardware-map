# `SBPressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 14 instance variables, 1 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"NSSet" _delayablePressTypes;
@"NSSet" _precedencePressTypes;
q _internalGestureState;
@"NSMutableArray" _delayedPressesInfo;
d _latestDispatchedPressTimestamp;
q _latestDispatchedPressPhase;
q _latestDispatchedPressType;
B _latestDispatchedPressWasLongClick;
@"NSMutableArray" _unbalancedPressBeganTypes;
@"BSAbsoluteMachTimer" _waitingGestureStateExpirationTimer;
B _isDispatchingPresses;
@"BSAbsoluteMachTimer" _waitingForPreemptionTimer;
d _precedencePressesTime;
d _waitForPreemptionTimeInterval;
```

## Properties

```
@property (T@"NSArray",&,N) pressTypesWithPrecedence;
```

## Instance methods

```
-[SBPressGestureRecognizer _updatePublicPressInfo:];
-[SBPressGestureRecognizer _applyGestureStateInfo:];
-[SBPressGestureRecognizer _waitGestureStateExpirationWithFireInterval:timerExpiredActionBlock:];
-[SBPressGestureRecognizer _didGestureBegin];
-[SBPressGestureRecognizer latestPressType];
-[SBPressGestureRecognizer latestPressWasLongClick];
-[SBPressGestureRecognizer _isDispatchingDelayedPresses];
-[SBPressGestureRecognizer _startDispatchingDelayedPresses];
-[SBPressGestureRecognizer waitForPreemptionTimeInterval];
-[SBPressGestureRecognizer _gestureStateInfoForPressInfo:];
-[SBPressGestureRecognizer _resetPublishedPressInfo];
-[SBPressGestureRecognizer _resetState];
-[SBPressGestureRecognizer setAllowedPressTypes:];
-[SBPressGestureRecognizer _processDelayablePresses:];
-[SBPressGestureRecognizer pressesCancelled:withEvent:];
-[SBPressGestureRecognizer pressTypesWithPrecedence];
-[SBPressGestureRecognizer requiredPressTypesCount];
-[SBPressGestureRecognizer pressesEnded:withEvent:];
-[SBPressGestureRecognizer _updateUnbalancedPressBeganTypesWithCurrentPressType:andPhase:result:];
-[SBPressGestureRecognizer dealloc];
-[SBPressGestureRecognizer _resetDelayedPresses];
-[SBPressGestureRecognizer _isGestureFailedOrCancelled];
-[SBPressGestureRecognizer latestPressPhase];
-[SBPressGestureRecognizer _delayedPressesCount];
-[SBPressGestureRecognizer reset];
-[SBPressGestureRecognizer _cancelGesture];
-[SBPressGestureRecognizer _addDelayedPress:];
-[SBPressGestureRecognizer _shouldStopDispatching];
-[SBPressGestureRecognizer setPressTypesWithPrecedence:];
-[SBPressGestureRecognizer _reallyStartDispatchingDelayedPresses];
-[SBPressGestureRecognizer _stopWaitingGestureStateExpiration];
-[SBPressGestureRecognizer initWithTarget:action:];
-[SBPressGestureRecognizer _allowedPressTypes];
-[SBPressGestureRecognizer gestureStateInfoForUnbalancedPressBeganCount:previousCount:];
-[SBPressGestureRecognizer _processPrecedencePresses:];
-[SBPressGestureRecognizer pressesBegan:withEvent:];
-[SBPressGestureRecognizer pressesChanged:withEvent:];
-[SBPressGestureRecognizer processPresses:];
-[SBPressGestureRecognizer latestPressTimestamp];
-[SBPressGestureRecognizer setWaitForPreemptionTimeInterval:];
-[SBPressGestureRecognizer name];
```
