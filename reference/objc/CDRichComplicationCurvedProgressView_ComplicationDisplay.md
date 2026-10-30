# `CDRichComplicationCurvedProgressView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationProgressView`
- 7 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
d _curveWidth;
q _progressFillStyle;
@"CDRichComplicationCurveView" _backgroundView;
@"CDRichComplicationCurveView" _foregroundView;
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
-[CDRichComplicationCurvedProgressView setProgress:];
-[CDRichComplicationCurvedProgressView endAngle];
-[CDRichComplicationCurvedProgressView setEndAngle:];
-[CDRichComplicationCurvedProgressView clockwise];
-[CDRichComplicationCurvedProgressView setClockwise:];
-[CDRichComplicationCurvedProgressView colorForView:accented:];
-[CDRichComplicationCurvedProgressView filterForView:style:];
-[CDRichComplicationCurvedProgressView filterForView:style:fraction:];
-[CDRichComplicationCurvedProgressView filtersForView:style:];
-[CDRichComplicationCurvedProgressView filtersForView:style:fraction:];
-[CDRichComplicationCurvedProgressView initWithFamily:curveWidth:padding:beginAngle:endAngle:forDevice:withFilterStyle:progressFillStyle:];
-[CDRichComplicationCurvedProgressView overrideBackgroundGradientColorsForGradientColors:];
-[CDRichComplicationCurvedProgressView overrideBackgroundGradientColorsForGradientColors:locations:];
-[CDRichComplicationCurvedProgressView beginAngle];
-[CDRichComplicationCurvedProgressView setBeginAngle:];
```
