# `CAMZoomPoint`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 8 properties, 11 instance methods, 7 class methods

## Instance variables

```
@"CAMZoomPoint" _baseZoomPoint;
d _zoomFactor;
d _displayZoomFactor;
q _customLens;
```

## Properties

```
@property (Tq,R,N,V_customLens) customLens;
@property (TB,R,N) isCustomLens;
@property (T@"CAMZoomPoint",R,N,V_baseZoomPoint) baseZoomPoint;
@property (T@"CAMZoomPoint",R,N) fundamentalZoomPoint;
@property (T@"NSArray",R,N) allZoomPoints;
@property (Td,R,N,V_zoomFactor) zoomFactor;
@property (Td,R,N,V_displayZoomFactor) displayZoomFactor;
@property (Td,R,N) displayFocalLength;
```

## Class methods

```
+[CAMZoomPoint significantIndexesInZoomPoints:];
+[CAMZoomPoint _canExtendFromCustomLens:toLens:withIntermediateLens:];
+[CAMZoomPoint displayZoomFactorsFromZoomPoints:];
+[CAMZoomPoint zoomFactorsFromZoomPoints:];
+[CAMZoomPoint zoomPointWithCustomLens:baseZoomPoint:];
+[CAMZoomPoint zoomPointWithFactor:displayed:];
+[CAMZoomPoint zoomPointsWithFactors:displayZoomFactors:customLensGroup:];
```

## Instance methods

```
-[CAMZoomPoint zoomFactor];
-[CAMZoomPoint description];
-[CAMZoomPoint isEqual:];
-[CAMZoomPoint allZoomPoints];
-[CAMZoomPoint baseZoomPoint];
-[CAMZoomPoint customLens];
-[CAMZoomPoint displayFocalLength];
-[CAMZoomPoint displayZoomFactor];
-[CAMZoomPoint fundamentalZoomPoint];
-[CAMZoomPoint isCustomLens];
-[CAMZoomPoint isEqualToZoomPoint:];
```
