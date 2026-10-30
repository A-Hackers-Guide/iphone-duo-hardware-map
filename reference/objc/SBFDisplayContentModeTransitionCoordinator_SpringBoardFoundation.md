# `SBFDisplayContentModeTransitionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 10 instance variables, 7 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _preflightActions;
@"NSMutableArray" _updateProgressActions;
@"NSMutableArray" _displayContentModeWillChangeActions;
@"NSMutableArray" _displayContentModeChangedActions;
@"NSMutableArray" _displayContentModeDidChangeActions;
@"NSMutableArray" _postflightActions;
@"SBFDisplayContentModeTransitionLockProvider" _lockProvider;
@"NSMapTable" _participantSignpostNames;
@"SBFDisplayContentModeResolver" _resolver;
@"SBFDisplayContentModeTransitionContext" _currentContext;
```

## Properties

```
@property (TB,R,N,GisLocked) locked;
@property (T@"SBFDisplayContentModeResolver",R,W,N,V_resolver) resolver;
@property (T@"SBFDisplayContentModeTransitionContext",R,N,V_currentContext) currentContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFDisplayContentModeTransitionCoordinator resolver];
-[SBFDisplayContentModeTransitionCoordinator isLocked];
-[SBFDisplayContentModeTransitionCoordinator currentContext];
-[SBFDisplayContentModeTransitionCoordinator debugDescription];
-[SBFDisplayContentModeTransitionCoordinator succinctDescription];
-[SBFDisplayContentModeTransitionCoordinator description];
-[SBFDisplayContentModeTransitionCoordinator appendDescriptionToStream:];
-[SBFDisplayContentModeTransitionCoordinator _acquireContinuationLockProviderForReason:continuationHandler:];
-[SBFDisplayContentModeTransitionCoordinator _applyContinuousFoldValuesFromPose:mechanicalAngleDegrees:continuousFoldEffectProgress:];
-[SBFDisplayContentModeTransitionCoordinator _applyDisplayContentModeChangeWithContinuationHandler:];
-[SBFDisplayContentModeTransitionCoordinator _completeTransitionWithContinuationHandler:];
-[SBFDisplayContentModeTransitionCoordinator _invalidateLocksThatShouldNoLongerBeHeld];
-[SBFDisplayContentModeTransitionCoordinator _notifyOfDisplayContentModeChangedWithContinuationHandler:];
-[SBFDisplayContentModeTransitionCoordinator _notifyOfInteractiveProgressForLockExemptParticipantsWithPose:mechanicalAngleDegrees:continuousFoldEffectProgress:];
-[SBFDisplayContentModeTransitionCoordinator _notifyOfInteractiveProgressWithPose:continuationHandler:];
-[SBFDisplayContentModeTransitionCoordinator _runContentModeChangeActions:reason:continuationHandler:];
-[SBFDisplayContentModeTransitionCoordinator _shouldHoldLockWithOptions:];
-[SBFDisplayContentModeTransitionCoordinator _signpostNameForParticipant:];
-[SBFDisplayContentModeTransitionCoordinator _startTransitionWithPose:mechanicalAngleDegrees:continuousFoldEffectProgress:continuationHandler:];
-[SBFDisplayContentModeTransitionCoordinator _updateProgressIgnoringLockWithPose:mechanicalAngleDegrees:continuousFoldEffectProgress:];
-[SBFDisplayContentModeTransitionCoordinator _updateProgressOfTransitionWithPose:mechanicalAngleDegrees:continuousFoldEffectProgress:];
-[SBFDisplayContentModeTransitionCoordinator addDisplayContentModeChangedHandler:];
-[SBFDisplayContentModeTransitionCoordinator addDisplayContentModeChangedHandlerFromParticipant:handler:];
-[SBFDisplayContentModeTransitionCoordinator addDisplayContentModeChangedHandlerFromParticipant:phase:handler:];
-[SBFDisplayContentModeTransitionCoordinator addDisplayContentModeDidChangeHandlerFromParticipant:handler:];
-[SBFDisplayContentModeTransitionCoordinator addDisplayContentModeWillChangeHandlerFromParticipant:handler:];
-[SBFDisplayContentModeTransitionCoordinator addInteractiveProgressHandler:];
-[SBFDisplayContentModeTransitionCoordinator addInteractiveProgressHandlerFromParticipant:handler:];
-[SBFDisplayContentModeTransitionCoordinator addInteractiveProgressHandlerFromParticipant:phase:handler:];
-[SBFDisplayContentModeTransitionCoordinator addPostflightActions:];
-[SBFDisplayContentModeTransitionCoordinator addPostflightActionsFromParticipant:actions:];
-[SBFDisplayContentModeTransitionCoordinator addPostflightActionsFromParticipant:phase:actions:];
-[SBFDisplayContentModeTransitionCoordinator addPreflightActions:];
-[SBFDisplayContentModeTransitionCoordinator addPreflightActionsFromParticipant:actions:];
-[SBFDisplayContentModeTransitionCoordinator addPreflightActionsFromParticipant:phase:actions:];
-[SBFDisplayContentModeTransitionCoordinator initWithResolver:context:];
```
