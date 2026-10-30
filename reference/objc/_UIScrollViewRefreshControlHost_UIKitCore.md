# `_UIScrollViewRefreshControlHost`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIRefreshControlHosting`
- 3 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
B _refreshControlAutomaticContentOffsetAdjustmentEnabledNeedsReset;
B _refreshControlAutomaticContentOffsetAdjustmentEnabledWhenLastIdle;
```

## Properties

```
@property (TB,R) refreshControlInsetsAffectScrollViewRubberBanding;
@property (T@"UIScrollView",R,W) scrollView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIScrollViewRefreshControlHost initWithScrollView:];
-[_UIScrollViewRefreshControlHost scrollView];
-[_UIScrollViewRefreshControlHost decrementInsetHeight:];
-[_UIScrollViewRefreshControlHost incrementInsetHeight:];
-[_UIScrollViewRefreshControlHost refreshControl:didChangeToState:fromState:];
-[_UIScrollViewRefreshControlHost refreshControlInsetsAffectScrollViewRubberBanding];
```
