# `_UISearchPopoverPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPopoverPresentationController`
- Protocols: `_UISearchControllerPresenting`
- 2 instance variables, 17 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"_UISearchPresentationAssistant" _assistant;
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
-[_UISearchPopoverPresentationController _presentationControllerForTraitCollection:];
-[_UISearchPopoverPresentationController setContentVisible:];
-[_UISearchPopoverPresentationController adaptivePresentationController];
-[_UISearchPopoverPresentationController searchBarContainerView];
-[_UISearchPopoverPresentationController statusBarAdjustment];
-[_UISearchPopoverPresentationController initWithPresentedViewController:presentingViewController:];
-[_UISearchPopoverPresentationController resultsControllerContentOffset];
-[_UISearchPopoverPresentationController shouldAccountForStatusBar];
-[_UISearchPopoverPresentationController searchBarToBecomeTopAttached];
-[_UISearchPopoverPresentationController presentationTransitionWillBegin];
-[_UISearchPopoverPresentationController _forcePresentationInPresenterScene];
-[_UISearchPopoverPresentationController _popoverHostingWindow];
-[_UISearchPopoverPresentationController _presentedViewControllerForSizeClassPair:];
-[_UISearchPopoverPresentationController _searchBar:didMoveFromWindow:newWindow:];
-[_UISearchPopoverPresentationController _transitionFromDidEnd];
-[_UISearchPopoverPresentationController _transitionFromWillBegin];
-[_UISearchPopoverPresentationController _transitionToDidEnd];
-[_UISearchPopoverPresentationController _transitionToWillBegin];
-[_UISearchPopoverPresentationController adaptivePresentationStyle];
-[_UISearchPopoverPresentationController animatorShouldLayoutPresentationViews];
-[_UISearchPopoverPresentationController edgeForHidingNavigationBar];
-[_UISearchPopoverPresentationController finalFrameForContainerView];
-[_UISearchPopoverPresentationController forceObeyNavigationBarInsets];
-[_UISearchPopoverPresentationController resultsUnderlapsSearchBar];
-[_UISearchPopoverPresentationController searchBarCanContainScopeBar];
-[_UISearchPopoverPresentationController searchBarShouldClipToBounds];
```
