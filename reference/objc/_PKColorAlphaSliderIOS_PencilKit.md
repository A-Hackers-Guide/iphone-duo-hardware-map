# `_PKColorAlphaSliderIOS`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_PKColorAlphaSlider`
- 11 instance variables, 15 properties, 34 instance methods, 4 class methods

## Instance variables

```
B _colorUserInterfaceStyleOnlyConvertsBlackAndWhite;
@"UIColor" _color;
q _colorUserInterfaceStyle;
@"<_PKColorAlphaSliderDelegate>" delegate;
d _maxAlpha;
d _minAlpha;
@"UIView" _colorView;
@"CAGradientLayer" _colorViewMaskLayer;
@"_PKCheckerGridView" _alphaGridView;
@"CAGradientLayer" _alphaGridViewMaskLayer;
@"UIView" _sliderKnobView;
```

## Properties

```
@property (T@"UIView",&,N,V_colorView) colorView;
@property (T@"CAGradientLayer",&,N,V_colorViewMaskLayer) colorViewMaskLayer;
@property (T@"_PKCheckerGridView",&,N,V_alphaGridView) alphaGridView;
@property (T@"CAGradientLayer",&,N,V_alphaGridViewMaskLayer) alphaGridViewMaskLayer;
@property (T@"UIView",&,N,V_sliderKnobView) sliderKnobView;
@property (T@"<_PKColorAlphaSliderDelegate>",W,N,Vdelegate) delegate;
@property (T@"UIColor",&,N,V_color) color;
@property (Tq,N,V_colorUserInterfaceStyle) colorUserInterfaceStyle;
@property (TB,N,V_colorUserInterfaceStyleOnlyConvertsBlackAndWhite) colorUserInterfaceStyleOnlyConvertsBlackAndWhite;
@property (Td,N,V_minAlpha) minAlpha;
@property (Td,N,V_maxAlpha) maxAlpha;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_PKColorAlphaSliderIOS _layoutGradientMaskLayer:frame:isReversed:];
+[_PKColorAlphaSliderIOS _outputForResistanceFunction:factor:];
+[_PKColorAlphaSliderIOS opacitySliderHeight];
+[_PKColorAlphaSliderIOS rgbaColorFromColorIfPossible:];
```

## Instance methods

```
-[_PKColorAlphaSliderIOS setColor:];
-[_PKColorAlphaSliderIOS layoutSubviews];
-[_PKColorAlphaSliderIOS color];
-[_PKColorAlphaSliderIOS sizeThatFits:];
-[_PKColorAlphaSliderIOS setDelegate:];
-[_PKColorAlphaSliderIOS delegate];
-[_PKColorAlphaSliderIOS initWithFrame:];
-[_PKColorAlphaSliderIOS setColorView:];
-[_PKColorAlphaSliderIOS colorView];
-[_PKColorAlphaSliderIOS maxAlpha];
-[_PKColorAlphaSliderIOS minAlpha];
-[_PKColorAlphaSliderIOS didPanSliderKnob:];
-[_PKColorAlphaSliderIOS setColorUserInterfaceStyle:];
-[_PKColorAlphaSliderIOS setColor:animated:];
-[_PKColorAlphaSliderIOS _colorViewTapGestureHandler:];
-[_PKColorAlphaSliderIOS _knobViewFrameForColorAlpha:];
-[_PKColorAlphaSliderIOS _setColorNoLayout:];
-[_PKColorAlphaSliderIOS _sliderKnobViewWidth];
-[_PKColorAlphaSliderIOS _uiColorUserInterfaceStyle];
-[_PKColorAlphaSliderIOS alphaGridView];
-[_PKColorAlphaSliderIOS alphaGridViewMaskLayer];
-[_PKColorAlphaSliderIOS colorAlphaForSliderKnobXPosition:];
-[_PKColorAlphaSliderIOS colorUserInterfaceStyle];
-[_PKColorAlphaSliderIOS colorUserInterfaceStyleOnlyConvertsBlackAndWhite];
-[_PKColorAlphaSliderIOS colorViewMaskLayer];
-[_PKColorAlphaSliderIOS setAlphaGridView:];
-[_PKColorAlphaSliderIOS setAlphaGridViewMaskLayer:];
-[_PKColorAlphaSliderIOS setColorUserInterfaceStyleOnlyConvertsBlackAndWhite:];
-[_PKColorAlphaSliderIOS setColorViewMaskLayer:];
-[_PKColorAlphaSliderIOS setMaxAlpha:];
-[_PKColorAlphaSliderIOS setMinAlpha:];
-[_PKColorAlphaSliderIOS setSliderKnobView:];
-[_PKColorAlphaSliderIOS sliderKnobView];
-[_PKColorAlphaSliderIOS sliderKnobXPositionForColorAlpha:];
```
