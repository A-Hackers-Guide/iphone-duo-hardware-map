# `PKHoverController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKPencilObserverGestureRecognizerDelegate`, `PKInputPointAltitudeAndAzimuthEdgeFilterDelegate`
- 45 instance variables, 4 properties, 26 instance methods, 0 class methods

## Instance variables

```
{?="delegateSupportsDidBegin"b1"delegateSupportsDidUpdate"b1"delegateSupportsDidEndFromTouch"b1"delegateSupportsDidLift"b1"delegateSupportsHoldGestureMeanInputPointLatestInputPoint"b1"delegateSupportsHoldGestureEnded"b1"delegateSupportsIntentionalHoverWithDuration"b1"delegateSupportsShouldBeActiveAt"b1"delegateSupportsGestureBegan"b1"delegateSupportsGestureEnded"b1} _delegateFlags;
{?="gestureSupportsAzimuth"b1"gestureSupportsAltitude"b1"gestureSupportsTimestamp"b1"gestureSupportsHoverHeight"b1} _gestureRecognizerFlags;
@"UIView" _view;
{vector<PKInputPoint, std::allocator<PKInputPoint>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _inputPoints;
B _activeInputPoint;
B _activeHoverHold;
B _waitingForHoverHold;
d _waitingForHoverHoldTimestamp;
d _latestInputPointTimestamp;
d _latestHoldTimestamp;
d _latestInputPointSentTimestamp;
{?=""(?="point"{CGPoint="x"d"y"d}"location"{CGPoint="x"d"y"d})"force"d"azimuth"d"altitude"d"velocity"d"directionAngle"d"zPosition"d"timestamp"d"predicted"B"estimationUpdateIndex"q"length"d"distance"d"hasEstimatedAltitudeAndAzimuth"B"rollAngle"d"estimatedActiveInputProperties"q"estimatedActiveInputPropertiesExpectingUpdates"q} _cachedLatestInputPoint;
{CGPoint="x"d"y"d} _latestHoldLocation;
d _latestHoldZPosition;
@"UIView" _hoverLabelView;
Q _currentInputPointCounter;
@"UIHoverGestureRecognizer" _gestureRecognizer;
@"NSTimer" _eventGeneratorTimer;
d _previousRollValue;
@"PKInputPointWeightedAverageFilter" _weightedAverageFilter;
@"PKInputPointAltitudeAndAzimuthNoiseFilter" _altitudeAndAzimuthNoiseFilter;
@"PKInputPointAltitudeAndAzimuthBucketingFilter" _altitudeAndAzimuthBucketingFilter;
@"PKInputPointAltitudeAndAzimuthZLimitFilter" _altitudeAndAzimuthZLimitFilter;
@"PKInputPointAltitudeAndAzimuthEdgeFilter" _altitudeAndAzimuthEdgeFilter;
@"PKInputPointExtraLatencyFilter" _extraLatencyFilter;
@"PKInputPointReduceFramerateFilter" _reduceFramerateFilter;
@"PKInputPointPredictionFilter" _predictionFilter;
@"NSArray" _allInputPointFilters;
d _intentionalHoverStartTimestamp;
d _intentionalHoverMinZValue;
d _intentionalHoverMaxZValue;
B _didReceiveNewPointToPredict;
d _timestampForLatestGestureUpdate;
@"CADisplayLink" _displayLink;
B _useUpdateCycle;
^{_UIUpdateSequenceItemInternal=} _updateCycleItem;
B _shouldShowHoverDebugLayer;
B _hasSeenAnyHoverEvent;
B _hasSeenAnyHoverEventWithAltitude;
B _supportsHoverAndHoldActions;
B _shouldLogHoverEvents;
B _shouldGenerate120HzEvents;
@"<PKHoverControllerDelegate>" _delegate;
@"NSAttributedString" _currentLabel;
d _maximumTimeIntervalBetweenEvents;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKHoverController gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[PKHoverController gestureRecognizer:shouldReceiveTouch:];
-[PKHoverController dealloc];
-[PKHoverController gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[PKHoverController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[PKHoverController pauseDisplayLink];
-[PKHoverController _sendDidUpdate:];
-[PKHoverController resetFromTouch:];
-[PKHoverController _endIntentionalHoverTracking];
-[PKHoverController _handleHoverInputPoint:];
-[PKHoverController _hoverGesture:];
-[PKHoverController _sendDidUpdateNow:];
-[PKHoverController _setupHoverGestureRecognizerInView:];
-[PKHoverController _setupPredictorForNewPoint:];
-[PKHoverController _trackIntentionalHover:];
-[PKHoverController _triggerHoldGestureIfNecessary];
-[PKHoverController _updateInputPointFilters];
-[PKHoverController checkDidLiftAfterGestureEnd];
-[PKHoverController currentInputPoint];
-[PKHoverController currentMovementSpeed];
-[PKHoverController hideLabel];
-[PKHoverController inputPointFilter:distanceToEdge:];
-[PKHoverController logInputPoint:];
-[PKHoverController startDisplayLink];
-[PKHoverController updateCurrentInputPointWithInputPoint:];
-[PKHoverController vsync];
```
