# `_UIPageControlVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 11 properties, 50 instance methods, 0 class methods

## Instance variables

```
@"UIPageControl" _pageControl;
q _displayedPage;
B _supportsContinuousInteraction;
q _interactionState;
@"UIImage" _preferredActiveIndicatorImage;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _activeTransformForTouchedPage;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _targetTransformForTouchedPage;
{CAColorMatrix="m11"f"m12"f"m13"f"m14"f"m15"f"m21"f"m22"f"m23"f"m24"f"m25"f"m31"f"m32"f"m33"f"m34"f"m35"f"m41"f"m42"f"m43"f"m44"f"m45"f} _pageIndicatorVibrantColorMatrix;
{CAColorMatrix="m11"f"m12"f"m13"f"m14"f"m15"f"m21"f"m22"f"m23"f"m24"f"m25"f"m31"f"m32"f"m33"f"m34"f"m35"f"m41"f"m42"f"m43"f"m44"f"m45"f} _activePageIndicatorVibrantColorMatrix;
```

## Properties

```
@property (Tq,R,N) displayedPage;
@property (Tq,N,V_interactionState) interactionState;
@property (TB,N,V_supportsContinuousInteraction) supportsContinuousInteraction;
@property (T{CGAffineTransform=dddddd},N,V_activeTransformForTouchedPage) activeTransformForTouchedPage;
@property (T{CGAffineTransform=dddddd},N,V_targetTransformForTouchedPage) targetTransformForTouchedPage;
@property (T{CAColorMatrix=ffffffffffffffffffff},N,V_pageIndicatorVibrantColorMatrix) pageIndicatorVibrantColorMatrix;
@property (T{CAColorMatrix=ffffffffffffffffffff},N,V_activePageIndicatorVibrantColorMatrix) activePageIndicatorVibrantColorMatrix;
@property (T@"UIImage",&,N) preferredIndicatorImage;
@property (T@"UIImage",&,N,V_preferredActiveIndicatorImage) preferredActiveIndicatorImage;
@property (Td,N) indicatorOpacity;
@property (T@"UIView",&,N) backgroundView;
```

## Instance methods

```
-[_UIPageControlVisualProvider invalidateIndicators];
-[_UIPageControlVisualProvider setInteractionState:];
-[_UIPageControlVisualProvider didUpdateNumberOfPages];
-[_UIPageControlVisualProvider intrinsicContentSize];
-[_UIPageControlVisualProvider updateDisplayedPageToCurrentPage];
-[_UIPageControlVisualProvider shouldDisableTouchTracking];
-[_UIPageControlVisualProvider setPreferredIndicatorImage:];
-[_UIPageControlVisualProvider setCustomActiveIndicatorImage:forPage:];
-[_UIPageControlVisualProvider traitCollectionDidChangeOnSubtree:];
-[_UIPageControlVisualProvider initWithPageControl:];
-[_UIPageControlVisualProvider layoutSubviews];
-[_UIPageControlVisualProvider sizeForNumberOfPages:];
-[_UIPageControlVisualProvider customIndicatorImageForPage:];
-[_UIPageControlVisualProvider preferredIndicatorImage];
-[_UIPageControlVisualProvider setCustomIndicatorImage:forPage:];
-[_UIPageControlVisualProvider setPreferredActiveIndicatorImage:];
-[_UIPageControlVisualProvider sizeThatFits:];
-[_UIPageControlVisualProvider setActivePageIndicatorVibrantColorMatrix:];
-[_UIPageControlVisualProvider setIndicatorOpacity:];
-[_UIPageControlVisualProvider preferredActiveIndicatorImage];
-[_UIPageControlVisualProvider didUpdateBackgroundEffect];
-[_UIPageControlVisualProvider prepare];
-[_UIPageControlVisualProvider didUpdatePageIndicatorTintColor];
-[_UIPageControlVisualProvider didUpdateCurrentPageIndicatorTintColor];
-[_UIPageControlVisualProvider pruneArchivedSubviews:];
-[_UIPageControlVisualProvider backgroundView];
-[_UIPageControlVisualProvider didUpdateBackgroundStyle];
-[_UIPageControlVisualProvider indicatorOpacity];
-[_UIPageControlVisualProvider didUpdateInteractionTypeAvailability];
-[_UIPageControlVisualProvider didUpdateLayoutDirection];
-[_UIPageControlVisualProvider didUpdatePageProgress];
-[_UIPageControlVisualProvider didUpdateCustomLayoutValues];
-[_UIPageControlVisualProvider interactionState];
-[_UIPageControlVisualProvider setBackgroundView:];
-[_UIPageControlVisualProvider supportsContinuousInteraction];
-[_UIPageControlVisualProvider setPage:interactionState:];
-[_UIPageControlVisualProvider didUpdateCurrentPageProgress];
-[_UIPageControlVisualProvider indicatorFrameForPage:];
-[_UIPageControlVisualProvider customActiveIndicatorImageForPage:];
-[_UIPageControlVisualProvider setPageIndicatorVibrantColorMatrix:];
-[_UIPageControlVisualProvider pageIndicatorVibrantColorMatrix];
-[_UIPageControlVisualProvider activePageIndicatorVibrantColorMatrix];
-[_UIPageControlVisualProvider activeTransformForTouchedPage];
-[_UIPageControlVisualProvider didEndTrackingWithTouch:];
-[_UIPageControlVisualProvider displayedPage];
-[_UIPageControlVisualProvider setActiveTransformForTouchedPage:];
-[_UIPageControlVisualProvider setSupportsContinuousInteraction:];
-[_UIPageControlVisualProvider setTargetTransformForTouchedPage:];
-[_UIPageControlVisualProvider targetTransformForTouchedPage];
-[_UIPageControlVisualProvider teardownPageControl];
```
