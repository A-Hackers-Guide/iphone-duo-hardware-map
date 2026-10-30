# `UIKBTutorialMultipageView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIScrollViewDelegate`
- 6 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _pageScrollView;
@"NSArray" _pageViews;
@"UIPageControl" _pageControl;
@"NSTimer" _nextPageScrollTimer;
d _pagingInterval;
@"NSArray" _mediaViewConstraints;
```

## Properties

```
@property (T@"UIScrollView",&,N,V_pageScrollView) pageScrollView;
@property (T@"NSArray",&,N,V_pageViews) pageViews;
@property (T@"UIPageControl",&,N,V_pageControl) pageControl;
@property (T@"NSTimer",&,N,V_nextPageScrollTimer) nextPageScrollTimer;
@property (Td,N,V_pagingInterval) pagingInterval;
@property (T@"NSArray",&,N,V_mediaViewConstraints) mediaViewConstraints;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKBTutorialMultipageView pageViews];
-[UIKBTutorialMultipageView layoutSubviews];
-[UIKBTutorialMultipageView setPageControl:];
-[UIKBTutorialMultipageView pageControl];
-[UIKBTutorialMultipageView scrollViewWillBeginDragging:];
-[UIKBTutorialMultipageView setPageViews:];
-[UIKBTutorialMultipageView scrollViewDidScroll:];
-[UIKBTutorialMultipageView configMediaView];
-[UIKBTutorialMultipageView initWithPageViews:pagingInterval:];
-[UIKBTutorialMultipageView mediaViewConstraints];
-[UIKBTutorialMultipageView nextPageScrollTimer];
-[UIKBTutorialMultipageView pageScrollView];
-[UIKBTutorialMultipageView pagingInterval];
-[UIKBTutorialMultipageView resetPageScrolling];
-[UIKBTutorialMultipageView scrollToNextPage];
-[UIKBTutorialMultipageView setMediaViewConstraints:];
-[UIKBTutorialMultipageView setNextPageScrollTimer:];
-[UIKBTutorialMultipageView setPageScrollView:];
-[UIKBTutorialMultipageView setPagingInterval:];
```
