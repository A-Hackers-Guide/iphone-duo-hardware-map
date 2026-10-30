# `UIPointerShape`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 15 properties, 29 instance methods, 8 class methods

## Instance variables

```
@"UIBezierPath" _path;
d _cornerRadius;
d _defaultCornerRadius;
d _beamLength;
Q _materialUsage;
q __type;
{CGPoint="x"d"y"d} _pinnedPoint;
{CGPoint="x"d"y"d} _inherentConstrainedSlip;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
```

## Properties

```
@property (T@"UIBezierPath",C,N,V_path) path;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect) rect;
@property (T{CGPoint=dd},N,V_pinnedPoint) pinnedPoint;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (Td,N,V_defaultCornerRadius) defaultCornerRadius;
@property (T{CGPoint=dd},N,V_inherentConstrainedSlip) inherentConstrainedSlip;
@property (Td,N,V_beamLength) beamLength;
@property (T{CGSize=dd},R,N) size;
@property (Td,R,N) effectiveCornerRadius;
@property (T@"NSString",R,N) cornerCurve;
@property (TB,R,N) isEmpty;
@property (TB,R,N) isCircle;
@property (TB,R,N) isElastic;
@property (TQ,N,V_materialUsage) materialUsage;
@property (Tq,N,S_setType:,V__type) _type;
```

## Class methods

```
+[UIPointerShape _elasticRectShapePinnedAtPoint:];
+[UIPointerShape _capsuleShapeWithRect:];
+[UIPointerShape _linkPointerShape];
+[UIPointerShape _shapeWithSymbol:pointSize:];
+[UIPointerShape beamWithPreferredLength:axis:];
+[UIPointerShape shapeWithPath:];
+[UIPointerShape shapeWithRoundedRect:];
+[UIPointerShape shapeWithRoundedRect:cornerRadius:];
```

## Instance methods

```
-[UIPointerShape _type];
-[UIPointerShape init];
-[UIPointerShape defaultCornerRadius];
-[UIPointerShape setCornerRadius:];
-[UIPointerShape size];
-[UIPointerShape rect];
-[UIPointerShape isEmpty];
-[UIPointerShape setRect:];
-[UIPointerShape cornerRadius];
-[UIPointerShape hash];
-[UIPointerShape description];
-[UIPointerShape setPath:];
-[UIPointerShape copyWithZone:];
-[UIPointerShape cornerCurve];
-[UIPointerShape isEqual:];
-[UIPointerShape _setType:];
-[UIPointerShape path];
-[UIPointerShape setPinnedPoint:];
-[UIPointerShape beamLength];
-[UIPointerShape effectiveCornerRadius];
-[UIPointerShape inherentConstrainedSlip];
-[UIPointerShape isCircle];
-[UIPointerShape isElastic];
-[UIPointerShape materialUsage];
-[UIPointerShape pinnedPoint];
-[UIPointerShape setBeamLength:];
-[UIPointerShape setDefaultCornerRadius:];
-[UIPointerShape setInherentConstrainedSlip:];
-[UIPointerShape setMaterialUsage:];
```
