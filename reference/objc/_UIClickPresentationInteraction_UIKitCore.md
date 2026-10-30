# `_UIClickPresentationInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIDragInteractionPresentationDelegate`, `_UIClickInteractionDriverDelegate`, `UIInteraction_Internal`, `UIGestureRecognizerDelegate`, `UIInteraction`
- 25 instance variables, 30 properties, 87 instance methods, 1 class methods

## Instance variables

```
Q _currentState;
{?="shouldBegin"B"previewForHighlightingAtLocation"B"shouldPresent"B"ended"B"activationStyle"B"asyncShouldBegin"B"shouldAllowRapidRestart"B"shouldAssociateWithDrag"B"shouldAllowDragAfterDismiss"B"liveDragPreviewForPresentation"B"previewForCancellingDragItem"B"willAnimateDragCancelWithAnimator"B"dragSessionDidEndForItems"B"interactionEffectForTargetedPreview"B"endedForPresentation"B"shouldPlayFeedback"B"shouldPresentWithCompletion"B"shouldBeDelayedByGestureRecognizer"B"secondaryPreviews"B"shouldMaintainKeyboardAssertion"B} _delegateImplements;
q _statsPresentation;
B _activatedFeedbackGeneratorForClick;
B _shouldAllowFeedback;
B _allowSimultaneousRecognition;
B _unableToClick;
@"_UIRelationshipGestureRecognizer" _gestureRecognizerForBeginningDragRelationships;
@"_UIGravityWellEffectKey" _activeEffectKey;
@"<_UIClickPresentationInteractionDelegate>" _delegate;
@"UIView" _view;
@"UIDragInteraction" _latentAssociatedDragInteraction;
@"<_UIClickInteractionDriving>" _activeDriver;
@"NSArray" _allDrivers;
@"_UIRelationshipGestureRecognizer" _exclusionRelationshipGestureRecognizer;
@"_UIRelationshipGestureRecognizer" _failureRelationshipGestureRecognizer;
@"<_UIClickPresentationAssisting>" _presentationAssistant;
@"_UIClickPresentation" _pendingPresentation;
@"_UIClickPresentationFeedbackGenerator" _feedbackGenerator;
@"UIDragInteraction" _associatedDragInteraction;
@"NSString" _debugIdentifier;
@"NSString" _presentationTypeDebugString;
Q _fallbackDriverStyle;
@"NSArray" _overrideDrivers;
{CAPoint3D="x"d"y"d"z"d} _initialLocation;
```

## Properties

```
@property (T@"UIDragInteraction",&,N,V_latentAssociatedDragInteraction) latentAssociatedDragInteraction;
@property (T@"<_UIClickInteractionDriving>",&,N,V_activeDriver) activeDriver;
@property (T@"NSArray",&,N,V_allDrivers) allDrivers;
@property (T@"_UIRelationshipGestureRecognizer",&,N,V_exclusionRelationshipGestureRecognizer) exclusionRelationshipGestureRecognizer;
@property (T@"_UIRelationshipGestureRecognizer",&,N,V_failureRelationshipGestureRecognizer) failureRelationshipGestureRecognizer;
@property (T@"<_UIClickPresentationAssisting>",&,N,V_presentationAssistant) presentationAssistant;
@property (T@"_UIClickPresentation",&,N,V_pendingPresentation) pendingPresentation;
@property (T{CAPoint3D=ddd},N,V_initialLocation) initialLocation;
@property (T@"_UIClickPresentationFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (T@"UIDragInteraction",W,N,V_associatedDragInteraction) associatedDragInteraction;
@property (T@"UIGestureRecognizer",R,N) gestureRecognizerForFailureRelationship;
@property (T@"UIGestureRecognizer",R,N) gestureRecognizerForBeginningDragRelationships;
@property (T@"NSString",C,N,V_debugIdentifier) debugIdentifier;
@property (T@"NSString",C,N,V_presentationTypeDebugString) presentationTypeDebugString;
@property (TQ,N,V_fallbackDriverStyle) fallbackDriverStyle;
@property (TQ,R,N) activatedDriverStyle;
@property (TQ,R,N) inputPrecision;
@property (T@"NSArray",&,N,V_overrideDrivers) overrideDrivers;
@property (T@"UITargetedPreview",R,N) primaryEffectPreview;
@property (T@"NSArray",R,N) secondaryEffectPreviews;
@property (TB,R,N,G_reachedForceThreshold) reachedForceThreshold;
@property (T@"<_UIClickPresentationInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (T@"UIGestureRecognizer",R,N) gestureRecognizerForExclusionRelationship;
@property (TB,N,V_allowSimultaneousRecognition) allowSimultaneousRecognition;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
```

## Class methods

```
+[_UIClickPresentationInteraction _setDefaultDriverClasses:forIdiom:];
```

## Instance methods

```
-[_UIClickPresentationInteraction _setDelegate:];
-[_UIClickPresentationInteraction present];
-[_UIClickPresentationInteraction clickDriver:didUpdateHighlightProgress:];
-[_UIClickPresentationInteraction setDebugIdentifier:];
-[_UIClickPresentationInteraction clickDriver:didPerformEvent:];
-[_UIClickPresentationInteraction setInitialLocation:];
-[_UIClickPresentationInteraction _gestureRecognizerFailed:];
-[_UIClickPresentationInteraction inputPrecision];
-[_UIClickPresentationInteraction setFeedbackGenerator:];
-[_UIClickPresentationInteraction clickDriver:shouldBeDelayedByGestureRecognizer:];
-[_UIClickPresentationInteraction feedbackGenerator];
-[_UIClickPresentationInteraction setExclusionRelationshipGestureRecognizer:];
-[_UIClickPresentationInteraction _driverEnded];
-[_UIClickPresentationInteraction clickDriver:shouldBegin:];
-[_UIClickPresentationInteraction activatedDriverStyle];
-[_UIClickPresentationInteraction _refreshAllDrivers];
-[_UIClickPresentationInteraction _performPresentation];
-[_UIClickPresentationInteraction _isActive];
-[_UIClickPresentationInteraction debugIdentifier];
-[_UIClickPresentationInteraction initWithDelegate:];
-[_UIClickPresentationInteraction _isControlledByCC];
-[_UIClickPresentationInteraction cancelInteraction];
-[_UIClickPresentationInteraction _performWhenPossibleForPresentation:presentationActions:];
-[_UIClickPresentationInteraction _transitionedFromState:toState:];
-[_UIClickPresentationInteraction setPresentationTypeDebugString:];
-[_UIClickPresentationInteraction primaryEffectPreview];
-[_UIClickPresentationInteraction setFallbackDriverStyle:];
-[_UIClickPresentationInteraction gestureRecognizerForExclusionRelationship];
-[_UIClickPresentationInteraction setAllowSimultaneousRecognition:];
-[_UIClickPresentationInteraction _dragInteractionPresentation:item:willAnimateCancelWithAnimator:];
-[_UIClickPresentationInteraction setOverrideDrivers:];
-[_UIClickPresentationInteraction endPanInteraction];
-[_UIClickPresentationInteraction setActiveDriver:];
-[_UIClickPresentationInteraction initialLocation];
-[_UIClickPresentationInteraction _clickDragDriver];
-[_UIClickPresentationInteraction associatedDragInteraction];
-[_UIClickPresentationInteraction _attemptDragLiftAtLocation:useDefaultLiftAnimation:];
-[_UIClickPresentationInteraction dealloc];
-[_UIClickPresentationInteraction _reachedForceThreshold];
-[_UIClickPresentationInteraction failureRelationshipGestureRecognizer];
-[_UIClickPresentationInteraction activeDriver];
-[_UIClickPresentationInteraction overrideDrivers];
-[_UIClickPresentationInteraction gestureRecognizerForFailureRelationship];
-[_UIClickPresentationInteraction _prepareInteractionEffect];
-[_UIClickPresentationInteraction _cancelWithReason:alongsideActions:completion:];
-[_UIClickPresentationInteraction allowSimultaneousRecognition];
-[_UIClickPresentationInteraction _cancelAllDrivers];
-[_UIClickPresentationInteraction setPresentationAssistant:];
-[_UIClickPresentationInteraction _dragInteractionPresentation:sessionDidEnd:withoutBeginning:];
-[_UIClickPresentationInteraction _performPreviewPresentation];
-[_UIClickPresentationInteraction locationInView:];
-[_UIClickPresentationInteraction _delegate_shouldAllowDragAfterDismiss];
-[_UIClickPresentationInteraction setFailureRelationshipGestureRecognizer:];
-[_UIClickPresentationInteraction _dragInteractionPresentation:previewForCancellingItem:defaultPreview:proposedPreview:];
-[_UIClickPresentationInteraction _associateWithActiveDragInteraction];
-[_UIClickPresentationInteraction view];
-[_UIClickPresentationInteraction presentationTypeDebugString];
-[_UIClickPresentationInteraction exclusionRelationshipGestureRecognizer];
-[_UIClickPresentationInteraction pendingPresentation];
-[_UIClickPresentationInteraction beginPanInteraction];
-[_UIClickPresentationInteraction _endInteractionWithContext:];
-[_UIClickPresentationInteraction willMoveToView:];
-[_UIClickPresentationInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UIClickPresentationInteraction _clickDriverTouch];
-[_UIClickPresentationInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIClickPresentationInteraction delegate];
-[_UIClickPresentationInteraction _delegate_interactionEndedWithContext:];
-[_UIClickPresentationInteraction allDrivers];
-[_UIClickPresentationInteraction gestureRecognizerForBeginningDragRelationships];
-[_UIClickPresentationInteraction presentationAssistant];
-[_UIClickPresentationInteraction fallbackDriverStyle];
-[_UIClickPresentationInteraction setAssociatedDragInteraction:];
-[_UIClickPresentationInteraction latentAssociatedDragInteraction];
-[_UIClickPresentationInteraction setAllDrivers:];
-[_UIClickPresentationInteraction setLatentAssociatedDragInteraction:];
-[_UIClickPresentationInteraction _viewTraitCollectionDidChange:];
-[_UIClickPresentationInteraction clickDriver:shouldDelayGestureRecognizer:];
-[_UIClickPresentationInteraction secondaryEffectPreviews];
-[_UIClickPresentationInteraction _candidateInteractionsForAssociation];
-[_UIClickPresentationInteraction setPendingPresentation:];
-[_UIClickPresentationInteraction didMoveToView:];
-[_UIClickPresentationInteraction _canPerformPresentation];
-[_UIClickPresentationInteraction _driverClickedUp];
-[_UIClickPresentationInteraction _supportsRapidRestart];
-[_UIClickPresentationInteraction _driverClickedDown];
-[_UIClickPresentationInteraction beginDragIfPossibleWithTouch:];
-[_UIClickPresentationInteraction _activeEffect];
```
