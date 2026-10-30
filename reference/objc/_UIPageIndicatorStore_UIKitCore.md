# `_UIPageIndicatorStore`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 8 properties, 42 instance methods, 0 class methods

## Instance variables

```
{?="fittingSize"{SizeForMaximumContentSizeCache="dirty"b1"fittingLength"d"maximumSize"{CGSize="width"d"height"d}}"indicatorCount"{NumberOfVisibleIndicatorsForStartIndexCache="dirty"b1"fittingLength"d"startIndex"q"numberOfIndicators"q}"contentSize"{ContentSizeForNumberOfPagesCache="dirty"b1"numberOfPages"d"contentSize"{CGSize="width"d"height"d}}"contentSizeInRange"{MinimumContentSizeForIndicatorsInRangeCache="dirty"b1"range"{_NSRange="location"Q"length"Q}"contentSize"{CGSize="width"d"height"d}}} _cache;
{?="fittingSize"{SizeForMaximumContentSizeCache="dirty"b1"fittingLength"d"maximumSize"{CGSize="width"d"height"d}}"indicatorCount"{NumberOfVisibleIndicatorsForStartIndexCache="dirty"b1"fittingLength"d"startIndex"q"numberOfIndicators"q}"contentSize"{ContentSizeForNumberOfPagesCache="dirty"b1"numberOfPages"d"contentSize"{CGSize="width"d"height"d}}"contentSizeInRange"{MinimumContentSizeForIndicatorsInRangeCache="dirty"b1"range"{_NSRange="location"Q"length"Q}"contentSize"{CGSize="width"d"height"d}}} _expandedCache;
@"UIImage" _defaultImage;
@"_UIPageIndicatorStoreObject" _defaultObject;
@"<_UIPageIndicatorStoreDelegate>" _delegate;
@"UIImage" _preferredImage;
@"UIImage" _preferredActiveImage;
d _indicatorSpacing;
q _direction;
@"NSMutableArray" _store;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_store) store;
@property (T@"<_UIPageIndicatorStoreDelegate>",W,N,V_delegate) delegate;
@property (T@"UIImage",&,N,V_preferredImage) preferredImage;
@property (T@"UIImage",&,N,V_preferredActiveImage) preferredActiveImage;
@property (Td,N,V_indicatorSpacing) indicatorSpacing;
@property (Tq,N,V_direction) direction;
@property (T@"UIImage",R,N) indicatorImage;
@property (Tq,R,N) numberOfPages;
```

## Instance methods

```
-[_UIPageIndicatorStore indicatorSpacing];
-[_UIPageIndicatorStore updateImage:forPage:];
-[_UIPageIndicatorStore updateActiveImage:forPage:];
-[_UIPageIndicatorStore contentSizeForNumberOfPages:hasExpandedActiveIndicator:];
-[_UIPageIndicatorStore preferredActiveImage];
-[_UIPageIndicatorStore store];
-[_UIPageIndicatorStore _objectIndexForPage:lower:upper:];
-[_UIPageIndicatorStore sizeForMaximumContentSizeFittingLength:hasExpandedActiveIndicator:];
-[_UIPageIndicatorStore init];
-[_UIPageIndicatorStore indicatorSizeForPage:];
-[_UIPageIndicatorStore minimumContentSizeForIndicatorsInRange:hasExpandedActiveIndicator:];
-[_UIPageIndicatorStore _resetStore];
-[_UIPageIndicatorStore preferredImage];
-[_UIPageIndicatorStore _removeImageForPage:active:];
-[_UIPageIndicatorStore _defaultIndicatorImage];
-[_UIPageIndicatorStore activeIndicatorImageForPage:];
-[_UIPageIndicatorStore setDirection:];
-[_UIPageIndicatorStore objectIndexForPage:];
-[_UIPageIndicatorStore customIndicatorImageForPage:];
-[_UIPageIndicatorStore indicatorImage];
-[_UIPageIndicatorStore _sizeForMaximumContentSizeFittingLength:hasExpandedActiveIndicator:];
-[_UIPageIndicatorStore validateDataStore];
-[_UIPageIndicatorStore direction];
-[_UIPageIndicatorStore setPreferredImage:];
-[_UIPageIndicatorStore resolvedIndicatorLayoutSizeForPage:];
-[_UIPageIndicatorStore setDelegate:];
-[_UIPageIndicatorStore _indicatorSizeForObject:];
-[_UIPageIndicatorStore indicatorPositionForContinuousPage:expandedIndicatorPage:];
-[_UIPageIndicatorStore numberOfVisibleIndicatorsForStartIndex:fittingLength:hasExpandedActiveIndicator:];
-[_UIPageIndicatorStore _insertImage:forPage:active:];
-[_UIPageIndicatorStore delegate];
-[_UIPageIndicatorStore _updateImage:forPage:active:];
-[_UIPageIndicatorStore setIndicatorSpacing:];
-[_UIPageIndicatorStore defaultIndicatorSize];
-[_UIPageIndicatorStore numberOfPages];
-[_UIPageIndicatorStore setPreferredActiveImage:];
-[_UIPageIndicatorStore invalidateLayoutCache];
-[_UIPageIndicatorStore setStore:];
-[_UIPageIndicatorStore _contentSizeForIndicatorsInRange:hasExpandedActiveIndicator:];
-[_UIPageIndicatorStore updateStoreForNumberOfPages:];
-[_UIPageIndicatorStore customActiveIndicatorImageForPage:];
-[_UIPageIndicatorStore indicatorImageForPage:];
```
