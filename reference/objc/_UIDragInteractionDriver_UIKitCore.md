# `_UIDragInteractionDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIDragInteractionDriving`
- 18 instance variables, 23 properties, 46 instance methods, 0 class methods

## Instance variables

```
{_UIDragInteractionDriverStateMachine="state"Q"eventsQueueEnd"^Q} _stateMachine;
{CAPoint3D="x"d"y"d"z"d} _initialLocationInWindow;
B _enabled;
B _additionalTouchesCancelLift;
B _allowsSimultaneousRecognitionDuringLift;
B _shouldAnimateLift;
B _cancellationTimerEnabled;
B _competingLongPressOnLift;
B _automaticallyAddsFailureRelationships;
@"<_UIDragInteractionDriverDelegate>" _delegate;
@"UIView" _view;
d _liftDelay;
d _cancellationDelay;
d _competingLongPressDelay;
d _liftMoveHysteresis;
@"NSArray" _allowedTouchTypes;
@? _itemUpdater;
@"UIGestureRecognizer" _gestureRecognizerForDragInitiation;
```

## Properties

```
@property (TB,N,V_shouldAnimateLift) shouldAnimateLift;
@property (T{CGPoint=dd},N) initialLocationInWindow;
@property (T@"UIGestureRecognizer",R,N,V_gestureRecognizerForDragInitiation) gestureRecognizerForDragInitiation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_UIDragInteractionDriverDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",W,N,V_view) view;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (Td,N,V_liftDelay) liftDelay;
@property (Td,N,V_liftMoveHysteresis) liftMoveHysteresis;
@property (TB,N,V_additionalTouchesCancelLift) additionalTouchesCancelLift;
@property (TB,N,V_competingLongPressOnLift) competingLongPressOnLift;
@property (TB,N,V_allowsSimultaneousRecognitionDuringLift) allowsSimultaneousRecognitionDuringLift;
@property (Td,N,V_cancellationDelay) cancellationDelay;
@property (Td,N,V_competingLongPressDelay) competingLongPressDelay;
@property (TB,N,V_cancellationTimerEnabled) cancellationTimerEnabled;
@property (TB,N,V_automaticallyAddsFailureRelationships) automaticallyAddsFailureRelationships;
@property (T@"NSArray",C,N,V_allowedTouchTypes) allowedTouchTypes;
@property (T@?,R,C,N,V_itemUpdater) itemUpdater;
@property (TB,R,N,GisActive) active;
@property (T@"<UIDragInteractionEffect>",?,R,N) interactionEffect;
```

## Instance methods

```
-[_UIDragInteractionDriver setCancellationTimerEnabled:];
-[_UIDragInteractionDriver setLiftMoveHysteresis:];
-[_UIDragInteractionDriver initialLocationInWindow];
-[_UIDragInteractionDriver gestureRecognizerForDragInitiation];
-[_UIDragInteractionDriver detachFromView:];
-[_UIDragInteractionDriver _state];
-[_UIDragInteractionDriver didTransitionToInactiveState];
-[_UIDragInteractionDriver liftDelay];
-[_UIDragInteractionDriver liftMoveHysteresis];
-[_UIDragInteractionDriver allowedTouchTypes];
-[_UIDragInteractionDriver setAdditionalTouchesCancelLift:];
-[_UIDragInteractionDriver shouldAnimateLift];
-[_UIDragInteractionDriver setShouldAnimateLift:];
-[_UIDragInteractionDriver cancellationDelay];
-[_UIDragInteractionDriver didTransitionToPreparing];
-[_UIDragInteractionDriver setCompetingLongPressOnLift:];
-[_UIDragInteractionDriver competingLongPressDelay];
-[_UIDragInteractionDriver didTransitionToDeferred];
-[_UIDragInteractionDriver itemUpdater];
-[_UIDragInteractionDriver additionalTouchesCancelLift];
-[_UIDragInteractionDriver setAllowedTouchTypes:];
-[_UIDragInteractionDriver attachToView:];
-[_UIDragInteractionDriver competingLongPressOnLift];
-[_UIDragInteractionDriver cancellationTimerEnabled];
-[_UIDragInteractionDriver didTransitionToCancelState];
-[_UIDragInteractionDriver setInitialLocationInWindow:];
-[_UIDragInteractionDriver setCompetingLongPressDelay:];
-[_UIDragInteractionDriver isGestureRecognizerForDragInitiation:];
-[_UIDragInteractionDriver didTransitionToInflightState];
-[_UIDragInteractionDriver setCancellationDelay:];
-[_UIDragInteractionDriver setAutomaticallyAddsFailureRelationships:];
-[_UIDragInteractionDriver setAllowsSimultaneousRecognitionDuringLift:];
-[_UIDragInteractionDriver _handleEvent:];
-[_UIDragInteractionDriver init];
-[_UIDragInteractionDriver automaticallyAddsFailureRelationships];
-[_UIDragInteractionDriver setLiftDelay:];
-[_UIDragInteractionDriver allowsSimultaneousRecognitionDuringLift];
-[_UIDragInteractionDriver setView:];
-[_UIDragInteractionDriver didTransitionToBeginState];
-[_UIDragInteractionDriver isEnabled];
-[_UIDragInteractionDriver view];
-[_UIDragInteractionDriver setDelegate:];
-[_UIDragInteractionDriver setEnabled:];
-[_UIDragInteractionDriver delegate];
-[_UIDragInteractionDriver isActive];
-[_UIDragInteractionDriver cancel];
```
