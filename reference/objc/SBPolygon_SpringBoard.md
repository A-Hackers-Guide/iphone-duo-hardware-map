# `SBPolygon`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 7 properties, 33 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _mutablePoints;
@"NSMutableArray" _weights;
{CGPoint="x"d"y"d} _centroid;
{CGPoint="x"d"y"d} _weightedCentroid;
```

## Properties

```
@property (T@"NSMutableArray",&,N,G_points,S_setPoints:,V_mutablePoints) mutablePoints;
@property (T{CGPoint=dd},N,G_centroid,S_setCentroid:,V_centroid) centroid;
@property (Td,R,N,G_perimeter) perimeter;
@property (T@"NSMutableArray",&,N,G_weights,S_setWeights:,V_weights) weights;
@property (T{CGPoint=dd},N,G_weightedCentroid,S_setWeightedCentroid:,V_weightedCentroid) weightedCentroid;
@property (TQ,R,N) pointCount;
@property (Td,R,N) distanceOfFarthestPointFromCentroid;
```

## Class methods

```
+[SBPolygon _pointAtIndex:ofPointArray:];
+[SBPolygon _sortPoints:];
```

## Instance methods

```
-[SBPolygon pointCount];
-[SBPolygon _translate:];
-[SBPolygon _updateProperties];
-[SBPolygon description];
-[SBPolygon isEqual:];
-[SBPolygon _points];
-[SBPolygon points];
-[SBPolygon initWithPoints:];
-[SBPolygon _applyTransform:];
-[SBPolygon _weightAtIndex:];
-[SBPolygon _scale:];
-[SBPolygon _updateCentroid];
-[SBPolygon _baseOrientation];
-[SBPolygon _centroid];
-[SBPolygon _flipHorizontally];
-[SBPolygon _isLeftHanded];
-[SBPolygon _meanFingertipRowAngle];
-[SBPolygon _meanRadius];
-[SBPolygon _perimeter];
-[SBPolygon _pointAtIndex:];
-[SBPolygon _rotate:];
-[SBPolygon _setCentroid:];
-[SBPolygon _setPoints:];
-[SBPolygon _setWeightedCentroid:];
-[SBPolygon _setWeights:];
-[SBPolygon _thumbIndex];
-[SBPolygon _updateWeightedCentroid];
-[SBPolygon _updateWeights];
-[SBPolygon _weightedCentroid];
-[SBPolygon _weights];
-[SBPolygon distanceOfFarthestPointFromCentroid];
-[SBPolygon enumeratePointsUsingBlock:];
-[SBPolygon initWithPoints:pointCount:];
```
