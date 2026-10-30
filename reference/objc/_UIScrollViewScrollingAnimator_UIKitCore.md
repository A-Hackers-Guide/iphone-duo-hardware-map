# `_UIScrollViewScrollingAnimator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 2 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
@"CADisplayLink" _displayLink;
@"_UIScrollViewScrollingAnimatorState" _currentScroll;
B _isScrollingInteractively;
B _isAdjustingScrollViewOffset;
{CGPoint="x"d"y"d} _velocity;
{CGPoint="x"d"y"d} _modelPosition;
{CGPoint="x"d"y"d} _idealPosition;
{CGPoint="x"d"y"d} _idealPositionForMinimumTravel;
@"NSHashTable" _trackedPressEvents;
```

## Properties

```
@property (T@"UIScrollView",R,W,N,V_scrollView) scrollView;
@property (TB,R,N,GisScrollingInteractively,V_isScrollingInteractively) scrollingInteractively;
```

## Instance methods

```
-[_UIScrollViewScrollingAnimator _displayLinkFired:];
-[_UIScrollViewScrollingAnimator initWithScrollView:];
-[_UIScrollViewScrollingAnimator scrollView];
-[_UIScrollViewScrollingAnimator dealloc];
-[_UIScrollViewScrollingAnimator invalidate];
-[_UIScrollViewScrollingAnimator _stopDisplayLink];
-[_UIScrollViewScrollingAnimator _beginInteractiveAnimationForScrollState:];
-[_UIScrollViewScrollingAnimator _distanceForIncrement:inDirection:];
-[_UIScrollViewScrollingAnimator _handlePressIfInterested:];
-[_UIScrollViewScrollingAnimator _interactiveScrollVelocity];
-[_UIScrollViewScrollingAnimator _keyboardHandlesPressEventForKeyInput:];
-[_UIScrollViewScrollingAnimator _rubberbandableDirections];
-[_UIScrollViewScrollingAnimator _scrollStateForDirection:granularity:];
-[_UIScrollViewScrollingAnimator _scrollStateForPress:];
-[_UIScrollViewScrollingAnimator _scrollToContentOffset:];
-[_UIScrollViewScrollingAnimator _scrollWithScrollToExtentAnimationTo:];
-[_UIScrollViewScrollingAnimator _scrollableDirectionsFromOffset:];
-[_UIScrollViewScrollingAnimator _startDisplayLinkIfNeeded];
-[_UIScrollViewScrollingAnimator _stopAnimatedScroll];
-[_UIScrollViewScrollingAnimator animateScrollInDirection:withGranularity:];
-[_UIScrollViewScrollingAnimator cancelInteractiveScroll];
-[_UIScrollViewScrollingAnimator finishHandlingPressEvent:];
-[_UIScrollViewScrollingAnimator handlePressEventIfInterested:];
-[_UIScrollViewScrollingAnimator isHandlingPressEvent:];
-[_UIScrollViewScrollingAnimator isInterestedInPress:];
-[_UIScrollViewScrollingAnimator isScrollingInteractively];
```
