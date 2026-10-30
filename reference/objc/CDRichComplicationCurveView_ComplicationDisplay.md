# `CDRichComplicationCurveView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationShapeView`
- 7 instance variables, 3 properties, 19 instance methods, 0 class methods

## Instance variables

```
d _curveWidth;
d _padding;
d _drawingBeginAngle;
d _drawingEndAngle;
B _clockwise;
d _beginAngle;
d _endAngle;
```

## Properties

```
@property (Td,N,V_beginAngle) beginAngle;
@property (Td,N,V_endAngle) endAngle;
@property (TB,N,V_clockwise) clockwise;
```

## Instance methods

```
-[CDRichComplicationCurveView layoutSubviews];
-[CDRichComplicationCurveView endAngle];
-[CDRichComplicationCurveView setEndAngle:];
-[CDRichComplicationCurveView _updatePath];
-[CDRichComplicationCurveView _centerPoint];
-[CDRichComplicationCurveView _outerRadius];
-[CDRichComplicationCurveView clockwise];
-[CDRichComplicationCurveView setClockwise:];
-[CDRichComplicationCurveView _shapeLineWidth];
-[CDRichComplicationCurveView _generatePath];
-[CDRichComplicationCurveView _normalizeGradientLocations:];
-[CDRichComplicationCurveView _pointAtProgress:];
-[CDRichComplicationCurveView _setupGradientLayer:];
-[CDRichComplicationCurveView _shouldReverseGradient];
-[CDRichComplicationCurveView _angleAtProgress:];
-[CDRichComplicationCurveView _totalDrawableAngle];
-[CDRichComplicationCurveView beginAngle];
-[CDRichComplicationCurveView initWithCurveWidth:padding:beginAngle:endAngle:forDevice:withFilterStyle:];
-[CDRichComplicationCurveView setBeginAngle:];
```
