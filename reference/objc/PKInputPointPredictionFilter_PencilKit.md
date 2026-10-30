# `PKInputPointPredictionFilter`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKInputPointBaseFilter`
- 5 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"PKInputPointPredictor" _predictor;
{?=""(?="point"{CGPoint="x"d"y"d}"location"{CGPoint="x"d"y"d})"force"d"azimuth"d"altitude"d"velocity"d"directionAngle"d"zPosition"d"timestamp"d"predicted"B"estimationUpdateIndex"q"length"d"distance"d"hasEstimatedAltitudeAndAzimuth"B"rollAngle"d"estimatedActiveInputProperties"q"estimatedActiveInputPropertiesExpectingUpdates"q} _fullPredictionTimeIntervalPoint;
{?=""(?="point"{CGPoint="x"d"y"d}"location"{CGPoint="x"d"y"d})"force"d"azimuth"d"altitude"d"velocity"d"directionAngle"d"zPosition"d"timestamp"d"predicted"B"estimationUpdateIndex"q"length"d"distance"d"hasEstimatedAltitudeAndAzimuth"B"rollAngle"d"estimatedActiveInputProperties"q"estimatedActiveInputPropertiesExpectingUpdates"q} _halfPredictionTimeIntervalPoint;
B _useHalfPredictionTimeInterval;
d _predictionTimeInterval;
```

## Instance methods

```
-[PKInputPointPredictionFilter resetFilter];
-[PKInputPointPredictionFilter addInputPoint:];
```
