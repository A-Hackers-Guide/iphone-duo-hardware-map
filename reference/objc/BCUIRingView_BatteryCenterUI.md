# `BCUIRingView`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](../userland/System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 19 instance methods, 1 class methods

## Instance variables

```
d _ringStart;
d _ringEnd;
d _lineWidth;
@"UIColor" _strokeColor;
@"UIColor" _fillColor;
```

## Properties

```
@property (Td,N,V_ringStart) ringStart;
@property (Td,N,V_ringEnd) ringEnd;
@property (Td,N,V_lineWidth) lineWidth;
@property (T@"UIColor",C,N,V_strokeColor) strokeColor;
@property (T@"UIColor",C,N,V_fillColor) fillColor;
```

## Class methods

```
+[BCUIRingView layerClass];
```

## Instance methods

```
-[BCUIRingView setFractionComplete:];
-[BCUIRingView lineWidth];
-[BCUIRingView setLineWidth:];
-[BCUIRingView setFillColor:];
-[BCUIRingView fillColor];
-[BCUIRingView setStrokeColor:];
-[BCUIRingView layoutSubviews];
-[BCUIRingView strokeColor];
-[BCUIRingView mt_applyVisualStyling:];
-[BCUIRingView sizeThatFits:];
-[BCUIRingView setFrame:];
-[BCUIRingView _shouldAnimatePropertyWithKey:];
-[BCUIRingView initWithFrame:];
-[BCUIRingView _shapeLayer];
-[BCUIRingView _invalidatePath];
-[BCUIRingView ringEnd];
-[BCUIRingView ringStart];
-[BCUIRingView setRingEnd:];
-[BCUIRingView setRingStart:];
```
