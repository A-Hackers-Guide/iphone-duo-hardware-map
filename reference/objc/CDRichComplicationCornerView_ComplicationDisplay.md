# `CDRichComplicationCornerView`

- Image: [`/System/Library/PrivateFrameworks/ComplicationDisplay.framework/ComplicationDisplay`](../userland/System__Library__PrivateFrameworks__ComplicationDisplay.framework__ComplicationDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CDRichComplicationTemplateView`
- Protocols: `CDRichComplicationCornerPositionable`
- 6 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
q _cornerComplicationPosition;
q _fontFallback;
@"UIBezierPath" _hitTestPath;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _hitTestBounds;
d _innerComponentRotationInDegree;
d _outerComponentRotationInDegree;
```

## Properties

```
@property (Td,N,V_innerComponentRotationInDegree) innerComponentRotationInDegree;
@property (Td,N,V_outerComponentRotationInDegree) outerComponentRotationInDegree;
@property (Tq,N,V_cornerComplicationPosition) cornerComplicationPosition;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CDRichComplicationCornerView viewSizeForDevice:];
```

## Instance methods

```
-[CDRichComplicationCornerView init];
-[CDRichComplicationCornerView pointInside:withEvent:];
-[CDRichComplicationCornerView initWithFamily:];
-[CDRichComplicationCornerView _createHitTestPathIfNecessary];
-[CDRichComplicationCornerView _transitToHighlightState:fraction:];
-[CDRichComplicationCornerView cornerComplicationPosition];
-[CDRichComplicationCornerView initWithFontFallback:];
-[CDRichComplicationCornerView setCornerComplicationPosition:];
-[CDRichComplicationCornerView _layoutCurvedLabel:centerAngleInDegree:editingRotationInDegree:];
-[CDRichComplicationCornerView _createAndAddColoringLabelWithFontSize:];
-[CDRichComplicationCornerView _fontWithSize:fontWeight:];
-[CDRichComplicationCornerView _fontWithSize:withFontDescriptor:];
-[CDRichComplicationCornerView _layoutView:origin:editingTranslation:editingRotationInDegree:];
-[CDRichComplicationCornerView _updateColoringLabel:withFontWeight:];
-[CDRichComplicationCornerView innerComponentRotationInDegree];
-[CDRichComplicationCornerView outerComponentRotationInDegree];
-[CDRichComplicationCornerView setInnerComponentRotationInDegree:];
-[CDRichComplicationCornerView setOuterComponentRotationInDegree:];
```
