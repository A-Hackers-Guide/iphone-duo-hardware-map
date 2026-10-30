# `_UIScrollViewGradientMaskView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 11 instance methods, 1 class methods

## Instance variables

```
q _gradientDirection;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _gradientStartInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _gradientEndInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _gradientIntensities;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},N,V_gradientStartInsets) gradientStartInsets;
@property (T{UIEdgeInsets=dddd},N,V_gradientEndInsets) gradientEndInsets;
@property (T{UIEdgeInsets=dddd},N,V_gradientIntensities) gradientIntensities;
@property (Tq,N,V_gradientDirection) gradientDirection;
```

## Class methods

```
+[_UIScrollViewGradientMaskView layerClass];
```

## Instance methods

```
-[_UIScrollViewGradientMaskView setGradientDirection:];
-[_UIScrollViewGradientMaskView gradientLayer];
-[_UIScrollViewGradientMaskView gradientDirection];
-[_UIScrollViewGradientMaskView initWithFrame:];
-[_UIScrollViewGradientMaskView gradientEndInsets];
-[_UIScrollViewGradientMaskView gradientIntensities];
-[_UIScrollViewGradientMaskView gradientStartInsets];
-[_UIScrollViewGradientMaskView setGradientEndInsets:];
-[_UIScrollViewGradientMaskView setGradientIntensities:];
-[_UIScrollViewGradientMaskView setGradientStartInsets:];
-[_UIScrollViewGradientMaskView updateWithFrame:gradientStartInsets:gradientEndInsets:gradientIntensities:];
```
