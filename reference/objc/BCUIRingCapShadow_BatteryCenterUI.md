# `BCUIRingCapShadow`

- Image: [`/System/Library/PrivateFrameworks/BatteryCenterUI.framework/BatteryCenterUI`](../userland/System__Library__PrivateFrameworks__BatteryCenterUI.framework__BatteryCenterUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 3 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"UIImageView" _shadowCapImageView;
d _lineWidth;
d _arcFraction;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _ringBounds;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_ringBounds) ringBounds;
@property (Td,R,N,V_lineWidth) lineWidth;
@property (Td,N,V_arcFraction) arcFraction;
```

## Class methods

```
+[BCUIRingCapShadow _ringCapShadowImageWithRingBounds:lineWidth:scale:];
+[BCUIRingCapShadow ringCapShadowForRingWithBounds:lineWidth:];
```

## Instance methods

```
-[BCUIRingCapShadow lineWidth];
-[BCUIRingCapShadow layoutSubviews];
-[BCUIRingCapShadow _shadowCapFrame];
-[BCUIRingCapShadow setArcFraction:];
-[BCUIRingCapShadow _initWithRingBounds:lineWidth:];
-[BCUIRingCapShadow arcFraction];
-[BCUIRingCapShadow ringBounds];
```
