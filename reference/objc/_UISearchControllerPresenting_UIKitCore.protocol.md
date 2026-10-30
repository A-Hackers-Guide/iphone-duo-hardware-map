# `_UISearchControllerPresenting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 13 properties, 14 instance methods, 0 class methods

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
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) finalFrameForContainerView;
@property (TB,R,N) animatorShouldLayoutPresentationViews;
@property (TB,R,N) forceObeyNavigationBarInsets;
@property (TQ,R,N) edgeForHidingNavigationBar;
```

## Instance methods

```
-[_UISearchControllerPresenting setContentVisible:];
-[_UISearchControllerPresenting adaptivePresentationController];
-[_UISearchControllerPresenting searchBarContainerView];
-[_UISearchControllerPresenting statusBarAdjustment];
-[_UISearchControllerPresenting resultsControllerContentOffset];
-[_UISearchControllerPresenting shouldAccountForStatusBar];
-[_UISearchControllerPresenting searchBarToBecomeTopAttached];
-[_UISearchControllerPresenting animatorShouldLayoutPresentationViews];
-[_UISearchControllerPresenting edgeForHidingNavigationBar];
-[_UISearchControllerPresenting finalFrameForContainerView];
-[_UISearchControllerPresenting forceObeyNavigationBarInsets];
-[_UISearchControllerPresenting resultsUnderlapsSearchBar];
-[_UISearchControllerPresenting searchBarCanContainScopeBar];
-[_UISearchControllerPresenting searchBarShouldClipToBounds];
```
