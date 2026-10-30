# `PKStrokeProviderSlice`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHStroke`
- 4 instance variables, 13 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"CHEncodedStrokeIdentifier" _encodedStrokeIdentifier;
@"PKStrokeProviderSliceIdentifier" _identifier;
@"PKStroke" _stroke;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
```

## Properties

```
@property (T@"CHEncodedStrokeIdentifier",R,N,V_encodedStrokeIdentifier) encodedStrokeIdentifier;
@property (T@"PKStrokeProviderSliceIdentifier",R,N,V_identifier) identifier;
@property (T@"PKStroke",R,N,V_stroke) stroke;
@property (T@"<CHStrokeIdentifier>",R,N) strokeIdentifier;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds) bounds;
@property (TQ,R,N) strokeAttributes;
@property (Td,R,N) startTimestamp;
@property (Td,R,N) endTimestamp;
@property (TB,R,N) isFinished;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKStrokeProviderSlice isFinished];
-[PKStrokeProviderSlice identifier];
-[PKStrokeProviderSlice compareTo:];
-[PKStrokeProviderSlice startTimestamp];
-[PKStrokeProviderSlice hash];
-[PKStrokeProviderSlice bounds];
-[PKStrokeProviderSlice description];
-[PKStrokeProviderSlice endTimestamp];
-[PKStrokeProviderSlice isEqual:];
-[PKStrokeProviderSlice initWithIdentifier:];
-[PKStrokeProviderSlice stroke];
-[PKStrokeProviderSlice encodedStrokeIdentifier];
-[PKStrokeProviderSlice enumeratePointsWithDistanceStep:usingBlock:];
-[PKStrokeProviderSlice enumeratePointsWithTimestep:usingBlock:];
-[PKStrokeProviderSlice strokeAttributes];
-[PKStrokeProviderSlice strokeIdentifier];
-[PKStrokeProviderSlice _lastPointIndex];
-[PKStrokeProviderSlice _firstPointIndex];
-[PKStrokeProviderSlice _interpolatedPointForSplineSegment:t:transform:];
-[PKStrokeProviderSlice _interpolatedTimeForSplineSegment:t:];
-[PKStrokeProviderSlice _lengthOfSplineSegment:transform:];
-[PKStrokeProviderSlice _splineControlPoint:transform:];
-[PKStrokeProviderSlice _strokeLength];
-[PKStrokeProviderSlice enumeratePointsWithDataStep:usingBlock:];
-[PKStrokeProviderSlice initWithStroke:tStart:tEnd:];
```
