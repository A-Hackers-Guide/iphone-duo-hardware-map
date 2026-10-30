# `CAMLivePhotoBloomView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _isOff;
@"UIImageView" __defaultImageView;
@"CALayer" __ringContainer;
@"CAShapeLayer" __outerRing;
@"CAShapeLayer" __middleRing;
@"CALayer" __innerRing;
@"CALayer" __centerRing;
@"NSDictionary" __layersByRing;
@"NSDictionary" __shapeLayersByRing;
```

## Properties

```
@property (T@"UIImageView",R,N,V__defaultImageView) _defaultImageView;
@property (T@"CALayer",R,N,V__ringContainer) _ringContainer;
@property (T@"CAShapeLayer",R,N,V__outerRing) _outerRing;
@property (T@"CAShapeLayer",R,N,V__middleRing) _middleRing;
@property (T@"CALayer",R,N,V__innerRing) _innerRing;
@property (T@"CALayer",R,N,V__centerRing) _centerRing;
@property (T@"NSDictionary",R,N,V__layersByRing) _layersByRing;
@property (T@"NSDictionary",R,N,V__shapeLayersByRing) _shapeLayersByRing;
@property (TB,N,V_isOff) isOff;
```

## Instance methods

```
-[CAMLivePhotoBloomView stopAnimating];
-[CAMLivePhotoBloomView intrinsicContentSize];
-[CAMLivePhotoBloomView layoutSubviews];
-[CAMLivePhotoBloomView tintColorDidChange];
-[CAMLivePhotoBloomView initWithFrame:];
-[CAMLivePhotoBloomView _updateDefaultImage];
-[CAMLivePhotoBloomView _centerRing];
-[CAMLivePhotoBloomView _defaultImageView];
-[CAMLivePhotoBloomView _diameterForRing:];
-[CAMLivePhotoBloomView _innerRing];
-[CAMLivePhotoBloomView _layersByRing];
-[CAMLivePhotoBloomView _middleRing];
-[CAMLivePhotoBloomView _outerRing];
-[CAMLivePhotoBloomView _pathForDiameter:center:];
-[CAMLivePhotoBloomView _pathForRing:center:];
-[CAMLivePhotoBloomView _ringContainer];
-[CAMLivePhotoBloomView _shapeLayersByRing];
-[CAMLivePhotoBloomView _strokeWidthForRing:];
-[CAMLivePhotoBloomView _updateRingColors];
-[CAMLivePhotoBloomView animateBloom];
-[CAMLivePhotoBloomView isOff];
-[CAMLivePhotoBloomView setIsOff:];
```
