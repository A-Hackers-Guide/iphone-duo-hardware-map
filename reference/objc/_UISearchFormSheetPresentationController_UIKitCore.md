# `_UISearchFormSheetPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPresentationController`
- Protocols: `_UISearchControllerPresenting`
- 3 instance variables, 17 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"_UISearchPresentationAssistant" _assistant;
@"UIView" _wrapperView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} finalFrameForContainerView;
```

## Properties

```
@property (T@"UIView",R,&,N) searchBarContainerView;
@property (TB,R,N) shouldAccountForStatusBar;
@property (Td,R,N) statusBarAdjustment;
@property (TB,R,N) searchBarToBecomeTopAttached;
@property (TB,R,N) resultsUnderlapsSearchBar;
@property (TB,R,N) searchBarCanContainScopeBar;
@property (TB,R,N) searchBarShouldClipToBounds;
@property (Td,R,N) resultsControllerContentOffset;
@property (T@"UIPresentationController<_UISearchControllerPresenting>",R,N) adaptivePresentationController;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,VfinalFrameForContainerView) finalFrameForContainerView;
@property (TB,R,N) animatorShouldLayoutPresentationViews;
@property (TB,R,N) forceObeyNavigationBarInsets;
@property (TQ,R,N) edgeForHidingNavigationBar;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISearchFormSheetPresentationController _shouldRespectDefinesPresentationContext];
-[_UISearchFormSheetPresentationController presentationTransitionDidEnd:];
-[_UISearchFormSheetPresentationController preferredContentSizeDidChangeForChildContentContainer:];
-[_UISearchFormSheetPresentationController _presentationControllerForTraitCollection:];
-[_UISearchFormSheetPresentationController setContentVisible:];
-[_UISearchFormSheetPresentationController dealloc];
-[_UISearchFormSheetPresentationController adaptivePresentationController];
-[_UISearchFormSheetPresentationController _shouldKeepCurrentFirstResponder];
-[_UISearchFormSheetPresentationController searchBarContainerView];
-[_UISearchFormSheetPresentationController statusBarAdjustment];
-[_UISearchFormSheetPresentationController initWithPresentedViewController:presentingViewController:];
-[_UISearchFormSheetPresentationController frameOfPresentedViewInContainerView];
-[_UISearchFormSheetPresentationController resultsControllerContentOffset];
-[_UISearchFormSheetPresentationController shouldAccountForStatusBar];
-[_UISearchFormSheetPresentationController searchBarToBecomeTopAttached];
-[_UISearchFormSheetPresentationController dismissalTransitionWillBegin];
-[_UISearchFormSheetPresentationController dismissalTransitionDidEnd:];
-[_UISearchFormSheetPresentationController presentationTransitionWillBegin];
-[_UISearchFormSheetPresentationController containerViewWillLayoutSubviews];
-[_UISearchFormSheetPresentationController _frameOfPresentedViewControllerViewInSuperview];
-[_UISearchFormSheetPresentationController _horizontalSizeClassChanged];
-[_UISearchFormSheetPresentationController _presentedView:enableFormSheetAccoutrements:];
-[_UISearchFormSheetPresentationController _presentedViewControllerForPresentationController:traitCollection:];
-[_UISearchFormSheetPresentationController _shouldSubscribeToKeyboardNotifications];
-[_UISearchFormSheetPresentationController _transitionFromDidEnd];
-[_UISearchFormSheetPresentationController _transitionFromWillBegin];
-[_UISearchFormSheetPresentationController _transitionToDidEnd];
-[_UISearchFormSheetPresentationController _transitionToPresentationController:withTransitionCoordinator:];
-[_UISearchFormSheetPresentationController _transitionToWillBegin];
-[_UISearchFormSheetPresentationController adaptivePresentationStyle];
-[_UISearchFormSheetPresentationController animatorShouldLayoutPresentationViews];
-[_UISearchFormSheetPresentationController edgeForHidingNavigationBar];
-[_UISearchFormSheetPresentationController finalFrameForContainerView];
-[_UISearchFormSheetPresentationController forceObeyNavigationBarInsets];
-[_UISearchFormSheetPresentationController presentedView];
-[_UISearchFormSheetPresentationController resultsUnderlapsSearchBar];
-[_UISearchFormSheetPresentationController searchBarCanContainScopeBar];
-[_UISearchFormSheetPresentationController searchBarShouldClipToBounds];
```
