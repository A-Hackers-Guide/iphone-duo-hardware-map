# `_UINavigationControllerRefreshControlHost`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIRefreshControlHosting`
- 8 instance variables, 14 properties, 31 instance methods, 1 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
@"<_UINavigationControllerRefreshControlHostDelegate>" _delegate;
@"UINavigationController" _navigationController;
d _restingHeightOfRefreshControl;
@"UIView" _hostContainerView;
d _unobstructedHeight;
@"UIRefreshControl" _refreshControl;
@"NSArray" _refreshControlConstraints;
```

## Properties

```
@property (T@"UIRefreshControl",W,V_refreshControl) refreshControl;
@property (T@"NSArray",&,V_refreshControlConstraints) refreshControlConstraints;
@property (T@"<_UINavigationControllerRefreshControlHostDelegate>",W,N,V_delegate) delegate;
@property (T@"UINavigationController",R,W,N,V_navigationController) navigationController;
@property (Td,N,V_restingHeightOfRefreshControl) restingHeightOfRefreshControl;
@property (Td,R,N) fullHeightOfRefreshControl;
@property (T@"UIView",&,N,V_hostContainerView) hostContainerView;
@property (Td,N,V_unobstructedHeight) unobstructedHeight;
@property (TB,R) refreshControlInsetsAffectScrollViewRubberBanding;
@property (T@"UIScrollView",R,W,V_scrollView) scrollView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UINavigationControllerRefreshControlHost canHostRefreshControlOwnedByScrollView:inNavigationController:];
```

## Instance methods

```
-[_UINavigationControllerRefreshControlHost stopAnimations];
-[_UINavigationControllerRefreshControlHost scrollView];
-[_UINavigationControllerRefreshControlHost dealloc];
-[_UINavigationControllerRefreshControlHost setDelegate:];
-[_UINavigationControllerRefreshControlHost delegate];
-[_UINavigationControllerRefreshControlHost description];
-[_UINavigationControllerRefreshControlHost setRefreshControl:];
-[_UINavigationControllerRefreshControlHost setHostContainerView:];
-[_UINavigationControllerRefreshControlHost hostContainerView];
-[_UINavigationControllerRefreshControlHost navigationController];
-[_UINavigationControllerRefreshControlHost _alphaForRefreshingControlStateWithPossiblyObstructedContent];
-[_UINavigationControllerRefreshControlHost _installRefreshControlIntoContainerView];
-[_UINavigationControllerRefreshControlHost _notifyLayoutDidChange];
-[_UINavigationControllerRefreshControlHost _removeRefreshControlFromContainerView];
-[_UINavigationControllerRefreshControlHost _thresholdForObstructedContentFullAlpha];
-[_UINavigationControllerRefreshControlHost _thresholdForObstructedContentZeroAlpha];
-[_UINavigationControllerRefreshControlHost _updateFadeOutProgress];
-[_UINavigationControllerRefreshControlHost decrementInsetHeight:];
-[_UINavigationControllerRefreshControlHost fullHeightOfRefreshControl];
-[_UINavigationControllerRefreshControlHost incrementInsetHeight:];
-[_UINavigationControllerRefreshControlHost initWithNavigationController:scrollView:];
-[_UINavigationControllerRefreshControlHost isHostingRefreshControlOwnedByScrollView:];
-[_UINavigationControllerRefreshControlHost refreshControl];
-[_UINavigationControllerRefreshControlHost refreshControl:didChangeToState:fromState:];
-[_UINavigationControllerRefreshControlHost refreshControlConstraints];
-[_UINavigationControllerRefreshControlHost refreshControlInsetsAffectScrollViewRubberBanding];
-[_UINavigationControllerRefreshControlHost restingHeightOfRefreshControl];
-[_UINavigationControllerRefreshControlHost setRefreshControlConstraints:];
-[_UINavigationControllerRefreshControlHost setRestingHeightOfRefreshControl:];
-[_UINavigationControllerRefreshControlHost setUnobstructedHeight:];
-[_UINavigationControllerRefreshControlHost unobstructedHeight];
```
