# `UIKBShadowEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIKBRenderEffect`
- 5 instance variables, 12 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSString" _colorName;
d _weight;
{CGSize="width"d"height"d} _offset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _insets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _concaveInsets;
```

## Properties

```
@property (T{CGSize=dd},N,V_offset) offset;
@property (T{UIEdgeInsets=dddd},N,V_insets) insets;
@property (T{UIEdgeInsets=dddd},N,V_concaveInsets) concaveInsets;
@property (TB,R,N) isValid;
@property (TB,R,N) renderUnder;
@property (Td,N,V_weight) weight;
@property (TB,R,N) usesRGBColors;
@property (T@"UIKBGradient",R,N) gradient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBShadowEffect effectWithColor:offset:insets:weight:];
```

## Instance methods

```
-[UIKBShadowEffect gradient];
-[UIKBShadowEffect CGColor];
-[UIKBShadowEffect weight];
-[UIKBShadowEffect usesRGBColors];
-[UIKBShadowEffect setWeight:];
-[UIKBShadowEffect isValid];
-[UIKBShadowEffect description];
-[UIKBShadowEffect setOffset:];
-[UIKBShadowEffect copyWithZone:];
-[UIKBShadowEffect isEqual:];
-[UIKBShadowEffect offset];
-[UIKBShadowEffect concaveInsets];
-[UIKBShadowEffect initWithColor:offset:insets:weight:];
-[UIKBShadowEffect insets];
-[UIKBShadowEffect renderEffectWithRenderer:traits:];
-[UIKBShadowEffect renderUnder];
-[UIKBShadowEffect setConcaveInsets:];
-[UIKBShadowEffect setInsets:];
```
