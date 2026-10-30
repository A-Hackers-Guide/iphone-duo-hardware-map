# `UIGlassEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIVisualEffect`
- 4 instance variables, 4 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"_UIViewGlass" _explicitGlass;
B _interactive;
@"UIColor" _tintColor;
q _style;
```

## Properties

```
@property (Tq,N,V_style) style;
@property (T@"_UIViewGlass",R,N) glass;
@property (TB,N,GisInteractive,V_interactive) interactive;
@property (T@"UIColor",C,N,V_tintColor) tintColor;
```

## Class methods

```
+[UIGlassEffect supportsSecureCoding];
+[UIGlassEffect effectWithGlass:];
+[UIGlassEffect effectWithStyle:];
```

## Instance methods

```
-[UIGlassEffect isInteractive];
-[UIGlassEffect glass];
-[UIGlassEffect style];
-[UIGlassEffect setStyle:];
-[UIGlassEffect setTintColor:];
-[UIGlassEffect encodeWithCoder:];
-[UIGlassEffect hash];
-[UIGlassEffect tintColor];
-[UIGlassEffect initWithCoder:];
-[UIGlassEffect copyWithZone:];
-[UIGlassEffect isEqual:];
-[UIGlassEffect setInteractive:];
```
