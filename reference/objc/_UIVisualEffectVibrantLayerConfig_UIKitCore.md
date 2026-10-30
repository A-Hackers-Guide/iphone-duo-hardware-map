# `_UIVisualEffectVibrantLayerConfig`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIVisualEffectLayerConfig`
- 3 instance variables, 3 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"UIColor" _vibrantColor;
@"UIColor" _tintColor;
@"NSDictionary" _filterAttributes;
```

## Properties

```
@property (T@"UIColor",R,N,V_vibrantColor) vibrantColor;
@property (T@"UIColor",R,N,V_tintColor) tintColor;
@property (T@"NSDictionary",R,C,N,V_filterAttributes) filterAttributes;
```

## Class methods

```
+[_UIVisualEffectVibrantLayerConfig layerWithVibrantColor:tintColor:filterType:];
+[_UIVisualEffectVibrantLayerConfig layerWithVibrantColor:tintColor:filterType:filterAttributes:];
```

## Instance methods

```
-[_UIVisualEffectVibrantLayerConfig description];
-[_UIVisualEffectVibrantLayerConfig tintColor];
-[_UIVisualEffectVibrantLayerConfig configureLayerView:];
-[_UIVisualEffectVibrantLayerConfig deconfigureLayerView:];
-[_UIVisualEffectVibrantLayerConfig filterAttributes];
-[_UIVisualEffectVibrantLayerConfig vibrantColor];
```
