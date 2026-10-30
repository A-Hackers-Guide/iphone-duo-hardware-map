# `CAMSlashMaskView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 1 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _slashBounds;
```

## Properties

```
@property (T@"CAShapeLayer",R,N) _shapeLayer;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_slashBounds) slashBounds;
```

## Class methods

```
+[CAMSlashMaskView layerClass];
```

## Instance methods

```
-[CAMSlashMaskView layoutSubviews];
-[CAMSlashMaskView initWithFrame:];
-[CAMSlashMaskView _shapeLayer];
-[CAMSlashMaskView setSlashBounds:];
-[CAMSlashMaskView _legibilityWeightChanged];
-[CAMSlashMaskView _updateShapeLayerAnimated:];
-[CAMSlashMaskView setSlashBounds:animated:];
-[CAMSlashMaskView slashBounds];
-[CAMSlashMaskView updateMaskAnimated];
```
