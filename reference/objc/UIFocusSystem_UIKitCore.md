# `UIFocusSystem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusMovementPerformerDelegate`, `_UIFocusEnvironmentInternal`, `_UIFocusEnvironmentPrivate`
- 22 instance variables, 34 properties, 116 instance methods, 6 class methods

## Instance variables

```
@"_UIFocusUpdateRequest" _pendingFocusUpdateRequest;
@"<UIFocusItem>" _deferredFocusUpdateTarget;
@"<UIFocusEnvironment>" _appearingFocusEnvironment;
@"<UIFocusEnvironment>" _disappearingFocusEnvironment;
@"NSHashTable" _focusItemAncestorCache;
@"NSTimer" _hasSeenFocusedItemDidExpireTimer;
{?="hasReceivedTeardownNotification"b1"shouldIgnoreFocusUpdateIfNeeded"b1"isPendingFocusRestoration"b1"isPostponingUpdates"b1"hasSeenFocusedItem"b1"isInsideUpdateFocusIfNeeded"b1"delegateRespondsToTopEnvironment"b1"delegateRespondsToPreferredFocusEnvironments"b1"delegateRespondsToOverridingPreferredFocusEnvironment"b1"delegateRespondsToShouldRestoreFocusInContext"b1"delegateRespondsToWillUpdateFocusInContext"b1"delegateRespondsToDidUpdateFocusInContext"b1"delegateRespondsToDidFinishUpdatingFocusInContext"b1"delegateRespondsToWillMessageOldFocusNodes"b1"delegateRespondsToWillMessageNewFocusNodes"b1"delegateRespondsToEnvironmentDidUpdateFocusInContext"b1"delegateRespondsToDidCancelFocusUpdateInContext"b1"delegateRespondsToFocusItemContainer"b1"delegateRespondsToClippingRect"b1"delegateRespondsToDidUpdateDeferralTarget"b1"delegateRespondsToHandleFailedMovementRequest"b1"delegateRespondsToShouldReverseLayoutDirectionForEnvironment"b1"delegateRespondsToShouldReverseLinearWrappingForEnvironment"b1"delegateRespondsToIsScrollingScrollableContainer"b1} _flags;
B _waitingForFocusMovementAction;
B _enabled;
@"_UIFocusMovementPerformer" _movementPerformer;
@"<UIFocusItem>" _focusedItem;
@"_UIFocusGroupHistory" _focusGroupHistory;
@"_UIFocusEnvironmentPreferenceCache" _deepestPreferredFocusableItemCacheForCurrentUpdate;
@"<UIFocusEnvironment>" _deepestPreferredFocusEnvironment;
@"UIFocusMovementAction" _pendingFocusMovementAction;
@"_UIFocusUpdateThrottle" _updateThrottle;
@"_UIFocusTreeLock" _treeLock;
@"<_UIFocusBehavior>" _behavior;
@"<_UIFocusSystemDelegate>" _delegate;
@"<UIFocusItem>" _previousFocusedItem;
@"NSNumber" _overrideFocusDeferralBehavior;
@"<_UIFocusCasting>" _focusCasting;
```

## Properties

```
@property (T@"UIFocusSystem",R,W,N,G_preferredFirstResponderFocusSystem) preferredFirstResponderFocusSystem;
@property (T@"UIResponder",R,W,N,G_preferredFirstResponder) preferredFirstResponder;
@property (TB,N,V_waitingForFocusMovementAction) waitingForFocusMovementAction;
@property (T@"UIFocusMovementAction",&,N,V_pendingFocusMovementAction) pendingFocusMovementAction;
@property (T@"_UIFocusUpdateThrottle",R,N,V_updateThrottle) updateThrottle;
@property (T@"_UIFocusTreeLock",R,N,V_treeLock) treeLock;
@property (T@"_UIFocusMovementPerformer",R,N,V_movementPerformer) _movementPerformer;
@property (T@"_UIFocusGroupHistory",R,N,G_focusGroupHistory,V_focusGroupHistory) focusGroupHistory;
@property (T@"<UIFocusEnvironment>",R,N,G_disappearingFocusEnvironment) disappearingFocusEnvironment;
@property (T@"_UIFocusEnvironmentPreferenceCache",R,N,V_deepestPreferredFocusableItemCacheForCurrentUpdate) _deepestPreferredFocusableItemCacheForCurrentUpdate;
@property (T@"<_UIFocusBehavior>",&,N,V_behavior) behavior;
@property (T@"<_UIFocusSystemDelegate>",W,N,V_delegate) delegate;
@property (TB,N,G_isEnabled,S_setEnabled:,V_enabled) enabled;
@property (T@"UIFocusSystem",R,W,N,G_hostFocusSystem) hostFocusSystem;
@property (T@"<UIFocusItem>",R,W,N,G_previousFocusedItem,V_previousFocusedItem) previousFocusedItem;
@property (T@"<UIFocusEnvironment>",R,W,N,V_deepestPreferredFocusEnvironment) _deepestPreferredFocusEnvironment;
@property (T@"NSNumber",&,N,G_overrideFocusDeferralBehavior,S_setOverrideFocusDeferralBehavior:,V_overrideFocusDeferralBehavior) overrideFocusDeferralBehavior;
@property (T@"<_UIFocusCasting>",&,N,G_focusCasting,S_setFocusCasting:,V_focusCasting) focusCasting;
@property (T@"<UIFocusItem>",R,W,N) _focusedItemOrDeferralTarget;
@property (T@"<UIFocusItem>",R,W,N,V_focusedItem) focusedItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_UIFocusRegionContainer>",?,R,W,N,G_focusMapContainer) focusMapContainer;
@property (TB,?,R,N,G_isEligibleForFocusInteraction) eligibleForFocusInteraction;
@property (TB,?,R,N,G_isEligibleForFocusOcclusion) eligibleForFocusOcclusion;
@property (Tq,?,R,N,G_preferredFocusMovementStyle) preferredFocusMovementStyle;
@property (T@"NSArray",?,R,C,N,G_linearFocusMovementSequences) linearFocusMovementSequences;
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusEnvironment>",R,W,N) parentFocusEnvironment;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
```

## Class methods

```
+[UIFocusSystem initialize];
+[UIFocusSystem registerURL:forSoundIdentifier:];
+[UIFocusSystem _allFocusSystems];
+[UIFocusSystem _focusSystemForEnvironment:];
+[UIFocusSystem environment:containsEnvironment:];
+[UIFocusSystem focusSystemForEnvironment:];
```

## Instance methods

```
-[UIFocusSystem _isEligibleForFocusInteraction];
-[UIFocusSystem _prefersFocusContainment];
-[UIFocusSystem updateFocusIfNeeded];
-[UIFocusSystem _setEnabled:];
-[UIFocusSystem _isEnabled];
-[UIFocusSystem init];
-[UIFocusSystem didUpdateFocusInContext:withAnimationCoordinator:];
-[UIFocusSystem setNeedsFocusUpdate];
-[UIFocusSystem parentFocusEnvironment];
-[UIFocusSystem focusItemContainer];
-[UIFocusSystem setDelegate:];
-[UIFocusSystem setBehavior:];
-[UIFocusSystem behavior];
-[UIFocusSystem delegate];
-[UIFocusSystem _isEligibleForFocusOcclusion];
-[UIFocusSystem description];
-[UIFocusSystem preferredFocusEnvironments];
-[UIFocusSystem shouldUpdateFocusInContext:];
-[UIFocusSystem _overridingPreferredFocusEnvironment];
-[UIFocusSystem _effectiveFocusDeferralBehavior];
-[UIFocusSystem _focusEnvironmentWillDisappear:];
-[UIFocusSystem _startDeferringFocusIfSupported];
-[UIFocusSystem _clearDeferredFocusUpdateTarget];
-[UIFocusSystem _clippingRectInCoordinateSpace:];
-[UIFocusSystem _contextForUpdateToEnvironment:];
-[UIFocusSystem _topEnvironment];
-[UIFocusSystem _updateFocusWithContext:report:];
-[UIFocusSystem _buildFocusItemAncestorCacheIfNecessary];
-[UIFocusSystem _cancelPendingFocusRestoration];
-[UIFocusSystem _clearFocusItemAncestorCache];
-[UIFocusSystem _closestFocusableItemToPoint:inEnvironment:constrainedToRect:distanceMeasuringUnitPoint:itemFilter:];
-[UIFocusSystem _configureFocusDeferralIfNecessaryForContext:report:];
-[UIFocusSystem _contextForFocusMovement:];
-[UIFocusSystem _contextForUpdateToEnvironment:allowsOverridingPreferedFocusEnvironments:allowsDeferral:];
-[UIFocusSystem _debug_isEnvironmentEligibleForFocusUpdate:debugReport:];
-[UIFocusSystem _deepestPreferredFocusEnvironment];
-[UIFocusSystem _deepestPreferredFocusableItemCacheForCurrentUpdate];
-[UIFocusSystem _didFinishUpdatingFocusInContext:];
-[UIFocusSystem _disappearingFocusEnvironment];
-[UIFocusSystem _dropFocusAndStartDeferring:suppressUpdate:];
-[UIFocusSystem _enableWithoutFocusRestoration];
-[UIFocusSystem _focusBehaviorDidChange];
-[UIFocusSystem _focusCasting];
-[UIFocusSystem _focusEnvironmentDidAppear:];
-[UIFocusSystem _focusEnvironmentDidBecomeVisible:];
-[UIFocusSystem _focusEnvironmentWillBecomeInvisible:];
-[UIFocusSystem _focusEnvironmentWillDisappear:remainingInHierarchy:];
-[UIFocusSystem _focusGroupHistory];
-[UIFocusSystem _focusItemForValidation];
-[UIFocusSystem _focusMapContainer];
-[UIFocusSystem _focusSystemIsValid];
-[UIFocusSystem _focusedItemIsContainedInEnvironment:includeSelf:];
-[UIFocusSystem _focusedItemOrDeferralTarget];
-[UIFocusSystem _handleFailedFocusMovementRequest:withPerformer:];
-[UIFocusSystem _handleFocusMovementAction:];
-[UIFocusSystem _hasSeenFocusedItemDidExpire];
-[UIFocusSystem _hasValidItemForCurrentDeferralState];
-[UIFocusSystem _hostFocusSystem];
-[UIFocusSystem _isEnvironmentEligibleForFocusUpdate:fallbackToEnvironment:debugReport:];
-[UIFocusSystem _isEnvironmentLocked:];
-[UIFocusSystem _isScrollingScrollableContainer:targetContentOffset:];
-[UIFocusSystem _lockEnvironment:];
-[UIFocusSystem _movementPerformer];
-[UIFocusSystem _notifyEnvironment:didUpdateFocusInContext:];
-[UIFocusSystem _overrideFocusDeferralBehavior];
-[UIFocusSystem _performDeferredFocusUpdateIfAvailable];
-[UIFocusSystem _performFocusMovement:];
-[UIFocusSystem _performWithoutFocusUpdates:];
-[UIFocusSystem _postsFocusUpdateNotifications];
-[UIFocusSystem _preferredFirstResponder];
-[UIFocusSystem _preferredFirstResponderFocusSystem];
-[UIFocusSystem _preferredFirstResponderFocusSystemForFocusedItem:];
-[UIFocusSystem _prefersDeferralForFocusUpdateInContext:];
-[UIFocusSystem _prepareForTeardown];
-[UIFocusSystem _previousFocusedItem];
-[UIFocusSystem _reevaluateLockedEnvironments];
-[UIFocusSystem _requestFocusUpdate:];
-[UIFocusSystem _resetFocusDeferral];
-[UIFocusSystem _safari_moveFocusToNextGroup];
-[UIFocusSystem _safari_moveFocusToPreviousGroup];
-[UIFocusSystem _sendDidUpdateFocusNotificationsInContext:];
-[UIFocusSystem _sendNotificationsForFocusUpdateInContext:usingBlock:];
-[UIFocusSystem _sendWillUpdateFocusNotificationsInContext:];
-[UIFocusSystem _setDeferredFocusUpdateTarget:];
-[UIFocusSystem _setFocusCasting:];
-[UIFocusSystem _setNeedsFocusRestoration];
-[UIFocusSystem _setOverrideFocusDeferralBehavior:];
-[UIFocusSystem _shouldRestoreFocusInContext:];
-[UIFocusSystem _shouldReverseLayoutDirectionForEnvironment:];
-[UIFocusSystem _shouldReverseLinearWrappingForEnvironment:];
-[UIFocusSystem _simulatedNonDeferredProgrammaticFocusUpdateToEnvironment:];
-[UIFocusSystem _tickHasSeenFocusedItemTimer:];
-[UIFocusSystem _uiktest_disableFocusDeferral];
-[UIFocusSystem _uiktest_disableThrottle];
-[UIFocusSystem _uiktest_performFocusMovement:withSearchInfo:];
-[UIFocusSystem _uiktest_setPreviousFocusedItem:];
-[UIFocusSystem _uiktest_updateFocusToItem:];
-[UIFocusSystem _unlockEnvironment:];
-[UIFocusSystem _updateFocusImmediatelyToEnvironment:];
-[UIFocusSystem _updateFocusImmediatelyToEnvironment:startDeferringOnLostFocus:suppressLostFocusUpdate:];
-[UIFocusSystem _updateFocusImmediatelyWithContext:];
-[UIFocusSystem _updateFocusUpdateThrottle];
-[UIFocusSystem _updateWantsTreeLocking];
-[UIFocusSystem _validatedAppearingFocusEnvironmentRequest];
-[UIFocusSystem _validatedPendingFocusUpdateRequest];
-[UIFocusSystem focusedItem];
-[UIFocusSystem initWithFocusBehavior:];
-[UIFocusSystem initWithFocusBehavior:enabled:];
-[UIFocusSystem invalidateFocusItemContainer:];
-[UIFocusSystem pendingFocusMovementAction];
-[UIFocusSystem requestFocusUpdateToEnvironment:];
-[UIFocusSystem setPendingFocusMovementAction:];
-[UIFocusSystem setWaitingForFocusMovementAction:];
-[UIFocusSystem treeLock];
-[UIFocusSystem updateThrottle];
-[UIFocusSystem waitingForFocusMovementAction];
```
