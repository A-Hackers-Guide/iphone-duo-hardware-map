# `UIBezierPath`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 16 instance variables, 10 properties, 65 instance methods, 21 class methods

## Instance variables

```
^{CGPath=} _path;
^d _lineDashPattern;
Q _lineDashPatternCount;
d _lineWidth;
d _miterLimit;
d _flatness;
d _lineDashPhase;
i _lineCapStyle;
i _lineJoinStyle;
B _usesEvenOddFillRule;
^{CGPath=} _immutablePath;
B _immutablePathIsValid;
B _isRoundedRect;
B _hasContinuousCorners;
Q _cornerMask;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _rawCornerRadii;
```

## Properties

```
@property (T^{CGPath=},N) CGPath;
@property (TB,R,GisEmpty) empty;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T{CGPoint=dd},R,N) currentPoint;
@property (Td,N,V_lineWidth) lineWidth;
@property (Ti,N,V_lineCapStyle) lineCapStyle;
@property (Ti,N,V_lineJoinStyle) lineJoinStyle;
@property (Td,N,V_miterLimit) miterLimit;
@property (Td,N,V_flatness) flatness;
@property (TB,N,V_usesEvenOddFillRule) usesEvenOddFillRule;
```

## Class methods

```
+[UIBezierPath supportsSecureCoding];
+[UIBezierPath _bezierPathWithArcRoundedRect:cornerRadius:];
+[UIBezierPath _bezierPathWithPillRect:cornerRadius:];
+[UIBezierPath _bezierPathWithRoundedRect:byRoundingCorners:cornerRadius:];
+[UIBezierPath _continuousRoundedCARectBezierPath:withRoundedCorners:cornerRadius:segments:];
+[UIBezierPath _continuousRoundedRectBezierPath:withRoundedCorners:cornerRadii:segments:smoothPillShapes:clampCornerRadii:];
+[UIBezierPath _continuousRoundedRectBezierPath:withRoundedCorners:cornerRadius:segments:];
+[UIBezierPath _roundedRectBezierPath:withRoundedCorners:cornerRadius:segments:];
+[UIBezierPath _roundedRectBezierPath:withRoundedCorners:cornerRadius:segments:legacyCorners:];
+[UIBezierPath bezierPath];
+[UIBezierPath bezierPathWithArcCenter:radius:startAngle:endAngle:clockwise:];
+[UIBezierPath bezierPathWithCGPath:];
+[UIBezierPath bezierPathWithOvalInRect:];
+[UIBezierPath bezierPathWithRect:];
+[UIBezierPath bezierPathWithRoundedRect:byRoundingCorners:cornerRadii:];
+[UIBezierPath bezierPathWithRoundedRect:cornerRadius:];
+[UIBezierPath roundedRectBezierPath:withRoundedCorners:withCornerRadii:];
+[UIBezierPath roundedRectBezierPath:withRoundedCorners:withCornerRadius:];
+[UIBezierPath roundedRectBezierPath:withRoundedEdges:];
+[UIBezierPath roundedRectBezierPath:withTopCornerRadius:withBottomCornerRadius:];
+[UIBezierPath shadowBezierPath:withRoundedEdges:];
```

## Instance methods

```
-[UIBezierPath lineWidth];
-[UIBezierPath setLineWidth:];
-[UIBezierPath _cornerRadius];
-[UIBezierPath init];
-[UIBezierPath dealloc];
-[UIBezierPath _cornerRadii];
-[UIBezierPath isEmpty];
-[UIBezierPath encodeWithCoder:];
-[UIBezierPath bounds];
-[UIBezierPath description];
-[UIBezierPath initWithCoder:];
-[UIBezierPath flatness];
-[UIBezierPath copyWithZone:];
-[UIBezierPath isEqual:];
-[UIBezierPath clip];
-[UIBezierPath setFlatness:];
-[UIBezierPath containsPoint:];
-[UIBezierPath miterLimit];
-[UIBezierPath setMiterLimit:];
-[UIBezierPath CGPath];
-[UIBezierPath addClip];
-[UIBezierPath addLineToPoint:];
-[UIBezierPath applyTransform:];
-[UIBezierPath removeAllPoints];
-[UIBezierPath appendBezierPathWithOvalInRect:];
-[UIBezierPath _addRoundedCornerWithTrueCorner:radius:corner:clockwise:];
-[UIBezierPath _addRoundedCornerWithTrueCorner:radius:corner:clockwise:leadInIsContinuous:leadOutIsContinuous:];
-[UIBezierPath _bezierPathConvertedFromCoordinateSpace:toCoordinateSpace:];
-[UIBezierPath _cornerMask];
-[UIBezierPath _createMutablePathByDecodingData:];
-[UIBezierPath _hasContinuousCorners];
-[UIBezierPath _hasUniformCornerRadii];
-[UIBezierPath _initWithCGMutablePath:];
-[UIBezierPath _invalidatePathMetadata];
-[UIBezierPath _invalidatePathMetadataIncludingCornerRadius:];
-[UIBezierPath _isRoundedRect];
-[UIBezierPath _mutablePath];
-[UIBezierPath _objcCodeDescription];
-[UIBezierPath _pathRef];
-[UIBezierPath addArcWithCenter:radius:startAngle:endAngle:clockwise:];
-[UIBezierPath addCurveToPoint:controlPoint1:controlPoint2:];
-[UIBezierPath addQuadCurveToPoint:controlPoint:];
-[UIBezierPath appendBezierPath:];
-[UIBezierPath appendBezierPathWithArcWithCenter:radius:startAngle:endAngle:clockwise:];
-[UIBezierPath appendBezierPathWithOvalInRect:transform:];
-[UIBezierPath appendBezierPathWithRect:];
-[UIBezierPath appendPath:];
-[UIBezierPath bezierPathByReversingPath];
-[UIBezierPath closePath];
-[UIBezierPath currentPoint];
-[UIBezierPath fill];
-[UIBezierPath fillWithBlendMode:alpha:];
-[UIBezierPath getLineDash:count:phase:];
-[UIBezierPath lineCapStyle];
-[UIBezierPath lineJoinStyle];
-[UIBezierPath lineToPoint:];
-[UIBezierPath moveToPoint:];
-[UIBezierPath setCGPath:];
-[UIBezierPath setLineCapStyle:];
-[UIBezierPath setLineDash:count:phase:];
-[UIBezierPath setLineJoinStyle:];
-[UIBezierPath setUsesEvenOddFillRule:];
-[UIBezierPath stroke];
-[UIBezierPath strokeWithBlendMode:alpha:];
-[UIBezierPath usesEvenOddFillRule];
```
