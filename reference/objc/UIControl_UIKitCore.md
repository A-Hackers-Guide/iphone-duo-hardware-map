# `UIControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIVariableGestureContextMenuInteractionDelegate`, `UIPointerInteractionDelegate`, `UIContextMenuInteractionDelegate_Private`, `UIContextMenuInteractionDelegate`
- 5 instance variables, 38 properties, 145 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _targetActions;
{CGPoint="x"d"y"d} _previousPoint;
d _downTime;
{?="disabled"b1"tracking"b1"touchInside"b1"touchDragged"b1"requiresDisplayOnTracking"b1"highlighted"b1"dontHighlightOnTouchDown"b1"allowActionsToQueue"b1"pendingUnhighlight"b1"selected"b1"verticalAlignment"b3"horizontalAlignment"b3"wasLastHighlightSuccessful"b1"touchHasHighlighted"b1"enableSymbolAnimations"b1"hasPointerInteraction"b1"hasProxyPointerInteraction"b1"hasContextMenuInteraction"b1"highlightForMenuPresentation"b1"showsMenuFromSource"b1"currentlyDeferringFinalActions"b1"wasTouchInside"b1} _controlFlags;
q _requiredButtonMask;
```

## Properties

```
@property (Tq,R,N) effectiveContentVerticalAlignment;
@property (TB,R,N,G_deferFinalActions) deferFinalActions;
@property (T@"NSArray",R,N,G_additionalTrackingViews) additionalTrackingViews;
@property (TB,R,N,G_wasTouchInside) wasTouchInside;
@property (TB,N,S_setHasActiveMenuPresentation:) _hasActiveMenuPresentation;
@property (T@"NSArray",R,N) _allTargetActions;
@property (T@"UIPointerInteraction",R,N) pointerInteraction;
@property (TB,N,GisPointerInteractionEnabled) pointerInteractionEnabled;
@property (T@"UIPointerInteraction",R,N) _pointerInteraction;
@property (T@"UIPointerInteraction",&,N,S_setProxyPointerInteraction:) _proxyPointerInteraction;
@property (T@,W,N,S_setProxySender:) _proxySender;
@property (TB,N,GisContextMenuEnabled) contextMenuEnabled;
@property (TB,N) contextMenuIsPrimary;
@property (TB,N) showsMenuFromSource;
@property (Tq,N,S_setRequiredButtonMask:,V_requiredButtonMask) _requiredButtonMask;
@property (TB,N,S_setEnableSymbolAnimations:) _enableSymbolAnimations;
@property (TB,R,N) _allowsSymbolAnimations;
@property (TB,D,N,GisEnabled) enabled;
@property (TB,D,N,GisSelected) selected;
@property (TB,D,N,GisHighlighted) highlighted;
@property (Tq,D,N) contentVerticalAlignment;
@property (Tq,D,N) contentHorizontalAlignment;
@property (Tq,R,N) effectiveContentHorizontalAlignment;
@property (TQ,R,D,N) state;
@property (TB,R,D,N,GisTracking) tracking;
@property (TB,R,D,N,GisTouchInside) touchInside;
@property (T@"NSSet",R,N) allTargets;
@property (TQ,R,N) allControlEvents;
@property (T@"UIContextMenuInteraction",R,N) contextMenuInteraction;
@property (TB,N,GisContextMenuInteractionEnabled) contextMenuInteractionEnabled;
@property (TB,N) showsMenuAsPrimaryAction;
@property (T@"NSString",C,N) toolTip;
@property (T@"UIToolTipInteraction",R,N) toolTipInteraction;
@property (TB,N,GisSymbolAnimationEnabled) symbolAnimationEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIControl _allowActionsToQueue];
+[UIControl _primaryStateForState:];
```

## Instance methods

```
-[UIControl _controlEventsForActionTriggered];
-[UIControl cancelTouchTracking];
-[UIControl touchesEnded:withEvent:];
-[UIControl setContentVerticalAlignment:];
-[UIControl contextMenuInteraction:willEndForConfiguration:animator:];
-[UIControl addAction:forControlEvents:];
-[UIControl setSelected:];
-[UIControl _systemDefaultFocusGroupIdentifier];
-[UIControl contextMenuInteraction:previewForDismissingMenuWithConfiguration:];
-[UIControl touchesCancelled:withEvent:];
-[UIControl pointerInteraction:styleForRegion:];
-[UIControl contextMenuInteraction:configurationForMenuAtLocation:];
-[UIControl _cancelDelayedActions];
-[UIControl setTracking:];
-[UIControl isHighlighted];
-[UIControl cancelTrackingWithEvent:];
-[UIControl setContextMenuIsPrimary:];
-[UIControl _proxySender];
-[UIControl endTrackingWithTouch:withEvent:];
-[UIControl continueTrackingWithTouch:withEvent:];
-[UIControl _focusedSound];
-[UIControl contextMenuInteraction:previewForHighlightingMenuWithConfiguration:];
-[UIControl menuAttachmentPointForConfiguration:];
-[UIControl hitTest:withEvent:];
-[UIControl contextMenuInteraction:willDisplayMenuForConfiguration:animator:];
-[UIControl _didMoveFromWindow:toWindow:];
-[UIControl beginTrackingWithTouch:withEvent:];
-[UIControl touchesBegan:withEvent:];
-[UIControl touchesMoved:withEvent:];
-[UIControl canBecomeFocused];
-[UIControl isEnabled];
-[UIControl _setProxySender:];
-[UIControl isTracking];
-[UIControl setHighlighted:];
-[UIControl isPointerInteractionEnabled];
-[UIControl contextMenuInteraction];
-[UIControl pointerInteraction];
-[UIControl _contextMenuInteraction:configuration:interactionEffectForTargetedPreview:];
-[UIControl setEnabled:];
-[UIControl sendAction:];
-[UIControl encodeWithCoder:];
-[UIControl isSelected];
-[UIControl pointerInteraction:regionForRequest:defaultRegion:];
-[UIControl setPointerInteractionEnabled:];
-[UIControl _willMoveToWindow:];
-[UIControl initWithCoder:];
-[UIControl canBecomeFirstResponder];
-[UIControl setContentHorizontalAlignment:];
-[UIControl initWithFrame:];
-[UIControl cancelMouseTracking];
-[UIControl _contextMenuInteraction:styleForMenuWithConfiguration:];
-[UIControl state];
-[UIControl touchesEstimatedPropertiesUpdated:];
-[UIControl isContextMenuInteractionEnabled];
-[UIControl _diagnoseFocusabilityForReport:];
-[UIControl _wasTouchInside];
-[UIControl toolTip];
-[UIControl __distributionStatisticsForUserInteractionDuration];
-[UIControl __scalarStatisticsForUserTouchUpInsideEvent];
-[UIControl __scalarStatisticsForUserValueChangedEvent];
-[UIControl _accessibilityShouldActivateOnHUDLift];
-[UIControl _activateForAccessibilityHUDLiftAtPoint:];
-[UIControl _addControlTargetAction:];
-[UIControl _additionalTrackingViews];
-[UIControl _allTargetActions];
-[UIControl _allowsSymbolAnimations];
-[UIControl _beginInteractionDurationStatisticMeasurements];
-[UIControl _clippedHighlightBounds];
-[UIControl _commitInteractionDurationStatisticMeasurements];
-[UIControl _commonInitForPrimaryAction:];
-[UIControl _connectInterfaceBuilderEventConnection:];
-[UIControl _contextMenuInteraction];
-[UIControl _contextMenuInteraction:willBeginWithConfiguration:];
-[UIControl _createPointerInteraction];
-[UIControl _deferFinalActions];
-[UIControl _delayActions];
-[UIControl _distributionStatisticsForUserInteractionDuration];
-[UIControl _enableSymbolAnimations];
-[UIControl _hasActionForEventMask:];
-[UIControl _hasActiveMenuPresentation];
-[UIControl _highlightCornerRadius];
-[UIControl _incrementStatisticsForUserActionForEvents:];
-[UIControl _invalidatePointerInteraction];
-[UIControl _pointerInteraction];
-[UIControl _providesCustomPointerInteraction];
-[UIControl _proxyPointerInteraction];
-[UIControl _registerCustomHoverStylePointerDriverIfNeeded];
-[UIControl _requiredButtonMask];
-[UIControl _scalarStatisticsForUserTouchUpInsideEvent];
-[UIControl _scalarStatisticsForUserValueChangedEvent];
-[UIControl _sceneDraggingBehaviorOnPan];
-[UIControl _sendActionsForEvents:withEvent:];
-[UIControl _sendDelayedActions];
-[UIControl _sendDelayedActions:];
-[UIControl _setEnableSymbolAnimations:];
-[UIControl _setHasActiveMenuPresentation:];
-[UIControl _setHighlightOnMouseDown:];
-[UIControl _setImplicitHoverStyle:];
-[UIControl _setLastHighlightSuccessful:];
-[UIControl _setProxyPointerInteraction:];
-[UIControl _setRequiredButtonMask:];
-[UIControl _setTouchHasHighlighted:];
-[UIControl _stateForFocusUpdateContext:];
-[UIControl _touchHasHighlighted];
-[UIControl _unhighlight];
-[UIControl _wasLastHighlightSuccessful];
-[UIControl actionsForTarget:forControlEvent:];
-[UIControl addTarget:action:forControlEvents:];
-[UIControl addTarget:action:forEvents:];
-[UIControl allControlEvents];
-[UIControl allTargets];
-[UIControl contentHorizontalAlignment];
-[UIControl contentVerticalAlignment];
-[UIControl contextMenuIsPrimary];
-[UIControl effectiveContentHorizontalAlignment];
-[UIControl effectiveContentVerticalAlignment];
-[UIControl enumerateEventHandlers:];
-[UIControl hasOneOrMoreTargets];
-[UIControl hitTest:forEvent:];
-[UIControl initWithFrame:primaryAction:];
-[UIControl isContextMenuEnabled];
-[UIControl isSymbolAnimationEnabled];
-[UIControl isTouchInside];
-[UIControl performPrimaryAction];
-[UIControl pointMostlyInside:withEvent:];
-[UIControl removeAction:forControlEvents:];
-[UIControl removeActionForIdentifier:forControlEvents:];
-[UIControl removeTarget:action:forControlEvents:];
-[UIControl removeTarget:forEvents:];
-[UIControl requiresDisplayOnTracking];
-[UIControl sendAction:to:forEvent:];
-[UIControl sendActionsForControlEvents:];
-[UIControl setContextMenuEnabled:];
-[UIControl setContextMenuInteractionEnabled:];
-[UIControl setHoverStyle:];
-[UIControl setRequiresDisplayOnTracking:];
-[UIControl setShowsMenuAsPrimaryAction:];
-[UIControl setShowsMenuFromSource:];
-[UIControl setSymbolAnimationEnabled:];
-[UIControl setToolTip:];
-[UIControl shouldTrack];
-[UIControl showsMenuAsPrimaryAction];
-[UIControl showsMenuFromSource];
-[UIControl toolTipInteraction];
-[UIControl touchDragged];
```
