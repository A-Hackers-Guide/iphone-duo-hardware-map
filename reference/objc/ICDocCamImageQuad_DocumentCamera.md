# `ICDocCamImageQuad`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ICDocCamImageQuad`, `NSSecureCoding`
- 5 instance variables, 17 properties, 42 instance methods, 3 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _topLeft;
{CGPoint="x"d"y"d} _topRight;
{CGPoint="x"d"y"d} _bottomLeft;
{CGPoint="x"d"y"d} _bottomRight;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBox;
```

## Properties

```
@property (T{CGPoint=dd},N,V_topLeft) topLeft;
@property (T{CGPoint=dd},N,V_topRight) topRight;
@property (T{CGPoint=dd},N,V_bottomLeft) bottomLeft;
@property (T{CGPoint=dd},N,V_bottomRight) bottomRight;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_boundingBox) boundingBox;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (TB,R,N) isConvex;
@property (TB,R,N) containsIntersectingLines;
@property (TB,R,N) containsPointsLessThanDistanceThreshold;
@property (TB,R,N) containsPointOutsideOfExtendedImageBounds;
@property (TB,R,N) containsAngleOutOfValidThreshold;
@property (Td,R,N) mininumAllowedDistanceBetweenPoints;
@property (TB,R,N) isValid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ICDocCamImageQuad supportsSecureCoding];
+[ICDocCamImageQuad quadFromCGRect:];
+[ICDocCamImageQuad quadFromVNRectangle:];
```

## Instance methods

```
-[ICDocCamImageQuad topRight];
-[ICDocCamImageQuad setBoundingBox:];
-[ICDocCamImageQuad bottomLeft];
-[ICDocCamImageQuad boundingBox];
-[ICDocCamImageQuad setTopLeft:];
-[ICDocCamImageQuad setBottomRight:];
-[ICDocCamImageQuad bottomRight];
-[ICDocCamImageQuad encodeWithCoder:];
-[ICDocCamImageQuad isValid];
-[ICDocCamImageQuad bounds];
-[ICDocCamImageQuad setTopRight:];
-[ICDocCamImageQuad description];
-[ICDocCamImageQuad initWithCoder:];
-[ICDocCamImageQuad setBottomLeft:];
-[ICDocCamImageQuad copyWithZone:];
-[ICDocCamImageQuad isEqual:];
-[ICDocCamImageQuad topLeft];
-[ICDocCamImageQuad containsIntersectingLines];
-[ICDocCamImageQuad initWithBottomLeft:bottomRight:topLeft:topRight:];
-[ICDocCamImageQuad intersectionOfLineFrom:to:withLineFrom:to:];
-[ICDocCamImageQuad normalizedQuadByConvertingFromView:toView:toViewSize:];
-[ICDocCamImageQuad quadByConvertingFromView:toView:isNormalized:];
-[ICDocCamImageQuad perspectiveCorrectedSize];
-[ICDocCamImageQuad addPointToQuadPoints:];
-[ICDocCamImageQuad applyOrientation:boundingBox:];
-[ICDocCamImageQuad clampQuadToRect:];
-[ICDocCamImageQuad containsAngleOutOfValidThreshold];
-[ICDocCamImageQuad containsAngleOutOfValidThreshold:];
-[ICDocCamImageQuad containsPointOutsideOfExtendedImageBounds];
-[ICDocCamImageQuad containsPointsLessThanDistanceThreshold];
-[ICDocCamImageQuad flipPointsWithSourceFrame:];
-[ICDocCamImageQuad flippedQuadFromSourceFrame:];
-[ICDocCamImageQuad imageQuadByScalingBy:];
-[ICDocCamImageQuad insertAndClipTopBy:];
-[ICDocCamImageQuad isConvex];
-[ICDocCamImageQuad mininumAllowedDistanceBetweenPoints];
-[ICDocCamImageQuad orientIfNecessary];
-[ICDocCamImageQuad pointRotatedClockwiseAroundOrigin:];
-[ICDocCamImageQuad removeOrientation:boundingBox:];
-[ICDocCamImageQuad rotatePointsByOrientation:];
-[ICDocCamImageQuad rotatePointsClockwise];
-[ICDocCamImageQuad rotatePointsRemovingOrientation:];
```
