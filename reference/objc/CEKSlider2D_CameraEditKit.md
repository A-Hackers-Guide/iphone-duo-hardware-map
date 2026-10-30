# `CEKSlider2D`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 17 instance variables, 17 properties, 45 instance methods, 1 class methods

## Instance variables

```
B _snapTouchesToDefaultValue;
B _pulsingValueIndicator;
B __active;
d _cornerRadius;
@"UIImage" _backgroundImage;
@"UIView" __backgroundSnapshotView1;
@"UIView" __backgroundSnapshotView2;
@"UIView" __backgroundSnapshotContainerView;
@"UIImageView" __backgroundImageView;
@"UIView" __gradientsView;
@"UIImageView" __gridView;
@"UIView" __valueIndicator;
@"UIView" __defaultValueIndicator;
@"UILongPressGestureRecognizer" __pressGestureRecognizer;
@"CEKSelectionFeedbackGenerator" __selectionFeedbackGenerator;
{CGPoint="x"d"y"d} _value;
{CGPoint="x"d"y"d} _defaultValue;
```

## Properties

```
@property (T@"UIView",R,N,V__backgroundSnapshotView1) _backgroundSnapshotView1;
@property (T@"UIView",R,N,V__backgroundSnapshotView2) _backgroundSnapshotView2;
@property (T@"UIView",R,N,V__backgroundSnapshotContainerView) _backgroundSnapshotContainerView;
@property (T@"UIImageView",R,N,V__backgroundImageView) _backgroundImageView;
@property (T@"UIView",R,N,V__gradientsView) _gradientsView;
@property (T@"UIImageView",R,N,V__gridView) _gridView;
@property (T@"UIView",R,N,V__valueIndicator) _valueIndicator;
@property (T@"UIView",R,N,V__defaultValueIndicator) _defaultValueIndicator;
@property (TB,N,V__active) _active;
@property (T@"UILongPressGestureRecognizer",R,N,V__pressGestureRecognizer) _pressGestureRecognizer;
@property (T@"CEKSelectionFeedbackGenerator",R,N,V__selectionFeedbackGenerator) _selectionFeedbackGenerator;
@property (T{CGPoint=dd},N,V_value) value;
@property (T{CGPoint=dd},N,V_defaultValue) defaultValue;
@property (TB,N,V_snapTouchesToDefaultValue) snapTouchesToDefaultValue;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (T@"UIImage",&,N,V_backgroundImage) backgroundImage;
@property (TB,N,GisPulsingValueIndicator,V_pulsingValueIndicator) pulsingValueIndicator;
```

## Class methods

```
+[CEKSlider2D backgroundImageWithImage:];
```

## Instance methods

```
-[CEKSlider2D setDefaultValue:];
-[CEKSlider2D _gridView];
-[CEKSlider2D setValue:animated:];
-[CEKSlider2D setBackgroundImage:];
-[CEKSlider2D backgroundImage];
-[CEKSlider2D defaultValue];
-[CEKSlider2D _active];
-[CEKSlider2D _handlePressGesture:];
-[CEKSlider2D value];
-[CEKSlider2D layoutSubviews];
-[CEKSlider2D setCornerRadius:];
-[CEKSlider2D setValue:];
-[CEKSlider2D cornerRadius];
-[CEKSlider2D setPulsingValueIndicator:];
-[CEKSlider2D initWithFrame:];
-[CEKSlider2D _backgroundImageView];
-[CEKSlider2D _selectionFeedbackGenerator];
-[CEKSlider2D _createGradientsViewIfNecessary];
-[CEKSlider2D _valueIndicator];
-[CEKSlider2D _backgroundSnapshotContainerView];
-[CEKSlider2D _backgroundSnapshotView1];
-[CEKSlider2D _backgroundSnapshotView2];
-[CEKSlider2D _blurFilter];
-[CEKSlider2D _createGridImageWithSize:];
-[CEKSlider2D _defaultValueIndicator];
-[CEKSlider2D _destroyGradientsViewIfNecessary];
-[CEKSlider2D _gradientsView];
-[CEKSlider2D _normalizedViewValueForValue:];
-[CEKSlider2D _performFeedback];
-[CEKSlider2D _prepareFeedback];
-[CEKSlider2D _pressGestureRecognizer];
-[CEKSlider2D _setActive:animated:];
-[CEKSlider2D _setValue:shouldNotify:animated:];
-[CEKSlider2D _shouldPerformFeedback];
-[CEKSlider2D _startScalingWithScale:duration:repeatCount:timingFunction:];
-[CEKSlider2D _stopScalingWithDuration:];
-[CEKSlider2D _updateGradientViews];
-[CEKSlider2D _valueForNormalizedViewValue:];
-[CEKSlider2D _wantsGradientLayers];
-[CEKSlider2D isPulsingValueIndicator];
-[CEKSlider2D setBackgroundAsSnapshotOfView:];
-[CEKSlider2D setBackgroundFromExistingSlider2D:];
-[CEKSlider2D setSnapTouchesToDefaultValue:];
-[CEKSlider2D set_active:];
-[CEKSlider2D snapTouchesToDefaultValue];
```
