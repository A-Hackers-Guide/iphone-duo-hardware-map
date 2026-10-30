# `_UITVScrollViewManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIScrollViewScrollObserver`
- 9 instance variables, 12 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _delegateScrollViewManagerDidFinishScrolling;
B _useCustomMaskForScrolling;
B _ignoreScrollAnimationDidEnd;
@"<_UITVScrollViewManagerDelegate>" _delegate;
@"UIScrollView" _scrollView;
q _scrollStyle;
@"CASpringAnimation" _scrollAnimation;
@"UIView" _snapshotViewForWindow;
{CGPoint="x"d"y"d} _targetOffset;
```

## Properties

```
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
@property (T@"CASpringAnimation",&,N,V_scrollAnimation) scrollAnimation;
@property (Tq,N,V_scrollStyle) scrollStyle;
@property (T@"UIView",&,N,V_snapshotViewForWindow) snapshotViewForWindow;
@property (TB,N,V_useCustomMaskForScrolling) useCustomMaskForScrolling;
@property (TB,N,V_ignoreScrollAnimationDidEnd) ignoreScrollAnimationDidEnd;
@property (T{CGPoint=dd},N,V_targetOffset) targetOffset;
@property (T@"<_UITVScrollViewManagerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITVScrollViewManager _observeScrollViewDidScroll:];
-[_UITVScrollViewManager setContentOffset:animated:];
-[_UITVScrollViewManager scrollView];
-[_UITVScrollViewManager dealloc];
-[_UITVScrollViewManager setScrollView:];
-[_UITVScrollViewManager setDelegate:];
-[_UITVScrollViewManager delegate];
-[_UITVScrollViewManager scrollAnimation];
-[_UITVScrollViewManager setIgnoreScrollAnimationDidEnd:];
-[_UITVScrollViewManager setScrollStyle:];
-[_UITVScrollViewManager initWithScrollView:scrollStyle:];
-[_UITVScrollViewManager _customScrollingMaskForScrollView:frame:];
-[_UITVScrollViewManager _removeScreenshotViewIfNeeded];
-[_UITVScrollViewManager _scroll:toContentOffset:];
-[_UITVScrollViewManager _scrollAnimationDidEnd:];
-[_UITVScrollViewManager _tearDown:];
-[_UITVScrollViewManager ignoreScrollAnimationDidEnd];
-[_UITVScrollViewManager scrollStyle];
-[_UITVScrollViewManager setScrollAnimation:];
-[_UITVScrollViewManager setSnapshotViewForWindow:];
-[_UITVScrollViewManager setTargetOffset:];
-[_UITVScrollViewManager setUseCustomMaskForScrolling:];
-[_UITVScrollViewManager snapshotViewForWindow];
-[_UITVScrollViewManager targetOffset];
-[_UITVScrollViewManager useCustomMaskForScrolling];
```
