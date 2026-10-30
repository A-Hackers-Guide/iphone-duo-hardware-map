# `CDRichComplicationProgressView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CLKMonochromeFilterProvider`, `CLKMonochromeComplicationView`
- 18 instance variables, 18 properties, 44 instance methods, 0 class methods

## Instance variables

```
q _family;
@"CLKDevice" _device;
@"NSNumber" _updateToken;
f _currentBackgroundViewAlphaPercentage;
B _enabled;
B _showHolePunch;
B _showIndicatorView;
B _showAlternateIndicatorColor;
@"<CLKMonochromeFilterProvider>" _filterProvider;
@"NSArray" _gradientColors;
d _progress;
q _style;
@"CLKGaugeProvider" _gaugeProvider;
@"UIView" _indicatorView;
@"CDRichComplicationShapeView" _backgroundView;
@"CDRichComplicationShapeView" _foregroundView;
@"UIView" _ringView;
@"CAShapeLayer" _ringLayer;
```

## Properties

```
@property (TB,N,V_showHolePunch) showHolePunch;
@property (TB,N,V_showIndicatorView) showIndicatorView;
@property (TB,N,V_showAlternateIndicatorColor) showAlternateIndicatorColor;
@property (T@"UIView",&,N,V_indicatorView) indicatorView;
@property (T@"CDRichComplicationShapeView",R,N,V_backgroundView) backgroundView;
@property (T@"CDRichComplicationShapeView",R,N,V_foregroundView) foregroundView;
@property (T@"UIView",R,N,V_ringView) ringView;
@property (T@"CAShapeLayer",R,N,V_ringLayer) ringLayer;
@property (T@"NSArray",&,N,V_gradientColors) gradientColors;
@property (Td,N,V_progress) progress;
@property (TB,N,V_enabled) enabled;
@property (Tq,N,V_style) style;
@property (T@"CLKGaugeProvider",&,N,V_gaugeProvider) gaugeProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<CLKMonochromeFilterProvider>",W,N,V_filterProvider) filterProvider;
```

## Instance methods

```
-[CDRichComplicationProgressView foregroundView];
-[CDRichComplicationProgressView setProgress:];
-[CDRichComplicationProgressView enabled];
-[CDRichComplicationProgressView dealloc];
-[CDRichComplicationProgressView layoutSubviews];
-[CDRichComplicationProgressView style];
-[CDRichComplicationProgressView setStyle:];
-[CDRichComplicationProgressView progress];
-[CDRichComplicationProgressView setEnabled:];
-[CDRichComplicationProgressView setIndicatorView:];
-[CDRichComplicationProgressView backgroundView];
-[CDRichComplicationProgressView indicatorView];
-[CDRichComplicationProgressView gradientColors];
-[CDRichComplicationProgressView ringLayer];
-[CDRichComplicationProgressView setGradientColors:];
-[CDRichComplicationProgressView gaugeProvider];
-[CDRichComplicationProgressView setGaugeProvider:];
-[CDRichComplicationProgressView _applyStyle];
-[CDRichComplicationProgressView ringView];
-[CDRichComplicationProgressView backgroundColorForView:];
-[CDRichComplicationProgressView colorForView:accented:];
-[CDRichComplicationProgressView filterForView:style:];
-[CDRichComplicationProgressView filterForView:style:fraction:];
-[CDRichComplicationProgressView filterProvider];
-[CDRichComplicationProgressView filtersForView:style:];
-[CDRichComplicationProgressView filtersForView:style:fraction:];
-[CDRichComplicationProgressView initForFamily:device:backgroundShapeView:foregroundShapeView:];
-[CDRichComplicationProgressView interpolatedColorForView:];
-[CDRichComplicationProgressView overrideBackgroundGradientColorsForGradientColors:];
-[CDRichComplicationProgressView overrideBackgroundGradientColorsForGradientColors:locations:];
-[CDRichComplicationProgressView setFilterProvider:];
-[CDRichComplicationProgressView transitionToMonochromeWithFraction:];
-[CDRichComplicationProgressView updateMonochromeColor];
-[CDRichComplicationProgressView setShowAlternateIndicatorColor:];
-[CDRichComplicationProgressView _adjustBackgroundViewAlphaWithPercentage:];
-[CDRichComplicationProgressView _updateRingShape];
-[CDRichComplicationProgressView _updateUIFromGaugeProvider];
-[CDRichComplicationProgressView animateToProgress:duration:];
-[CDRichComplicationProgressView setGradientColors:locations:];
-[CDRichComplicationProgressView setShowHolePunch:];
-[CDRichComplicationProgressView setShowIndicatorView:];
-[CDRichComplicationProgressView showAlternateIndicatorColor];
-[CDRichComplicationProgressView showHolePunch];
-[CDRichComplicationProgressView showIndicatorView];
```
