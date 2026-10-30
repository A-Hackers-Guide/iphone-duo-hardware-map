# `TURepeatingActor`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _stopped;
B _currentlyPerformingAction;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _accessorLock;
@"TURepeatingAction" _currentRepeatingAction;
@"NSObject<OS_dispatch_queue>" _queue;
@"TURepeatingAction" _pendingRepeatingAction;
@? _attemptNextIterationBlock;
```

## Properties

```
@property (T{os_unfair_lock_s=I},R,N,V_accessorLock) accessorLock;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (TB,N,GisStopped,V_stopped) stopped;
@property (TB,N,GisCurrentlyPerformingAction,V_currentlyPerformingAction) currentlyPerformingAction;
@property (T@"TURepeatingAction",&,N,V_currentRepeatingAction) currentRepeatingAction;
@property (T@"TURepeatingAction",&,N,V_pendingRepeatingAction) pendingRepeatingAction;
@property (T@?,C,N,V_attemptNextIterationBlock) attemptNextIterationBlock;
@property (TB,R,N,GisRunning) running;
```

## Instance methods

```
-[TURepeatingActor isRunning];
-[TURepeatingActor accessorLock];
-[TURepeatingActor isStopped];
-[TURepeatingActor setStopped:];
-[TURepeatingActor setCurrentlyPerformingAction:];
-[TURepeatingActor attemptNextIterationBlock];
-[TURepeatingActor setAttemptNextIterationBlock:];
-[TURepeatingActor init];
-[TURepeatingActor stop];
-[TURepeatingActor queue];
-[TURepeatingActor isCurrentlyPerformingAction];
-[TURepeatingActor _beginRepeatingAction:];
-[TURepeatingActor pendingRepeatingAction];
-[TURepeatingActor _completeWithDidFinish:];
-[TURepeatingActor currentRepeatingAction];
-[TURepeatingActor setPendingRepeatingAction:];
-[TURepeatingActor beginRepeatingAction:iterations:completion:];
-[TURepeatingActor beginRepeatingAction:iterations:pauseDurationBetweenIterations:completion:];
-[TURepeatingActor _stopWithDidFinish:];
-[TURepeatingActor _attemptNextIteration];
-[TURepeatingActor _hasIterationsRemaining];
-[TURepeatingActor setCurrentRepeatingAction:];
```
