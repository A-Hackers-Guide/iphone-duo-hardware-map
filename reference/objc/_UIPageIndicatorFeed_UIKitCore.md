# `_UIPageIndicatorFeed`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIPageControl" _pageControl;
@"<_UIPageIndicatorFeedDelegate>" _delegate;
@"NSMutableArray" _activeQueue;
@"NSMutableArray" _reuseQueue;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_activeQueue) activeQueue;
@property (T@"NSMutableArray",&,N,V_reuseQueue) reuseQueue;
@property (T@"NSArray",R,N) indicators;
@property (T@"<_UIPageIndicatorFeedDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[_UIPageIndicatorFeed invalidateIndicators];
-[_UIPageIndicatorFeed setReuseQueue:];
-[_UIPageIndicatorFeed indicatorSizeForPage:];
-[_UIPageIndicatorFeed indicators];
-[_UIPageIndicatorFeed initWithPageControl:];
-[_UIPageIndicatorFeed activeQueue];
-[_UIPageIndicatorFeed updateReuseQueue];
-[_UIPageIndicatorFeed reuseQueue];
-[_UIPageIndicatorFeed _isPageWithinActiveBounds:];
-[_UIPageIndicatorFeed setDelegate:];
-[_UIPageIndicatorFeed setActiveQueue:];
-[_UIPageIndicatorFeed indicatorForPage:forSizeOnly:];
-[_UIPageIndicatorFeed reloadIndicatorImages];
-[_UIPageIndicatorFeed reloadIndicatorImageForPage:];
-[_UIPageIndicatorFeed indicatorForPage:];
-[_UIPageIndicatorFeed delegate];
-[_UIPageIndicatorFeed activeIndicatorForPage:];
-[_UIPageIndicatorFeed prepareIndicatorsFrom:to:];
-[_UIPageIndicatorFeed indicatorSizeForCustomImage:];
```
