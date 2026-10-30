# `_UIAlertControllerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 15 instance variables, 15 properties, 45 instance methods, 0 class methods

## Instance variables

```
B _actionsReversed;
B _shouldHaveBackdropView;
B _alignsToKeyboard;
B _hasDimmingView;
B _presentedAsPopover;
@"NSString" _title;
@"NSString" _message;
@"NSAttributedString" _attributedTitle;
@"NSAttributedString" _attributedMessage;
@"NSAttributedString" _attributedDetailMessage;
@"UIAlertController" _alertController;
@"UIView" __contentView;
@"UIView" __dimmingView;
@"UIAlertControllerVisualStyle" __visualStyle;
d _effectAlpha;
```

## Properties

```
@property (T@"NSString",C,N,S_setTitle:,V_title) title;
@property (T@"NSString",C,N,S_setMessage:,V_message) message;
@property (T@"NSAttributedString",C,N,S_setAttributedTitle:,V_attributedTitle) attributedTitle;
@property (T@"NSAttributedString",C,N,S_setAttributedMessage:,V_attributedMessage) attributedMessage;
@property (T@"NSAttributedString",C,N,S_setAttributedDetailMessage:,V_attributedDetailMessage) attributedDetailMessage;
@property (T@"UIAlertController",W,V_alertController) alertController;
@property (T@"UIView",R,V__contentView) _contentView;
@property (T@"UIView",R,V__dimmingView) _dimmingView;
@property (T@"UIAlertControllerVisualStyle",&,N,S_setVisualStyle:,V__visualStyle) _visualStyle;
@property (TB,N,G_actionsReversed,S_setActionsReversed:,V_actionsReversed) actionsReversed;
@property (Td,N,V_effectAlpha) effectAlpha;
@property (TB,V_shouldHaveBackdropView) shouldHaveBackdropView;
@property (TB,V_alignsToKeyboard) alignsToKeyboard;
@property (TB,V_hasDimmingView) hasDimmingView;
@property (TB,V_presentedAsPopover) presentedAsPopover;
```

## Instance methods

```
-[_UIAlertControllerView _setMessage:];
-[_UIAlertControllerView message];
-[_UIAlertControllerView alertController];
-[_UIAlertControllerView _contentView];
-[_UIAlertControllerView _visualStyle];
-[_UIAlertControllerView deselectAllActions];
-[_UIAlertControllerView title];
-[_UIAlertControllerView attributedTitle];
-[_UIAlertControllerView _setVisualStyle:];
-[_UIAlertControllerView beginTrackingSessionByTakingOverForSystemProvidedGestureRecognizer:];
-[_UIAlertControllerView attributedMessage];
-[_UIAlertControllerView _dimmingView];
-[_UIAlertControllerView setAlertController:];
-[_UIAlertControllerView _setTitle:];
-[_UIAlertControllerView _actionsChanged];
-[_UIAlertControllerView setEffectAlpha:];
-[_UIAlertControllerView _updateTextAlignmentAfterLayout];
-[_UIAlertControllerView _actionLayoutDirectionChanged];
-[_UIAlertControllerView _actionsReversed];
-[_UIAlertControllerView _addContentViewControllerToViewHierarchyIfNecessary];
-[_UIAlertControllerView _focusedAction];
-[_UIAlertControllerView _performBatchActionChangesWithBlock:];
-[_UIAlertControllerView _propertiesChanged];
-[_UIAlertControllerView _reapplyContentViewControllerLayoutGuideActionSequenceConstraintsIfNeeded];
-[_UIAlertControllerView _removeContentViewControllerViewFromHierarchy];
-[_UIAlertControllerView _setActionsReversed:];
-[_UIAlertControllerView _setAttributedDetailMessage:];
-[_UIAlertControllerView _setAttributedMessage:];
-[_UIAlertControllerView _setAttributedTitle:];
-[_UIAlertControllerView _textFieldsChanged];
-[_UIAlertControllerView _updateLabelProperties];
-[_UIAlertControllerView _updatePreferredAction];
-[_UIAlertControllerView alignsToKeyboard];
-[_UIAlertControllerView attributedDetailMessage];
-[_UIAlertControllerView configureForDismissAlongsideTransitionCoordinator:];
-[_UIAlertControllerView configureForPresentAlongsideTransitionCoordinator:];
-[_UIAlertControllerView contentViewControllerLayoutGuide];
-[_UIAlertControllerView effectAlpha];
-[_UIAlertControllerView hasDimmingView];
-[_UIAlertControllerView presentedAsPopover];
-[_UIAlertControllerView setAlignsToKeyboard:];
-[_UIAlertControllerView setHasDimmingView:];
-[_UIAlertControllerView setPresentedAsPopover:];
-[_UIAlertControllerView setShouldHaveBackdropView:];
-[_UIAlertControllerView shouldHaveBackdropView];
```
