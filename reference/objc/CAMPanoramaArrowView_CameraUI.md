# `CAMPanoramaArrowView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 10 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _arrowHead;
@"UIView" _arrowTail;
@"CAShapeLayer" _arrowTailPiecesLayer;
^{CGPath=} _currentTailPiecesPath;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _arrowTailRect;
d _currentNormalizedSpeed;
d _tailBiggestDelta;
d _tailBigDelta;
d _tailMediumDelta;
d _tailSmallDelta;
```

## Instance methods

```
-[CAMPanoramaArrowView intrinsicContentSize];
-[CAMPanoramaArrowView dealloc];
-[CAMPanoramaArrowView reset];
-[CAMPanoramaArrowView layoutSubviews];
-[CAMPanoramaArrowView initWithFrame:];
-[CAMPanoramaArrowView _newTailPiecesPathOfWidth:];
-[CAMPanoramaArrowView _updateTailWithAnimationDuration:];
-[CAMPanoramaArrowView animateWithNormalizedSpeed:duration:];
```
