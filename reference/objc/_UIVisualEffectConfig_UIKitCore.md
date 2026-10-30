# `_UIVisualEffectConfig`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _layerConfigs;
@"_UIVisualEffectLayerConfig" _contentConfig;
```

## Properties

```
@property (T@"NSArray",R,N,V_layerConfigs) layerConfigs;
@property (T@"_UIVisualEffectLayerConfig",R,N,V_contentConfig) contentConfig;
```

## Class methods

```
+[_UIVisualEffectConfig configWithContentConfig:];
+[_UIVisualEffectConfig configWithLayerConfigs:];
```

## Instance methods

```
-[_UIVisualEffectConfig description];
-[_UIVisualEffectConfig addLayerConfig:];
-[_UIVisualEffectConfig contentConfig];
-[_UIVisualEffectConfig enumerateLayerConfigs:];
-[_UIVisualEffectConfig layerConfigs];
```
