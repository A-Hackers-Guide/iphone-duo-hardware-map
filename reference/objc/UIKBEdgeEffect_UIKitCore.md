# `UIKBEdgeEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIKBRenderEffect`
- 6 instance variables, 12 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"NSString" _colorName;
Q _edges;
d _weight;
@"UIKBGradient" _gradient;
d _opacity;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _insets;
```

## Properties

```
@property (TQ,N,V_edges) edges;
@property (T{UIEdgeInsets=dddd},N,V_insets) insets;
@property (T@"UIKBGradient",&,N,V_gradient) gradient;
@property (Td,N,V_opacity) opacity;
@property (TB,R,N) isValid;
@property (TB,R,N) renderUnder;
@property (Td,N,V_weight) weight;
@property (TB,R,N) usesRGBColors;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBEdgeEffect effectWithColor:edges:inset:weight:];
+[UIKBEdgeEffect effectWithColor:edges:insets:weight:];
```

## Instance methods

```
-[UIKBEdgeEffect gradient];
-[UIKBEdgeEffect CGColor];
-[UIKBEdgeEffect edges];
-[UIKBEdgeEffect setEdges:];
-[UIKBEdgeEffect weight];
-[UIKBEdgeEffect usesRGBColors];
-[UIKBEdgeEffect setGradient:];
-[UIKBEdgeEffect opacity];
-[UIKBEdgeEffect setWeight:];
-[UIKBEdgeEffect setOpacity:];
-[UIKBEdgeEffect isValid];
-[UIKBEdgeEffect description];
-[UIKBEdgeEffect copyWithZone:];
-[UIKBEdgeEffect isEqual:];
-[UIKBEdgeEffect initWithColor:edges:insets:weight:];
-[UIKBEdgeEffect insets];
-[UIKBEdgeEffect renderEffectWithRenderer:traits:];
-[UIKBEdgeEffect renderUnder];
-[UIKBEdgeEffect setInsets:];
```
