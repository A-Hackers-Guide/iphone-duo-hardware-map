# `_UIPageIndicatorView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 20 instance variables, 20 properties, 57 instance methods, 0 class methods

## Instance variables

```
@"<UITraitChangeRegistration>" _displayScaleTraitChangeRegistration;
B _active;
B _supportsExpandedIndicator;
f _currentProgress;
q _page;
q _mode;
q _direction;
@"UIImage" _image;
@"UIImage" _activeImage;
@"UIColor" _indicatorColor;
@"UIColor" _activeIndicatorColor;
d _imageDisplayScaleFactor;
@"_UIPageIndicatorImageView" _imageView;
@"_UIPageIndicatorProgressView" _progressView;
@"UIViewFloatAnimatableProperty" _expandProgress;
q _offsetDirection;
{CGSize="width"d"height"d} _defaultModeSize;
{CGSize="width"d"height"d} _expandedModeSize;
{CAColorMatrix="m11"f"m12"f"m13"f"m14"f"m15"f"m21"f"m22"f"m23"f"m24"f"m25"f"m31"f"m32"f"m33"f"m34"f"m35"f"m41"f"m42"f"m43"f"m44"f"m45"f} _vibrantColorMatrix;
{CAColorMatrix="m11"f"m12"f"m13"f"m14"f"m15"f"m21"f"m22"f"m23"f"m24"f"m25"f"m31"f"m32"f"m33"f"m34"f"m35"f"m41"f"m42"f"m43"f"m44"f"m45"f} _activeVibrantColorMatrix;
```

## Properties

```
@property (T@"_UIPageIndicatorImageView",R,N,V_imageView) imageView;
@property (T@"_UIPageIndicatorProgressView",R,N,V_progressView) progressView;
@property (T@"UIViewFloatAnimatableProperty",R,N,V_expandProgress) expandProgress;
@property (Tq,R,N,V_offsetDirection) offsetDirection;
@property (Tq,N,V_page) page;
@property (TB,N,GisActive,V_active) active;
@property (TB,N,V_supportsExpandedIndicator) supportsExpandedIndicator;
@property (Tq,R,N,V_mode) mode;
@property (Tq,N,V_direction) direction;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"UIImage",&,N,V_activeImage) activeImage;
@property (T@"UIColor",&,N,V_indicatorColor) indicatorColor;
@property (T@"UIColor",&,N,V_activeIndicatorColor) activeIndicatorColor;
@property (T{CAColorMatrix=ffffffffffffffffffff},N,V_vibrantColorMatrix) vibrantColorMatrix;
@property (T{CAColorMatrix=ffffffffffffffffffff},N,V_activeVibrantColorMatrix) activeVibrantColorMatrix;
@property (Tf,N,V_currentProgress) currentProgress;
@property (T{CGSize=dd},N,V_defaultModeSize) defaultModeSize;
@property (T{CGSize=dd},N,V_expandedModeSize) expandedModeSize;
@property (T{CGAffineTransform=dddddd},N) contentTransform;
@property (Td,N,V_imageDisplayScaleFactor) imageDisplayScaleFactor;
```

## Instance methods

```
-[_UIPageIndicatorView setImageDisplayScaleFactor:];
-[_UIPageIndicatorView debugDescription];
-[_UIPageIndicatorView setCurrentProgress:];
-[_UIPageIndicatorView supportsExpandedIndicator];
-[_UIPageIndicatorView defaultModeSize];
-[_UIPageIndicatorView offsetDirection];
-[_UIPageIndicatorView activeIndicatorColor];
-[_UIPageIndicatorView setSupportsExpandedIndicator:];
-[_UIPageIndicatorView setDefaultModeSize:];
-[_UIPageIndicatorView setDirection:];
-[_UIPageIndicatorView setContentTransform:];
-[_UIPageIndicatorView layoutSubviews];
-[_UIPageIndicatorView setActiveIndicatorColor:];
-[_UIPageIndicatorView _updateImage];
-[_UIPageIndicatorView progressView];
-[_UIPageIndicatorView _updateImageDisplayScaleOverride];
-[_UIPageIndicatorView activeImage];
-[_UIPageIndicatorView setPage:];
-[_UIPageIndicatorView setActive:];
-[_UIPageIndicatorView setActiveVibrantColorMatrix:];
-[_UIPageIndicatorView _adjustedDefaultModeSize];
-[_UIPageIndicatorView contentTransform];
-[_UIPageIndicatorView currentExpandProgress];
-[_UIPageIndicatorView isInvalidated];
-[_UIPageIndicatorView expandProgress];
-[_UIPageIndicatorView _transitionDirection];
-[_UIPageIndicatorView _currentImageContentInsets];
-[_UIPageIndicatorView direction];
-[_UIPageIndicatorView invalidate];
-[_UIPageIndicatorView sizeThatFits:];
-[_UIPageIndicatorView sizeForImage:traits:];
-[_UIPageIndicatorView activeVibrantColorMatrix];
-[_UIPageIndicatorView _updateVibrantColorMatrix];
-[_UIPageIndicatorView indicatorColor];
-[_UIPageIndicatorView _updateProgressBar];
-[_UIPageIndicatorView _isDefaultSymbolImage];
-[_UIPageIndicatorView expandedModeSize];
-[_UIPageIndicatorView prepare];
-[_UIPageIndicatorView vibrantColorMatrix];
-[_UIPageIndicatorView page];
-[_UIPageIndicatorView mode];
-[_UIPageIndicatorView _hasOngoingExpandTransition];
-[_UIPageIndicatorView currentProgress];
-[_UIPageIndicatorView setVibrantColorMatrix:];
-[_UIPageIndicatorView setIndicatorColor:];
-[_UIPageIndicatorView initWithCoder:];
-[_UIPageIndicatorView imageDisplayScaleFactor];
-[_UIPageIndicatorView setMode:direction:];
-[_UIPageIndicatorView isActive];
-[_UIPageIndicatorView image];
-[_UIPageIndicatorView _adjustedExpandedModeSize];
-[_UIPageIndicatorView setActiveImage:];
-[_UIPageIndicatorView imageView];
-[_UIPageIndicatorView _updateIndicatorExpandProgress];
-[_UIPageIndicatorView initWithFrame:];
-[_UIPageIndicatorView setExpandedModeSize:];
-[_UIPageIndicatorView setImage:];
```
