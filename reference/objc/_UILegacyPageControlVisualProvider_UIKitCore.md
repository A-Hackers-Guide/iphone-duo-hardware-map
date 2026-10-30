# `_UILegacyPageControlVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIPageControlVisualProvider`
- 6 instance variables, 0 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"UIImage" _currentPageImage;
@"UIImage" _pageImage;
@"NSMutableArray" _currentPageImages;
@"NSMutableArray" _pageImages;
@"UIVisualEffectView" _backgroundVisualEffectView;
@"NSMutableArray" _indicators;
```

## Instance methods

```
-[_UILegacyPageControlVisualProvider invalidateIndicators];
-[_UILegacyPageControlVisualProvider didUpdateNumberOfPages];
-[_UILegacyPageControlVisualProvider intrinsicContentSize];
-[_UILegacyPageControlVisualProvider updateDisplayedPageToCurrentPage];
-[_UILegacyPageControlVisualProvider effectiveContentView];
-[_UILegacyPageControlVisualProvider layoutSubviews];
-[_UILegacyPageControlVisualProvider sizeForNumberOfPages:];
-[_UILegacyPageControlVisualProvider preferredIndicatorImage];
-[_UILegacyPageControlVisualProvider sizeThatFits:];
-[_UILegacyPageControlVisualProvider prepare];
-[_UILegacyPageControlVisualProvider didUpdatePageIndicatorTintColor];
-[_UILegacyPageControlVisualProvider didUpdateCurrentPageIndicatorTintColor];
-[_UILegacyPageControlVisualProvider pruneArchivedSubviews:];
-[_UILegacyPageControlVisualProvider _indicatorSpacing];
-[_UILegacyPageControlVisualProvider _hasCustomImageForPage:enabled:];
-[_UILegacyPageControlVisualProvider defaultActivePageIndicatorImage];
-[_UILegacyPageControlVisualProvider _cachePageIndicatorImages];
-[_UILegacyPageControlVisualProvider _cachedPageIndicatorCurrentImageForPage:];
-[_UILegacyPageControlVisualProvider _cachedPageIndicatorImageForPage:];
-[_UILegacyPageControlVisualProvider _drawModernIndicatorInView:enabled:];
-[_UILegacyPageControlVisualProvider _indicatorFrameAtIndex:];
-[_UILegacyPageControlVisualProvider _indicatorViewEnabled:index:];
-[_UILegacyPageControlVisualProvider _modernBounds];
-[_UILegacyPageControlVisualProvider _modernColorEnabled:];
-[_UILegacyPageControlVisualProvider _modernCornerRadius];
-[_UILegacyPageControlVisualProvider _pageIndicatorCurrentImageForPage:];
-[_UILegacyPageControlVisualProvider _pageIndicatorImageForPage:];
-[_UILegacyPageControlVisualProvider _setDisplayedPage:];
-[_UILegacyPageControlVisualProvider _transitionIndicator:toEnabled:index:];
-[_UILegacyPageControlVisualProvider didEndTrackingWithTouch:];
```
