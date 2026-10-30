# `UIDragInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIViewInternalDraggingSourceDelegate`, `_UIDragInteractionDriverDelegate`, `_UIDragInteractionSessionRelinquishing`, `_UIVisualStyleStylable`, `UIInteraction`
- 30 instance variables, 28 properties, 114 instance methods, 3 class methods

## Instance variables

```
B _didSetEnabled;
B _enabled;
@"_UIDragSessionImpl" _preliminarySession;
@"_UIDragSessionImpl" _sessionForAddingItems;
@"UIDragInteractionContextImpl" _interactionContext;
@"_UIDragAddItemsGesture" _gestureRecognizerForAddingItems;
@"<_UIDragInteractionDefaultDriverProvider>" _defaultDriverProvider;
{?="itemsForBeginningSession"b1"previewForLiftingItem"b1"willAnimateLiftWithAnimator"b1"sessionWillBegin"b1"sessionAllowsMoveOperation"b1"sessionIsRestrictedToDraggingApplication"b1"prefersFullSizePreviewsForSession"b1"sessionDidMove"b1"willEndWithOperation"b1"didEndWithOperation"b1"sessionDidTransferItems"b1"itemsForAddingToSession"b1"sessionForAddingItems"b1"willAddItems"b1"previewForCancellingItem"b1"willAnimateCancelWithAnimator"b1"viewToSnapshotItem"b1"allowsDragOverridingMasterSwitch"b1"prepareForSession"b1"liftAnimationDidChangeDirection"b1"didCancelLiftWithoutDragging"b1"shouldDelayCompetingGestureRecognizer"b1"canExcludeCompetingGestureRecognizer"b1"competingGestureRecognizerShouldDelayLift"b1"dataOwnerForSession"b1"dataOwnerForAddingToSession"b1"sessionSupportsSystemDrag"b1"customSpringAnimationBehaviorForCancellingItem"b1"sessionPropertiesForSession"b1"itemsForAddingToSessionAsync"b1"itemsForAddingToSession3D"b1"sessionForAddingItems3D"b1"dynamicallyUpdatesPrefersFullSizePreviews"b1"shouldBecomeDraggingSourceDelegate"b1"delayForLiftBeginningAtLocation"b1} _delegateImplements;
{?="previewForCancellingItem"b1"willAnimateCancelWithAnimator"b1"sessionDidEnd"b1} _presentationDelegateImplements;
B _allowsSimultaneousRecognitionDuringLift;
B _allowsPointerDragBeforeLiftDelay;
B _cancellationTimerEnabled;
B _competingLongPressOnLift;
B _automaticallyAddsFailureRelationships;
B _allowsMultipleSessions;
B _additionalTouchesCancelLift;
@"<UIDragInteractionDelegate>" _delegate;
Q _liftBehavior;
@"UIView" _view;
@"NSSet" _initiationDrivers;
@"<_UIDragInteractionPresentationDelegate>" _presentationDelegate;
@"<UIDragInteractionEffect>" _interactionEffect;
d _liftDelay;
d _pointerLiftDelay;
d _cancellationDelay;
d _competingLongPressDelay;
d _liftMoveHysteresis;
d _pointerLiftMoveHysteresis;
q _addItemsGestureConfiguration;
@"NSArray" _allowedTouchTypes;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"NSSet",&,N,G_initiationDrivers,S_setInitiationDrivers:,V_initiationDrivers) initiationDrivers;
@property (T@"<_UIDragInteractionPresentationDelegate>",W,N,G_presentationDelegate,S_setPresentationDelegate:,V_presentationDelegate) presentationDelegate;
@property (T@"<UIDragInteractionEffect>",&,N,V_interactionEffect) interactionEffect;
@property (Td,N,G_liftDelay,S_setLiftDelay:,V_liftDelay) liftDelay;
@property (Td,N,G_pointerLiftDelay,S_setPointerLiftDelay:,V_pointerLiftDelay) pointerLiftDelay;
@property (TB,N,G_isCancellationTimerEnabled,S_setCancellationTimerEnabled:,V_cancellationTimerEnabled) cancellationTimerEnabled;
@property (Td,N,G_cancellationDelay,S_setCancellationDelay:,V_cancellationDelay) cancellationDelay;
@property (TB,N,G_competingLongPressOnLift,S_setCompetingLongPressOnLift:,V_competingLongPressOnLift) competingLongPressOnLift;
@property (Td,N,G_competingLongPressDelay,S_setCompetingLongPressDelay:,V_competingLongPressDelay) competingLongPressDelay;
@property (Td,N,G_liftMoveHysteresis,S_setLiftMoveHysteresis:,V_liftMoveHysteresis) liftMoveHysteresis;
@property (Td,N,G_pointerLiftMoveHysteresis,S_setPointerLiftMoveHysteresis:,V_pointerLiftMoveHysteresis) pointerLiftMoveHysteresis;
@property (TB,N,S_setAllowsPointerDragBeforeLiftDelay:) _allowsPointerDragBeforeLiftDelay;
@property (TB,N,G_automaticallyAddsFailureRelationships,S_setAutomaticallyAddsFailureRelationships:,V_automaticallyAddsFailureRelationships) automaticallyAddsFailureRelationships;
@property (TB,N,G_allowsMultipleSessions,S_setAllowsMultipleSessions:,V_allowsMultipleSessions) allowsMultipleSessions;
@property (Tq,N,G_addItemsGestureConfiguration,S_setAddItemsGestureConfiguration:,V_addItemsGestureConfiguration) addItemsGestureConfiguration;
@property (TB,N,G_additionalTouchesCancelLift,S_setAdditionalTouchesCancelLift:,V_additionalTouchesCancelLift) additionalTouchesCancelLift;
@property (T@"NSArray",C,N,G_allowedTouchTypes,S_setAllowedTouchTypes:,V_allowedTouchTypes) allowedTouchTypes;
@property (TB,R,N,G_isActive) isActive;
@property (T@"<UIDragInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_allowsSimultaneousRecognitionDuringLift) allowsSimultaneousRecognitionDuringLift;
@property (TB,N,V_allowsPointerDragBeforeLiftDelay) allowsPointerDragBeforeLiftDelay;
@property (TQ,N,V_liftBehavior) liftBehavior;
@property (TB,N,GisEnabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIDragInteraction isEnabledByDefault];
+[UIDragInteraction visualStyleRegistryIdentity];
+[UIDragInteraction _cancelAllDrags];
```

## Instance methods

```
-[UIDragInteraction _allowedTouchTypes];
-[UIDragInteraction _queryDelegate:forItemsForBeginningSession:];
-[UIDragInteraction _liftDelay];
-[UIDragInteraction dragDriver:shouldDelayCompetingGestureRecognizer:];
-[UIDragInteraction dragDriverCancelLift:];
-[UIDragInteraction liftDelay];
-[UIDragInteraction _itemsToDragFromView:];
-[UIDragInteraction _sessionDidMove:];
-[UIDragInteraction _queryDelegate:forLiftPreviewsUsingItems:session:];
-[UIDragInteraction _setAllowsPointerDragBeforeLiftDelay:];
-[UIDragInteraction _accessibilityPrepareForDragAtPoint:completion:];
-[UIDragInteraction _cancelDrag];
-[UIDragInteraction _gestureRecognizerFailed:];
-[UIDragInteraction _updateInteractionEffectWithContext:notifyDelegate:];
-[UIDragInteraction _immediatelyBeginDragWithTouch:completion:];
-[UIDragInteraction dragDriver:canExcludeCompetingGestureRecognizer:];
-[UIDragInteraction _prepareForSession:completion:];
-[UIDragInteraction _setPresentationDelegate:];
-[UIDragInteraction _cancellationDelay];
-[UIDragInteraction _pointerLiftDelay];
-[UIDragInteraction _viewFailedToDrag:];
-[UIDragInteraction _supportsAddingItemsAsynchronously];
-[UIDragInteraction _beginLiftForItems:session:animated:];
-[UIDragInteraction _relinquishPreliminaryDragSessionToAdopter:];
-[UIDragInteraction _createDefaultInitiationDrivers];
-[UIDragInteraction setAllowsSimultaneousRecognitionDuringLift:];
-[UIDragInteraction gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[UIDragInteraction dragDriverBeginLift:];
-[UIDragInteraction _allowsMultipleSessions];
-[UIDragInteraction _pointerLiftMoveHysteresis];
-[UIDragInteraction _isActive];
-[UIDragInteraction _setCancellationDelay:];
-[UIDragInteraction _isCancellationTimerEnabled];
-[UIDragInteraction initWithDelegate:];
-[UIDragInteraction _locationInView:];
-[UIDragInteraction _setAllowedTouchTypes:];
-[UIDragInteraction interactionEffect];
-[UIDragInteraction _initiationDriver];
-[UIDragInteraction _initiationDrivers];
-[UIDragInteraction _session:sourceOperationMaskForDraggingWithinApp:];
-[UIDragInteraction _setLiftDelay:];
-[UIDragInteraction _accessibilityCanAddItemsToDragSession];
-[UIDragInteraction _liftMoveHysteresis];
-[UIDragInteraction _setCompetingLongPressDelay:];
-[UIDragInteraction gestureRecognizer:shouldReceiveTouch:];
-[UIDragInteraction _additionalTouchesCancelLift];
-[UIDragInteraction _isPointerDriver:];
-[UIDragInteraction _competingLongPressOnLift];
-[UIDragInteraction _sessionDidTransferItems:];
-[UIDragInteraction dragDriver:beginDragWithTouches:itemUpdater:beginningSessionHandler:];
-[UIDragInteraction _endLiftWithoutDragging];
-[UIDragInteraction dragDriver:shouldReceiveTouch:];
-[UIDragInteraction dragDriver:shouldBeginAtLocation:];
-[UIDragInteraction _addItemsGestureConfiguration];
-[UIDragInteraction _setAutomaticallyAddsFailureRelationships:];
-[UIDragInteraction _finalizeLiftCancellation];
-[UIDragInteraction _sessionDidEnd:withOperation:];
-[UIDragInteraction setLiftBehavior:];
-[UIDragInteraction _session:willAddItems:forInteraction:];
-[UIDragInteraction _presentationDelegate];
-[UIDragInteraction _dataOwnerOfDragFromView:];
-[UIDragInteraction _viewDragSessionProperties:];
-[UIDragInteraction _handoffSession:];
-[UIDragInteraction _canDragFromView:];
-[UIDragInteraction _session:targetedPreviewForCancellingItem:duiPreview:snapshotView:container:];
-[UIDragInteraction _viewRestrictsDragToSourceApp:];
-[UIDragInteraction liftBehavior];
-[UIDragInteraction dragDriverWantsExclusionOverride:];
-[UIDragInteraction _view:willBeginDraggingWithSession:];
-[UIDragInteraction _allowsPointerDragBeforeLiftDelay];
-[UIDragInteraction _setAddItemsGestureConfiguration:];
-[UIDragInteraction _requiredContextIDsForDragSessionInView:];
-[UIDragInteraction _updateDriverParameters];
-[UIDragInteraction setInteractionEffect:];
-[UIDragInteraction _sessionPrefersFullSizePreviews:];
-[UIDragInteraction setAllowsPointerDragBeforeLiftDelay:];
-[UIDragInteraction setLiftDelay:];
-[UIDragInteraction _sessionWillEnd:withOperation:];
-[UIDragInteraction _itemsForAddingToSession:atPoint:completion:];
-[UIDragInteraction _setPointerLiftMoveHysteresis:];
-[UIDragInteraction _sessionHandedOffDragImage:];
-[UIDragInteraction _setCancellationTimerEnabled:];
-[UIDragInteraction _sessionWillBegin:];
-[UIDragInteraction dragDriver:prepareToLiftWithCompletion:];
-[UIDragInteraction _accessibilityAddItemsToDragSessionAtPoint:];
-[UIDragInteraction dragDriverCancelAddItemsGesture:];
-[UIDragInteraction _session:item:willCancelWithAnimator:];
-[UIDragInteraction allowsPointerDragBeforeLiftDelay];
-[UIDragInteraction allowsSimultaneousRecognitionDuringLift];
-[UIDragInteraction _sessionDynamicallyUpdatesPrefersFullSizePreviews:];
-[UIDragInteraction _automaticallyAddsFailureRelationships];
-[UIDragInteraction _setCompetingLongPressOnLift:];
-[UIDragInteraction _session:customSpringAnimationBehaviorForCancellingItem:];
-[UIDragInteraction _setAllowsMultipleSessions:];
-[UIDragInteraction _setLiftMoveHysteresis:];
-[UIDragInteraction setDragCancellationDelay:];
-[UIDragInteraction _setPointerLiftDelay:];
-[UIDragInteraction _delegateRespondsToAddingItems];
-[UIDragInteraction _setInitiationDrivers:];
-[UIDragInteraction _cancelLift];
-[UIDragInteraction dragDriver:shouldBeginAtLocation3D:];
-[UIDragInteraction dragDriver:competingGestureRecognizerShouldDelayLift:];
-[UIDragInteraction _competingLongPressDelay];
-[UIDragInteraction _setAdditionalTouchesCancelLift:];
-[UIDragInteraction setView:];
-[UIDragInteraction isEnabled];
-[UIDragInteraction view];
-[UIDragInteraction gestureRecognizerShouldBegin:];
-[UIDragInteraction setEnabled:];
-[UIDragInteraction willMoveToView:];
-[UIDragInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[UIDragInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIDragInteraction delegate];
-[UIDragInteraction didMoveToView:];
```
