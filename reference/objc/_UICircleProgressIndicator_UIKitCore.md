# `_UICircleProgressIndicator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 14 instance variables, 7 properties, 25 instance methods, 3 class methods

## Instance variables

```
d _animatedValue;
d _animationEndTime;
d _animationStartTime;
d _animationStartValue;
@"UIImage" _borderImage;
@"UIImage" _centerImage;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _centerImageInsets;
@"CADisplayLink" _displayLink;
@"UIImage" _fillImage;
B _highlighted;
@"UIImageView" _indeterminateView;
B _isAnimating;
d _progress;
@"UIColor" _unhighlightedBackgroundColor;
```

## Properties

```
@property (T@"UIImage",&,N,V_borderImage) borderImage;
@property (T@"UIImage",&,N,V_fillImage) fillImage;
@property (T@"UIImage",&,N,V_centerImage) image;
@property (T{UIEdgeInsets=dddd},N,V_centerImageInsets) imageInsets;
@property (TB,N,GisIndeterminate) indeterminate;
@property (Td,N,V_progress) progress;
@property (TB,N,GisHighlighted,V_highlighted) highlighted;
```

## Class methods

```
+[_UICircleProgressIndicator _borderImage];
+[_UICircleProgressIndicator _fillImage];
+[_UICircleProgressIndicator _indeterminateImage];
```

## Instance methods

```
-[_UICircleProgressIndicator didMoveToWindow];
-[_UICircleProgressIndicator setProgress:];
-[_UICircleProgressIndicator isHighlighted];
-[_UICircleProgressIndicator dealloc];
-[_UICircleProgressIndicator drawRect:];
-[_UICircleProgressIndicator setIndeterminate:];
-[_UICircleProgressIndicator layoutSubviews];
-[_UICircleProgressIndicator fillImage];
-[_UICircleProgressIndicator progress];
-[_UICircleProgressIndicator sizeThatFits:];
-[_UICircleProgressIndicator tintColorDidChange];
-[_UICircleProgressIndicator setHighlighted:];
-[_UICircleProgressIndicator setImageInsets:];
-[_UICircleProgressIndicator imageInsets];
-[_UICircleProgressIndicator image];
-[_UICircleProgressIndicator initWithFrame:];
-[_UICircleProgressIndicator isIndeterminate];
-[_UICircleProgressIndicator setProgress:animated:];
-[_UICircleProgressIndicator setImage:];
-[_UICircleProgressIndicator setBorderImage:];
-[_UICircleProgressIndicator _animateValueOnDisplayLink:];
-[_UICircleProgressIndicator _setHidesBorderView:];
-[_UICircleProgressIndicator _startIndeterminateAnimation];
-[_UICircleProgressIndicator borderImage];
-[_UICircleProgressIndicator setFillImage:];
```
