# `CMOdometryManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
{InertialOdometryData="timestampSecs"d"state"{?="timestamp"Q"position"{?="x"f"y"f"z"f}"deltaVelocityCumSum"{?="x"f"y"f"z"f}"timestampPositionRollOver"Q"timestampVelocityRollOver"Q"timestampDeltaPositionUnavailable"[3Q]"timestampUninitialized"Q"attitude"[4f]"rotationArbitraryToTrueNorth"f"displacingState"C}} _previousOdometryData;
{InertialOdometryData="timestampSecs"d"state"{?="timestamp"Q"position"{?="x"f"y"f"z"f}"deltaVelocityCumSum"{?="x"f"y"f"z"f}"timestampPositionRollOver"Q"timestampVelocityRollOver"Q"timestampDeltaPositionUnavailable"[3Q]"timestampUninitialized"Q"attitude"[4f]"rotationArbitraryToTrueNorth"f"displacingState"C}} _currentOdometryData;
B _hasFirstSample;
Q _referenceFrame;
^{Dispatcher=^^?@} _odometryDispatcher;
d _odometryUpdateInterval;
@? _odometryHandler;
@"NSOperationQueue" _odometryQueue;
```

## Instance methods

```
-[CMOdometryManagerInternal init];
```
