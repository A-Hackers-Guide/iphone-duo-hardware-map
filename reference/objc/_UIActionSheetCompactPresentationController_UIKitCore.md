# `_UIActionSheetCompactPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPresentationController`
- 12 instance variables, 14 properties, 57 instance methods, 0 class methods

## Instance variables

```
B _avoidsKeyboardDisabled;
B _shouldAdoptPresentedAppearance;
B _hasPendingAnimatedLayout;
@"<_UIActionSheetCompactPresentationControllerDelegate>" _actionSheetDelegate;
@"UIView<UIActionSheetPresentationControllerDismissActionView>" _dismissActionView;
@"UILongPressGestureRecognizer" _dismissActionViewGestureRecognizer;
@"UITapGestureRecognizer" _dimmingViewDismissTapGestureRecognizer;
@"UIView" _dimmingView;
@"_UIDimmingKnockoutBackdropView" _backdropView;
@"_UIAnimationCoordinator" _animationCoordinator;
@"<UIActionSheetPresentationControllerVisualStyle>" _visualStyle;
d _pseudoAlertPreferredTop;
```

## Properties

```
@property (TB,N,V_shouldAdoptPresentedAppearance) shouldAdoptPresentedAppearance;
@property (T@"UIView<UIActionSheetPresentationControllerDismissActionView>",&,N,V_dismissActionView) dismissActionView;
@property (T@"UILongPressGestureRecognizer",&,N,V_dismissActionViewGestureRecognizer) dismissActionViewGestureRecognizer;
@property (T@"UITapGestureRecognizer",&,N,V_dimmingViewDismissTapGestureRecognizer) dimmingViewDismissTapGestureRecognizer;
@property (T@"UIView",&,N,V_dimmingView) dimmingView;
@property (T@"_UIDimmingKnockoutBackdropView",&,N,V_backdropView) backdropView;
@property (T@"_UIAnimationCoordinator",&,N,V_animationCoordinator) animationCoordinator;
@property (T@"<UIActionSheetPresentationControllerVisualStyle>",&,N,V_visualStyle) visualStyle;
@property (Td,N,V_pseudoAlertPreferredTop) pseudoAlertPreferredTop;
@property (TB,N,V_hasPendingAnimatedLayout) hasPendingAnimatedLayout;
@property (T@"NSString",C,N) dismissActionTitle;
@property (TB,N,V_avoidsKeyboardDisabled) avoidsKeyboardDisabled;
@property (TB,N) dismissActionUsesShorterHeightWhenCompactVertically;
@property (T@"<_UIActionSheetCompactPresentationControllerDelegate>",W,N,V_actionSheetDelegate) actionSheetDelegate;
```

## Instance methods

```
-[_UIActionSheetCompactPresentationController setBackdropView:];
-[_UIActionSheetCompactPresentationController _dismiss];
-[_UIActionSheetCompactPresentationController backdropView];
-[_UIActionSheetCompactPresentationController setVisualStyle:];
-[_UIActionSheetCompactPresentationController dimmingView];
-[_UIActionSheetCompactPresentationController preferredContentSizeDidChangeForChildContentContainer:];
-[_UIActionSheetCompactPresentationController _keyboardChanged:];
-[_UIActionSheetCompactPresentationController visualStyle];
-[_UIActionSheetCompactPresentationController dealloc];
-[_UIActionSheetCompactPresentationController _baseContentInsetsWithLeftMargin:rightMargin:];
-[_UIActionSheetCompactPresentationController setDimmingView:];
-[_UIActionSheetCompactPresentationController _shouldOccludeDuringPresentation];
-[_UIActionSheetCompactPresentationController viewWillTransitionToSize:withTransitionCoordinator:];
-[_UIActionSheetCompactPresentationController frameOfPresentedViewInContainerView];
-[_UIActionSheetCompactPresentationController shouldPresentInFullscreen];
-[_UIActionSheetCompactPresentationController preferredContentSize];
-[_UIActionSheetCompactPresentationController _shouldPresentedViewControllerControlStatusBarAppearance];
-[_UIActionSheetCompactPresentationController dismissalTransitionWillBegin];
-[_UIActionSheetCompactPresentationController presentationTransitionWillBegin];
-[_UIActionSheetCompactPresentationController _handleDismiss:];
-[_UIActionSheetCompactPresentationController _applyVisualAffordancesToViews];
-[_UIActionSheetCompactPresentationController _currentLayoutGeometry];
-[_UIActionSheetCompactPresentationController _frameOfPresentedViewControllerViewInSuperview];
-[_UIActionSheetCompactPresentationController _layoutViews];
-[_UIActionSheetCompactPresentationController _minimumSizeForDismissButton];
-[_UIActionSheetCompactPresentationController _resizeAnimationDuration];
-[_UIActionSheetCompactPresentationController _shouldDisableAvoidsKeyboard];
-[_UIActionSheetCompactPresentationController _subscribeToKeyboardNotifications];
-[_UIActionSheetCompactPresentationController _transitionToPresentationController:withTransitionCoordinator:];
-[_UIActionSheetCompactPresentationController _unsubscribeFromKeyboardNotifications];
-[_UIActionSheetCompactPresentationController _updateForKeyboardStartFrame:endFrame:duration:curve:];
-[_UIActionSheetCompactPresentationController _willRunTransitionForCurrentStateDeferred:];
-[_UIActionSheetCompactPresentationController actionSheetDelegate];
-[_UIActionSheetCompactPresentationController animationCoordinator];
-[_UIActionSheetCompactPresentationController avoidsKeyboardDisabled];
-[_UIActionSheetCompactPresentationController beginPseudoAlertPresentationMode];
-[_UIActionSheetCompactPresentationController dimmingViewDismissTapGestureRecognizer];
-[_UIActionSheetCompactPresentationController dismissActionTitle];
-[_UIActionSheetCompactPresentationController dismissActionUsesShorterHeightWhenCompactVertically];
-[_UIActionSheetCompactPresentationController dismissActionView];
-[_UIActionSheetCompactPresentationController dismissActionViewGestureRecognizer];
-[_UIActionSheetCompactPresentationController endPseudoAlertPresentationMode];
-[_UIActionSheetCompactPresentationController hasPendingAnimatedLayout];
-[_UIActionSheetCompactPresentationController initWithPresentedViewController:presentingViewController:visualStyle:];
-[_UIActionSheetCompactPresentationController pseudoAlertPreferredTop];
-[_UIActionSheetCompactPresentationController setActionSheetDelegate:];
-[_UIActionSheetCompactPresentationController setAnimationCoordinator:];
-[_UIActionSheetCompactPresentationController setAvoidsKeyboardDisabled:];
-[_UIActionSheetCompactPresentationController setDimmingViewDismissTapGestureRecognizer:];
-[_UIActionSheetCompactPresentationController setDismissActionTitle:];
-[_UIActionSheetCompactPresentationController setDismissActionUsesShorterHeightWhenCompactVertically:];
-[_UIActionSheetCompactPresentationController setDismissActionView:];
-[_UIActionSheetCompactPresentationController setDismissActionViewGestureRecognizer:];
-[_UIActionSheetCompactPresentationController setHasPendingAnimatedLayout:];
-[_UIActionSheetCompactPresentationController setPseudoAlertPreferredTop:];
-[_UIActionSheetCompactPresentationController setShouldAdoptPresentedAppearance:];
-[_UIActionSheetCompactPresentationController shouldAdoptPresentedAppearance];
```
