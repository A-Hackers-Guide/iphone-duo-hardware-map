# `_UIPageIndicatorStoreObject`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UIImage" _customImage;
@"UIImage" _activeImage;
q _startIndex;
q _endIndex;
{CGSize="width"d"height"d} _indicatorSize;
{CGSize="width"d"height"d} _activeIndicatorSize;
```

## Properties

```
@property (T@"UIImage",&,N,V_customImage) customImage;
@property (T{CGSize=dd},N,V_indicatorSize) indicatorSize;
@property (T@"UIImage",&,N,V_activeImage) activeImage;
@property (T{CGSize=dd},N,V_activeIndicatorSize) activeIndicatorSize;
@property (Tq,N,V_startIndex) startIndex;
@property (Tq,N,V_endIndex) endIndex;
@property (TB,R,N) hasImage;
@property (T{CGSize=dd},R,N) resolvedSize;
```

## Instance methods

```
-[_UIPageIndicatorStoreObject startIndex];
-[_UIPageIndicatorStoreObject setActiveIndicatorSize:];
-[_UIPageIndicatorStoreObject customImage];
-[_UIPageIndicatorStoreObject hasImage];
-[_UIPageIndicatorStoreObject invalidateLayoutInfo];
-[_UIPageIndicatorStoreObject activeImage];
-[_UIPageIndicatorStoreObject indicatorSize];
-[_UIPageIndicatorStoreObject setStartIndex:];
-[_UIPageIndicatorStoreObject setEndIndex:];
-[_UIPageIndicatorStoreObject validPageWithinBound:];
-[_UIPageIndicatorStoreObject endIndex];
-[_UIPageIndicatorStoreObject _copyImagesFromObject:];
-[_UIPageIndicatorStoreObject resolvedSize];
-[_UIPageIndicatorStoreObject splitAtIndex:withImage:active:];
-[_UIPageIndicatorStoreObject initWithStartIndex:endIndex:];
-[_UIPageIndicatorStoreObject description];
-[_UIPageIndicatorStoreObject activeIndicatorSize];
-[_UIPageIndicatorStoreObject setIndicatorSize:];
-[_UIPageIndicatorStoreObject setActiveImage:];
-[_UIPageIndicatorStoreObject setCustomImage:];
```
