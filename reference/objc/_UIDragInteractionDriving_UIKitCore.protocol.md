# `_UIDragInteractionDriving` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 18 properties, 33 instance methods, 0 class methods

## Properties

```
@property (T@"<_UIDragInteractionDriverDelegate>",W,N) delegate;
@property (T@"UIView",W,N) view;
@property (TB,N,GisEnabled) enabled;
@property (Td,N) liftDelay;
@property (Td,N) liftMoveHysteresis;
@property (TB,N) additionalTouchesCancelLift;
@property (TB,N) competingLongPressOnLift;
@property (TB,N) allowsSimultaneousRecognitionDuringLift;
@property (Td,N) cancellationDelay;
@property (Td,N) competingLongPressDelay;
@property (TB,N) cancellationTimerEnabled;
@property (TB,N) automaticallyAddsFailureRelationships;
@property (T@"NSArray",C,N) allowedTouchTypes;
@property (T@?,R,C,N) itemUpdater;
@property (T{CGPoint=dd},R,N) initialLocationInWindow;
@property (TB,R,N) shouldAnimateLift;
@property (TB,R,N,GisActive) active;
@property (T@"<UIDragInteractionEffect>",?,R,N) interactionEffect;
```

## Instance methods

```
-[_UIDragInteractionDriving setCancellationTimerEnabled:];
-[_UIDragInteractionDriving setLiftMoveHysteresis:];
-[_UIDragInteractionDriving initialLocationInWindow];
-[_UIDragInteractionDriving liftDelay];
-[_UIDragInteractionDriving liftMoveHysteresis];
-[_UIDragInteractionDriving allowedTouchTypes];
-[_UIDragInteractionDriving setAdditionalTouchesCancelLift:];
-[_UIDragInteractionDriving shouldAnimateLift];
-[_UIDragInteractionDriving cancellationDelay];
-[_UIDragInteractionDriving setCompetingLongPressOnLift:];
-[_UIDragInteractionDriving competingLongPressDelay];
-[_UIDragInteractionDriving itemUpdater];
-[_UIDragInteractionDriving additionalTouchesCancelLift];
-[_UIDragInteractionDriving setAllowedTouchTypes:];
-[_UIDragInteractionDriving competingLongPressOnLift];
-[_UIDragInteractionDriving cancellationTimerEnabled];
-[_UIDragInteractionDriving setCompetingLongPressDelay:];
-[_UIDragInteractionDriving isGestureRecognizerForDragInitiation:];
-[_UIDragInteractionDriving setCancellationDelay:];
-[_UIDragInteractionDriving setAutomaticallyAddsFailureRelationships:];
-[_UIDragInteractionDriving setAllowsSimultaneousRecognitionDuringLift:];
-[_UIDragInteractionDriving automaticallyAddsFailureRelationships];
-[_UIDragInteractionDriving setLiftDelay:];
-[_UIDragInteractionDriving allowsSimultaneousRecognitionDuringLift];
-[_UIDragInteractionDriving setView:];
-[_UIDragInteractionDriving isEnabled];
-[_UIDragInteractionDriving view];
-[_UIDragInteractionDriving setDelegate:];
-[_UIDragInteractionDriving setEnabled:];
-[_UIDragInteractionDriving delegate];
-[_UIDragInteractionDriving isActive];
-[_UIDragInteractionDriving cancel];
-[_UIDragInteractionDriving interactionEffect];
```
