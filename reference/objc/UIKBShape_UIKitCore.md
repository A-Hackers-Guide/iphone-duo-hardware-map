# `UIKBShape`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `NSCopying`
- 8 instance variables, 8 properties, 35 instance methods, 3 class methods

## Instance variables

```
@"UIKBGeometry" m_geometry;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} m_frame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} m_paddedFrame;
Q m_concaveCorner;
{CGSize="width"d"height"d} m_concaveCornerOffset;
Q m_uid;
B m_scaled;
@"UIKBShape" m_originalShape;
```

## Properties

```
@property (TB,N,Vm_scaled) scaled;
@property (T@"UIKBShape",&,N,Vm_originalShape) originalShape;
@property (T@"UIKBGeometry",&,N,Vm_geometry) geometry;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,Vm_frame) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,Vm_paddedFrame) paddedFrame;
@property (TQ,N,Vm_concaveCorner) concaveCorner;
@property (T{CGSize=dd},N,Vm_concaveCornerOffset) concaveCornerOffset;
@property (TQ,R,N,Vm_uid) uid;
```

## Class methods

```
+[UIKBShape shape];
+[UIKBShape shapeByCombining:withShape:];
+[UIKBShape shapeByResizingShape:byAmount:];
```

## Instance methods

```
-[UIKBShape setConcaveCorner:];
-[UIKBShape paddedFrame];
-[UIKBShape setPaddedFrame:];
-[UIKBShape scaled];
-[UIKBShape concaveCorner];
-[UIKBShape addRectFrom:];
-[UIKBShape init];
-[UIKBShape makeLikeOther:];
-[UIKBShape setConcaveCornerOffset:];
-[UIKBShape initWithGeometry:frame:paddedFrame:];
-[UIKBShape setConcaveCornerSize:];
-[UIKBShape _scaleRect:inYAxis:];
-[UIKBShape geometry];
-[UIKBShape scaleWidth:];
-[UIKBShape setGeometry:];
-[UIKBShape addRectFrom:widthFraction:heightFraction:adjustOriginXFactor:adjustOriginYFactor:absoluteOriginFactors:];
-[UIKBShape initWithGeometry:frame:paddedFrame:concaveCorner:concaveCornerOffset:];
-[UIKBShape originalShape];
-[UIKBShape setOriginalShape:];
-[UIKBShape addRectFrom:mergeActionFactors:inRightToLeft:];
-[UIKBShape isEmpty];
-[UIKBShape encodeWithCoder:];
-[UIKBShape setFrame:];
-[UIKBShape hash];
-[UIKBShape description];
-[UIKBShape initWithCoder:];
-[UIKBShape addRectFrom:widthFraction:heightFraction:adjustOriginXFactor:adjustOriginYFactor:];
-[UIKBShape uid];
-[UIKBShape shouldUseGeometry];
-[UIKBShape copyWithZone:];
-[UIKBShape isEqual:];
-[UIKBShape scaleIfNeeded:onlyYAxis:];
-[UIKBShape setScaled:];
-[UIKBShape concaveCornerOffset];
-[UIKBShape frame];
```
