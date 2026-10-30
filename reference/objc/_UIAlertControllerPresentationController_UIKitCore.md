# `_UIAlertControllerPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPresentationController`
- Protocols: `UIAdaptivePresentationControllerDelegate`, `UIForcePresentationController`
- 16 instance variables, 14 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"UIView" _dimmingView;
@"_UIKeyboardLayoutAlignmentView" keyboardLayoutAlignmentView;
@"UIView" keyboardLayoutAlignmentAvailableSpaceView;
@"UIAlertVisualStyleUpdatableConstraints" _visualStyleUpdatableConstraints;
@"NSLayoutConstraint" _topAvailableSpaceConstraint;
@"NSLayoutConstraint" _bottomAvailableSpaceConstraint;
B constraintsPrepared;
B _sourceViewSnapshotAndScaleTransformSuppressed;
B _chromeHidden;
B __isCurrentContext;
B __shouldRespectNearestCurrentContextPresenter;
@"UIGestureRecognizer" _panningGestureRecognizer;
@? _presentationPhaseCompletionBlock;
@"<_UIForcePresentationControllerDelegate>" _forcePresentationControllerDelegate;
@"UIView" _revealContainerView;
@"_UIStatesFeedbackGenerator" _feedbackGenerator;
```

## Properties

```
@property (T@"UIView",R,V_dimmingView) _dimmingView;
@property (TB,S_setIsCurrentContext:,V__isCurrentContext) _isCurrentContext;
@property (TB,S_setShouldRespectNearestCurrentContextPresenter:,V__shouldRespectNearestCurrentContextPresenter) _shouldRespectNearestCurrentContextPresenter;
@property (TB,N,G_isChromeHidden,S_setChromeHidden:,V_chromeHidden) _chromeHidden;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@?,C,N,V_presentationPhaseCompletionBlock) presentationPhaseCompletionBlock;
@property (T@"UIGestureRecognizer",&,N,V_panningGestureRecognizer) panningGestureRecognizer;
@property (TB,N,V_sourceViewSnapshotAndScaleTransformSuppressed) _sourceViewSnapshotAndScaleTransformSuppressed;
@property (T@"UIView",R,N,V_revealContainerView) _revealContainerView;
@property (T@"_UIStatesFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (T@"<_UIForcePresentationControllerDelegate>",W,N,V_forcePresentationControllerDelegate) forcePresentationControllerDelegate;
```

## Instance methods

```
-[_UIAlertControllerPresentationController adaptivePresentationStyleForPresentationController:];
-[_UIAlertControllerPresentationController _shouldRespectDefinesPresentationContext];
-[_UIAlertControllerPresentationController setFeedbackGenerator:];
-[_UIAlertControllerPresentationController feedbackGenerator];
-[_UIAlertControllerPresentationController preferredContentSizeDidChangeForChildContentContainer:];
-[_UIAlertControllerPresentationController initWithPresentedViewController:presentingViewController:];
-[_UIAlertControllerPresentationController setDelegate:];
-[_UIAlertControllerPresentationController _shouldOccludeDuringPresentation];
-[_UIAlertControllerPresentationController viewWillTransitionToSize:withTransitionCoordinator:];
-[_UIAlertControllerPresentationController shouldPresentInFullscreen];
-[_UIAlertControllerPresentationController _createVisualStyleForProvider:];
-[_UIAlertControllerPresentationController _dimmingView];
-[_UIAlertControllerPresentationController presentationTransitionWillBegin];
-[_UIAlertControllerPresentationController _preserveResponderAcrossWindows];
-[_UIAlertControllerPresentationController _isChromeHidden];
-[_UIAlertControllerPresentationController containerViewWillLayoutSubviews];
-[_UIAlertControllerPresentationController _canCommitPresentation];
-[_UIAlertControllerPresentationController _canDismissPresentation];
-[_UIAlertControllerPresentationController _frameForTransitionViewInPresentationSuperview:];
-[_UIAlertControllerPresentationController _isCurrentContext];
-[_UIAlertControllerPresentationController _keyboardShouldAnimateAlongsideForInteractiveTransitions];
-[_UIAlertControllerPresentationController _prepareConstraintsIfNecessary];
-[_UIAlertControllerPresentationController _prepareDimmingViewIfNecessary];
-[_UIAlertControllerPresentationController _presentedAlertController];
-[_UIAlertControllerPresentationController _presentedAlertControllerDidAdapt];
-[_UIAlertControllerPresentationController _revealContainerView];
-[_UIAlertControllerPresentationController _setChromeHidden:];
-[_UIAlertControllerPresentationController _setIsCurrentContext:];
-[_UIAlertControllerPresentationController _setShouldRespectNearestCurrentContextPresenter:];
-[_UIAlertControllerPresentationController _shouldRespectNearestCurrentContextPresenter];
-[_UIAlertControllerPresentationController _sourceViewSnapshotAndScaleTransformSuppressed];
-[_UIAlertControllerPresentationController _updateConstraintsIfNecessary];
-[_UIAlertControllerPresentationController _willRunTransitionForCurrentStateDeferred:];
-[_UIAlertControllerPresentationController adaptivePresentationStyle];
-[_UIAlertControllerPresentationController containerViewDidLayoutSubviews];
-[_UIAlertControllerPresentationController forcePresentationControllerDelegate];
-[_UIAlertControllerPresentationController panningGestureRecognizer];
-[_UIAlertControllerPresentationController presentationController:viewControllerForAdaptivePresentationStyle:];
-[_UIAlertControllerPresentationController presentationPhaseCompletionBlock];
-[_UIAlertControllerPresentationController setForcePresentationControllerDelegate:];
-[_UIAlertControllerPresentationController setPanningGestureRecognizer:];
-[_UIAlertControllerPresentationController setPresentationPhaseCompletionBlock:];
-[_UIAlertControllerPresentationController set_sourceViewSnapshotAndScaleTransformSuppressed:];
```
