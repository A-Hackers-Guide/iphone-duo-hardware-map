# `UIKBRenderGeometry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 21 instance variables, 23 properties, 65 instance methods, 3 class methods

## Instance variables

```
B _detachedVariants;
B _tallPopup;
i _popupBias;
Q _concaveCorner;
Q _roundRectCorners;
d _roundRectRadius;
q _flickDirection;
@"NSValue" _splitLeftRect;
@"NSValue" _splitRightRect;
q _popupDirection;
d _layeredBackgroundRoundRectRadius;
d _layeredForegroundRoundRectRadius;
{CGPoint="x"d"y"d} _popupSource;
{CGSize="width"d"height"d} _concaveCornerOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _paddedFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _displayFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _symbolFrame;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _layoutMargins;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _layeredBackgroundPaddedFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _layeredForegroundPaddedFrame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_paddedFrame) paddedFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_displayFrame) displayFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_symbolFrame) symbolFrame;
@property (TQ,N,V_concaveCorner) concaveCorner;
@property (T{CGSize=dd},N,V_concaveCornerOffset) concaveCornerOffset;
@property (T{CGPoint=dd},N,V_popupSource) popupSource;
@property (Td,N,V_roundRectRadius) roundRectRadius;
@property (TQ,N,V_roundRectCorners) roundRectCorners;
@property (Ti,N,V_popupBias) popupBias;
@property (T{UIEdgeInsets=dddd},N,V_layoutMargins) layoutMargins;
@property (Tq,N,V_flickDirection) flickDirection;
@property (TB,N,V_detachedVariants) detachedVariants;
@property (TB,N,V_tallPopup) tallPopup;
@property (T@"NSValue",&,N,V_splitLeftRect) splitLeftRect;
@property (T@"NSValue",&,N,V_splitRightRect) splitRightRect;
@property (T{UIEdgeInsets=dddd},R,N) displayInsets;
@property (T{UIEdgeInsets=dddd},R,N) paddedInsets;
@property (Tq,N,V_popupDirection) popupDirection;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_layeredBackgroundPaddedFrame) layeredBackgroundPaddedFrame;
@property (Td,N,V_layeredBackgroundRoundRectRadius) layeredBackgroundRoundRectRadius;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_layeredForegroundPaddedFrame) layeredForegroundPaddedFrame;
@property (Td,N,V_layeredForegroundRoundRectRadius) layeredForegroundRoundRectRadius;
```

## Class methods

```
+[UIKBRenderGeometry geometryWithFrame:paddedFrame:];
+[UIKBRenderGeometry geometryWithShape:];
+[UIKBRenderGeometry sortedGeometries:leftToRight:];
```

## Instance methods

```
-[UIKBRenderGeometry setConcaveCorner:];
-[UIKBRenderGeometry paddedFrame];
-[UIKBRenderGeometry layoutMargins];
-[UIKBRenderGeometry setPaddedFrame:];
-[UIKBRenderGeometry concaveCorner];
-[UIKBRenderGeometry setLayeredBackgroundPaddedFrame:];
-[UIKBRenderGeometry displayInsets];
-[UIKBRenderGeometry roundRectCorners];
-[UIKBRenderGeometry copyForFlickDirection:scale:];
-[UIKBRenderGeometry setLayoutMargins:];
-[UIKBRenderGeometry iPhoneVariantGeometries:annotationIndex:];
-[UIKBRenderGeometry adjustForTranslucentGapsInFrameWithSize_10Key:centerX:bottomEdge:topEdge:inclusive:];
-[UIKBRenderGeometry setPopupDirection:];
-[UIKBRenderGeometry paddedInsets];
-[UIKBRenderGeometry setFlickDirection:];
-[UIKBRenderGeometry initWithShape:];
-[UIKBRenderGeometry setLayeredBackgroundRoundRectRadius:];
-[UIKBRenderGeometry adjustForConsistentGapsWithSize:inFrame:];
-[UIKBRenderGeometry setConcaveCornerOffset:];
-[UIKBRenderGeometry setSplitRightRect:];
-[UIKBRenderGeometry setSplitLeftRect:];
-[UIKBRenderGeometry copyForPopupDirection:scale:];
-[UIKBRenderGeometry setRoundRectCorners:];
-[UIKBRenderGeometry setLayeredForegroundRoundRectRadius:];
-[UIKBRenderGeometry splitLeftRect];
-[UIKBRenderGeometry popupSource];
-[UIKBRenderGeometry layeredBackgroundRoundRectRadius];
-[UIKBRenderGeometry iPadVariantGeometries:rowLimit:];
-[UIKBRenderGeometry applyOffset:];
-[UIKBRenderGeometry similarShape];
-[UIKBRenderGeometry symbolFrame];
-[UIKBRenderGeometry applyShadowInsets:];
-[UIKBRenderGeometry flickDirection];
-[UIKBRenderGeometry adjustForTranslucentGapsWithSize:inFrame:];
-[UIKBRenderGeometry layeredForegroundRoundRectRadius];
-[UIKBRenderGeometry setPopupBias:];
-[UIKBRenderGeometry tallPopup];
-[UIKBRenderGeometry setFrame:];
-[UIKBRenderGeometry layeredBackgroundPaddedFrame];
-[UIKBRenderGeometry setRoundRectRadius:];
-[UIKBRenderGeometry description];
-[UIKBRenderGeometry setLayeredForegroundPaddedFrame:];
-[UIKBRenderGeometry overlayWithGeometry:];
-[UIKBRenderGeometry splitRightRect];
-[UIKBRenderGeometry _copyForDirection:positionFactor:inwardSizeFactor:outwardSizeFactor:perpendicularSizeFactor:sizeAspectRatio:scale:];
-[UIKBRenderGeometry roundRectRadius];
-[UIKBRenderGeometry setSymbolFrame:];
-[UIKBRenderGeometry copyWithZone:];
-[UIKBRenderGeometry adjustToTopWithInsets:];
-[UIKBRenderGeometry displayFrame];
-[UIKBRenderGeometry detachedVariants];
-[UIKBRenderGeometry isEqual:];
-[UIKBRenderGeometry adjustForTranslucentGapsInFrameWithSize_10Key:centerX:bottomEdge:topEdge:];
-[UIKBRenderGeometry setTallPopup:];
-[UIKBRenderGeometry setDisplayFrame:];
-[UIKBRenderGeometry setPopupSource:];
-[UIKBRenderGeometry watchVariantGeometries:annotationIndex:];
-[UIKBRenderGeometry setDetachedVariants:];
-[UIKBRenderGeometry popupBias];
-[UIKBRenderGeometry popupDirection];
-[UIKBRenderGeometry applyInsets:];
-[UIKBRenderGeometry makeIntegralWithScale:];
-[UIKBRenderGeometry layeredForegroundPaddedFrame];
-[UIKBRenderGeometry concaveCornerOffset];
-[UIKBRenderGeometry frame];
```
