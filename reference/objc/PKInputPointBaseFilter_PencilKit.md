# `PKInputPointBaseFilter`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKInputPointFilter`
- 3 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
d _maxZDistance;
q _numInputPoints;
{?=""(?="point"{CGPoint="x"d"y"d}"location"{CGPoint="x"d"y"d})"force"d"azimuth"d"altitude"d"velocity"d"directionAngle"d"zPosition"d"timestamp"d"predicted"B"estimationUpdateIndex"q"length"d"distance"d"hasEstimatedAltitudeAndAzimuth"B"rollAngle"d"estimatedActiveInputProperties"q"estimatedActiveInputPropertiesExpectingUpdates"q} _filteredPoint;
```

## Instance methods

```
-[PKInputPointBaseFilter init];
-[PKInputPointBaseFilter resetFilter];
-[PKInputPointBaseFilter addInputPoint:];
-[PKInputPointBaseFilter currentFilteredPoint];
```
