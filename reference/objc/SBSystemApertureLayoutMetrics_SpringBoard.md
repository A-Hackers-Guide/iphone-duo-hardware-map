# `SBSystemApertureLayoutMetrics`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUISystemApertureLayoutMetrics`
- 0 instance variables, 1 properties, 11 instance methods, 1 class methods

## Properties

```
@property (TQ,R,N) sensorVariant;
```

## Class methods

```
+[SBSystemApertureLayoutMetrics metricsForWindowScene:];
```

## Instance methods

```
-[SBSystemApertureLayoutMetrics initUniqueInstanceWithWindowScene:];
-[SBSystemApertureLayoutMetrics _realSensorSize];
-[SBSystemApertureLayoutMetrics _edgeInsetsForSensorWithOrientation:prefersHorizontalStatusBar:];
-[SBSystemApertureLayoutMetrics _displayPointsPerCanvasPoint];
-[SBSystemApertureLayoutMetrics blankingRegionGeometryForIdentifier:];
-[SBSystemApertureLayoutMetrics frameForBlankingRegionWithIdentifier:];
-[SBSystemApertureLayoutMetrics frameForIndicatorAboveRegionWithIdentifier:];
-[SBSystemApertureLayoutMetrics frameForSensorRegionInBounds:orientation:prefersHorizontalStatusBar:];
-[SBSystemApertureLayoutMetrics maximumPersistentFrameInBounds:orientation:];
-[SBSystemApertureLayoutMetrics screenEdgeInsetsWithOrientation:prefersHorizontalStatusBar:];
-[SBSystemApertureLayoutMetrics sensorVariant];
```
