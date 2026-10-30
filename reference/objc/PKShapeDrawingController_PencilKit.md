# `PKShapeDrawingController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 26 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
{vector<ClipperLib::IntPoint, std::allocator<ClipperLib::IntPoint>>="__begin_"^{IntPoint}"__end_"^{IntPoint}""{?="__cap_"^{IntPoint}}} _currentStrokePoints;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentStrokeBounds;
B _closedShapeDetected;
B _stopGestureDetected;
B _hasDetected;
B _shouldDetect;
{vector<TimestampedPoint, std::allocator<TimestampedPoint>>="__begin_"^{TimestampedPoint}"__end_"^{TimestampedPoint}""{?="__cap_"^{TimestampedPoint}}} _timestampedPoints;
{vector<TimestampedAngles, std::allocator<TimestampedAngles>>="__begin_"^{TimestampedAngles}"__end_"^{TimestampedAngles}""{?="__cap_"^{TimestampedAngles}}} _timestampedAngles;
@"PKAveragePointGenerator" _averageInputPointGenerator;
Q _numInputPoints;
d _strokeStartTime;
d _latestAddedPointTime;
d _strokeDuration;
d _minimumRecognitionDelay;
d _maximumRecognitionDelay;
d _maximumFastRecognitionDelay;
d _previousRecognitionTimestamp;
B _smartFillEnabled;
B _shapeRecognitionOn;
B _fastDetectionEnabled;
B _fastDetectionAllowedForInkAndInputType;
@"<PKShapeDrawingControllerDelegate>" _delegate;
@"PKShape" _detectedShape;
@"PKStrokeRenderMask" _smartFillRenderMask;
@"NSUUID" _smartFillGroupID;
@"CHRecognizer" _shapeRecognizer;
```
