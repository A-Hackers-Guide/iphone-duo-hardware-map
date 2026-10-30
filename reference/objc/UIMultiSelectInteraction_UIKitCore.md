# `UIMultiSelectInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIMultiSelectOneFingerPanGestureDelegate`, `_UIScrollViewScrollObserver`, `UIInteraction`
- 16 instance variables, 15 properties, 63 instance methods, 0 class methods

## Instance variables

```
B _isScrollView;
B _delegateConformsToProtocol;
@"UIKeyCommand" _extendToCellAboveCommand;
@"UIKeyCommand" _extendToCellBelowCommand;
@"UIKeyCommand" _extendToCellRightCommand;
@"UIKeyCommand" _extendToCellLeftCommand;
{?="respondsToShouldPreventDragLiftGesture"b1"respondsToShouldAllowSelectionExtensionAtPoint"b1"respondsToShouldAllowSelectionExtensionAtIndexPath"b1"respondsToShouldAllowSelectionAppendageAtPoint"b1"respondsToDidCancelMultiSelectInteraction"b1"respondsToSelectItemsWithinRect"b1"respondsToToggleSelectionWithinRect"b1"respondsToShouldStartBandSelectionAtPoint"b1"respondsToShouldShowBandForSelectionStartingAtPoint"b1"respondsToSupportsKeyboardSelectionExtension"b1"respondsToExtendSelectionInDirection"b1"respondsToChildScrollViewAtLocation"b1"respondsToShouldBeginMultiSelectInteraction"b1"respondsToWillBeginMultiSelectInteractionKeepingSelection"b1} _optionalDelegateFlags;
B _enabled;
@"_UIMultiSelectOneFingerPanGesture" _multiSelectModePan;
@"UIPanGestureRecognizer" _multiFingerPan;
@"UITapGestureRecognizer" _multiFingerTap;
@"_UISingleFingerTapExtensionGesture" _singleFingerExtensionTap;
q _activeGestureType;
@"<UIMultiSelectInteractionDelegate>" _delegate;
@"UIView" _view;
@"UIBandSelectionInteraction" _bandSelectionInteraction;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"_UIMultiSelectOneFingerPanGesture",&,N,V_multiSelectModePan) _multiSelectModePan;
@property (T@"UIPanGestureRecognizer",&,N,V_multiFingerPan) _multiFingerPan;
@property (T@"UITapGestureRecognizer",&,N,V_multiFingerTap) _multiFingerTap;
@property (T@"_UISingleFingerTapExtensionGesture",&,N,V_singleFingerExtensionTap) _singleFingerExtensionTap;
@property (T@"UIBandSelectionInteraction",&,N,V_bandSelectionInteraction) bandSelectionInteraction;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"<UIMultiSelectInteractionDelegate>",W,N,V_delegate) delegate;
@property (Td,D,N) singleTouchPanGestureHysteresis;
@property (T@"NSArray",R,N) gesturesForFailureRequirements;
@property (Tq,R,N,V_activeGestureType) activeGestureType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIMultiSelectInteraction keyCommandsForSelectionExtension];
-[UIMultiSelectInteraction _observeScrollViewDidScroll:];
-[UIMultiSelectInteraction gesturesForFailureRequirements];
-[UIMultiSelectInteraction _multiSelectModePan];
-[UIMultiSelectInteraction _isActive];
-[UIMultiSelectInteraction _didInvokeMultiSelectExtendGestureAtLocation:];
-[UIMultiSelectInteraction _multiFingerPan];
-[UIMultiSelectInteraction gestureRecognizer:shouldReceiveTouch:];
-[UIMultiSelectInteraction setSingleTouchPanGestureHysteresis:];
-[UIMultiSelectInteraction setBandSelectionInteraction:];
-[UIMultiSelectInteraction init];
-[UIMultiSelectInteraction _sendWillBeginInteractionAtPoint:keepingSelection:];
-[UIMultiSelectInteraction _currentExtensionTypeForOneFingerTapGesture:];
-[UIMultiSelectInteraction _areSelectionExtensionKeyCommandsEnabled];
-[UIMultiSelectInteraction _handleSelectionExtensionTapGesture:];
-[UIMultiSelectInteraction _triggeredLegacyPathInsteadForGestureRecognizer:velocity:shouldBegin:];
-[UIMultiSelectInteraction setView:];
-[UIMultiSelectInteraction _attemptToAutomaticallyTransitionToMultiSelectModeIfNecessaryAtPoint:withVelocity:];
-[UIMultiSelectInteraction _cancelScrollingInScrollView:];
-[UIMultiSelectInteraction _beginCommonPan:];
-[UIMultiSelectInteraction set_multiFingerPan:];
-[UIMultiSelectInteraction _singleFingerExtensionTap];
-[UIMultiSelectInteraction set_multiFingerTap:];
-[UIMultiSelectInteraction multiSelectOneFingerPanGestureShouldPreventDragInteractionGesture:];
-[UIMultiSelectInteraction _shouldBeginBandSelectionInteraction:atPoint:];
-[UIMultiSelectInteraction _isShiftKeyBeingHeldWithGesture:];
-[UIMultiSelectInteraction _endCommonPan:];
-[UIMultiSelectInteraction isEnabled];
-[UIMultiSelectInteraction _beginObservingScrollViewOffsetUpdates];
-[UIMultiSelectInteraction view];
-[UIMultiSelectInteraction setDelegate:];
-[UIMultiSelectInteraction _updateCommonPan:];
-[UIMultiSelectInteraction gestureRecognizerShouldBegin:];
-[UIMultiSelectInteraction _cancelScrollingInViewForGesture:];
-[UIMultiSelectInteraction _gestureTypeForGestureInstance:];
-[UIMultiSelectInteraction setEnabled:];
-[UIMultiSelectInteraction _beginInteractionWithTrigger:point:keepingSelection:];
-[UIMultiSelectInteraction willMoveToView:];
-[UIMultiSelectInteraction _endInteractionAtPoint:canceled:];
-[UIMultiSelectInteraction gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[UIMultiSelectInteraction singleTouchPanGestureHysteresis];
-[UIMultiSelectInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIMultiSelectInteraction _handleKeyboardSelectionExtensionKeyCommand:];
-[UIMultiSelectInteraction delegate];
-[UIMultiSelectInteraction _interactionDelegate];
-[UIMultiSelectInteraction _handleCommonPanGestureStateChanged:];
-[UIMultiSelectInteraction set_singleFingerExtensionTap:];
-[UIMultiSelectInteraction _multiFingerTapGesture:];
-[UIMultiSelectInteraction _viewAsScrollView];
-[UIMultiSelectInteraction _isBandSelectionAllowedAtPoint:];
-[UIMultiSelectInteraction _cancelCommonPan:];
-[UIMultiSelectInteraction _didInvokeMultiSelectAppendGestureAtLocation:];
-[UIMultiSelectInteraction _multiFingerTap];
-[UIMultiSelectInteraction activeGestureType];
-[UIMultiSelectInteraction _endObservingScrollViewOffsetUpdates];
-[UIMultiSelectInteraction _updateDelegateConformance];
-[UIMultiSelectInteraction set_multiSelectModePan:];
-[UIMultiSelectInteraction _askDelegateToAutomaticallyTransitionToMultiSelectModeKeepingSelection:];
-[UIMultiSelectInteraction _isCommandKeyBeingHeldWithGesture:];
-[UIMultiSelectInteraction bandSelectionInteraction];
-[UIMultiSelectInteraction _shouldBeginInteractionWithGestureType:location:velocity:];
-[UIMultiSelectInteraction didMoveToView:];
-[UIMultiSelectInteraction _handleBandSelectionInteraction:];
```
