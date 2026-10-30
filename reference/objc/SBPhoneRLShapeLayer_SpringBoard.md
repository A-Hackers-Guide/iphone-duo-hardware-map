# `SBPhoneRLShapeLayer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAShapeLayer`
- 4 instance variables, 2 properties, 11 instance methods, 9 class methods

## Instance variables

```
@"CAShapeLayer" _glowLayer;
@"CAShapeLayer" _glowMask;
@"CAFilter" _glowBlur;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _apertureFrame;
```

## Properties

```
@property (Td,D,N) phoneRLWidth;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_apertureFrame) apertureFrame;
```

## Class methods

```
+[SBPhoneRLShapeLayer needsDisplayForKey:];
+[SBPhoneRLShapeLayer _notchEdgeForAperture:inBounds:];
+[SBPhoneRLShapeLayer _addContinuousCornerToPath:corner:tangentIn:tangentOut:];
+[SBPhoneRLShapeLayer _addCornerToPath:corner:tangentIn:tangentOut:controlFraction:];
+[SBPhoneRLShapeLayer _canonicalRectForRect:edge:inBounds:];
+[SBPhoneRLShapeLayer _canonicalSizeForEdge:actualSize:];
+[SBPhoneRLShapeLayer _cornerRadiusForWidth:];
+[SBPhoneRLShapeLayer _topEdgeCutoutPathWithBounds:aperture:width:];
+[SBPhoneRLShapeLayer _transformFromCanonicalForEdge:inBounds:];
```

## Instance methods

```
-[SBPhoneRLShapeLayer actionForKey:];
-[SBPhoneRLShapeLayer display];
-[SBPhoneRLShapeLayer setFillColor:];
-[SBPhoneRLShapeLayer init];
-[SBPhoneRLShapeLayer initWithLayer:];
-[SBPhoneRLShapeLayer _bezierPathForWidth:];
-[SBPhoneRLShapeLayer _innerGlowBezierPathForWidth:];
-[SBPhoneRLShapeLayer _presentationShapeLayer];
-[SBPhoneRLShapeLayer apertureFrame];
-[SBPhoneRLShapeLayer ringContainsPoint:extendedByInset:];
-[SBPhoneRLShapeLayer setApertureFrame:];
```
