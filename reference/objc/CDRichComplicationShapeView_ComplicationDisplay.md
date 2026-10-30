# `CDRichComplicationShapeView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CLKMonochromeComplicationView`
- 14 instance variables, 8 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"CLKDevice" _device;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _previousBounds;
B _willUnfreezeForTransaction;
@"UIView" _filterView;
@"CALayer" _freezeLayer;
@"CAShapeLayer" _shapeLayer;
@"CAGradientLayer" _gradientLayer;
@"NSArray" _gradientColors;
@"NSArray" _filteredGradientColors;
@"NSArray" _gradientLocations;
d _monochromeFraction;
@"<CLKMonochromeFilterProvider>" _filterProvider;
d _progress;
q _filterStyle;
```

## Properties

```
@property (T@"NSArray",&,N,V_gradientColors) gradientColors;
@property (Td,N,V_progress) progress;
@property (Tq,R,N,V_filterStyle) filterStyle;
@property (T@"<CLKMonochromeFilterProvider>",W,N,V_filterProvider) filterProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CDRichComplicationShapeView shapeLayer];
-[CDRichComplicationShapeView setProgress:];
-[CDRichComplicationShapeView device];
-[CDRichComplicationShapeView layoutSubviews];
-[CDRichComplicationShapeView progress];
-[CDRichComplicationShapeView filterStyle];
-[CDRichComplicationShapeView gradientLayer];
-[CDRichComplicationShapeView _updateGradient];
-[CDRichComplicationShapeView _updatePath];
-[CDRichComplicationShapeView gradientColors];
-[CDRichComplicationShapeView setGradientColors:];
-[CDRichComplicationShapeView _shapeLineWidth];
-[CDRichComplicationShapeView _generatePath];
-[CDRichComplicationShapeView _normalizeGradientLocations:];
-[CDRichComplicationShapeView _pointAtProgress:];
-[CDRichComplicationShapeView _setupGradientLayer:];
-[CDRichComplicationShapeView _setupShapeLayer:];
-[CDRichComplicationShapeView _shapeStrokeColor];
-[CDRichComplicationShapeView _shouldReverseGradient];
-[CDRichComplicationShapeView filterProvider];
-[CDRichComplicationShapeView initForDevice:withFilterStyle:];
-[CDRichComplicationShapeView setFilterProvider:];
-[CDRichComplicationShapeView transitionToMonochromeWithFraction:];
-[CDRichComplicationShapeView updateMonochromeColor];
-[CDRichComplicationShapeView pointAtProgress:];
-[CDRichComplicationShapeView setGradientColors:locations:];
-[CDRichComplicationShapeView unfreezeForTransaction];
```
