# `_UIDocumentLaunchViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIDocumentUnavailableBrowserPresentationControllerDelegate`, `UIViewControllerTransitioningDelegate`, `UIViewControllerAnimatedTransitioning`
- 17 instance variables, 4 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"_UISystemBackgroundView" _backgroundView;
@"_UIDocumentUnavailableTitleView" _titleView;
@"UIView" _backgroundAccessoryView;
@"UIView" _foregroundAccessoryView;
@"_UIDocumentUnavailablePageBackgroundAccessoryView" _defaultBackgroundAccessoryView;
@"_UIDocumentUnavailableBrowserContainerViewController" _browserContainerViewController;
@"_UIDocumentUnavailableBrowserPresentationController" _browserPresentationController;
@"_UITouchPassthroughView" _contentContainerView;
@"_UITouchPassthroughView" _titleContainerView;
@"_UITouchPassthroughView" _backgroundAccessoryContainerView;
@"_UITouchPassthroughView" _foregroundAccessoryContainerView;
@"_UIMagicMorphAnimation" _morphAnimation;
@"DOCAnimatableInfo" _documentAnimationInfo;
@"UIViewPropertyAnimator" _transitionAnimator;
@"UIView" _animationInteractionView;
{?="shouldPresentBrowserViewController"b1"isPresentingBrowserViewController"b1"isRecoveringBrowserViewController"b1"isAnimatingTransition"b1"needsContentConfigurationUpdate"b1} _flags;
@"_UIDocumentUnavailableConfiguration" _configuration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDocumentLaunchViewController _firstResponderDidChange:];
-[_UIDocumentLaunchViewController animationControllerForDismissedController:];
-[_UIDocumentLaunchViewController animateTransition:];
-[_UIDocumentLaunchViewController animationControllerForPresentedController:presentingController:sourceController:];
-[_UIDocumentLaunchViewController transitionDuration:];
-[_UIDocumentLaunchViewController presentationControllerForPresentedViewController:presentingViewController:sourceViewController:];
-[_UIDocumentLaunchViewController viewLayoutMarginsDidChange];
-[_UIDocumentLaunchViewController willMoveToParentViewController:];
-[_UIDocumentLaunchViewController interruptibleAnimatorForTransition:];
-[_UIDocumentLaunchViewController animationEnded:];
-[_UIDocumentLaunchViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[_UIDocumentLaunchViewController loadView];
-[_UIDocumentLaunchViewController viewSafeAreaInsetsDidChange];
-[_UIDocumentLaunchViewController viewWillLayoutSubviews];
-[_UIDocumentLaunchViewController didMoveToParentViewController:];
-[_UIDocumentLaunchViewController _minimumLayoutMarginsForView];
-[_UIDocumentLaunchViewController browserPresentationControllerDidInvalidateSheetDetentValues:];
-[_UIDocumentLaunchViewController browserPresentationControllerDidInvalidateUntransformedFrame:];
-[_UIDocumentLaunchViewController browserPresentationControllerDismissalTransitionDidEnd:];
-[_UIDocumentLaunchViewController browserPresentationControllerDismissalTransitionWillBegin:];
-[_UIDocumentLaunchViewController browserPresentationControllerPerformLayout:];
-[_UIDocumentLaunchViewController browserPresentationControllerPresentationTransitionDidEnd:];
-[_UIDocumentLaunchViewController browserPresentationControllerPresentationTransitionWillBegin:];
```
