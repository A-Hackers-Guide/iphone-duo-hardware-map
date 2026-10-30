# `UITextRefinementInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextInteraction`
- Protocols: `_UITextLoupeResponderProxyDelegate`
- 9 instance variables, 8 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"UIDelayedAction" _delayedLoupeAction;
@"UIDelayedAction" _delayedSelectionAction;
B _hasPerformedInteraction;
{CGPoint="x"d"y"d} _initialPointFromPreviousInteraction;
B _triggeredByLongPress;
@"UITextGestureTuning" _gestureTuning;
q _inheritedGranularity;
@"<UITextRefinementInteractionBehaviorDelegate>" _behaviorDelegate;
@"_UITextLoupeResponderProxy" _responderProxy;
```

## Properties

```
@property (T@"_UITextLoupeResponderProxy",&,N,V_responderProxy) responderProxy;
@property (Tq,N,V_inheritedGranularity) inheritedGranularity;
@property (TB,N,V_triggeredByLongPress) triggeredByLongPress;
@property (TB,N) shouldUseLineThreshold;
@property (TB,N) strongerBiasAgainstUp;
@property (T@"UIResponder",R,N) responder;
@property (T@"UITextGestureTuning",R,N,V_gestureTuning) gestureTuning;
@property (T@"<UITextRefinementInteractionBehaviorDelegate>",&,N,V_behaviorDelegate) behaviorDelegate;
```

## Instance methods

```
-[UITextRefinementInteraction finishSetup];
-[UITextRefinementInteraction responderProxy];
-[UITextRefinementInteraction setResponderProxy:];
-[UITextRefinementInteraction gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[UITextRefinementInteraction willBeginExternalGesture];
-[UITextRefinementInteraction touchAlignedPointForPoint:translation:];
-[UITextRefinementInteraction gestureTuning];
-[UITextRefinementInteraction updateInitialPoint:];
-[UITextRefinementInteraction loupeGesture:];
-[UITextRefinementInteraction setBehaviorDelegate:];
-[UITextRefinementInteraction inheritedGranularity];
-[UITextRefinementInteraction initWithBehaviorDelegate:];
-[UITextRefinementInteraction _processGestureForCustomHighlighter:];
-[UITextRefinementInteraction canBeginDragCursor:];
-[UITextRefinementInteraction responder];
-[UITextRefinementInteraction setStrongerBiasAgainstUp:];
-[UITextRefinementInteraction _createGestureTuningIfNecessary];
-[UITextRefinementInteraction _shouldAllowEnforcedTouchTypeForTouch:forGestureRecognizer:];
-[UITextRefinementInteraction pointIfPlacedCarefully:];
-[UITextRefinementInteraction _performGestureType:state:location:locationOfFirstTouch:forTouchType:];
-[UITextRefinementInteraction translationIsWithinAllowableMovement:];
-[UITextRefinementInteraction delayedDisplayLoupe:];
-[UITextRefinementInteraction delayedSelectionAction:];
-[UITextRefinementInteraction willMoveToView:];
-[UITextRefinementInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[UITextRefinementInteraction behaviorDelegate];
-[UITextRefinementInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UITextRefinementInteraction loupeGestureWithState:location:translation:velocity:modifierFlags:shouldCancel:];
-[UITextRefinementInteraction updateVisibilityOffsetForGesture:];
-[UITextRefinementInteraction triggeredByLongPress];
-[UITextRefinementInteraction strongerBiasAgainstUp];
-[UITextRefinementInteraction delayedLoupeAction:];
-[UITextRefinementInteraction setupGestureExclusionRequirements];
-[UITextRefinementInteraction shouldUseLineThreshold];
-[UITextRefinementInteraction updateOrCancelDelayedLoupeActionWithPoint:translation:];
-[UITextRefinementInteraction setShouldUseLineThreshold:];
-[UITextRefinementInteraction cancelDelayedLoupeActionIfNecessary];
-[UITextRefinementInteraction setupDelayedLoupeActionWithInitialPoint:];
-[UITextRefinementInteraction setTriggeredByLongPress:];
-[UITextRefinementInteraction setInheritedGranularity:];
-[UITextRefinementInteraction didMoveToView:];
-[UITextRefinementInteraction canPerformAction:withSender:];
-[UITextRefinementInteraction interaction_gestureRecognizerShouldBegin:];
```
