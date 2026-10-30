# `CDRichComplicationSegmentedView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationCurveView`
- 1 instance variables, 1 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _segments;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_segments) segments;
```

## Class methods

```
+[CDRichComplicationSegmentedView isXL];
```

## Instance methods

```
-[CDRichComplicationSegmentedView segments];
-[CDRichComplicationSegmentedView setProgress:];
-[CDRichComplicationSegmentedView setSegments:];
-[CDRichComplicationSegmentedView setGradientColors:];
-[CDRichComplicationSegmentedView _setupShapeLayer:];
-[CDRichComplicationSegmentedView _shapeStrokeColor];
-[CDRichComplicationSegmentedView _addSegmentsToLayer:];
-[CDRichComplicationSegmentedView _arcAngleWithOuterRadius:segmentGapAngle:numberOfSegments:];
-[CDRichComplicationSegmentedView _colorForSegment:];
-[CDRichComplicationSegmentedView _segmentShapeStyleForIndex:angle:];
-[CDRichComplicationSegmentedView _updateSegmentsWithColors:];
-[CDRichComplicationSegmentedView setGradientColors:locations:];
```
