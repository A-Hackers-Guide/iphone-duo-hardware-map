# `PKAngularOpacitySlider`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`, `_PKColorAlphaSlider`
- 16 instance variables, 16 properties, 30 instance methods, 0 class methods

## Instance variables

```
^{CGPath=} _baseShapeLayerPathForHitTesting;
@"UIColor" _color;
q _colorUserInterfaceStyle;
@"<_PKColorAlphaSliderDelegate>" delegate;
d _maxAlpha;
d _minAlpha;
d _startAngle;
d _endAngle;
d _arcRadius;
d _arcWidth;
@"UIView" _colorView;
@"CAGradientLayer" _colorViewMaskLayer;
@"_PKCheckerGridView" _alphaGridView;
@"CAGradientLayer" _alphaGridViewMaskLayer;
@"PKPerforatedOpacitySliderKnobView" _sliderKnob;
@"CAShapeLayer" _baseShapeLayer;
```

## Properties

```
@property (T@"UIView",&,N,V_colorView) colorView;
@property (T@"CAGradientLayer",&,N,V_colorViewMaskLayer) colorViewMaskLayer;
@property (T@"_PKCheckerGridView",&,N,V_alphaGridView) alphaGridView;
@property (T@"CAGradientLayer",&,N,V_alphaGridViewMaskLayer) alphaGridViewMaskLayer;
@property (T@"PKPerforatedOpacitySliderKnobView",&,N,V_sliderKnob) sliderKnob;
@property (T@"CAShapeLayer",&,N,V_baseShapeLayer) baseShapeLayer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_PKColorAlphaSliderDelegate>",W,N,Vdelegate) delegate;
@property (T@"UIColor",&,N,V_color) color;
@property (Tq,N,V_colorUserInterfaceStyle) colorUserInterfaceStyle;
@property (TB,N) colorUserInterfaceStyleOnlyConvertsBlackAndWhite;
@property (Td,N,V_minAlpha) minAlpha;
@property (Td,N,V_maxAlpha) maxAlpha;
```

## Instance methods

```
-[PKAngularOpacitySlider setColor:];
-[PKAngularOpacitySlider gestureRecognizer:shouldReceiveTouch:];
-[PKAngularOpacitySlider dealloc];
-[PKAngularOpacitySlider layoutSubviews];
-[PKAngularOpacitySlider hitTest:withEvent:];
-[PKAngularOpacitySlider color];
-[PKAngularOpacitySlider sizeThatFits:];
-[PKAngularOpacitySlider setDelegate:];
-[PKAngularOpacitySlider delegate];
-[PKAngularOpacitySlider setColorView:];
-[PKAngularOpacitySlider colorView];
-[PKAngularOpacitySlider maxAlpha];
-[PKAngularOpacitySlider minAlpha];
-[PKAngularOpacitySlider setColorUserInterfaceStyle:];
-[PKAngularOpacitySlider setColor:animated:];
-[PKAngularOpacitySlider _colorViewTapGestureHandler:];
-[PKAngularOpacitySlider _didPanSliderKnob:];
-[PKAngularOpacitySlider alphaGridView];
-[PKAngularOpacitySlider alphaGridViewMaskLayer];
-[PKAngularOpacitySlider baseShapeLayer];
-[PKAngularOpacitySlider colorUserInterfaceStyle];
-[PKAngularOpacitySlider colorViewMaskLayer];
-[PKAngularOpacitySlider setAlphaGridView:];
-[PKAngularOpacitySlider setAlphaGridViewMaskLayer:];
-[PKAngularOpacitySlider setBaseShapeLayer:];
-[PKAngularOpacitySlider setColorViewMaskLayer:];
-[PKAngularOpacitySlider setMaxAlpha:];
-[PKAngularOpacitySlider setMinAlpha:];
-[PKAngularOpacitySlider setSliderKnob:];
-[PKAngularOpacitySlider sliderKnob];
```
