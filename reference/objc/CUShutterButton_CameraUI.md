# `CUShutterButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- 17 instance variables, 19 properties, 52 instance methods, 5 class methods

## Instance variables

```
B _spinning;
B _showDisabled;
q _mode;
@"<CAMShutterButtonDelegate>" _delegate;
@"UIColor" _contentColor;
@"UIColor" _stopModeBackgroundColor;
@"CAMShutterButtonRingView" __outerView;
@"UIImageView" __outerImageView;
@"UIView" __glassBackground;
@"CAMTimelapseShutterRingView" __timelapseOuterView;
@"UIView" __innerView;
@"UIView" __innerViewContrastView;
@"UIView" __stopModeBackground;
@"UIView" __spinnerView;
q _layoutStyle;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _tappableEdgeInsets;
{CAMShutterButtonSpec="outerRingDiameter"d"outerRingStrokeWidth"d"stopSquareSideLength"d"stopSquareCornerRadius"d"interRingSpacing"d} _spec;
```

## Properties

```
@property (T@"CAMShutterButtonRingView",R,N,V__outerView) _outerView;
@property (T@"UIImageView",R,N,V__outerImageView) _outerImageView;
@property (T@"UIView",R,N,V__glassBackground) _glassBackground;
@property (T@"CAMTimelapseShutterRingView",R,N,V__timelapseOuterView) _timelapseOuterView;
@property (T@"UIView",R,N,V__innerView) _innerView;
@property (T@"UIView",R,N,V__innerViewContrastView) _innerViewContrastView;
@property (T@"UIView",&,N,V__stopModeBackground) _stopModeBackground;
@property (T@"UIView",&,N,V__spinnerView) _spinnerView;
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (T{CAMShutterButtonSpec=ddddd},N,V_spec) spec;
@property (Tq,N) layoutStyle;
@property (T{CAMShutterButtonSpec=ddddd},N) spec;
@property (Tq,N,V_mode) mode;
@property (T@"<CAMShutterButtonDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisSpinning,V_spinning) spinning;
@property (TB,N,V_showDisabled) showDisabled;
@property (T{UIEdgeInsets=dddd},N,V_tappableEdgeInsets) tappableEdgeInsets;
@property (T@"UIColor",&,N,V_contentColor) contentColor;
@property (T@"UIColor",&,N,V_stopModeBackgroundColor) stopModeBackgroundColor;
```

## Class methods

```
+[CUShutterButton shutterButton];
+[CUShutterButton shutterButtonWithLayoutStyle:];
+[CUShutterButton shutterButtonWithSpec:];
+[CUShutterButton smallShutterButton];
+[CUShutterButton smallShutterButtonWithLayoutStyle:];
```

## Instance methods

```
-[CUShutterButton setLayoutStyle:];
-[CUShutterButton setSpec:];
-[CUShutterButton layoutStyle];
-[CUShutterButton setContentColor:];
-[CUShutterButton setSpinning:];
-[CUShutterButton intrinsicContentSize];
-[CUShutterButton _contentColor];
-[CUShutterButton alignmentRectInsets];
-[CUShutterButton spec];
-[CUShutterButton showDisabled];
-[CUShutterButton layoutSubviews];
-[CUShutterButton hitTest:withEvent:];
-[CUShutterButton contentColor];
-[CUShutterButton setMode:];
-[CUShutterButton sizeThatFits:];
-[CUShutterButton setDelegate:];
-[CUShutterButton setHighlighted:];
-[CUShutterButton setShowDisabled:];
-[CUShutterButton _spinnerView];
-[CUShutterButton mode];
-[CUShutterButton setTappableEdgeInsets:];
-[CUShutterButton delegate];
-[CUShutterButton _updateSpinningAnimations];
-[CUShutterButton initWithCoder:];
-[CUShutterButton _performHighlightAnimation];
-[CUShutterButton tappableEdgeInsets];
-[CUShutterButton isSpinning];
-[CUShutterButton set_spinnerView:];
-[CUShutterButton initWithFrame:];
-[CUShutterButton _outerImageForMode:layoutStyle:];
-[CUShutterButton initWithFrame:layoutStyle:spec:];
-[CUShutterButton _outerImageView];
-[CUShutterButton _commonCAMShutterButtonInitializationWithLayoutStyle:spec:];
-[CUShutterButton _cornerRadiusForMode:];
-[CUShutterButton _glassBackground];
-[CUShutterButton _innerCircleColorForMode:spinning:];
-[CUShutterButton _innerView];
-[CUShutterButton _innerViewContrastView];
-[CUShutterButton _isSpinningSupportedForLayoutStyle:];
-[CUShutterButton _outerView];
-[CUShutterButton _performModeSwitchAnimationFromMode:toMode:animated:];
-[CUShutterButton _shouldShowBackgroundViewForMode:];
-[CUShutterButton _shouldShowContrastBorderForMode:layoutStyle:];
-[CUShutterButton _sizeForMode:];
-[CUShutterButton _stopModeBackground];
-[CUShutterButton _timelapseOuterView];
-[CUShutterButton _timelapseRingSpecForLayoutStyle:];
-[CUShutterButton _updateOuterAndInnerLayers];
-[CUShutterButton setMode:animated:];
-[CUShutterButton setStopModeBackgroundColor:];
-[CUShutterButton set_stopModeBackground:];
-[CUShutterButton stopModeBackgroundColor];
```
