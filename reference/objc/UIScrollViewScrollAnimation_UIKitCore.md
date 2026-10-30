# `UIScrollViewScrollAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIAnimation`
- 11 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _originalOffset;
{CGPoint="x"d"y"d} _targetOffset;
B _targetOffsetValidAtStart;
d _accuracy;
B _adjustsForContentOffsetDelta;
@"CABasicAnimation" _customAnimation;
d _totalDuration;
B _forDiscreteScroll;
B _beingReplacedForDiscreteScroll;
B _revealsHorizontalScrollIndicator;
B _revealsVerticalScrollIndicator;
```

## Properties

```
@property (TB,N,V_revealsHorizontalScrollIndicator) revealsHorizontalScrollIndicator;
@property (TB,N,V_revealsVerticalScrollIndicator) revealsVerticalScrollIndicator;
```

## Instance methods

```
-[UIScrollViewScrollAnimation setProgress:];
-[UIScrollViewScrollAnimation setRevealsHorizontalScrollIndicator:];
-[UIScrollViewScrollAnimation adjustForContentOffsetDelta:];
-[UIScrollViewScrollAnimation setRevealsVerticalScrollIndicator:];
-[UIScrollViewScrollAnimation dealloc];
-[UIScrollViewScrollAnimation progressForFraction:];
-[UIScrollViewScrollAnimation revealsHorizontalScrollIndicator];
-[UIScrollViewScrollAnimation revealsVerticalScrollIndicator];
```
