# `SBFPagedScrollView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSUIScrollView`
- 5 instance variables, 4 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _changingScrollViewLayout;
B _gestureEnabled;
@"NSArray" _pageViews;
Q _currentPageIndex;
{_NSRange="location"Q"length"Q} _visiblePageRange;
```

## Properties

```
@property (TQ,N,V_currentPageIndex) currentPageIndex;
@property (T{_NSRange=QQ},N,V_visiblePageRange) visiblePageRange;
@property (T@"NSArray",C,N,V_pageViews) pageViews;
@property (TB,N,V_gestureEnabled) gestureEnabled;
```

## Instance methods

```
-[SBFPagedScrollView currentScrollInterval];
-[SBFPagedScrollView gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBFPagedScrollView setVisiblePageRange:];
-[SBFPagedScrollView gestureRecognizer:shouldReceiveTouch:];
-[SBFPagedScrollView scrollToPageAtIndex:animated:withCompletion:];
-[SBFPagedScrollView gestureEnabled];
-[SBFPagedScrollView pageViews];
-[SBFPagedScrollView _updateVisiblePages];
-[SBFPagedScrollView layoutSubviews];
-[SBFPagedScrollView scrollToPageAtIndex:withAnimationSettings:withCompletion:];
-[SBFPagedScrollView visiblePageRange];
-[SBFPagedScrollView resetContentOffsetToCurrentPage];
-[SBFPagedScrollView contentOffsetForPageAtIndex:];
-[SBFPagedScrollView setGestureEnabled:];
-[SBFPagedScrollView currentPageIndex];
-[SBFPagedScrollView _bs_didEndScrolling];
-[SBFPagedScrollView pageRelativeScrollOffset];
-[SBFPagedScrollView setFrame:];
-[SBFPagedScrollView layoutPages];
-[SBFPagedScrollView setCurrentPageIndex:];
-[SBFPagedScrollView _updateCurrentPageForScrollOffset];
-[SBFPagedScrollView setPageViews:];
-[SBFPagedScrollView _bs_willBeginScrolling];
-[SBFPagedScrollView initWithFrame:];
-[SBFPagedScrollView _bs_didScrollWithContext:];
-[SBFPagedScrollView scrollToPageAtIndex:animated:];
-[SBFPagedScrollView _layoutScrollView];
-[SBFPagedScrollView unclippedPageRelativeScrollOffset];
```
