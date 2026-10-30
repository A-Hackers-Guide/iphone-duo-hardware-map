# `CDRichComplicationRingView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationShapeView`
- Protocols: `CLKMonochromeComplicationView`
- 7 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
d _curveWidth;
d _padding;
@"UIView" _foregroundView;
@"CAShapeLayer" _headLayer;
@"CAShapeLayer" _tailLayer;
@"CAShapeLayer" _tailStrokeLayer;
B _clockwise;
```

## Properties

```
@property (TB,N,V_clockwise) clockwise;
@property (T@"<CLKMonochromeFilterProvider>",W,N) filterProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CDRichComplicationRingView _disabledLayerActions];
```

## Instance methods

```
-[CDRichComplicationRingView setProgress:];
-[CDRichComplicationRingView layoutSubviews];
-[CDRichComplicationRingView _updateGradient];
-[CDRichComplicationRingView clockwise];
-[CDRichComplicationRingView setClockwise:];
-[CDRichComplicationRingView _shapeLineWidth];
-[CDRichComplicationRingView _generatePath];
-[CDRichComplicationRingView _normalizeGradientLocations:];
-[CDRichComplicationRingView _pointAtProgress:];
-[CDRichComplicationRingView _setupGradientLayer:];
-[CDRichComplicationRingView _shouldReverseGradient];
-[CDRichComplicationRingView initWithCurveWidth:padding:forDevice:withFilterStyle:];
-[CDRichComplicationRingView transitionToMonochromeWithFraction:];
-[CDRichComplicationRingView updateMonochromeColor];
-[CDRichComplicationRingView _createHeadTailViewWithStartAngle:endAngle:clockwise:additionalWidth:];
-[CDRichComplicationRingView _layoutHeadTailView:forProgress:];
```
