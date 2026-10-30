# `_UIDragInteractionLongPressDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDragInteractionDriver`
- Protocols: `UIGestureRecognizerDelegate`
- 6 instance variables, 7 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"UIDelayedAction" _gateTimer;
@"UIDelayedAction" _cancellationTimer;
@"_UIDragLiftGestureRecognizer" _gestureRecognizerForDragInitiation;
Q _behavior;
@"_UIRelationshipGestureRecognizer" _gestureRecognizerForFailureRelationship;
@"_UIRelationshipGestureRecognizer" _gestureRecognizerForExclusionRelationship;
```

## Properties

```
@property (T@"_UIRelationshipGestureRecognizer",R,N,V_gestureRecognizerForFailureRelationship) gestureRecognizerForFailureRelationship;
@property (T@"_UIRelationshipGestureRecognizer",R,N,V_gestureRecognizerForExclusionRelationship) gestureRecognizerForExclusionRelationship;
@property (TQ,R,N,V_behavior) behavior;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDragInteractionLongPressDriver setLiftMoveHysteresis:];
-[_UIDragInteractionLongPressDriver gestureRecognizerForDragInitiation];
-[_UIDragInteractionLongPressDriver detachFromView:];
-[_UIDragInteractionLongPressDriver didTransitionToInactiveState];
-[_UIDragInteractionLongPressDriver hasMoveHysteresisBeenReached];
-[_UIDragInteractionLongPressDriver _gestureRecognizerFailed:];
-[_UIDragInteractionLongPressDriver didTransitionToPreparing];
-[_UIDragInteractionLongPressDriver didTransitionToDeferred];
-[_UIDragInteractionLongPressDriver setAllowedTouchTypes:];
-[_UIDragInteractionLongPressDriver attachToView:];
-[_UIDragInteractionLongPressDriver didTransitionToCancelState];
-[_UIDragInteractionLongPressDriver isGestureRecognizerForDragInitiation:];
-[_UIDragInteractionLongPressDriver didTransitionToInflightState];
-[_UIDragInteractionLongPressDriver setAutomaticallyAddsFailureRelationships:];
-[_UIDragInteractionLongPressDriver gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UIDragInteractionLongPressDriver initWithBehavior:];
-[_UIDragInteractionLongPressDriver gestureRecognizer:shouldReceiveTouch:];
-[_UIDragInteractionLongPressDriver hasExceededAllowableMovement];
-[_UIDragInteractionLongPressDriver gestureRecognizerForExclusionRelationship];
-[_UIDragInteractionLongPressDriver openCompetingGestureRecognizerGateCancelingGestures:];
-[_UIDragInteractionLongPressDriver init];
-[_UIDragInteractionLongPressDriver setLiftDelay:];
-[_UIDragInteractionLongPressDriver reset];
-[_UIDragInteractionLongPressDriver gestureRecognizerForFailureRelationship];
-[_UIDragInteractionLongPressDriver dragInitiationGestureStateChanged:];
-[_UIDragInteractionLongPressDriver didTransitionToBeginState];
-[_UIDragInteractionLongPressDriver invalidateCancellationTimer];
-[_UIDragInteractionLongPressDriver behavior];
-[_UIDragInteractionLongPressDriver gestureRecognizerShouldBegin:];
-[_UIDragInteractionLongPressDriver translationInWindow];
-[_UIDragInteractionLongPressDriver gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UIDragInteractionLongPressDriver gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIDragInteractionLongPressDriver _dragInitiationGestureStateChanged:];
-[_UIDragInteractionLongPressDriver _updateLiftMoveHysteresisInDragInitiationGesture];
-[_UIDragInteractionLongPressDriver _wantsTimeDelayedFailureRequirementGate];
-[_UIDragInteractionLongPressDriver shouldDelayCompetingGestureRecognizer:];
-[_UIDragInteractionLongPressDriver openGateCancelingAddItemsGestures];
-[_UIDragInteractionLongPressDriver canExcludeCompetingGestureRecognizer:];
-[_UIDragInteractionLongPressDriver _gateCompetingGestureRecognizers];
-[_UIDragInteractionLongPressDriver invalidateCompetingGestureRecognizerGateTimer];
```
