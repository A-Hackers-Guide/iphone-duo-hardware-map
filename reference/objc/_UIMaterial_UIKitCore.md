# `_UIMaterial`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 4 class methods

## Instance variables

```
B _vibrant;
@"NSArray" _backgroundEffects;
@"NSArray" _contentEffects;
```

## Properties

```
@property (TB,R,N,GisVibrant,V_vibrant) vibrant;
@property (T@"NSArray",R,N,V_backgroundEffects) backgroundEffects;
@property (T@"NSArray",R,N,V_contentEffects) contentEffects;
```

## Class methods

```
+[_UIMaterial _labelMaterial];
+[_UIMaterial materialForSystemColorName:];
+[_UIMaterial _resolvesMaterialBySystemColorName:];
+[_UIMaterial _solariumMaterialForColor:traitCollection:];
```

## Instance methods

```
-[_UIMaterial backgroundEffects];
-[_UIMaterial initWithVibrancy:forBlurEffectStyle:];
-[_UIMaterial isVibrant];
-[_UIMaterial contentEffects];
-[_UIMaterial description];
-[_UIMaterial initWithVibrantVisualEffect:];
```
